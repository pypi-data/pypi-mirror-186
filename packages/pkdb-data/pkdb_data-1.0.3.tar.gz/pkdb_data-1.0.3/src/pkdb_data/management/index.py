"""Functions for manipulating the elastic index."""
import multiprocessing
import threading
import time
from datetime import timedelta
from typing import Any, Dict

import requests
from pymetadata.log import get_logger

from pkdb_data.management.query import check_json_response, requests_with_client


logger = get_logger(__name__)


class IndexProcess(multiprocessing.Process):
    """Process for indexing elastic.

    Allows to run the indexing in a separate thread.
    """

    def __init__(
        self, sid: str, api_url: str, auth_headers: Dict[str, str], client: Any = None
    ):
        """Initialize IndexProcess."""
        multiprocessing.Process.__init__(
            self,
            target=_update_study_index_log,
            args=(sid, api_url, auth_headers, client),
        )


class IndexThread(threading.Thread):
    """Thread for indexing elastic."""

    def __init__(
        self, sid: str, api_url: str, auth_headers: Dict[str, str], client: Any = None
    ):
        """Initialize IndexThread."""
        threading.Thread.__init__(self)
        self.sid = sid
        self.api_url = api_url
        self.auth_headers = auth_headers
        self.client = client

    def run(self) -> None:
        """Run indexing thread."""
        _update_study_index_log(self.sid, self.api_url, self.auth_headers, self.client)


def _update_study_index_log(
    sid: str, api_url: str, auth_headers: Dict[str, str], client: Any = None
) -> None:
    """Update the study index log."""
    logger.info(f"Start indexing {sid}")
    start_time = time.time()
    update_study_index(
        sid=sid, api_url=api_url, auth_headers=auth_headers, client=client
    )
    index_time = timedelta(seconds=time.time() - start_time).total_seconds()
    logger.info(f"[white on black]Finished indexing {sid} in {index_time:.2f} [s]")


def update_study_index(
    sid: str, api_url: str, auth_headers: Dict[str, str], client: Any = None
) -> None:
    """Update the elasticsearch index for given study_sid."""
    response = requests_with_client(
        client,
        requests,
        f"{api_url}/update_index/",
        method="post",
        data={"sid": sid},
        headers=auth_headers,
    )
    check_json_response(response)
