"""Resource client to obtain information on sidecar bindings"""

from typing import Any, Dict, List

from ..client import Client
from .resource import ResourceClient
from .listener import ListenerClient


class NoMatchingListenerException(Exception):
    """NoMatchingListenerException is raised if the binding has no listener
    with the requested settings."""


class BindingClient(ResourceClient):
    """BindingClient can be used to get information about the binding of a
    repo to a sidecar.
    """

    def __init__(
        self,
        cyral_client: Client,
        sidecar_id: str,
        binding_id: str,
    ) -> None:
        super().__init__(cyral_client)
        self.cyral_client = cyral_client
        self.sidecar_id = sidecar_id
        self.binding_id = binding_id

    def get(self) -> Dict[str, Any]:
        """fetch information related to the binding"""
        uri = f"/v1/sidecars/{self.sidecar_id}/bindings/{self.binding_id}"
        return self.do_get(uri)

    def port(
        self, binding_info: Dict[str, Any], proxy_mode: bool = False
    ) -> int:
        """port returns the (first) sidecar listener port for the binding.
        For S3 and dynamo_db repos, the port for the specified proxy
        mode is returned.
        """
        binding_listeners: List[Dict[str, Any]] = binding_info["binding"][
            "listenerBindings"
        ]

        for binding_listener in binding_listeners:
            listener_id = binding_listener["listenerId"]
            listener_info = ListenerClient(
                self.cyral_client, self.sidecar_id, listener_id
            ).get()
            listener_config = listener_info["listenerConfig"]
            repo_types = listener_config["repoTypes"]
            matched_listener = False
            if "s3" in repo_types:
                s3_settings = listener_config["s3Settings"]
                if s3_settings["proxyMode"] == proxy_mode:
                    matched_listener = True
            elif "dynamodb" in repo_types:
                ddb_settings = listener_config["dynamoDbSettings"]
                if ddb_settings["proxyMode"] == proxy_mode:
                    matched_listener = True
            else:
                # neither S3 nor dynamoDB, use the first listener we found.
                matched_listener = True
            if matched_listener:
                return listener_config["address"]["port"]

        # we didn't find any matching listener, raise an exception
        raise NoMatchingListenerException(
            "the binding has no listener with matching settings"
        )
