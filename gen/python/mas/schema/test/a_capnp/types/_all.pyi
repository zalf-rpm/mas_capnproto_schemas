"""This is an automatically generated stub for `a.capnp`."""

from collections.abc import Awaitable
from typing import NamedTuple, Protocol, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _InterfaceModule,
)

class _AInterfaceModule(_InterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> AClient: ...
    class Server(_DynamicCapabilityServer):
        def method(
            self,
            param: str,
            _context: MethodCallContext,
            **kwargs: object,
        ) -> Awaitable[str | MethodResultTuple | None]: ...
        def method_context(self, context: MethodCallContext) -> Awaitable[None]: ...

class MethodRequest(Protocol):
    param: str
    def send(self) -> MethodResult: ...

class MethodResult(Awaitable[MethodResult], Protocol):
    res: str

class MethodServerResult(_DynamicStructBuilder):
    @property
    def res(self) -> str: ...
    @res.setter
    def res(self, value: str) -> None: ...

class MethodParams(Protocol):
    param: str

class MethodCallContext(Protocol):
    params: MethodParams
    @property
    def results(self) -> MethodServerResult: ...

class MethodResultTuple(NamedTuple):
    res: str

class AClient(_DynamicCapabilityClient):
    def method(self, param: str | None = None) -> MethodResult: ...
    def method_request(self, param: str | None = None) -> MethodRequest: ...

A: _AInterfaceModule

# Top-level type aliases for use in type annotations
AServer = _AInterfaceModule.Server
