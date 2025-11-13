"""This is an automatically generated stub for `service.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator, Sequence
from contextlib import contextmanager
from io import BufferedWriter
from typing import (
    Any,
    BinaryIO,
    Generic,
    Literal,
    NamedTuple,
    Protocol,
    TypeAlias,
    TypeVar,
    overload,
)

from .common_capnp import Identifiable, IdentifiableClient, Pair

Factory_Payload = TypeVar("Factory_Payload")

class Admin:
    class HeartbeatRequest(Protocol):
        def send(self) -> None: ...

    class SettimeoutRequest(Protocol):
        seconds: int
        def send(self) -> None: ...

    class StopRequest(Protocol):
        def send(self) -> None: ...

    class IdentitiesRequest(Protocol):
        def send(self) -> Admin.IdentitiesResult: ...

    class IdentitiesResult(Awaitable[IdentitiesResult], Protocol):
        infos: Any

    class UpdateidentityRequest(Protocol):
        oldId: str
        def send(self) -> None: ...

    @classmethod
    def _new_client(cls, server: Admin.Server | Identifiable.Server) -> AdminClient: ...
    class Server(Identifiable.Server):
        class IdentitiesResultTuple(NamedTuple):
            pass

        class HeartbeatCallContext(Protocol):
            params: Admin.HeartbeatRequest

        class SettimeoutCallContext(Protocol):
            params: Admin.SettimeoutRequest

        class StopCallContext(Protocol):
            params: Admin.StopRequest

        class IdentitiesCallContext(Protocol):
            params: Admin.IdentitiesRequest
            results: Admin.IdentitiesResult

        class UpdateidentityCallContext(Protocol):
            params: Admin.UpdateidentityRequest

        def heartbeat(
            self, _context: Admin.Server.HeartbeatCallContext, **kwargs: Any
        ) -> Awaitable[None]: ...
        def heartbeat_context(
            self, context: Admin.Server.HeartbeatCallContext
        ) -> Awaitable[None]: ...
        def setTimeout(
            self,
            seconds: int,
            _context: Admin.Server.SettimeoutCallContext,
            **kwargs: Any,
        ) -> Awaitable[None]: ...
        def setTimeout_context(
            self, context: Admin.Server.SettimeoutCallContext
        ) -> Awaitable[None]: ...
        def stop(
            self, _context: Admin.Server.StopCallContext, **kwargs: Any
        ) -> Awaitable[None]: ...
        def stop_context(
            self, context: Admin.Server.StopCallContext
        ) -> Awaitable[None]: ...
        def identities(
            self, _context: Admin.Server.IdentitiesCallContext, **kwargs: Any
        ) -> Awaitable[Admin.Server.IdentitiesResultTuple | None]: ...
        def identities_context(
            self, context: Admin.Server.IdentitiesCallContext
        ) -> Awaitable[None]: ...
        def updateIdentity(
            self,
            oldId: str,
            _context: Admin.Server.UpdateidentityCallContext,
            **kwargs: Any,
        ) -> Awaitable[None]: ...
        def updateIdentity_context(
            self, context: Admin.Server.UpdateidentityCallContext
        ) -> Awaitable[None]: ...

class AdminClient(IdentifiableClient):
    def heartbeat(self) -> None: ...
    def setTimeout(self, seconds: int | None = None) -> None: ...
    def stop(self) -> None: ...
    def identities(self) -> Admin.IdentitiesResult: ...
    def updateIdentity(self, oldId: str | None = None) -> None: ...
    def heartbeat_request(self) -> Admin.HeartbeatRequest: ...
    def setTimeout_request(
        self, seconds: int | None = None
    ) -> Admin.SettimeoutRequest: ...
    def stop_request(self) -> Admin.StopRequest: ...
    def identities_request(self) -> Admin.IdentitiesRequest: ...
    def updateIdentity_request(
        self, oldId: str | None = None
    ) -> Admin.UpdateidentityRequest: ...

class SimpleFactory:
    class CreateRequest(Protocol):
        def send(self) -> SimpleFactory.CreateResult: ...

    class CreateResult(Awaitable[CreateResult], Protocol):
        caps: Sequence[Identifiable]

    @classmethod
    def _new_client(
        cls, server: SimpleFactory.Server | Identifiable.Server
    ) -> SimpleFactoryClient: ...
    class Server(Identifiable.Server):
        class CreateResultTuple(NamedTuple):
            caps: Sequence[Identifiable]

        class CreateCallContext(Protocol):
            params: SimpleFactory.CreateRequest
            results: SimpleFactory.CreateResult

        def create(
            self, _context: SimpleFactory.Server.CreateCallContext, **kwargs: Any
        ) -> Awaitable[SimpleFactory.Server.CreateResultTuple | None]: ...
        def create_context(
            self, context: SimpleFactory.Server.CreateCallContext
        ) -> Awaitable[None]: ...

class SimpleFactoryClient(IdentifiableClient):
    def create(self) -> SimpleFactory.CreateResult: ...
    def create_request(self) -> SimpleFactory.CreateRequest: ...

class Factory:
    CreateParamsBuilder: TypeAlias = CreateParams.Builder
    CreateParamsReader: TypeAlias = CreateParams.Reader
    class CreateParams(Generic[Factory_Payload]):
        class Reader:
            @property
            def timeoutSeconds(self) -> int: ...
            @property
            def interfaceNameToRegistrySR(self) -> Sequence[Pair.Reader]: ...
            @property
            def msgPayload(self) -> Factory_Payload: ...
            def as_builder(self) -> Factory.CreateParams.Builder: ...

        class Builder:
            @property
            def timeoutSeconds(self) -> int: ...
            @timeoutSeconds.setter
            def timeoutSeconds(self, value: int) -> None: ...
            @property
            def interfaceNameToRegistrySR(self) -> Sequence[Pair.Builder]: ...
            @interfaceNameToRegistrySR.setter
            def interfaceNameToRegistrySR(
                self,
                value: Sequence[Pair.Builder | Pair.Reader] | Sequence[dict[str, Any]],
            ) -> None: ...
            @property
            def msgPayload(self) -> Factory_Payload: ...
            @msgPayload.setter
            def msgPayload(self, value: Factory_Payload) -> None: ...
            @staticmethod
            def from_dict(
                dictionary: dict[str, Any],
            ) -> Factory.CreateParams.Builder: ...
            def init(
                self, name: Literal["interfaceNameToRegistrySR"], size: int = ...
            ) -> Sequence[Pair.Builder]: ...
            def copy(self) -> Factory.CreateParams.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Factory.CreateParams.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        @contextmanager
        @staticmethod
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Factory.CreateParams.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Factory.CreateParams.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            timeoutSeconds: int | None = None,
            interfaceNameToRegistrySR: Sequence[Pair.Builder]
            | Sequence[dict[str, Any]]
            | None = None,
            msgPayload: Factory_Payload | None = None,
        ) -> Factory.CreateParams.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Factory.CreateParams.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Factory.CreateParams.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    AccessInfoBuilder: TypeAlias = AccessInfo.Builder
    AccessInfoReader: TypeAlias = AccessInfo.Reader
    class AccessInfo:
        class Reader:
            @property
            def adminCap(self) -> Any: ...
            @property
            def serviceCaps(self) -> Sequence[Identifiable]: ...
            @property
            def error(self) -> str: ...
            def as_builder(self) -> Factory.AccessInfo.Builder: ...

        class Builder:
            @property
            def adminCap(self) -> Any: ...
            @adminCap.setter
            def adminCap(self, value: Any) -> None: ...
            @property
            def serviceCaps(self) -> Sequence[Identifiable]: ...
            @serviceCaps.setter
            def serviceCaps(self, value: Sequence[Identifiable]) -> None: ...
            @property
            def error(self) -> str: ...
            @error.setter
            def error(self, value: str) -> None: ...
            @staticmethod
            def from_dict(dictionary: dict[str, Any]) -> Factory.AccessInfo.Builder: ...
            def init(
                self, name: Literal["serviceCaps"], size: int = ...
            ) -> Sequence[Identifiable]: ...
            def copy(self) -> Factory.AccessInfo.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Factory.AccessInfo.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        @contextmanager
        @staticmethod
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Factory.AccessInfo.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Factory.AccessInfo.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            adminCap: Any | None = None,
            serviceCaps: Sequence[Identifiable] | None = None,
            error: str | None = None,
        ) -> Factory.AccessInfo.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Factory.AccessInfo.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Factory.AccessInfo.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    class CreateRequest(Protocol):
        timeoutSeconds: int
        interfaceNameToRegistrySR: Sequence[Pair[str, str]] | Sequence[dict[str, Any]]
        msgPayload: Any
        @overload
        def init(
            self, name: Literal["interfaceNameToRegistrySR"], size: int = ...
        ) -> Sequence[Pair[str, str].Builder]: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> Factory.CreateResult: ...

    class CreateResult(Awaitable[CreateResult], Protocol):
        adminCap: Any
        serviceCaps: Sequence[Identifiable]
        error: str

    class ServiceinterfacenamesRequest(Protocol):
        def send(self) -> Factory.ServiceinterfacenamesResult: ...

    class ServiceinterfacenamesResult(Awaitable[ServiceinterfacenamesResult], Protocol):
        names: Sequence[str]

    @classmethod
    def _new_client(
        cls, server: Factory.Server | Identifiable.Server
    ) -> FactoryClient: ...
    class Server(Identifiable.Server):
        class CreateResultTuple(NamedTuple):
            adminCap: Any
            serviceCaps: Sequence[Identifiable]
            error: str

        class ServiceinterfacenamesResultTuple(NamedTuple):
            names: Sequence[str]

        class CreateCallContext(Protocol):
            params: Factory.CreateRequest
            results: Factory.CreateResult

        class ServiceinterfacenamesCallContext(Protocol):
            params: Factory.ServiceinterfacenamesRequest
            results: Factory.ServiceinterfacenamesResult

        def create(
            self,
            timeoutSeconds: int,
            interfaceNameToRegistrySR: Sequence[Pair[str, str].Reader],
            msgPayload: Any,
            _context: Factory.Server.CreateCallContext,
            **kwargs: Any,
        ) -> Awaitable[Factory.Server.CreateResultTuple | None]: ...
        def create_context(
            self, context: Factory.Server.CreateCallContext
        ) -> Awaitable[None]: ...
        def serviceInterfaceNames(
            self,
            _context: Factory.Server.ServiceinterfacenamesCallContext,
            **kwargs: Any,
        ) -> Awaitable[Factory.Server.ServiceinterfacenamesResultTuple | None]: ...
        def serviceInterfaceNames_context(
            self, context: Factory.Server.ServiceinterfacenamesCallContext
        ) -> Awaitable[None]: ...

class FactoryClient(IdentifiableClient):
    def create(
        self,
        timeoutSeconds: int | None = None,
        interfaceNameToRegistrySR: Sequence[Pair[str, str]]
        | Sequence[dict[str, Any]]
        | None = None,
        msgPayload: Any | None = None,
    ) -> Factory.CreateResult: ...
    def serviceInterfaceNames(self) -> Factory.ServiceinterfacenamesResult: ...
    def create_request(
        self,
        timeoutSeconds: int | None = None,
        interfaceNameToRegistrySR: Sequence[Pair[str, str]]
        | Sequence[dict[str, Any]]
        | None = None,
        msgPayload: Any | None = None,
    ) -> Factory.CreateRequest: ...
    def serviceInterfaceNames_request(self) -> Factory.ServiceinterfacenamesRequest: ...

class Stoppable:
    class StopRequest(Protocol):
        def send(self) -> Stoppable.StopResult: ...

    class StopResult(Awaitable[StopResult], Protocol):
        success: bool

    @classmethod
    def _new_client(cls, server: Stoppable.Server) -> StoppableClient: ...
    class Server(Protocol):
        class StopResultTuple(NamedTuple):
            success: bool

        class StopCallContext(Protocol):
            params: Stoppable.StopRequest
            results: Stoppable.StopResult

        def stop(
            self, _context: Stoppable.Server.StopCallContext, **kwargs: Any
        ) -> Awaitable[bool | Stoppable.Server.StopResultTuple | None]: ...
        def stop_context(
            self, context: Stoppable.Server.StopCallContext
        ) -> Awaitable[None]: ...

class StoppableClient(Protocol):
    def stop(self) -> Stoppable.StopResult: ...
    def stop_request(self) -> Stoppable.StopRequest: ...
