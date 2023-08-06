import importlib
import logging
import os
import sys

def get_mapping_fn(configuration_directory, pipeline_id, mapping_filename):
    for filename in os.listdir(os.path.join(configuration_directory, pipeline_id)):
        if filename.endswith('.py') and filename != mapping_filename:  # wait to import mapping file last
            _import_config_python_file(configuration_directory, pipeline_id, filename)

    logging.info(f"Loading {mapping_filename}...")
    module = _import_config_python_file(configuration_directory, pipeline_id, mapping_filename)

    return getattr(module, "mapping") if module else None

def _import_config_python_file(configuration_directory, pipeline_id, config_filename):
    config_python_file_path = os.path.join(configuration_directory, pipeline_id, config_filename)
    if os.path.isfile(config_python_file_path):
        file_split = config_filename.rsplit(".", 1)
        if file_split[1] == "py":
            module_name = f"alira.{pipeline_id}.{file_split[0]}"  # without .py file ending

            try:
                spec = importlib.util.spec_from_file_location(module_name, config_python_file_path)
                module = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = module
                spec.loader.exec_module(module)

                return module
            except Exception:
                logging.exception(f"There was an error loading {config_python_file_path} as module {module_name}")
        else:
            logging.warning(f"Configuration file {config_filename} is not a python file")
    else:
        logging.warning(f"Could not find config python file {config_python_file_path}")
        return None
