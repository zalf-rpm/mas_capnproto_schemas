"""This is an automatically generated stub for `modam.capnp`."""

from collections.abc import Awaitable
from typing import NamedTuple, Protocol, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _InterfaceModule,
)

class _ModamWrapperServiceInterfaceModule(_InterfaceModule):
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> ModamWrapperServiceClient: ...
    class Server(_DynamicCapabilityServer):
        def runAemModel(
            self,
            input: str,
            _context: RunaemmodelCallContext,
            **kwargs: object,
        ) -> Awaitable[str | RunaemmodelResultTuple | None]: ...
        def runAemModel_context(
            self,
            context: RunaemmodelCallContext,
        ) -> Awaitable[None]: ...
        def runFieldModel(
            self,
            input: str,
            _context: RunfieldmodelCallContext,
            **kwargs: object,
        ) -> Awaitable[str | RunfieldmodelResultTuple | None]: ...
        def runFieldModel_context(
            self,
            context: RunfieldmodelCallContext,
        ) -> Awaitable[None]: ...

class RunaemmodelRequest(Protocol):
    input: str
    def send(self) -> RunaemmodelResult: ...

class RunaemmodelResult(Awaitable[RunaemmodelResult], Protocol):
    output: str

class RunaemmodelServerResult(_DynamicStructBuilder):
    @property
    def output(self) -> str: ...
    @output.setter
    def output(self, value: str) -> None: ...

class RunaemmodelParams(Protocol):
    input: str

class RunaemmodelCallContext(Protocol):
    params: RunaemmodelParams
    @property
    def results(self) -> RunaemmodelServerResult: ...

class RunaemmodelResultTuple(NamedTuple):
    output: str

class RunfieldmodelRequest(Protocol):
    input: str
    def send(self) -> RunfieldmodelResult: ...

class RunfieldmodelResult(Awaitable[RunfieldmodelResult], Protocol):
    output: str

class RunfieldmodelServerResult(_DynamicStructBuilder):
    @property
    def output(self) -> str: ...
    @output.setter
    def output(self, value: str) -> None: ...

class RunfieldmodelParams(Protocol):
    input: str

class RunfieldmodelCallContext(Protocol):
    params: RunfieldmodelParams
    @property
    def results(self) -> RunfieldmodelServerResult: ...

class RunfieldmodelResultTuple(NamedTuple):
    output: str

class ModamWrapperServiceClient(_DynamicCapabilityClient):
    def runAemModel(self, input: str | None = None) -> RunaemmodelResult: ...
    def runFieldModel(self, input: str | None = None) -> RunfieldmodelResult: ...
    def runAemModel_request(self, input: str | None = None) -> RunaemmodelRequest: ...
    def runFieldModel_request(
        self,
        input: str | None = None,
    ) -> RunfieldmodelRequest: ...

ModamWrapperService: _ModamWrapperServiceInterfaceModule

# Top-level type aliases for use in type annotations
ModamWrapperServiceServer = _ModamWrapperServiceInterfaceModule.Server
