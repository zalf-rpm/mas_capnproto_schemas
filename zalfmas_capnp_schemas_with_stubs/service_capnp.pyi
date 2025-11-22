"""This is an automatically generated stub for `service.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator, Sequence
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
    IdentifiableClient,
    IdInformationBuilder,
    IdInformationReader,
    PairBuilder,
    PairReader,
    _IdentifiableModule,
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

        class IdentitiesResult(_DynamicStructBuilder):
            @property
            def infos(self) -> IdInformationListBuilder: ...
            @infos.setter
            def infos(
                self,
                value: IdInformationListBuilder
                | IdInformationListReader
                | Sequence[Any],
            ) -> None: ...
            @overload
            def init(
                self, field: Literal["infos"], size: int | None = None
            ) -> IdInformationListBuilder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...

        class UpdateidentityResult(Awaitable[None], Protocol): ...

        class IdentitiesResultTuple(NamedTuple):
            infos: IdInformationListBuilder | IdInformationListReader

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
            @property
            def results(self) -> _AdminModule.Server.IdentitiesResult: ...

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
            infos: IdInformationListReader

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

class _IdInformationList:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> IdInformationReader: ...
        def __iter__(self) -> Iterator[IdInformationReader]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> IdInformationBuilder: ...
        def __setitem__(
            self,
            key: int,
            value: IdInformationReader | IdInformationBuilder | dict[str, Any],
        ) -> None: ...
        def __iter__(self) -> Iterator[IdInformationBuilder]: ...
        def init(self, index: int, size: int | None = None) -> IdInformationBuilder: ...

Admin: _AdminModule

class _SimpleFactoryModule(_IdentifiableModule):
    class CreateRequest(Protocol):
        def send(self) -> _SimpleFactoryModule.SimpleFactoryClient.CreateResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _SimpleFactoryModule.SimpleFactoryClient: ...
    class Server(_IdentifiableModule.Server):
        class CreateResult(_DynamicStructBuilder):
            @property
            def caps(self) -> IdentifiableClientListBuilder: ...
            @caps.setter
            def caps(
                self,
                value: IdentifiableClientListBuilder
                | IdentifiableClientListReader
                | Sequence[Any],
            ) -> None: ...
            @overload
            def init(
                self, field: Literal["caps"], size: int | None = None
            ) -> IdentifiableClientListBuilder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...

        class CreateResultTuple(NamedTuple):
            caps: IdentifiableClientListBuilder | IdentifiableClientListReader

        class CreateParams(Protocol): ...

        class CreateCallContext(Protocol):
            params: _SimpleFactoryModule.Server.CreateParams
            @property
            def results(self) -> _SimpleFactoryModule.Server.CreateResult: ...

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
            caps: IdentifiableClientListReader

        def create(self) -> _SimpleFactoryModule.SimpleFactoryClient.CreateResult: ...
        def create_request(self) -> _SimpleFactoryModule.CreateRequest: ...

class _IdentifiableClientList:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> IdentifiableClient: ...
        def __iter__(self) -> Iterator[IdentifiableClient]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> IdentifiableClient: ...
        def __setitem__(
            self, key: int, value: IdentifiableClient | _IdentifiableModule.Server
        ) -> None: ...
        def __iter__(self) -> Iterator[IdentifiableClient]: ...

SimpleFactory: _SimpleFactoryModule

class _FactoryModule(_IdentifiableModule):
    class _CreateParamsModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def timeoutSeconds(self) -> int: ...
            @property
            def interfaceNameToRegistrySR(self) -> PairListReader: ...
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
            def interfaceNameToRegistrySR(self) -> PairListBuilder: ...
            @interfaceNameToRegistrySR.setter
            def interfaceNameToRegistrySR(
                self, value: PairListBuilder | PairListReader | dict[str, Any]
            ) -> None: ...
            @property
            def msgPayload(self) -> _DynamicObjectReader: ...
            @msgPayload.setter
            def msgPayload(self, value: AnyPointer) -> None: ...
            def init(
                self,
                field: Literal["interfaceNameToRegistrySR"],
                size: int | None = None,
            ) -> PairListBuilder: ...
            @override
            def as_reader(self) -> CreateParamsReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            timeoutSeconds: int | None = None,
            interfaceNameToRegistrySR: PairListBuilder | dict[str, Any] | None = None,
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
            def serviceCaps(self) -> IdentifiableClientListReader: ...
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
            def serviceCaps(self) -> IdentifiableClientListBuilder: ...
            @serviceCaps.setter
            def serviceCaps(
                self,
                value: IdentifiableClientListBuilder
                | IdentifiableClientListReader
                | dict[str, Any],
            ) -> None: ...
            @property
            def error(self) -> str: ...
            @error.setter
            def error(self, value: str) -> None: ...
            def init(
                self, field: Literal["serviceCaps"], size: int | None = None
            ) -> IdentifiableClientListBuilder: ...
            @override
            def as_reader(self) -> AccessInfoReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            adminCap: Capability | None = None,
            serviceCaps: IdentifiableClientListBuilder | dict[str, Any] | None = None,
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
        interfaceNameToRegistrySR: PairListBuilder | PairListReader | Sequence[Any]
        msgPayload: AnyPointer
        @overload
        def init(
            self, name: Literal["interfaceNameToRegistrySR"], size: int = ...
        ) -> PairListBuilder: ...
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
            serviceCaps: IdentifiableClientListBuilder | IdentifiableClientListReader
            error: str

        class ServiceinterfacenamesResult(_DynamicStructBuilder):
            @property
            def names(self) -> TextListBuilder: ...
            @names.setter
            def names(
                self, value: TextListBuilder | TextListReader | Sequence[Any]
            ) -> None: ...
            @overload
            def init(
                self, field: Literal["names"], size: int | None = None
            ) -> TextListBuilder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...

        class CreateResultTuple(NamedTuple):
            adminCap: Capability
            serviceCaps: IdentifiableClientListBuilder | IdentifiableClientListReader
            error: str

        class ServiceinterfacenamesResultTuple(NamedTuple):
            names: TextListBuilder | TextListReader

        class CreateParams(Protocol):
            timeoutSeconds: int
            interfaceNameToRegistrySR: PairListReader
            msgPayload: AnyPointer

        class CreateCallContext(Protocol):
            params: _FactoryModule.Server.CreateParams
            @property
            def results(self) -> AccessInfoBuilder: ...

        class ServiceinterfacenamesParams(Protocol): ...

        class ServiceinterfacenamesCallContext(Protocol):
            params: _FactoryModule.Server.ServiceinterfacenamesParams
            @property
            def results(self) -> _FactoryModule.Server.ServiceinterfacenamesResult: ...

        def create(
            self,
            timeoutSeconds: int,
            interfaceNameToRegistrySR: PairListReader,
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
            serviceCaps: IdentifiableClientListReader
            error: str

        class ServiceinterfacenamesResult(
            Awaitable[ServiceinterfacenamesResult], Protocol
        ):
            names: TextListReader

        def create(
            self,
            timeoutSeconds: int | None = None,
            interfaceNameToRegistrySR: PairListBuilder
            | PairListReader
            | Sequence[Any]
            | None = None,
            msgPayload: AnyPointer | None = None,
        ) -> _FactoryModule.FactoryClient.CreateResult: ...
        def serviceInterfaceNames(
            self,
        ) -> _FactoryModule.FactoryClient.ServiceinterfacenamesResult: ...
        def create_request(
            self,
            timeoutSeconds: int | None = None,
            interfaceNameToRegistrySR: PairListBuilder
            | PairListReader
            | Sequence[Any]
            | None = None,
            msgPayload: AnyPointer | None = None,
        ) -> _FactoryModule.CreateRequest: ...
        def serviceInterfaceNames_request(
            self,
        ) -> _FactoryModule.ServiceinterfacenamesRequest: ...

class _PairList:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> PairReader: ...
        def __iter__(self) -> Iterator[PairReader]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> PairBuilder: ...
        def __setitem__(
            self, key: int, value: PairReader | PairBuilder | dict[str, Any]
        ) -> None: ...
        def __iter__(self) -> Iterator[PairBuilder]: ...
        def init(self, index: int, size: int | None = None) -> PairBuilder: ...

class _TextList:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> str: ...
        def __iter__(self) -> Iterator[str]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> str: ...
        def __setitem__(self, key: int, value: str) -> None: ...
        def __iter__(self) -> Iterator[str]: ...

Factory: _FactoryModule

class _StoppableModule(_InterfaceModule):
    class StopRequest(Protocol):
        def send(self) -> _StoppableModule.StoppableClient.StopResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _StoppableModule.StoppableClient: ...
    class Server(_DynamicCapabilityServer):
        class StopResult(_DynamicStructBuilder):
            @property
            def success(self) -> bool: ...
            @success.setter
            def success(self, value: bool) -> None: ...

        class StopResultTuple(NamedTuple):
            success: bool

        class StopParams(Protocol): ...

        class StopCallContext(Protocol):
            params: _StoppableModule.Server.StopParams
            @property
            def results(self) -> _StoppableModule.Server.StopResult: ...

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
type AdminServer = _AdminModule.Server
type CreateParamsBuilder = _FactoryModule._CreateParamsModule.Builder
type CreateParamsReader = _FactoryModule._CreateParamsModule.Reader
type CreateResult = _FactoryModule.FactoryClient.CreateResult
type FactoryClient = _FactoryModule.FactoryClient
type FactoryServer = _FactoryModule.Server
type HeartbeatResult = _AdminModule.AdminClient.HeartbeatResult
type IdInformationListBuilder = _IdInformationList.Builder
type IdInformationListReader = _IdInformationList.Reader
type IdentifiableClientListBuilder = _IdentifiableClientList.Builder
type IdentifiableClientListReader = _IdentifiableClientList.Reader
type IdentitiesResult = _AdminModule.AdminClient.IdentitiesResult
type PairListBuilder = _PairList.Builder
type PairListReader = _PairList.Reader
type ServiceinterfacenamesResult = (
    _FactoryModule.FactoryClient.ServiceinterfacenamesResult
)
type SettimeoutResult = _AdminModule.AdminClient.SettimeoutResult
type SimpleFactoryClient = _SimpleFactoryModule.SimpleFactoryClient
type SimpleFactoryServer = _SimpleFactoryModule.Server
type StopResult = _StoppableModule.StoppableClient.StopResult
type StoppableClient = _StoppableModule.StoppableClient
type StoppableServer = _StoppableModule.Server
type TextListBuilder = _TextList.Builder
type TextListReader = _TextList.Reader
type UpdateidentityResult = _AdminModule.AdminClient.UpdateidentityResult
