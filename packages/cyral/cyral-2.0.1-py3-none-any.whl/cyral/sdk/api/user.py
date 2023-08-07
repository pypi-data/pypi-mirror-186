"""Resource client to obtain user information"""

from typing import Any, Dict

from .resource import ResourceClient


class UserClient(ResourceClient):
    """UserClient can be used to obtain information about users in Cyral.
    At this time, only information about "self" can be obtained.
    """

    def get_current_user(self) -> Dict[str, Any]:
        """fetch information related to the logged in user"""
        uri = "/v1/users/users/_self"
        return self.do_get(uri)
