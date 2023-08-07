"""Resource client to obtain information about sidecars."""

from typing import Any, Dict

from ..client import Client
from .resource import ResourceClient


class SidecarClient(ResourceClient):
    """class SidecarClient can be used to obtain information about sidecars."""

    def __init__(self, cyral_client: Client, sidecar_id: str) -> None:
        super().__init__(cyral_client)
        self.sidecar_id = sidecar_id

    def get(self) -> Dict[str, Any]:
        """get fetches information related to the sidecar"""
        uri = f"/v1/sidecars/{self.sidecar_id}"
        return self.do_get(uri)

    @staticmethod
    def endpoint(sidecar_info: Dict[str, Any]) -> str:
        """endpoint returns the DNS name for the sidecar."""
        user_endpoint = sidecar_info["userEndpoint"]
        return user_endpoint if user_endpoint else sidecar_info["endpoint"]
