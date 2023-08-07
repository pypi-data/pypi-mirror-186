"""Utility functions for writing credentials to .pgpass file."""

import re
from os import environ as env
import os
from pathlib import Path
from typing import List, Tuple


def _create_pgpass(pgpass: Path) -> Path:
    """If given PGPASS file path does not exist, create the file
    with correct the permissions.
    """
    if not pgpass.is_file():
        pgpass.touch(mode=0o600)
    return pgpass


def _find_pgpass() -> Path:
    """Returns the path to the PGPASS file.
    PG Reference: https://www.postgresql.org/docs/current/libpq-pgpass.html
    """
    if "PGPASSFILE" in env:
        return _create_pgpass(Path(env["PGPASSFILE"]))
    # if no env, use pgpass at home directory
    homepgpass = os.path.join("~", ".pgpass")
    homepgpass = os.path.expanduser(homepgpass)
    return _create_pgpass(Path(homepgpass))


def _read_pgpass() -> Tuple[str, Path]:
    path = _find_pgpass()
    with open(path, encoding="utf-8") as file:
        return file.read(), path


def _write_pgpass(path: Path, content: str):
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


def _update_pgpass_str(
    pgpass: str,
    hosts: List[str],
    access_token: str,
) -> str:
    for host in hosts:
        newline = f"{host}:*:*:*:{access_token}"
        pattern = re.compile(rf"{host}:\*:\*:\*:.*")
        pgpass, num_replaces = pattern.subn(newline, pgpass)
        if num_replaces == 0:
            # match is not found, add line on top
            pgpass = "\n".join((newline, pgpass))
    return pgpass


def update_pgpass(access_token: str, hosts: List[str]) -> None:
    """Update pgpass file for the Cyral sidecar endpoints."""
    if not hosts:
        return
    pgpass, path = _read_pgpass()
    newpgpass = _update_pgpass_str(pgpass, hosts, access_token)
    _write_pgpass(path, newpgpass)
