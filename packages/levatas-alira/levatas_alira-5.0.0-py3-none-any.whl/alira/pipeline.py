import os
import logging
import yaml
import sys
import importlib.util
import redis
import re

from datetime import datetime
from rq import Queue, Retry
from importlib import import_module

from alira.instance import Instance
from alira.modules.module import InternalError
from alira.common.database import Database

rq_worker_logger = logging.getLogger("rq.worker")

CONFIGURATION_FILENAME = "configuration.yml"
PIPELINE_PYTHON_FILENAME = "pipeline.py"


class Pipeline(object):
    def __init__(
        self,
        pipeline_id: str = None,
        pipeline_configuration: any = None,
        configuration_directory: str = None,
        redis_server: str = None,
        mysql_server: str = None,
        asynchronous: bool = True,
        **kwargs
    ):
        self.kwargs = kwargs

        self.pipeline_id = pipeline_id
        self.configuration_directory = configuration_directory or os.path.abspath(
            os.getcwd()
        )
        self.redis_server = redis_server or "redis://localhost:6379/"
        self.mysql_server = mysql_server
        self.asynchronous = asynchronous

        # We are going to read the list of modules from the pipeline.yml file.
        self.modules = None
        self.dependencies = None
        self._load_pipeline_configuration(pipeline_configuration)

    def run(self, data: dict) -> Instance:
        data.update({"pipeline_id": self.pipeline_id})
        instance = Instance.create(data)

        database = Database(self.mysql_server)
        database.instance_dao().put(instance)
        database.flat_instance_metadata_dao(self.pipeline_id).put(instance)

        if self.asynchronous:
            redis_connection = redis.from_url(self.redis_server)
        else:
            import fakeredis

            redis_connection = fakeredis.FakeStrictRedis()

        queue = Queue(
            self.pipeline_id,
            connection=redis_connection,
            is_async=self.asynchronous,
        )

        job = None
        for module in self.modules:
            module_signature = f"{module.__module__}.{module.__class__.__name__}"

            logging.info(f"Scheduling module {module_signature}...")

            arguments = {} if job is None else {"depends_on": job}

            if hasattr(module, "schedule"):
                max_retries, *interval = module.schedule
                retry = Retry(max=max_retries, interval=interval)
                arguments["retry"] = retry

            job = queue.enqueue(
                Pipeline.run_module,
                module=module,
                module_signature=module_signature,
                instance=instance,
                dependencies=self.dependencies,
                pipeline_id=self.pipeline_id,
                configuration_directory=self.configuration_directory,
                database=database,
                **arguments
            )

        instance_from_database = Pipeline.get_instance_from_database(instance.instance_id, database=database)
        return instance_from_database if instance_from_database else instance

    @classmethod
    def run_module(
        cls,
        module,
        module_signature,
        instance,
        dependencies,
        pipeline_id,
        configuration_directory,
        database,
    ):
        rq_worker_logger.info(f"Running module {module_signature}...")

        Pipeline.load_pipeline_python_file(pipeline_id, configuration_directory)
        instance_from_database = Pipeline.get_instance_from_database(instance.instance_id, database=database)
        instance = instance_from_database if instance_from_database else instance

        rq_worker_logger.debug(f"Input instance: {instance.to_dict()}")
        rq_worker_logger.debug(f"Dependencies: {dependencies}")

        module_name = (
            module.module_id if hasattr(module, "module_id") else module_signature
        )

        try:
            result = module.run(instance, **dependencies)

            if result is None:
                result = dict()

            if isinstance(result, dict):
                if not "status" in result:
                    result["status"] = "SUCCESS"
            else:
                raise RuntimeError(f"Result for module {module_name} must be a dictionary.")
        except InternalError as e:
            error = f"Internal Exception: {e}"
            rq_worker_logger.exception(error)
            result = {
                "status": "FAILURE",
                "message": error
            }
        except Exception as e:
            error = f"Unable to run module: {e}"
            rq_worker_logger.exception(error)
            result = {
                "status": "FAILURE",
                "message": error
            }

        module_output = {module_name: result}

        # Load the instance again to avoid overwriting another asynchronous module's data
        instance_from_database = Pipeline.get_instance_from_database(instance.instance_id, database=database)
        instance = instance_from_database if instance_from_database else instance

        instance.instance_properties.update(module_output)
        instance.last_update_date = datetime.utcnow().isoformat()
        database.instance_dao().put(instance)

        rq_worker_logger.debug(f"Output instance: {instance.to_dict()}")
        return module_output

    @classmethod
    def load_pipeline_python_file(cls, pipeline_id, configuration_directory):
        python_filename = os.path.join(
            configuration_directory, PIPELINE_PYTHON_FILENAME
        )
        if os.path.isfile(python_filename):
            rq_worker_logger.info(
                f"Adding {PIPELINE_PYTHON_FILENAME} content to system path..."
            )

            module_name = f"{pipeline_id}.pipeline"

            try:
                spec = importlib.util.spec_from_file_location(
                    module_name, python_filename
                )
                module = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = module
                spec.loader.exec_module(module)

                logging.info(f"Loaded {python_filename} as module {module_name}")
            except Exception:
                logging.exception(
                    f"There was an error loading {python_filename} "
                    f"as module {module_name}"
                )

    @staticmethod
    def get_instance_from_database(instance_id, database=None, mysql_server=None):
        if database is None:
            database = Database(mysql_server)
        instance_row = database.instance_dao().get_instance(instance_id=instance_id)

        if instance_row:
            return Instance.create_from_row(instance_row)
        return None

    def _load_pipeline_configuration(self, pipeline_configuration):
        if pipeline_configuration is None:
            pipeline_configuration = os.path.join(self.configuration_directory, CONFIGURATION_FILENAME)

        if hasattr(pipeline_configuration, "read"):
            pipeline_configuration = self._load_pipeline_configuration_from_stream(pipeline_configuration)
        else:
            pipeline_configuration = self._load_pipeline_configuration_from_file(pipeline_configuration)

        module_arguments = {}
        for module_data in pipeline_configuration.get("default-module-configuration", []):
            default_arguments = {
                "pipeline_id": self.pipeline_id,
                "configuration_directory": self.configuration_directory,
            }
            # Augment default_arguments with arguments from default-module-configuration and pipeline kwargs
            for argument_id, argument in module_data.items():
                default_arguments[argument_id] = argument
            default_arguments.update(self.kwargs)

            # Store the module arguments in a dictionary with a unique reference
            reference = self._get_reference(module_data, module_arguments.keys())
            module_arguments[reference] = default_arguments

        self.dependencies = self._load_modules(pipeline_configuration, "dependencies", module_arguments)
        self.modules = list(self._load_modules(pipeline_configuration, "pipeline", module_arguments).values())

    def _load_modules(self, pipeline_configuration: dict, section: str, module_arguments: dict):
        result = {}

        modules_data = pipeline_configuration.get(section, {}).get(self.pipeline_id, [])

        for module_data in modules_data:
            overwrite_arguments = {}
            for argument_id, argument in module_data.items():
                overwrite_arguments[argument_id] = argument

            reference = self._get_reference(module_data, result.keys())

            final_arguments = module_arguments.get(reference, {})
            final_arguments.update(overwrite_arguments)

            try:
                # Get module path/name from either `module_data` or `final_arguments` (allows specifying just module_id in the pipeline configuration)
                module_str = module_data["module"] if "module" in module_data else final_arguments["module"]
                module_path, _, module_name = module_str.rpartition(".")
                del final_arguments["module"]  # Don't need to pass as a parameter to the module

                # Import the module
                module = getattr(import_module(module_path), module_name)
                logging.info(f"Loaded module {module_path}.{module_name}")
            except ModuleNotFoundError as e:
                raise RuntimeError(
                    f"Unable to load module {module_path}.{module_name}"
                ) from e

            # Create the module instance and add it to the return result
            result[reference] = module(**final_arguments)

        return result

    def _get_reference(self, module_data: dict, keys: set):
        # Every module should have a `reference`. This will be the configured
        # `module_id` or a snake_case name based on the module name.

        if "module_id" in module_data:
            reference = module_data["module_id"]
        else:
            module_name = module_data["module"].rpartition(".")[2]
            reference = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", module_name)
            reference = re.sub("([a-z0-9])([A-Z])", r"\1_\2", reference).lower()

        while reference in keys:
            reference += "_"

        return reference


    def _load_pipeline_configuration_from_stream(self, pipeline_configuration):
        try:
            return yaml.safe_load(pipeline_configuration.read())
        except Exception as e:
            logging.exception(e)
            raise RuntimeError("Unable to load pipeline configuration") from e

    def _load_pipeline_configuration_from_file(self, pipeline_configuration):
        logging.info(f"Loading pipeline configuration from {pipeline_configuration}...")

        try:
            with open(pipeline_configuration) as file:
                return yaml.load(file.read(), Loader=yaml.FullLoader)
        except Exception as e:
            logging.exception(e)
            raise RuntimeError(
                "Unable to load pipeline configuration from "
                f"file {pipeline_configuration}"
            ) from e
