"""This is an automatically generated stub for `service.capnp`."""

from collections.abc import Awaitable, Callable, Iterator, Sequence
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

from mas.schema.common.common_capnp.types.builders import (
    IdInformationBuilder,
    PairBuilder,
)
from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.common.common_capnp.types.readers import IdInformationReader, PairReader

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

class _AdminInterfaceModule(_IdentifiableInterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> AdminClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def heartbeat(
            self,
            _context: HeartbeatCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def heartbeat_context(
            self,
            context: HeartbeatCallContext,
        ) -> Awaitable[None]: ...
        def setTimeout(
            self,
            seconds: int,
            _context: SettimeoutCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def setTimeout_context(
            self,
            context: SettimeoutCallContext,
        ) -> Awaitable[None]: ...
        def stop(
            self,
            _context: AdminStopCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def stop_context(self, context: AdminStopCallContext) -> Awaitable[None]: ...
        def identities(
            self,
            _context: IdentitiesCallContext,
            **kwargs: object,
        ) -> Awaitable[
            IdInformationListBuilder
            | IdInformationListReader
            | Sequence[Any]
            | IdentitiesResultTuple
            | None
        ]: ...
        def identities_context(
            self,
            context: IdentitiesCallContext,
        ) -> Awaitable[None]: ...
        def updateIdentity(
            self,
            oldId: str,
            newInfo: IdInformationReader,
            _context: UpdateidentityCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def updateIdentity_context(
            self,
            context: UpdateidentityCallContext,
        ) -> Awaitable[None]: ...

class HeartbeatRequest(Protocol):
    def send(self) -> HeartbeatResult: ...

class HeartbeatResult(Awaitable[None], Protocol): ...
class HeartbeatParams(Protocol): ...

class HeartbeatCallContext(Protocol):
    params: HeartbeatParams

class SettimeoutRequest(Protocol):
    seconds: int
    def send(self) -> SettimeoutResult: ...

class SettimeoutResult(Awaitable[None], Protocol): ...

class SettimeoutParams(Protocol):
    seconds: int

class SettimeoutCallContext(Protocol):
    params: SettimeoutParams

class AdminStopRequest(Protocol):
    def send(self) -> AdminStopResult: ...

class AdminStopResult(Awaitable[None], Protocol): ...
class AdminStopParams(Protocol): ...

class AdminStopCallContext(Protocol):
    params: AdminStopParams

class IdentitiesRequest(Protocol):
    def send(self) -> IdentitiesResult: ...

class _IdInformationList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> IdInformationReader: ...
        @override
        def __iter__(self) -> Iterator[IdInformationReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> IdInformationBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: IdInformationReader | IdInformationBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[IdInformationBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> IdInformationBuilder: ...

class IdentitiesResult(Awaitable[IdentitiesResult], Protocol):
    infos: IdInformationListReader

class IdentitiesServerResult(_DynamicStructBuilder):
    @property
    def infos(self) -> IdInformationListBuilder: ...
    @infos.setter
    def infos(
        self,
        value: IdInformationListBuilder | IdInformationListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["infos"],
        size: int | None = None,
    ) -> IdInformationListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class IdentitiesParams(Protocol): ...

class IdentitiesCallContext(Protocol):
    params: IdentitiesParams
    @property
    def results(self) -> IdentitiesServerResult: ...

class IdentitiesResultTuple(NamedTuple):
    infos: IdInformationListBuilder | IdInformationListReader | Sequence[Any]

class UpdateidentityRequest(Protocol):
    oldId: str
    newInfo: IdInformationBuilder
    @overload
    def init(self, name: Literal["newInfo"]) -> IdInformationBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> UpdateidentityResult: ...

class UpdateidentityResult(Awaitable[None], Protocol): ...

class UpdateidentityParams(Protocol):
    oldId: str
    newInfo: IdInformationReader

class UpdateidentityCallContext(Protocol):
    params: UpdateidentityParams

class AdminClient(IdentifiableClient):
    def heartbeat(self) -> HeartbeatResult: ...
    def setTimeout(self, seconds: int | None = None) -> SettimeoutResult: ...
    def stop(self) -> AdminStopResult: ...
    def identities(self) -> IdentitiesResult: ...
    def updateIdentity(
        self,
        oldId: str | None = None,
        newInfo: IdInformationBuilder
        | IdInformationReader
        | dict[str, Any]
        | None = None,
    ) -> UpdateidentityResult: ...
    def heartbeat_request(self) -> HeartbeatRequest: ...
    def setTimeout_request(self, seconds: int | None = None) -> SettimeoutRequest: ...
    def stop_request(self) -> AdminStopRequest: ...
    def identities_request(self) -> IdentitiesRequest: ...
    def updateIdentity_request(
        self,
        oldId: str | None = None,
        newInfo: IdInformationBuilder | None = None,
    ) -> UpdateidentityRequest: ...

Admin: _AdminInterfaceModule

class _SimpleFactoryInterfaceModule(_IdentifiableInterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> SimpleFactoryClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def create(
            self,
            _context: SimpleFactoryCreateCallContext,
            **kwargs: object,
        ) -> Awaitable[
            IdentifiableClientListBuilder
            | IdentifiableClientListReader
            | Sequence[Any]
            | SimpleFactoryCreateResultTuple
            | None
        ]: ...
        def create_context(
            self,
            context: SimpleFactoryCreateCallContext,
        ) -> Awaitable[None]: ...

class SimpleFactoryCreateRequest(Protocol):
    def send(self) -> SimpleFactoryCreateResult: ...

class _IdentifiableClientList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> IdentifiableClient: ...
        @override
        def __iter__(self) -> Iterator[IdentifiableClient]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> IdentifiableClient: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: IdentifiableClient | _IdentifiableInterfaceModule.Server,
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[IdentifiableClient]: ...

class SimpleFactoryCreateResult(Awaitable[SimpleFactoryCreateResult], Protocol):
    caps: IdentifiableClientListReader

class SimpleFactoryCreateServerResult(_DynamicStructBuilder):
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
        self,
        field: Literal["caps"],
        size: int | None = None,
    ) -> IdentifiableClientListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class SimpleFactoryCreateParams(Protocol): ...

class SimpleFactoryCreateCallContext(Protocol):
    params: SimpleFactoryCreateParams
    @property
    def results(self) -> SimpleFactoryCreateServerResult: ...

class SimpleFactoryCreateResultTuple(NamedTuple):
    caps: IdentifiableClientListBuilder | IdentifiableClientListReader | Sequence[Any]

class SimpleFactoryClient(IdentifiableClient):
    def create(self) -> SimpleFactoryCreateResult: ...
    def create_request(self) -> SimpleFactoryCreateRequest: ...

SimpleFactory: _SimpleFactoryInterfaceModule

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
            interfaceNameToRegistrySR: PairListBuilder | dict[str, Any] | None = None,
            msgPayload: AnyPointer | None = None,
            **kwargs: object,
        ) -> CreateParamsBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[CreateParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[CreateParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[CreateParamsBuilder]: ...
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
        ) -> CreateParamsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> CreateParamsReader: ...

    CreateParams: _CreateParamsStructModule
    class _AccessInfoStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            adminCap: Capability | None = None,
            serviceCaps: IdentifiableClientListBuilder | dict[str, Any] | None = None,
            error: str | None = None,
            **kwargs: object,
        ) -> AccessInfoBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[AccessInfoReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[AccessInfoReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[AccessInfoBuilder]: ...
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
        ) -> AccessInfoReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AccessInfoReader: ...

    AccessInfo: _AccessInfoStructModule
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> FactoryClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def create(
            self,
            timeoutSeconds: int,
            interfaceNameToRegistrySR: PairListReader,
            msgPayload: AnyPointer,
            _context: FactoryCreateCallContext,
            **kwargs: object,
        ) -> Awaitable[FactoryCreateResultTuple | None]: ...
        def create_context(
            self,
            context: FactoryCreateCallContext,
        ) -> Awaitable[None]: ...
        def serviceInterfaceNames(
            self,
            _context: ServiceinterfacenamesCallContext,
            **kwargs: object,
        ) -> Awaitable[
            TextListBuilder
            | TextListReader
            | Sequence[Any]
            | ServiceinterfacenamesResultTuple
            | None
        ]: ...
        def serviceInterfaceNames_context(
            self,
            context: ServiceinterfacenamesCallContext,
        ) -> Awaitable[None]: ...

class _PairList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> PairReader: ...
        @override
        def __iter__(self) -> Iterator[PairReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> PairBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: PairReader | PairBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[PairBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> PairBuilder: ...

class CreateParamsReader(_DynamicStructReader):
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> CreateParamsBuilder: ...

class CreateParamsBuilder(_DynamicStructBuilder):
    @property
    def timeoutSeconds(self) -> int: ...
    @timeoutSeconds.setter
    def timeoutSeconds(self, value: int) -> None: ...
    @property
    def interfaceNameToRegistrySR(self) -> PairListBuilder: ...
    @interfaceNameToRegistrySR.setter
    def interfaceNameToRegistrySR(
        self,
        value: PairListBuilder | PairListReader | dict[str, Any],
    ) -> None: ...
    @property
    def msgPayload(self) -> _DynamicObjectReader: ...
    @msgPayload.setter
    def msgPayload(self, value: AnyPointer) -> None: ...
    @override
    def init(
        self,
        field: Literal["interfaceNameToRegistrySR"],
        size: int | None = None,
    ) -> PairListBuilder: ...
    @override
    def as_reader(self) -> CreateParamsReader: ...

class AccessInfoReader(_DynamicStructReader):
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> AccessInfoBuilder: ...

class AccessInfoBuilder(_DynamicStructBuilder):
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
    @override
    def init(
        self,
        field: Literal["serviceCaps"],
        size: int | None = None,
    ) -> IdentifiableClientListBuilder: ...
    @override
    def as_reader(self) -> AccessInfoReader: ...

class FactoryCreateRequest(Protocol):
    timeoutSeconds: int
    interfaceNameToRegistrySR: PairListBuilder | PairListReader | Sequence[Any]
    msgPayload: AnyPointer
    @overload
    def init(
        self,
        name: Literal["interfaceNameToRegistrySR"],
        size: int = ...,
    ) -> PairListBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> FactoryCreateResult: ...

class FactoryCreateResult(Awaitable[FactoryCreateResult], Protocol):
    adminCap: _DynamicCapabilityClient
    serviceCaps: IdentifiableClientListReader
    error: str

class FactoryCreateCallContext(Protocol):
    params: CreateParamsReader
    @property
    def results(self) -> AccessInfoBuilder: ...

class FactoryCreateResultTuple(NamedTuple):
    adminCap: Capability
    serviceCaps: (
        IdentifiableClientListBuilder | IdentifiableClientListReader | Sequence[Any]
    )
    error: str

class ServiceinterfacenamesRequest(Protocol):
    def send(self) -> ServiceinterfacenamesResult: ...

class _TextList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> str: ...
        @override
        def __iter__(self) -> Iterator[str]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> str: ...
        @override
        def __setitem__(self, key: int, value: str) -> None: ...
        @override
        def __iter__(self) -> Iterator[str]: ...

class ServiceinterfacenamesResult(Awaitable[ServiceinterfacenamesResult], Protocol):
    names: TextListReader

class ServiceinterfacenamesServerResult(_DynamicStructBuilder):
    @property
    def names(self) -> TextListBuilder: ...
    @names.setter
    def names(
        self,
        value: TextListBuilder | TextListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["names"],
        size: int | None = None,
    ) -> TextListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class ServiceinterfacenamesParams(Protocol): ...

class ServiceinterfacenamesCallContext(Protocol):
    params: ServiceinterfacenamesParams
    @property
    def results(self) -> ServiceinterfacenamesServerResult: ...

class ServiceinterfacenamesResultTuple(NamedTuple):
    names: TextListBuilder | TextListReader | Sequence[Any]

class FactoryClient(IdentifiableClient):
    def create(
        self,
        timeoutSeconds: int | None = None,
        interfaceNameToRegistrySR: PairListBuilder
        | PairListReader
        | Sequence[Any]
        | None = None,
        msgPayload: AnyPointer | None = None,
    ) -> FactoryCreateResult: ...
    def serviceInterfaceNames(self) -> ServiceinterfacenamesResult: ...
    def create_request(
        self,
        timeoutSeconds: int | None = None,
        interfaceNameToRegistrySR: PairListBuilder
        | PairListReader
        | Sequence[Any]
        | None = None,
        msgPayload: AnyPointer | None = None,
    ) -> FactoryCreateRequest: ...
    def serviceInterfaceNames_request(self) -> ServiceinterfacenamesRequest: ...

Factory: _FactoryInterfaceModule

class _StoppableInterfaceModule(_InterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> StoppableClient: ...
    class Server(_DynamicCapabilityServer):
        def stop(
            self,
            _context: StoppableStopCallContext,
            **kwargs: object,
        ) -> Awaitable[bool | StoppableStopResultTuple | None]: ...
        def stop_context(
            self,
            context: StoppableStopCallContext,
        ) -> Awaitable[None]: ...

class StoppableStopRequest(Protocol):
    def send(self) -> StoppableStopResult: ...

class StoppableStopResult(Awaitable[StoppableStopResult], Protocol):
    success: bool

class StoppableStopServerResult(_DynamicStructBuilder):
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class StoppableStopParams(Protocol): ...

class StoppableStopCallContext(Protocol):
    params: StoppableStopParams
    @property
    def results(self) -> StoppableStopServerResult: ...

class StoppableStopResultTuple(NamedTuple):
    success: bool

class StoppableClient(_DynamicCapabilityClient):
    def stop(self) -> StoppableStopResult: ...
    def stop_request(self) -> StoppableStopRequest: ...

Stoppable: _StoppableInterfaceModule

# Top-level type aliases for use in type annotations
AdminServer = _AdminInterfaceModule.Server
FactoryServer = _FactoryInterfaceModule.Server
type IdInformationListBuilder = _IdInformationList.Builder
type IdInformationListReader = _IdInformationList.Reader
type IdentifiableClientListBuilder = _IdentifiableClientList.Builder
type IdentifiableClientListReader = _IdentifiableClientList.Reader
type PairListBuilder = _PairList.Builder
type PairListReader = _PairList.Reader
SimpleFactoryServer = _SimpleFactoryInterfaceModule.Server
StoppableServer = _StoppableInterfaceModule.Server
type TextListBuilder = _TextList.Builder
type TextListReader = _TextList.Reader
