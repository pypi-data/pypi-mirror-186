"""Resource client for obtaining information about repos accessible
to a user.
"""

from typing import Any, Dict, Generator, List, Optional, Union
from urllib.parse import urlencode

from ..client import Client
from .resource import ResourceClient


class AccessInfoClient(ResourceClient):
    """AccessInfoClient is used to obtain information about the
    repos that the user has access to.
    """

    def __init__(  # pylint: disable=too-many-arguments
        self,
        cyral_client: Client,
        repo_name: Optional[str] = None,
        repo_tags: Optional[List[str]] = None,
        repo_type: Optional[str] = None,
        page_size: int = 10,
    ) -> None:
        super().__init__(cyral_client)
        self.repo_name = repo_name
        self.repo_tags = repo_tags
        self.repo_type = repo_type
        self.page_size = page_size

    def __iter__(self) -> Generator[List[Dict[str, Any]], None, None]:
        query_filter: Dict[str, Union[str, List[str]]] = {}
        if self.repo_name:
            query_filter["repoName"] = self.repo_name
        if self.repo_tags:
            query_filter["repoTags"] = self.repo_tags
        if self.repo_type:
            query_filter["repoTypes"] = [self.repo_type]

        done = False
        cursor = ""
        while not done:
            query_params: Dict[str, str] = {"pageSize": str(self.page_size)}
            if cursor:
                query_params["pageAfter"] = cursor
            uri = f"/v1/accessInfo?{urlencode(query_params)}"
            resp = self.do_post(uri, data=query_filter)
            repos = resp["results"]
            count = len(repos)
            if count == 0:
                return  # to avoid ever yielding an empty list
            if count == self.page_size:
                cursor = repos[count - 1]["repoID"]
            else:
                done = True
            yield repos
