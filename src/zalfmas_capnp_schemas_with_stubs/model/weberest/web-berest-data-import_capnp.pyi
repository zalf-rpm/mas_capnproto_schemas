"""This is an automatically generated stub for `web-berest-data-import.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable
from typing import Protocol

class DWLABImport(Protocol):
    class ImportdataResult(Awaitable[ImportdataResult], Protocol):
        id: str
        successA: bool
        successB: bool

    def importData(self, id: str, dwla: bytes, dwlb: bytes) -> ImportdataResult: ...
    class ImportdataRequest(Protocol):
        id: str
        dwla: bytes
        dwlb: bytes
        def send(self) -> DWLABImport.ImportdataResult: ...

    def importData_request(self) -> ImportdataRequest: ...
    class Server:
        def importData(
            self, id: str, dwla: bytes, dwlb: bytes, **kwargs
        ) -> Awaitable[DWLABImport.ImportdataResult]: ...
