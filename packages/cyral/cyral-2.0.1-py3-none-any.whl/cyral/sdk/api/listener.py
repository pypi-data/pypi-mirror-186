"""Resource client to obtain information on sidecar listeners"""

from typing import Any, Dict

from ..client import Client
from .resource import ResourceClient


class ListenerClient(ResourceClient):
    """ListenerClient can be used to get information about a network listener
    on a sidecar.
    """

    def __init__(
        self,
        cyral_client: Client,
        sidecar_id: str,
        listener_id: str,
    ) -> None:
        super().__init__(cyral_client)
        self.sidecar_id = sidecar_id
        self.listener_id = listener_id

    def get(self) -> Dict[str, Any]:
        """fetch information related to the listener"""
        uri = f"/v1/sidecars/{self.sidecar_id}/listeners/{self.listener_id}"
        return self.do_get(uri)
