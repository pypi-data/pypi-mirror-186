from contextlib import contextmanager
import logging
import math
import os
import sqlalchemy as db

from alira.instance import Instance
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base


DeclarativeBase = declarative_base()

FIRST_INSTANCE_COLUMNS = [  # The 'instances' table columns to be included in flat instances
    "creation_date",
    "mission_id",
    "waypoint_id",
    "prediction"
]

@contextmanager
def db_session(db_url):
    engine = db.create_engine(db_url)
    session = sessionmaker(bind=engine, autoflush=True, autocommit=False)()
    yield session
    session.close()

class Instances(DeclarativeBase):
    __tablename__ = "instances"

    instance_id = db.Column(db.VARCHAR(36), primary_key=True)
    creation_date = db.Column(db.VARCHAR(36), nullable=False)
    last_update_date = db.Column(db.VARCHAR(36), nullable=False)
    pipeline_id = db.Column(db.VARCHAR(32), nullable=False)

    prediction = db.Column(db.Integer, nullable=True)
    confidence = db.Column(db.Float, nullable=True)
    files = db.Column(db.JSON(), nullable=True)
    waypoint_id = db.Column(db.VARCHAR(64), nullable=True)
    mission_id = db.Column(db.VARCHAR(64), nullable=True)
    source_id = db.Column(db.VARCHAR(32), nullable=True)
    instance_metadata = db.Column(db.JSON(), nullable=True)
    instance_properties = db.Column(db.JSON(), nullable=True)


class Database:
    def __init__(self, url: str = None):
        self.url = url or "mysql+pymysql://root:{}@alira-mysql:{}/alira".format(
            os.environ.get("MYSQL_ROOT_PASSWORD"),
            os.environ.get("MYSQL_PORT")
        )

    def instance_dao(self):
        return InstanceDAO(self.url)

    def flat_instance_metadata_dao(self, pipeline_id: str):
        return FlatInstanceMetadataDAO(self.url, pipeline_id)


class BaseDAO:
    def __init__(self, url: str):
        self.url = url


class InstanceDAO(BaseDAO):
    def __init__(self, url: str):
        super(InstanceDAO, self).__init__(url)

    def get_instance(self, instance_id: str):
        with db_session(self.url) as session:
            result = session.query(Instances).filter(Instances.instance_id == instance_id).first()
        return result

    def get_filtered_instances(
        self,
        pipeline_id: str = None,
        mission_id: str = None,
        waypoint_id: str = None,
        limit: int = 100,
        page: int = 1
    ):
        limit = max(min(limit, 500), 1)
        page = max(page, 1)

        with db_session(self.url) as session:
            query = session.query(Instances)

        if mission_id:
            query = query.filter(Instances.mission_id == mission_id)
            if waypoint_id:
                query = query.filter(Instances.waypoint_id == waypoint_id)
        elif waypoint_id:
            logging.warning("Waypoint ID provided without mission ID, ignoring waypoint ID")

        if pipeline_id:
            query = query.filter(Instances.pipeline_id == pipeline_id)

        total_count_before_pagination = query.count()

        query = query.order_by(Instances.creation_date.desc()) \
                     .limit(limit) \
                     .offset((page-1) * limit)

        return {
            "instances": query.all(),
            "metadata": {
                "limit": limit,
                "page": page,
                "total": total_count_before_pagination,
                "pages": int(math.ceil(total_count_before_pagination / limit))
            }
        }

    def put(self, instance: Instance):
        instance_from_table = self.get_instance(instance_id=instance.instance_id)

        with db_session(self.url) as session:
            if instance_from_table:
                instance_from_table.creation_date = instance.creation_date
                instance_from_table.last_update_date = instance.last_update_date
                instance_from_table.pipeline_id = instance.pipeline_id
                instance_from_table.prediction = instance.prediction
                instance_from_table.confidence = instance.confidence
                instance_from_table.files = instance.files
                instance_from_table.waypoint_id = instance.waypoint_id
                instance_from_table.mission_id = instance.mission_id
                instance_from_table.source_id = instance.source_id
                instance_from_table.instance_metadata = instance.instance_metadata
                instance_from_table.instance_properties = instance.instance_properties

                session.add(instance_from_table)
                session.commit()
            else:
                instance_row = Instances(
                    instance_id=instance.instance_id,
                    creation_date=instance.creation_date,
                    last_update_date=instance.last_update_date,
                    pipeline_id=instance.pipeline_id,
                    prediction=instance.prediction,
                    confidence=instance.confidence,
                    files=instance.files,
                    waypoint_id=instance.waypoint_id,
                    mission_id=instance.mission_id,
                    source_id=instance.source_id,
                    instance_metadata=instance.instance_metadata,
                    instance_properties=instance.instance_properties
                )

                session.add(instance_row)
                session.commit()

        return instance


class FlatInstanceMetadataDAO(BaseDAO):
    def __init__(self, url: str, pipeline_id: str):
        super(FlatInstanceMetadataDAO, self).__init__(url)
        engine = db.create_engine(url)
        AutoMapBase = automap_base()
        AutoMapBase.prepare(autoload_with=engine)
        metadata = db.MetaData(bind=engine)

        metadata.reflect()
        self.table = None
        self.Model = None
        if pipeline_id in metadata.tables:
            self.table = metadata.tables[pipeline_id]
            self.Model = getattr(AutoMapBase.classes, pipeline_id)
        self.pipeline_id = pipeline_id

    def get_flat_instance_metadata(self, instance_id: str):
        with db_session(self.url) as session:
            result = session.query(self.table).filter(self.table.columns.instance_id == instance_id).first()
        return result

    def get_flat_instances(self):
        # We split the instance columns into two groups for CSV order (FIRST_INSTANCE_COLUMNS and last_instance_columns)
        last_instance_columns = [column.name for column in Instances.__table__.columns if
                                 (column.name not in FIRST_INSTANCE_COLUMNS)
                                 and (column.name not in ["pipeline_id", "instance_properties", "instance_metadata"])
                                 ]

        flat_instance_metadata_columns = []
        with db_session(self.url) as session:
            query = session.query(Instances).filter(Instances.pipeline_id == self.pipeline_id)

        # If the pipeline-specific instance table exists, enrich column list and query with its data
        if self.table is not None:
            flat_instance_metadata_columns: list = self.table.columns.keys()
            flat_instance_metadata_columns.remove("instance_id")  # It's already in last_instance_columns
            query = query.join(self.table, Instances.instance_id == self.table.columns.instance_id)

        columns = FIRST_INSTANCE_COLUMNS + flat_instance_metadata_columns + last_instance_columns

        results = query.order_by(Instances.creation_date.desc()).with_entities(
            *(list(getattr(Instances, column) for column in FIRST_INSTANCE_COLUMNS)
              + list(getattr(self.table.columns, column) for column in flat_instance_metadata_columns)
              + list(getattr(Instances, column) for column in last_instance_columns)
              )
        ).all()

        return columns, results

    def put(self, instance: Instance):
        if self.table is None:
            logging.info(f"There does not seem to be a MySQL table for pipeline '{self.pipeline_id}'")
            return

        instance_metadata: dict = instance.instance_metadata

        kwargs = dict()
        for col in self.table.columns:
            if col.name == "instance_id":
                kwargs["instance_id"] = instance.instance_id
            elif col.name in instance_metadata:
                kwargs[col.name] = instance_metadata[col.name]
        with db_session(self.url) as session:
            session.add(self.Model(**kwargs))
            session.commit()
