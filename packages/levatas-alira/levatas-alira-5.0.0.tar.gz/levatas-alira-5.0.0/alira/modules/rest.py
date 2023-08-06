import logging
import json
import requests
import os

from alira.common.database import Database
from alira.instance import Instance
from alira.modules.module import Connection, InternalError

PIPELINE_MODULE_NAME = "rest"


class RestAuthentication:
    def __init__(
        self, service: str = None, username: str = None, password: str = None, **kwargs
    ):
        self.service = service or os.environ.get("ALIRA_REST_SERVICE", None)
        self.username = username or os.environ.get("ALIRA_REST_USERNAME", None)
        self.password = password or os.environ.get("ALIRA_REST_PASSWORD", None)
        self.access_token = None

    def get_access_token(self, refresh: bool = False):
        if self.access_token is None or refresh:
            logging.info(f"Authenticating Rest module at {self.service}")

            try:
                response = self._request()
                if response.status_code != 200:
                    raise InternalError(
                        f"There was an error authenticating with the Rest service. Status code: {response.status_code} "
                        f"Message: {response.text}"
                    )
                token = json.loads(response.text)

                self.access_token = token["access_token"]
            except InternalError as e:
                raise e
            except Exception as e:
                raise InternalError(
                    f"There was an error authenticating with the Rest service. {e}"
                ) from e

        return self.access_token

    def _request(self):
        url = "/".join(
            map(
                lambda x: str(x).rstrip("/"),
                [self.service, "login"],
            )
        )
        return requests.post(
            url=url, json={"username": self.username, "password": self.password}
        )


class Rest(Connection):
    def __init__(
        self,
        configuration_directory: str,
        module_id: str = None,
        pipeline_id: str = None,
        files: str = None,
        files_directory: str = None,
        upload_files: bool = True,
        database_url: str = None,
        **kwargs,
    ):
        super().__init__(
            configuration_directory=configuration_directory,
            module_id=module_id or PIPELINE_MODULE_NAME,
            pipeline_id=pipeline_id,
            **kwargs,
        )

        self.files = files
        self.files_directory = files_directory or "files"
        self.upload_files = upload_files
        self.database_url = database_url

    def run(self, instance: Instance, rest_authentication, **kwargs):
        super().run(instance, **kwargs)

        database = Database(self.database_url)
        database.instance_dao().put(instance)
        database.flat_instance_metadata_dao(instance.pipeline_id).put(instance)

        access_token = rest_authentication.get_access_token()

        try:
            files = self._get_files(instance)
            response = self._request(rest_authentication, access_token, files)

            # If the access token we are currently using is expired, we want to
            # refresh it and try again.
            if response.status_code == 401:
                access_token = rest_authentication.get_access_token(refresh=True)
                response = self._request(rest_authentication, access_token, files)

            if response.status_code != 201:
                raise InternalError(
                    f"Status Code: {response.status_code}. \
                    There was an error uploading the files for instance {instance.instance_id}. \
                    Message: {response.text}"
                )

            result = json.loads(response.text)

            return {
                "instance_id": instance.instance_id,
                "files": result.get("filenames", [])
            }

        except InternalError as e:
            raise e
        except Exception as e:
            raise InternalError(
                f"There was an error uploading the files for instance {instance.instance_id}. {e}"
            ) from e

    def _get_files(self, instance: Instance):
        if self.files:
            filenames = instance.get_attribute(self.files, default=instance.files)
        else:
            filenames = instance.files

        if not isinstance(filenames, list):
            filenames = [filenames]

        result = {}
        for filename in filenames:
            if self.upload_files:
                try:
                    file_path = os.path.join(
                        self.configuration_directory, self.files_directory, filename
                    )
                    data = open(file_path, "rb").read()
                except Exception:
                    logging.error(f"There was an error loading the file {file_path}")
                    data = None
            else:
                data = None

            result[filename] = data

        return result

    def _request(self, rest_authentication, access_token, files):
        url = "/".join(
            map(
                lambda x: str(x).rstrip("/"),
                [rest_authentication.service, "files", self.pipeline_id],
            )
        )
        return requests.post(url=url, files=files, headers={"Authorization": f"Bearer {access_token}"})
