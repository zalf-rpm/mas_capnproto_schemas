"""This is an automatically generated stub for `web-berest-data-import.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable
from typing import Any, NamedTuple, Protocol

class DWLABImport:
    class ImportdataRequest(Protocol):
        id: str
        dwla: bytes
        dwlb: bytes
        def send(self) -> DWLABImport.ImportdataResult: ...

    class ImportdataResult(Awaitable[ImportdataResult], Protocol):
        id: str
        successA: bool
        successB: bool

    @classmethod
    def _new_client(cls, server: DWLABImport.Server) -> DWLABImportClient: ...
    class Server(Protocol):
        class ImportdataResultTuple(NamedTuple):
            id: str
            successA: bool
            successB: bool

        class ImportdataCallContext(Protocol):
            params: DWLABImport.ImportdataRequest
            results: DWLABImport.ImportdataResult

        def importData(
            self,
            id: str,
            dwla: bytes,
            dwlb: bytes,
            _context: DWLABImport.Server.ImportdataCallContext,
            **kwargs: Any,
        ) -> Awaitable[DWLABImport.Server.ImportdataResultTuple | None]: ...
        def importData_context(
            self, context: DWLABImport.Server.ImportdataCallContext
        ) -> Awaitable[None]: ...

class DWLABImportClient(Protocol):
    def importData(
        self,
        id: str | None = None,
        dwla: bytes | None = None,
        dwlb: bytes | None = None,
    ) -> DWLABImport.ImportdataResult: ...
    def importData_request(
        self,
        id: str | None = None,
        dwla: bytes | None = None,
        dwlb: bytes | None = None,
    ) -> DWLABImport.ImportdataRequest: ...
