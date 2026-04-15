"""This is an automatically generated stub for `web_berest_data_import.capnp`."""

from collections.abc import Awaitable
from typing import NamedTuple, Protocol, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _InterfaceModule,
)

class _DWLABImportInterfaceModule(_InterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> DWLABImportClient: ...
    class Server(_DynamicCapabilityServer):
        def importData(
            self,
            id: str,
            dwla: bytes,
            dwlb: bytes,
            _context: ImportdataCallContext,
            **kwargs: object,
        ) -> Awaitable[ImportdataResultTuple | None]: ...
        def importData_context(
            self,
            context: ImportdataCallContext,
        ) -> Awaitable[None]: ...

class ImportdataRequest(Protocol):
    id: str
    dwla: bytes
    dwlb: bytes
    def send(self) -> ImportdataResult: ...

class ImportdataResult(Awaitable[ImportdataResult], Protocol):
    id: str
    successA: bool
    successB: bool

class ImportdataServerResult(_DynamicStructBuilder):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str) -> None: ...
    @property
    def successA(self) -> bool: ...
    @successA.setter
    def successA(self, value: bool) -> None: ...
    @property
    def successB(self) -> bool: ...
    @successB.setter
    def successB(self, value: bool) -> None: ...

class ImportdataParams(Protocol):
    id: str
    dwla: bytes
    dwlb: bytes

class ImportdataCallContext(Protocol):
    params: ImportdataParams
    @property
    def results(self) -> ImportdataServerResult: ...

class ImportdataResultTuple(NamedTuple):
    id: str
    successA: bool
    successB: bool

class DWLABImportClient(_DynamicCapabilityClient):
    def importData(
        self,
        id: str | None = None,
        dwla: bytes | None = None,
        dwlb: bytes | None = None,
    ) -> ImportdataResult: ...
    def importData_request(
        self,
        id: str | None = None,
        dwla: bytes | None = None,
        dwlb: bytes | None = None,
    ) -> ImportdataRequest: ...

DWLABImport: _DWLABImportInterfaceModule

# Top-level type aliases for use in type annotations
DWLABImportServer = _DWLABImportInterfaceModule.Server
