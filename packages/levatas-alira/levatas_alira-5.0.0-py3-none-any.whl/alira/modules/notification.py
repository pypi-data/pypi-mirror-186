import json
import logging
import requests

from alira.common.marked_attributes import MarkedAttributes
from alira.common.utils import get_mapping_fn
from alira.instance import Instance
from alira.modules.module import Connection, Module


class Notification(Connection):
    def __init__(
        self,
        module_id: str,
        filtering: str = None,
        mapping_filename: str = None,
        **kwargs,
    ):
        super().__init__(
            module_id=module_id,
            **kwargs,
        )

        self.filtering = self._load_function(filtering)
        self.mapping_filename = mapping_filename
        self.html_text = None

    def run(self, instance: Instance, **kwargs):
        super().run(instance, **kwargs)

        if self.mapping_filename:
            if self.html_text is None:
                self.attributes = []
                marked_attributes = MarkedAttributes(instance, self.attributes)
                mapping_fn = get_mapping_fn(self.configuration_directory, self.pipeline_id, self.mapping_filename)
                mapping_fn(instance, marked_attributes)

                self.html_text = "<html><body>"
                for attribute in self.attributes:
                    self.html_text += f"<p><b>{attribute['label']}</b>: {attribute['value']}</p>"
                self.html_text += "</body></html>"


class SocketIO(Module):
    def __init__(
        self,
        pipeline_id: str,
        endpoint: str,
        event: str = "dispatch",
        **kwargs,
    ):
        super().__init__(
            pipeline_id=pipeline_id,
            **kwargs,
        )
        self.endpoint = endpoint
        self.event = event

    def run(self, instance: Instance, **kwargs):
        payload = {
            "message": "pipeline-new-instance",
            "data": instance.__dict__,
            "pipeline_id": self.pipeline_id,
        }

        self.emit(self.event, payload)

        return None

    def emit(self, event: str, payload=None):
        if not self.endpoint:
            return

        logging.info(
            f"Sending Socket IO notification to {self.endpoint}. "
            f"Namespace: {self.pipeline_id}"
        )

        payload["event"] = event
        payload["namespace"] = self.pipeline_id

        try:
            requests.post(
                url=self.endpoint,
                data=json.dumps(payload),
                headers={"Content-type": "application/json"},
            )
        except Exception:
            logging.exception("There was an error sending the socket io notification")
