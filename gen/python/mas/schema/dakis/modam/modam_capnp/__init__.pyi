"""This is an automatically generated stub for `modam.capnp`."""

from collections.abc import Awaitable
from typing import Any, NamedTuple, Protocol, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _InterfaceModule,
)

class _ModamWrapperServiceInterfaceModule(_InterfaceModule):
    class RunRequest(Protocol):
        input: str
        def send(
            self,
        ) -> (
            _ModamWrapperServiceInterfaceModule.ModamWrapperServiceClient.RunResult
        ): ...

    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> _ModamWrapperServiceInterfaceModule.ModamWrapperServiceClient: ...
    class Server(_DynamicCapabilityServer):
        class RunResult(_DynamicStructBuilder):
            @property
            def output(self) -> str: ...
            @output.setter
            def output(self, value: str) -> None: ...

        class RunResultTuple(NamedTuple):
            output: str

        class RunParams(Protocol):
            input: str

        class RunCallContext(Protocol):
            params: _ModamWrapperServiceInterfaceModule.Server.RunParams
            @property
            def results(
                self,
            ) -> _ModamWrapperServiceInterfaceModule.Server.RunResult: ...

        def run(
            self,
            input: str,
            _context: _ModamWrapperServiceInterfaceModule.Server.RunCallContext,
            **kwargs: Any,
        ) -> Awaitable[
            str | _ModamWrapperServiceInterfaceModule.Server.RunResultTuple | None
        ]: ...
        def run_context(
            self,
            context: _ModamWrapperServiceInterfaceModule.Server.RunCallContext,
        ) -> Awaitable[None]: ...

    class ModamWrapperServiceClient(_DynamicCapabilityClient):
        class RunResult(Awaitable[RunResult], Protocol):
            output: str

        def run(
            self,
            input: str | None = None,
        ) -> (
            _ModamWrapperServiceInterfaceModule.ModamWrapperServiceClient.RunResult
        ): ...
        def run_request(
            self,
            input: str | None = None,
        ) -> _ModamWrapperServiceInterfaceModule.RunRequest: ...

ModamWrapperService: _ModamWrapperServiceInterfaceModule

# Top-level type aliases for use in type annotations
type ModamWrapperServiceClient = (
    _ModamWrapperServiceInterfaceModule.ModamWrapperServiceClient
)
type ModamWrapperServiceServer = _ModamWrapperServiceInterfaceModule.Server
type RunResult = _ModamWrapperServiceInterfaceModule.ModamWrapperServiceClient.RunResult
