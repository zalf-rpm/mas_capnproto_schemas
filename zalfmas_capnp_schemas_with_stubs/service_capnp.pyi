"""This is an automatically generated stub for `service.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator, MutableSequence, Sequence
from typing import (
    Any,
    Generic,
    Literal,
    NamedTuple,
    Protocol,
    TypeAlias,
    TypeVar,
    overload,
    override,
)

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicObjectReader,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
    _Request,
    _StructModule,
)

from .common_capnp import (
    Identifiable,
    IdentifiableClient,
    _IdentifiableModule,
    _PairModule,
)

_FactoryModule_Payload = TypeVar("_FactoryModule_Payload")

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
        def send(self) -> _AdminModule.AdminClient.UpdateidentityResult: ...

    @classmethod
    def _new_client(cls, server: _AdminModule.Server | _IdentifiableModule.Server) -> _AdminModule.AdminClient: ...
    class Server(_IdentifiableModule.Server):
        class HeartbeatResult(Awaitable[None], Protocol): ...
        class SettimeoutResult(Awaitable[None], Protocol): ...
        class StopResult(Awaitable[None], Protocol): ...

        class IdentitiesResult(Awaitable[IdentitiesResult], Protocol):
            infos: Any

        class UpdateidentityResult(Awaitable[None], Protocol): ...

        class IdentitiesResultTuple(NamedTuple):
            pass

        class HeartbeatCallContext(Protocol):
            params: _AdminModule.HeartbeatRequest

        class SettimeoutCallContext(Protocol):
            params: _AdminModule.SettimeoutRequest

        class StopCallContext(Protocol):
            params: _AdminModule.StopRequest

        class IdentitiesCallContext(Protocol):
            params: _AdminModule.IdentitiesRequest
            results: _AdminModule.Server.IdentitiesResult

        class UpdateidentityCallContext(Protocol):
            params: _AdminModule.UpdateidentityRequest

        def heartbeat(self, _context: _AdminModule.Server.HeartbeatCallContext, **kwargs: Any) -> Awaitable[None]: ...
        def heartbeat_context(self, context: _AdminModule.Server.HeartbeatCallContext) -> Awaitable[None]: ...
        def setTimeout(self, seconds: int, _context: _AdminModule.Server.SettimeoutCallContext, **kwargs: Any) -> Awaitable[None]: ...
        def setTimeout_context(self, context: _AdminModule.Server.SettimeoutCallContext) -> Awaitable[None]: ...
        def stop(self, _context: _AdminModule.Server.StopCallContext, **kwargs: Any) -> Awaitable[None]: ...
        def stop_context(self, context: _AdminModule.Server.StopCallContext) -> Awaitable[None]: ...
        def identities(self, _context: _AdminModule.Server.IdentitiesCallContext, **kwargs: Any) -> Awaitable[_AdminModule.Server.IdentitiesResultTuple | None]: ...
        def identities_context(self, context: _AdminModule.Server.IdentitiesCallContext) -> Awaitable[None]: ...
        def updateIdentity(self, oldId: str, _context: _AdminModule.Server.UpdateidentityCallContext, **kwargs: Any) -> Awaitable[None]: ...
        def updateIdentity_context(self, context: _AdminModule.Server.UpdateidentityCallContext) -> Awaitable[None]: ...

    class AdminClient(_IdentifiableModule.IdentifiableClient):
        class HeartbeatResult(Awaitable[None], Protocol): ...
        class SettimeoutResult(Awaitable[None], Protocol): ...
        class StopResult(Awaitable[None], Protocol): ...

        class IdentitiesResult(Awaitable[IdentitiesResult], Protocol):
            infos: Any

        class UpdateidentityResult(Awaitable[None], Protocol): ...

        def heartbeat(self) -> _AdminModule.AdminClient.HeartbeatResult: ...
        def setTimeout(self, seconds: int | None = None) -> _AdminModule.AdminClient.SettimeoutResult: ...
        def stop(self) -> _AdminModule.AdminClient.StopResult: ...
        def identities(self) -> _AdminModule.AdminClient.IdentitiesResult: ...
        def updateIdentity(self, oldId: str | None = None) -> _AdminModule.AdminClient.UpdateidentityResult: ...
        def heartbeat_request(self) -> _AdminModule.HeartbeatRequest: ...
        def setTimeout_request(self, seconds: int | None = None) -> _AdminModule.SettimeoutRequest: ...
        def stop_request(self) -> _AdminModule.StopRequest: ...
        def identities_request(self) -> _AdminModule.IdentitiesRequest: ...
        def updateIdentity_request(self, oldId: str | None = None) -> _AdminModule.UpdateidentityRequest: ...

Admin: _AdminModule
AdminClient: TypeAlias = _AdminModule.AdminClient

class _SimpleFactoryModule(_IdentifiableModule):
    class CreateRequest(Protocol):
        def send(self) -> _SimpleFactoryModule.SimpleFactoryClient.CreateResult: ...

    @classmethod
    def _new_client(cls, server: _SimpleFactoryModule.Server | _IdentifiableModule.Server) -> _SimpleFactoryModule.SimpleFactoryClient: ...
    class Server(_IdentifiableModule.Server):
        class CreateResult(Awaitable[CreateResult], Protocol):
            caps: Sequence[_IdentifiableModule]

        class CreateResultTuple(NamedTuple):
            caps: Sequence[_IdentifiableModule]

        class CreateCallContext(Protocol):
            params: _SimpleFactoryModule.CreateRequest
            results: _SimpleFactoryModule.Server.CreateResult

        def create(self, _context: _SimpleFactoryModule.Server.CreateCallContext, **kwargs: Any) -> Awaitable[_SimpleFactoryModule.Server.CreateResultTuple | None]: ...
        def create_context(self, context: _SimpleFactoryModule.Server.CreateCallContext) -> Awaitable[None]: ...

    class SimpleFactoryClient(_IdentifiableModule.IdentifiableClient):
        class CreateResult(Awaitable[CreateResult], Protocol):
            caps: Sequence[_IdentifiableModule]

        def create(self) -> _SimpleFactoryModule.SimpleFactoryClient.CreateResult: ...
        def create_request(self) -> _SimpleFactoryModule.CreateRequest: ...

SimpleFactory: _SimpleFactoryModule
SimpleFactoryClient: TypeAlias = _SimpleFactoryModule.SimpleFactoryClient

class _FactoryModule(_IdentifiableModule):
    class _CreateParamsModule(Generic[_FactoryModule_Payload], _StructModule):
        class Reader(_DynamicStructReader):
            @property
            def timeoutSeconds(self) -> int: ...
            @property
            def interfaceNameToRegistrySR(self) -> Sequence[_PairModule.Reader]: ...
            @property
            def msgPayload(self) -> _FactoryModule_Payload: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _FactoryModule._CreateParamsModule.Builder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def timeoutSeconds(self) -> int: ...
            @timeoutSeconds.setter
            def timeoutSeconds(self, value: int) -> None: ...
            @property
            def interfaceNameToRegistrySR(self) -> MutableSequence[_PairModule.Builder]: ...
            @interfaceNameToRegistrySR.setter
            def interfaceNameToRegistrySR(self, value: Sequence[_PairModule.Builder | _PairModule.Reader] | Sequence[dict[str, Any]]) -> None: ...
            @property
            def msgPayload(self) -> _FactoryModule_Payload: ...
            @msgPayload.setter
            def msgPayload(self, value: _FactoryModule_Payload) -> None: ...
            def init(self, field: Literal["interfaceNameToRegistrySR"], size: int | None = None) -> MutableSequence[_PairModule.Builder]: ...
            @override
            def as_reader(self) -> _FactoryModule._CreateParamsModule.Reader: ...

        @override
        def new_message(
            self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, timeoutSeconds: int | None = None, interfaceNameToRegistrySR: Sequence[_PairModule.Builder] | Sequence[dict[str, Any]] | None = None, msgPayload: _FactoryModule_Payload | None = None
        ) -> _FactoryModule._CreateParamsModule.Builder: ...

    CreateParamsReader: TypeAlias = _CreateParamsModule.Reader
    CreateParamsBuilder: TypeAlias = _CreateParamsModule.Builder
    CreateParams: _CreateParamsModule
    class _AccessInfoModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def adminCap(self) -> Any: ...
            @property
            def serviceCaps(self) -> Sequence[_IdentifiableModule]: ...
            @property
            def error(self) -> str: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _FactoryModule._AccessInfoModule.Builder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def adminCap(self) -> Any: ...
            @adminCap.setter
            def adminCap(self, value: Any) -> None: ...
            @property
            def serviceCaps(self) -> MutableSequence[_IdentifiableModule]: ...
            @serviceCaps.setter
            def serviceCaps(self, value: Sequence[_IdentifiableModule]) -> None: ...
            @property
            def error(self) -> str: ...
            @error.setter
            def error(self, value: str) -> None: ...
            def init(self, field: Literal["serviceCaps"], size: int | None = None) -> MutableSequence[_IdentifiableModule]: ...
            @override
            def as_reader(self) -> _FactoryModule._AccessInfoModule.Reader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, adminCap: Any | None = None, serviceCaps: Sequence[_IdentifiableModule] | None = None, error: str | None = None) -> _FactoryModule._AccessInfoModule.Builder: ...

    AccessInfoReader: TypeAlias = _AccessInfoModule.Reader
    AccessInfoBuilder: TypeAlias = _AccessInfoModule.Builder
    AccessInfo: _AccessInfoModule
    class CreateRequest(Protocol):
        timeoutSeconds: int
        interfaceNameToRegistrySR: Sequence[_PairModule[str, str]] | Sequence[dict[str, Any]]
        msgPayload: _DynamicObjectReader
        @overload
        def init(self, name: Literal["interfaceNameToRegistrySR"], size: int = ...) -> MutableSequence[_PairModule[str, str].Builder]: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> _FactoryModule.FactoryClient.CreateResult: ...

    class ServiceinterfacenamesRequest(Protocol):
        def send(self) -> _FactoryModule.FactoryClient.ServiceinterfacenamesResult: ...

    @classmethod
    def _new_client(cls, server: _FactoryModule.Server | _IdentifiableModule.Server) -> _FactoryModule.FactoryClient: ...
    class Server(_IdentifiableModule.Server):
        class CreateResult(Awaitable[CreateResult], Protocol):
            adminCap: str | bytes | _DynamicStructBuilder | _DynamicStructReader | _DynamicCapabilityClient | _DynamicCapabilityServer
            serviceCaps: Sequence[_IdentifiableModule]
            error: str

        class ServiceinterfacenamesResult(Awaitable[ServiceinterfacenamesResult], Protocol):
            names: Sequence[str]

        class CreateResultTuple(NamedTuple):
            adminCap: str | bytes | _DynamicStructBuilder | _DynamicStructReader | _DynamicCapabilityClient | _DynamicCapabilityServer
            serviceCaps: Sequence[_IdentifiableModule]
            error: str

        class ServiceinterfacenamesResultTuple(NamedTuple):
            names: Sequence[str]

        class CreateCallContext(Protocol):
            params: _FactoryModule.CreateRequest
            results: _FactoryModule.Server.CreateResult

        class ServiceinterfacenamesCallContext(Protocol):
            params: _FactoryModule.ServiceinterfacenamesRequest
            results: _FactoryModule.Server.ServiceinterfacenamesResult

        def create(self, timeoutSeconds: int, interfaceNameToRegistrySR: Sequence[_PairModule[str, str].Reader], msgPayload: _DynamicObjectReader, _context: _FactoryModule.Server.CreateCallContext, **kwargs: Any) -> Awaitable[_FactoryModule.Server.CreateResultTuple | None]: ...
        def create_context(self, context: _FactoryModule.Server.CreateCallContext) -> Awaitable[None]: ...
        def serviceInterfaceNames(self, _context: _FactoryModule.Server.ServiceinterfacenamesCallContext, **kwargs: Any) -> Awaitable[_FactoryModule.Server.ServiceinterfacenamesResultTuple | None]: ...
        def serviceInterfaceNames_context(self, context: _FactoryModule.Server.ServiceinterfacenamesCallContext) -> Awaitable[None]: ...

    class FactoryClient(_IdentifiableModule.IdentifiableClient):
        class CreateResult(Awaitable[CreateResult], Protocol):
            adminCap: _DynamicObjectReader
            serviceCaps: Sequence[_IdentifiableModule]
            error: str

        class ServiceinterfacenamesResult(Awaitable[ServiceinterfacenamesResult], Protocol):
            names: Sequence[str]

        def create(self, timeoutSeconds: int | None = None, interfaceNameToRegistrySR: Sequence[_PairModule[str, str]] | Sequence[dict[str, Any]] | None = None, msgPayload: _DynamicObjectReader | None = None) -> _FactoryModule.FactoryClient.CreateResult: ...
        def serviceInterfaceNames(self) -> _FactoryModule.FactoryClient.ServiceinterfacenamesResult: ...
        def create_request(self, timeoutSeconds: int | None = None, interfaceNameToRegistrySR: Sequence[_PairModule[str, str]] | Sequence[dict[str, Any]] | None = None, msgPayload: _DynamicObjectReader | None = None) -> _FactoryModule.CreateRequest: ...
        def serviceInterfaceNames_request(self) -> _FactoryModule.ServiceinterfacenamesRequest: ...

Factory: _FactoryModule
FactoryClient: TypeAlias = _FactoryModule.FactoryClient

class _StoppableModule(_InterfaceModule):
    class StopRequest(Protocol):
        def send(self) -> _StoppableModule.StoppableClient.StopResult: ...

    @classmethod
    def _new_client(cls, server: _StoppableModule.Server) -> _StoppableModule.StoppableClient: ...
    class Server(_DynamicCapabilityServer):
        class StopResult(Awaitable[StopResult], Protocol):
            success: bool

        class StopResultTuple(NamedTuple):
            success: bool

        class StopCallContext(Protocol):
            params: _StoppableModule.StopRequest
            results: _StoppableModule.Server.StopResult

        def stop(self, _context: _StoppableModule.Server.StopCallContext, **kwargs: Any) -> Awaitable[bool | _StoppableModule.Server.StopResultTuple | None]: ...
        def stop_context(self, context: _StoppableModule.Server.StopCallContext) -> Awaitable[None]: ...

    class StoppableClient(_DynamicCapabilityClient):
        class StopResult(Awaitable[StopResult], Protocol):
            success: bool

        def stop(self) -> _StoppableModule.StoppableClient.StopResult: ...
        def stop_request(self) -> _StoppableModule.StopRequest: ...

Stoppable: _StoppableModule
StoppableClient: TypeAlias = _StoppableModule.StoppableClient

# Top-level type aliases for use in type annotations
AccessInfoBuilder: TypeAlias = _FactoryModule._AccessInfoModule.Builder
AccessInfoReader: TypeAlias = _FactoryModule._AccessInfoModule.Reader
CreateParamsBuilder: TypeAlias = _FactoryModule._CreateParamsModule.Builder
CreateParamsReader: TypeAlias = _FactoryModule._CreateParamsModule.Reader
