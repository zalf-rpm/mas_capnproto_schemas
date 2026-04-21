"""Client result helper types for `web_berest_data_import.capnp`."""

from collections.abc import Awaitable
from typing import Protocol

class ImportdataResult(Awaitable[ImportdataResult], Protocol):
    id: str
    successA: bool
    successB: bool
