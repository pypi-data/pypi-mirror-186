from __future__ import annotations

from os import PathLike

from blx.cid import CID
from blx.client import get_client
from blx.progress import Progress
from blx.service_exit import ServiceExit

__all__ = ["download"]


def download(cid: CID, file: str | PathLike[str], show_progress=True):
    with Progress("Download", disable=not show_progress) as progress:
        try:
            client = get_client()
            client.get(cid, file, progress)
        except ServiceExit as excp:
            progress.shutdown()
            raise excp
