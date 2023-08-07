"""This module defines classes corresponding to Cyral REST API resources.
"""

from typing import Any, Dict

import requests

from ..client import Client


class ResourceClient:  # pylint: disable=too-few-public-methods
    """ResourceClient is the base class for all specific resource
    client classes.
    """

    def __init__(self, cyral_client: Client):
        self.client = cyral_client
        self.cp_address = cyral_client.cp_address

    def authorization_header(self) -> Dict[str, str]:
        """authorization_header returns the custom header needed
        in API requests to authenticate to the control plane.
        """
        headers = self.client.get_auth_header()
        return headers

    def do_get(self, uri: str, timeout: int = 5) -> Any:
        """Make a GET call to an API endpoint."""
        url = f"https://{self.cp_address}{uri}"
        resp = requests.get(
            url,
            headers=self.authorization_header(),
            timeout=timeout,
        )
        resp.raise_for_status()
        return resp.json()

    def do_post(self, uri: str, data: Any, timeout: int = 5) -> Any:
        """Make a POST call to an API endpoint."""
        url = f"https://{self.cp_address}{uri}"
        resp = requests.post(
            url,
            json=data,
            headers=self.authorization_header(),
            timeout=timeout,
        )
        resp.raise_for_status()
        return resp.json()
