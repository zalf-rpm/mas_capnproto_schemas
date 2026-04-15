"""Module helper types for `service.capnp`."""

from collections.abc import Awaitable, Callable, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
    _StructModule,
)

from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.common.common_capnp.types.readers import IdInformationReader

from . import _all as _all

class _AdminInterfaceModule(_IdentifiableInterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> _all.AdminClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def heartbeat(
            self,
            _context: _all.HeartbeatCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def heartbeat_context(
            self,
            context: _all.HeartbeatCallContext,
        ) -> Awaitable[None]: ...
        def setTimeout(
            self,
            seconds: int,
            _context: _all.SettimeoutCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def setTimeout_context(
            self,
            context: _all.SettimeoutCallContext,
        ) -> Awaitable[None]: ...
        def stop(
            self,
            _context: _all.AdminStopCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def stop_context(
            self,
            context: _all.AdminStopCallContext,
        ) -> Awaitable[None]: ...
        def identities(
            self,
            _context: _all.IdentitiesCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _all.IdInformationListBuilder
            | _all.IdInformationListReader
            | Sequence[Any]
            | _all.IdentitiesResultTuple
            | None
        ]: ...
        def identities_context(
            self,
            context: _all.IdentitiesCallContext,
        ) -> Awaitable[None]: ...
        def updateIdentity(
            self,
            oldId: str,
            newInfo: IdInformationReader,
            _context: _all.UpdateidentityCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def updateIdentity_context(
            self,
            context: _all.UpdateidentityCallContext,
        ) -> Awaitable[None]: ...

class _SimpleFactoryInterfaceModule(_IdentifiableInterfaceModule):
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> _all.SimpleFactoryClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def create(
            self,
            _context: _all.SimpleFactoryCreateCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _all.IdentifiableClientListBuilder
            | _all.IdentifiableClientListReader
            | Sequence[Any]
            | _all.SimpleFactoryCreateResultTuple
            | None
        ]: ...
        def create_context(
            self,
            context: _all.SimpleFactoryCreateCallContext,
        ) -> Awaitable[None]: ...

class _FactoryInterfaceModule(_IdentifiableInterfaceModule):
    class _CreateParamsStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            timeoutSeconds: int | None = None,
            interfaceNameToRegistrySR: _all.PairListBuilder
            | dict[str, Any]
            | None = None,
            msgPayload: _all.AnyPointer | None = None,
            **kwargs: object,
        ) -> _all.CreateParamsBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.CreateParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.CreateParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.CreateParamsBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.CreateParamsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.CreateParamsReader: ...

    CreateParams: _CreateParamsStructModule
    class _AccessInfoStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            adminCap: _all.Capability | None = None,
            serviceCaps: _all.IdentifiableClientListBuilder
            | dict[str, Any]
            | None = None,
            error: str | None = None,
            **kwargs: object,
        ) -> _all.AccessInfoBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.AccessInfoReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.AccessInfoReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.AccessInfoBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.AccessInfoReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.AccessInfoReader: ...

    AccessInfo: _AccessInfoStructModule
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> _all.FactoryClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def create(
            self,
            timeoutSeconds: int,
            interfaceNameToRegistrySR: _all.PairListReader,
            msgPayload: _all.AnyPointer,
            _context: _all.FactoryCreateCallContext,
            **kwargs: object,
        ) -> Awaitable[_all.FactoryCreateResultTuple | None]: ...
        def create_context(
            self,
            context: _all.FactoryCreateCallContext,
        ) -> Awaitable[None]: ...
        def serviceInterfaceNames(
            self,
            _context: _all.ServiceinterfacenamesCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _all.TextListBuilder
            | _all.TextListReader
            | Sequence[Any]
            | _all.ServiceinterfacenamesResultTuple
            | None
        ]: ...
        def serviceInterfaceNames_context(
            self,
            context: _all.ServiceinterfacenamesCallContext,
        ) -> Awaitable[None]: ...

class _StoppableInterfaceModule(_InterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> _all.StoppableClient: ...
    class Server(_DynamicCapabilityServer):
        def stop(
            self,
            _context: _all.StoppableStopCallContext,
            **kwargs: object,
        ) -> Awaitable[bool | _all.StoppableStopResultTuple | None]: ...
        def stop_context(
            self,
            context: _all.StoppableStopCallContext,
        ) -> Awaitable[None]: ...
