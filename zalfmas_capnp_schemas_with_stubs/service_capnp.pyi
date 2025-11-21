"""This is an automatically generated stub for `service.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, MutableSequence, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, NamedTuple, Protocol, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicListBuilder,
    _DynamicListReader,
    _DynamicObjectBuilder,
    _DynamicObjectReader,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
    _StructModule,
)

from .common_capnp import (
    IdInformationBuilder,
    IdInformationReader,
    PairBuilder,
    PairReader,
    _IdentifiableModule,
    _PairModule,
)

# Type alias for AnyPointer parameters (accepts all Cap'n Proto pointer types)
type AnyPointer = (
    str
    | bytes
    | _DynamicStructBuilder
    | _DynamicStructReader
    | _DynamicCapabilityClient
    | _DynamicCapabilityServer
    | _DynamicListBuilder
    | _DynamicListReader
    | _DynamicObjectReader
    | _DynamicObjectBuilder
)

# Type alias for Capability parameters
type Capability = (
    _DynamicCapabilityClient
    | _DynamicCapabilityServer
    | _DynamicObjectReader
    | _DynamicObjectBuilder
)

class _AdminModule(_IdentifiableModule):
    class HeartbeatRequest(Protocol):
        def send(self) -> _AdminModule.AdminClient.HeartbeatResult: ...

    class SettimeoutRequest(Protocol):
        seconds: int
        def send(self) -> _AdminModule.AdminClient.SettimeoutResult: ...

    class StopRequest(Protocol):
        def send(self) -> _AdminModule.AdminClient.StopResult: ...

    class IdentitiesRequest(Protocol):
        def send(self) -> _AdminModule.AdminClient.IdentitiesResult: ...

    class UpdateidentityRequest(Protocol):
        oldId: str
        newInfo: IdInformationBuilder
        @overload
        def init(self, name: Literal["newInfo"]) -> IdInformationBuilder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> _AdminModule.AdminClient.UpdateidentityResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _AdminModule.AdminClient: ...
    class Server(_IdentifiableModule.Server):
        class HeartbeatResult(Awaitable[None], Protocol): ...
        class SettimeoutResult(Awaitable[None], Protocol): ...
        class StopResult(Awaitable[None], Protocol): ...

        class IdentitiesResult(Awaitable[IdentitiesResult], Protocol):
            infos: Sequence[IdInformationBuilder | IdInformationReader]

        class UpdateidentityResult(Awaitable[None], Protocol): ...

        class IdentitiesResultTuple(NamedTuple):
            infos: Sequence[IdInformationBuilder | IdInformationReader]

        class HeartbeatParams(Protocol): ...

        class HeartbeatCallContext(Protocol):
            params: _AdminModule.Server.HeartbeatParams

        class SettimeoutParams(Protocol):
            seconds: int

        class SettimeoutCallContext(Protocol):
            params: _AdminModule.Server.SettimeoutParams

        class StopParams(Protocol): ...

        class StopCallContext(Protocol):
            params: _AdminModule.Server.StopParams

        class IdentitiesParams(Protocol): ...

        class IdentitiesCallContext(Protocol):
            params: _AdminModule.Server.IdentitiesParams
            results: _AdminModule.Server.IdentitiesResult

        class UpdateidentityParams(Protocol):
            oldId: str
            newInfo: IdInformationReader

        class UpdateidentityCallContext(Protocol):
            params: _AdminModule.Server.UpdateidentityParams

        def heartbeat(
            self,
            _context: _AdminModule.Server.HeartbeatCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[None]: ...
        def heartbeat_context(
            self, context: _AdminModule.Server.HeartbeatCallContext
        ) -> Awaitable[None]: ...
        def setTimeout(
            self,
            seconds: int,
            _context: _AdminModule.Server.SettimeoutCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[None]: ...
        def setTimeout_context(
            self, context: _AdminModule.Server.SettimeoutCallContext
        ) -> Awaitable[None]: ...
        def stop(
            self,
            _context: _AdminModule.Server.StopCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[None]: ...
        def stop_context(
            self, context: _AdminModule.Server.StopCallContext
        ) -> Awaitable[None]: ...
        def identities(
            self,
            _context: _AdminModule.Server.IdentitiesCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[
            Sequence[IdInformationBuilder | IdInformationReader]
            | _AdminModule.Server.IdentitiesResultTuple
            | None
        ]: ...
        def identities_context(
            self, context: _AdminModule.Server.IdentitiesCallContext
        ) -> Awaitable[None]: ...
        def updateIdentity(
            self,
            oldId: str,
            newInfo: IdInformationReader,
            _context: _AdminModule.Server.UpdateidentityCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[None]: ...
        def updateIdentity_context(
            self, context: _AdminModule.Server.UpdateidentityCallContext
        ) -> Awaitable[None]: ...

    class AdminClient(_IdentifiableModule.IdentifiableClient):
        class HeartbeatResult(Awaitable[None], Protocol): ...
        class SettimeoutResult(Awaitable[None], Protocol): ...
        class StopResult(Awaitable[None], Protocol): ...

        class IdentitiesResult(Awaitable[IdentitiesResult], Protocol):
            infos: Sequence[IdInformationReader]

        class UpdateidentityResult(Awaitable[None], Protocol): ...

        def heartbeat(self) -> _AdminModule.AdminClient.HeartbeatResult: ...
        def setTimeout(
            self, seconds: int | None = None
        ) -> _AdminModule.AdminClient.SettimeoutResult: ...
        def stop(self) -> _AdminModule.AdminClient.StopResult: ...
        def identities(self) -> _AdminModule.AdminClient.IdentitiesResult: ...
        def updateIdentity(
            self,
            oldId: str | None = None,
            newInfo: IdInformationBuilder
            | IdInformationReader
            | dict[str, Any]
            | None = None,
        ) -> _AdminModule.AdminClient.UpdateidentityResult: ...
        def heartbeat_request(self) -> _AdminModule.HeartbeatRequest: ...
        def setTimeout_request(
            self, seconds: int | None = None
        ) -> _AdminModule.SettimeoutRequest: ...
        def stop_request(self) -> _AdminModule.StopRequest: ...
        def identities_request(self) -> _AdminModule.IdentitiesRequest: ...
        def updateIdentity_request(
            self, oldId: str | None = None, newInfo: IdInformationBuilder | None = None
        ) -> _AdminModule.UpdateidentityRequest: ...

Admin: _AdminModule

class _SimpleFactoryModule(_IdentifiableModule):
    class CreateRequest(Protocol):
        def send(self) -> _SimpleFactoryModule.SimpleFactoryClient.CreateResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _SimpleFactoryModule.SimpleFactoryClient: ...
    class Server(_IdentifiableModule.Server):
        class CreateResult(Awaitable[CreateResult], Protocol):
            caps: Sequence[
                _IdentifiableModule.Server | _IdentifiableModule.IdentifiableClient
            ]

        class CreateResultTuple(NamedTuple):
            caps: Sequence[
                _IdentifiableModule.Server | _IdentifiableModule.IdentifiableClient
            ]

        class CreateParams(Protocol): ...

        class CreateCallContext(Protocol):
            params: _SimpleFactoryModule.Server.CreateParams
            results: _SimpleFactoryModule.Server.CreateResult

        def create(
            self,
            _context: _SimpleFactoryModule.Server.CreateCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[
            Sequence[_IdentifiableModule]
            | _SimpleFactoryModule.Server.CreateResultTuple
            | None
        ]: ...
        def create_context(
            self, context: _SimpleFactoryModule.Server.CreateCallContext
        ) -> Awaitable[None]: ...

    class SimpleFactoryClient(_IdentifiableModule.IdentifiableClient):
        class CreateResult(Awaitable[CreateResult], Protocol):
            caps: Sequence[_IdentifiableModule.IdentifiableClient]

        def create(self) -> _SimpleFactoryModule.SimpleFactoryClient.CreateResult: ...
        def create_request(self) -> _SimpleFactoryModule.CreateRequest: ...

SimpleFactory: _SimpleFactoryModule

class _FactoryModule(_IdentifiableModule):
    class _CreateParamsModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def timeoutSeconds(self) -> int: ...
            @property
            def interfaceNameToRegistrySR(self) -> Sequence[PairReader]: ...
            @property
            def msgPayload(self) -> _DynamicObjectReader: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> CreateParamsBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def timeoutSeconds(self) -> int: ...
            @timeoutSeconds.setter
            def timeoutSeconds(self, value: int) -> None: ...
            @property
            def interfaceNameToRegistrySR(self) -> MutableSequence[PairBuilder]: ...
            @interfaceNameToRegistrySR.setter
            def interfaceNameToRegistrySR(
                self,
                value: Sequence[PairBuilder | PairReader] | Sequence[dict[str, Any]],
            ) -> None: ...
            @property
            def msgPayload(self) -> _DynamicObjectReader: ...
            @msgPayload.setter
            def msgPayload(self, value: AnyPointer) -> None: ...
            def init(
                self,
                field: Literal["interfaceNameToRegistrySR"],
                size: int | None = None,
            ) -> MutableSequence[PairBuilder]: ...
            @override
            def as_reader(self) -> CreateParamsReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            timeoutSeconds: int | None = None,
            interfaceNameToRegistrySR: Sequence[PairBuilder]
            | Sequence[dict[str, Any]]
            | None = None,
            msgPayload: AnyPointer | None = None,
            **kwargs: Any,
        ) -> CreateParamsBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[CreateParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[CreateParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[CreateParamsBuilder]: ...
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> CreateParamsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> CreateParamsReader: ...

    type CreateParamsReader = _CreateParamsModule.Reader
    type CreateParamsBuilder = _CreateParamsModule.Builder
    CreateParams: _CreateParamsModule
    class _AccessInfoModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def adminCap(self) -> _DynamicObjectReader: ...
            @property
            def serviceCaps(self) -> Sequence[_IdentifiableModule]: ...
            @property
            def error(self) -> str: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> AccessInfoBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def adminCap(self) -> _DynamicObjectReader: ...
            @adminCap.setter
            def adminCap(self, value: Capability) -> None: ...
            @property
            def serviceCaps(self) -> MutableSequence[_IdentifiableModule]: ...
            @serviceCaps.setter
            def serviceCaps(self, value: Sequence[_IdentifiableModule]) -> None: ...
            @property
            def error(self) -> str: ...
            @error.setter
            def error(self, value: str) -> None: ...
            def init(
                self, field: Literal["serviceCaps"], size: int | None = None
            ) -> MutableSequence[_IdentifiableModule]: ...
            @override
            def as_reader(self) -> AccessInfoReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            adminCap: Capability | None = None,
            serviceCaps: Sequence[_IdentifiableModule] | None = None,
            error: str | None = None,
            **kwargs: Any,
        ) -> AccessInfoBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[AccessInfoReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[AccessInfoReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[AccessInfoBuilder]: ...
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AccessInfoReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AccessInfoReader: ...

    type AccessInfoReader = _AccessInfoModule.Reader
    type AccessInfoBuilder = _AccessInfoModule.Builder
    AccessInfo: _AccessInfoModule
    class CreateRequest(Protocol):
        timeoutSeconds: int
        interfaceNameToRegistrySR: Sequence[_PairModule] | Sequence[dict[str, Any]]
        msgPayload: AnyPointer
        @overload
        def init(
            self, name: Literal["interfaceNameToRegistrySR"], size: int = ...
        ) -> MutableSequence[PairBuilder]: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> _FactoryModule.FactoryClient.CreateResult: ...

    class ServiceinterfacenamesRequest(Protocol):
        def send(self) -> _FactoryModule.FactoryClient.ServiceinterfacenamesResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _FactoryModule.FactoryClient: ...
    class Server(_IdentifiableModule.Server):
        class CreateResult(Awaitable[CreateResult], Protocol):
            adminCap: _DynamicCapabilityClient | _DynamicCapabilityServer
            serviceCaps: Sequence[_IdentifiableModule]
            error: str

        class ServiceinterfacenamesResult(
            Awaitable[ServiceinterfacenamesResult], Protocol
        ):
            names: Sequence[str]

        class CreateResultTuple(NamedTuple):
            adminCap: Capability
            serviceCaps: Sequence[
                _IdentifiableModule.Server | _IdentifiableModule.IdentifiableClient
            ]
            error: str

        class ServiceinterfacenamesResultTuple(NamedTuple):
            names: Sequence[str]

        class CreateParams(Protocol):
            timeoutSeconds: int
            interfaceNameToRegistrySR: Sequence[_PairModule.Reader]
            msgPayload: AnyPointer

        class CreateCallContext(Protocol):
            params: _FactoryModule.Server.CreateParams
            results: _FactoryModule.Server.CreateResult

        class ServiceinterfacenamesParams(Protocol): ...

        class ServiceinterfacenamesCallContext(Protocol):
            params: _FactoryModule.Server.ServiceinterfacenamesParams
            results: _FactoryModule.Server.ServiceinterfacenamesResult

        def create(
            self,
            timeoutSeconds: int,
            interfaceNameToRegistrySR: Sequence[_PairModule.Reader],
            msgPayload: AnyPointer,
            _context: _FactoryModule.Server.CreateCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_FactoryModule.Server.CreateResultTuple | None]: ...
        def create_context(
            self, context: _FactoryModule.Server.CreateCallContext
        ) -> Awaitable[None]: ...
        def serviceInterfaceNames(
            self,
            _context: _FactoryModule.Server.ServiceinterfacenamesCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[
            Sequence[str]
            | _FactoryModule.Server.ServiceinterfacenamesResultTuple
            | None
        ]: ...
        def serviceInterfaceNames_context(
            self, context: _FactoryModule.Server.ServiceinterfacenamesCallContext
        ) -> Awaitable[None]: ...

    class FactoryClient(_IdentifiableModule.IdentifiableClient):
        class CreateResult(Awaitable[CreateResult], Protocol):
            adminCap: _DynamicCapabilityClient
            serviceCaps: Sequence[_IdentifiableModule]
            error: str

        class ServiceinterfacenamesResult(
            Awaitable[ServiceinterfacenamesResult], Protocol
        ):
            names: Sequence[str]

        def create(
            self,
            timeoutSeconds: int | None = None,
            interfaceNameToRegistrySR: Sequence[_PairModule]
            | Sequence[dict[str, Any]]
            | None = None,
            msgPayload: AnyPointer | None = None,
        ) -> _FactoryModule.FactoryClient.CreateResult: ...
        def serviceInterfaceNames(
            self,
        ) -> _FactoryModule.FactoryClient.ServiceinterfacenamesResult: ...
        def create_request(
            self,
            timeoutSeconds: int | None = None,
            interfaceNameToRegistrySR: Sequence[_PairModule]
            | Sequence[dict[str, Any]]
            | None = None,
            msgPayload: AnyPointer | None = None,
        ) -> _FactoryModule.CreateRequest: ...
        def serviceInterfaceNames_request(
            self,
        ) -> _FactoryModule.ServiceinterfacenamesRequest: ...

Factory: _FactoryModule

class _StoppableModule(_InterfaceModule):
    class StopRequest(Protocol):
        def send(self) -> _StoppableModule.StoppableClient.StopResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _StoppableModule.StoppableClient: ...
    class Server(_DynamicCapabilityServer):
        class StopResult(Awaitable[StopResult], Protocol):
            success: bool

        class StopResultTuple(NamedTuple):
            success: bool

        class StopParams(Protocol): ...

        class StopCallContext(Protocol):
            params: _StoppableModule.Server.StopParams
            results: _StoppableModule.Server.StopResult

        def stop(
            self,
            _context: _StoppableModule.Server.StopCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[bool | _StoppableModule.Server.StopResultTuple | None]: ...
        def stop_context(
            self, context: _StoppableModule.Server.StopCallContext
        ) -> Awaitable[None]: ...

    class StoppableClient(_DynamicCapabilityClient):
        class StopResult(Awaitable[StopResult], Protocol):
            success: bool

        def stop(self) -> _StoppableModule.StoppableClient.StopResult: ...
        def stop_request(self) -> _StoppableModule.StopRequest: ...

Stoppable: _StoppableModule

# Top-level type aliases for use in type annotations
type AccessInfoBuilder = _FactoryModule._AccessInfoModule.Builder
type AccessInfoReader = _FactoryModule._AccessInfoModule.Reader
type AdminClient = _AdminModule.AdminClient
type CreateParamsBuilder = _FactoryModule._CreateParamsModule.Builder
type CreateParamsReader = _FactoryModule._CreateParamsModule.Reader
type CreateResult = _FactoryModule.FactoryClient.CreateResult
type FactoryClient = _FactoryModule.FactoryClient
type HeartbeatResult = _AdminModule.AdminClient.HeartbeatResult
type IdentitiesResult = _AdminModule.AdminClient.IdentitiesResult
type ServiceinterfacenamesResult = (
    _FactoryModule.FactoryClient.ServiceinterfacenamesResult
)
type SettimeoutResult = _AdminModule.AdminClient.SettimeoutResult
type SimpleFactoryClient = _SimpleFactoryModule.SimpleFactoryClient
type StopResult = _StoppableModule.StoppableClient.StopResult
type StoppableClient = _StoppableModule.StoppableClient
type UpdateidentityResult = _AdminModule.AdminClient.UpdateidentityResult
