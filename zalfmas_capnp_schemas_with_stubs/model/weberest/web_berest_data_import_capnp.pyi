"""This is an automatically generated stub for `web-berest-data-import.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable
from typing import Any, NamedTuple, Protocol

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _InterfaceModule,
)

class _DWLABImportModule(_InterfaceModule):
    class ImportdataRequest(Protocol):
        id: str
        dwla: bytes
        dwlb: bytes
        def send(self) -> _DWLABImportModule.DWLABImportClient.ImportdataResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _DWLABImportModule.DWLABImportClient: ...
    class Server(_DynamicCapabilityServer):
        class ImportdataResult(Awaitable[ImportdataResult], Protocol):
            id: str
            successA: bool
            successB: bool

        class ImportdataResultTuple(NamedTuple):
            id: str
            successA: bool
            successB: bool

        class ImportdataParams(Protocol):
            id: str
            dwla: bytes
            dwlb: bytes

        class ImportdataCallContext(Protocol):
            params: _DWLABImportModule.Server.ImportdataParams
            results: _DWLABImportModule.Server.ImportdataResult

        def importData(
            self,
            id: str,
            dwla: bytes,
            dwlb: bytes,
            _context: _DWLABImportModule.Server.ImportdataCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_DWLABImportModule.Server.ImportdataResultTuple | None]: ...
        def importData_context(
            self, context: _DWLABImportModule.Server.ImportdataCallContext
        ) -> Awaitable[None]: ...

    class DWLABImportClient(_DynamicCapabilityClient):
        class ImportdataResult(Awaitable[ImportdataResult], Protocol):
            id: str
            successA: bool
            successB: bool

        def importData(
            self,
            id: str | None = None,
            dwla: bytes | None = None,
            dwlb: bytes | None = None,
        ) -> _DWLABImportModule.DWLABImportClient.ImportdataResult: ...
        def importData_request(
            self,
            id: str | None = None,
            dwla: bytes | None = None,
            dwlb: bytes | None = None,
        ) -> _DWLABImportModule.ImportdataRequest: ...

DWLABImport: _DWLABImportModule

# Top-level type aliases for use in type annotations
type DWLABImportClient = _DWLABImportModule.DWLABImportClient
type ImportdataResult = _DWLABImportModule.DWLABImportClient.ImportdataResult
