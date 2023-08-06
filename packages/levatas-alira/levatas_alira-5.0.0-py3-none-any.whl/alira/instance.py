import uuid
import jmespath

from datetime import datetime


class Instance(object):
    def __init__(
            self,
            instance_id: str = None,
            pipeline_id: str = None,
            creation_date: str = None,
            last_update_date: str = None,
            prediction: int = None,
            confidence: float = None,
            files: list = None,
            waypoint_id: str = None,
            mission_id: str = None,
            source_id: str = None,
            instance_metadata: dict = None,
            instance_properties: dict = None
    ) -> None:
        if instance_metadata is not None and not isinstance(instance_metadata, dict):
            raise ValueError("The field 'instance_metadata' must be a dictionary.")

        self.instance_id = instance_id or uuid.uuid4().hex
        self.pipeline_id = pipeline_id
        self.creation_date = creation_date
        self.last_update_date = last_update_date

        self.prediction = prediction
        self.confidence = confidence
        self.files = files

        if self.files and not isinstance(self.files, list):
            self.files = [self.files]

        self.waypoint_id = waypoint_id
        self.mission_id = mission_id
        self.source_id = source_id
        self.instance_metadata = instance_metadata or {}
        self.instance_properties = instance_properties or {}

    def has_attribute(self, name: str):
        try:
            self.get_attribute(name)
            return True
        except AttributeError:
            return False

    def get_attribute(self, name: str, *arg, **kwargs):
        def raise_exception(name: str, value):
            raise AttributeError(f"The attribute '{name}' does not exist.")

        def default_value(name, value):
            return value

        value = None
        attribute_doesnt_exist = raise_exception
        if "default" in kwargs:
            attribute_doesnt_exist = default_value
            value = kwargs["default"]
        elif len(arg) == 1:
            attribute_doesnt_exist = default_value
            value = arg[0]

        if name is None:
            return attribute_doesnt_exist(name, value)

        expression = jmespath.search(name, self.to_dict())
        if expression is None:
            return attribute_doesnt_exist(name, value)

        return expression

    def to_dict(self):
        result = self.__dict__.copy()

        # Remove the private attribute representing the image
        # and add the value of the property.
        if "_Instance__image" in result:
            del result["_Instance__image"]

        return result

    @staticmethod
    def create(data):
        data = data.copy()

        instance_id = data.get("instance_id", None)
        pipeline_id = data.get("pipeline_id", None)
        creation_date = data.get("creation_date", datetime.utcnow().isoformat())
        last_update_date = data.get("last_update_date", creation_date)
        prediction = data.get("prediction", None)
        confidence = data.get("confidence", None)
        files = data.get("files", None)
        waypoint_id = data.get("waypoint_id", None)
        mission_id = data.get("mission_id", None)
        source_id = data.get("source_id", None)

        if "instance_id" in data:
            del data["instance_id"]
        if "prediction" in data:
            del data["prediction"]
        if "confidence" in data:
            del data["confidence"]
        if "files" in data:
            del data["files"]
        if "waypoint_id" in data:
            del data["waypoint_id"]
        if "mission_id" in data:
            del data["mission_id"]
        if "source_id" in data:
            del data["source_id"]
        if "pipeline_id" in data:
            del data["pipeline_id"]

        if "instance_metadata" in data:
            instance_metadata = data["instance_metadata"]
            del data["instance_metadata"]
        else:
            instance_metadata = {}

        if "instance_properties" in data:
            instance_properties = data["instance_properties"]
            del data["instance_properties"]
        else:
            instance_properties = {}

        for key, value in data.items():  # Anything left in data after 'del' statements is placed in metadata
            instance_metadata[key] = value

        instance = Instance(
            instance_id=instance_id,
            pipeline_id=pipeline_id,
            creation_date=creation_date,
            last_update_date=last_update_date,
            prediction=prediction,
            confidence=confidence,
            files=files,
            waypoint_id=waypoint_id,
            mission_id=mission_id,
            source_id=source_id,
            instance_metadata=instance_metadata,
            instance_properties=instance_properties,
        )

        return instance

    @staticmethod
    def create_from_row(instances_row):
        return Instance(
            instance_id=instances_row.instance_id,
            pipeline_id=instances_row.pipeline_id,
            creation_date=instances_row.creation_date,
            last_update_date=instances_row.last_update_date,
            prediction=instances_row.prediction,
            confidence=instances_row.confidence,
            files=instances_row.files,
            waypoint_id=instances_row.waypoint_id,
            mission_id=instances_row.mission_id,
            source_id=instances_row.source_id,
            instance_metadata=instances_row.instance_metadata,
            instance_properties=instances_row.instance_properties
        )

    @staticmethod
    def _format(data: dict) -> dict:
        for key, value in data.items():
            data[key] = value

        return data


def onlyPositiveInstances(instance: Instance):
    return instance.prediction == 1


def onlyNegativeInstances(instance: Instance):
    return instance.prediction == 0
