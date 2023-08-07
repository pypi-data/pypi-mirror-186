"""Resource client to fetch CA bundle from Cyral control plane."""

import requests

from .resource import ResourceClient


class CABundleClient(ResourceClient):
    """CABundle resource can be used to get the Cyral CA certificate bundle."""

    def get(self, timeout: int = 5) -> str:
        "fetch CA certificate bundle"
        url = f"https://{self.cp_address}/v1/templates/ca_bundle"
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status()
        return resp.text
