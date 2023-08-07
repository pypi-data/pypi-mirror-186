"""Resource client for obtaining an access token.
"""
from .resource import ResourceClient


class AccessTokenClient(ResourceClient):
    """AccessTokenClient is used to obtain access tokens to
    authenticate to databases.
    """

    def get(self) -> str:
        """get retrieves and returns the access token for the user."""
        resp = self.do_get("/v1/opaqueToken/accessToken")
        return resp["accessToken"]
