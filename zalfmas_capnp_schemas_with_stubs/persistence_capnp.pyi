"""This is an automatically generated stub for `persistence.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator
from contextlib import contextmanager
from io import BufferedWriter
from typing import (
    Any,
    BinaryIO,
    Literal,
    NamedTuple,
    Protocol,
    Self,
    TypeAlias,
    overload,
)

from .common_capnp import Identifiable, IdentifiableClient

VatIdBuilder: TypeAlias = VatId.Builder
VatIdReader: TypeAlias = VatId.Reader

class VatId:
    class Reader:
        @property
        def publicKey0(self) -> int: ...
        @property
        def publicKey1(self) -> int: ...
        @property
        def publicKey2(self) -> int: ...
        @property
        def publicKey3(self) -> int: ...
        def as_builder(self) -> VatId.Builder: ...

    class Builder:
        @property
        def publicKey0(self) -> int: ...
        @publicKey0.setter
        def publicKey0(self, value: int) -> None: ...
        @property
        def publicKey1(self) -> int: ...
        @publicKey1.setter
        def publicKey1(self, value: int) -> None: ...
        @property
        def publicKey2(self) -> int: ...
        @publicKey2.setter
        def publicKey2(self, value: int) -> None: ...
        @property
        def publicKey3(self) -> int: ...
        @publicKey3.setter
        def publicKey3(self, value: int) -> None: ...
        @staticmethod
        def from_dict(dictionary: dict[str, Any]) -> VatId.Builder: ...
        def copy(self) -> VatId.Builder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> VatId.Reader: ...
        @staticmethod
        def write(file: BufferedWriter) -> None: ...
        @staticmethod
        def write_packed(file: BufferedWriter) -> None: ...

    @staticmethod
    @contextmanager
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[VatId.Reader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> VatId.Reader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        publicKey0: int | None = None,
        publicKey1: int | None = None,
        publicKey2: int | None = None,
        publicKey3: int | None = None,
    ) -> VatId.Builder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> VatId.Reader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> VatId.Reader: ...
    def to_dict(self) -> dict[str, Any]: ...

AddressBuilder: TypeAlias = Address.Builder
AddressReader: TypeAlias = Address.Reader

class Address:
    Ip6Builder: TypeAlias = Ip6.Builder
    Ip6Reader: TypeAlias = Ip6.Reader
    class Ip6:
        class Reader:
            @property
            def lower64(self) -> int: ...
            @property
            def upper64(self) -> int: ...
            def as_builder(self) -> Address.Ip6.Builder: ...

        class Builder:
            @property
            def lower64(self) -> int: ...
            @lower64.setter
            def lower64(self, value: int) -> None: ...
            @property
            def upper64(self) -> int: ...
            @upper64.setter
            def upper64(self, value: int) -> None: ...
            @staticmethod
            def from_dict(dictionary: dict[str, Any]) -> Address.Ip6.Builder: ...
            def copy(self) -> Address.Ip6.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Address.Ip6.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Address.Ip6.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Address.Ip6.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            lower64: int | None = None,
            upper64: int | None = None,
        ) -> Address.Ip6.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Address.Ip6.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Address.Ip6.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    class Reader:
        @property
        def ip6(self) -> Address.Ip6.Reader: ...
        @property
        def port(self) -> int: ...
        @property
        def host(self) -> str: ...
        def which(self) -> Literal["ip6", "host"]: ...
        def as_builder(self) -> Address.Builder: ...

    class Builder:
        @property
        def ip6(self) -> Address.Ip6.Builder: ...
        @ip6.setter
        def ip6(
            self, value: Address.Ip6.Builder | Address.Ip6.Reader | dict[str, Any]
        ) -> None: ...
        @property
        def port(self) -> int: ...
        @port.setter
        def port(self, value: int) -> None: ...
        @property
        def host(self) -> str: ...
        @host.setter
        def host(self, value: str) -> None: ...
        def which(self) -> Literal["ip6", "host"]: ...
        @staticmethod
        def from_dict(dictionary: dict[str, Any]) -> Address.Builder: ...
        def init(self, name: Literal["ip6"]) -> Address.Ip6.Builder: ...
        def copy(self) -> Address.Builder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> Address.Reader: ...
        @staticmethod
        def write(file: BufferedWriter) -> None: ...
        @staticmethod
        def write_packed(file: BufferedWriter) -> None: ...

    def which(self) -> Literal["ip6", "host"]: ...
    def init(self, name: Literal["ip6"]) -> Address.Ip6: ...
    @staticmethod
    @contextmanager
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[Address.Reader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Address.Reader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        ip6: Address.Ip6.Builder | dict[str, Any] | None = None,
        port: int | None = None,
        host: str | None = None,
    ) -> Address.Builder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Address.Reader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Address.Reader: ...
    def to_dict(self) -> dict[str, Any]: ...

VatPathBuilder: TypeAlias = VatPath.Builder
VatPathReader: TypeAlias = VatPath.Reader

class VatPath:
    class Reader:
        @property
        def id(self) -> VatId.Reader: ...
        @property
        def address(self) -> Address.Reader: ...
        def as_builder(self) -> VatPath.Builder: ...

    class Builder:
        @property
        def id(self) -> VatId.Builder: ...
        @id.setter
        def id(self, value: VatId.Builder | VatId.Reader | dict[str, Any]) -> None: ...
        @property
        def address(self) -> Address.Builder: ...
        @address.setter
        def address(
            self, value: Address.Builder | Address.Reader | dict[str, Any]
        ) -> None: ...
        @staticmethod
        def from_dict(dictionary: dict[str, Any]) -> VatPath.Builder: ...
        @overload
        def init(self: Any, name: Literal["id"]) -> VatId.Builder: ...
        @overload
        def init(self: Any, name: Literal["address"]) -> Address.Builder: ...
        def init(self: Any, name: str, size: int = ...) -> Any: ...
        def copy(self) -> VatPath.Builder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> VatPath.Reader: ...
        @staticmethod
        def write(file: BufferedWriter) -> None: ...
        @staticmethod
        def write_packed(file: BufferedWriter) -> None: ...

    @overload
    def init(self, name: Literal["id"]) -> VatId: ...
    @overload
    def init(self, name: Literal["address"]) -> Address: ...
    def init(self: Any, name: str, size: int = ...) -> Any: ...
    @staticmethod
    @contextmanager
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[VatPath.Reader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> VatPath.Reader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        id: VatId.Builder | dict[str, Any] | None = None,
        address: Address.Builder | dict[str, Any] | None = None,
    ) -> VatPath.Builder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> VatPath.Reader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> VatPath.Reader: ...
    def to_dict(self) -> dict[str, Any]: ...

SturdyRefBuilder: TypeAlias = SturdyRef.Builder
SturdyRefReader: TypeAlias = SturdyRef.Reader

class SturdyRef:
    OwnerBuilder: TypeAlias = Owner.Builder
    OwnerReader: TypeAlias = Owner.Reader
    class Owner:
        class Reader:
            @property
            def guid(self) -> str: ...
            def as_builder(self) -> SturdyRef.Owner.Builder: ...

        class Builder:
            @property
            def guid(self) -> str: ...
            @guid.setter
            def guid(self, value: str) -> None: ...
            @staticmethod
            def from_dict(dictionary: dict[str, Any]) -> SturdyRef.Owner.Builder: ...
            def copy(self) -> SturdyRef.Owner.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> SturdyRef.Owner.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[SturdyRef.Owner.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> SturdyRef.Owner.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            guid: str | None = None,
        ) -> SturdyRef.Owner.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> SturdyRef.Owner.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> SturdyRef.Owner.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    TokenBuilder: TypeAlias = Token.Builder
    TokenReader: TypeAlias = Token.Reader
    class Token:
        class Reader:
            @property
            def text(self) -> str: ...
            @property
            def data(self) -> bytes: ...
            def which(self) -> Literal["text", "data"]: ...
            def as_builder(self) -> SturdyRef.Token.Builder: ...

        class Builder:
            @property
            def text(self) -> str: ...
            @text.setter
            def text(self, value: str) -> None: ...
            @property
            def data(self) -> bytes: ...
            @data.setter
            def data(self, value: bytes) -> None: ...
            def which(self) -> Literal["text", "data"]: ...
            @staticmethod
            def from_dict(dictionary: dict[str, Any]) -> SturdyRef.Token.Builder: ...
            def copy(self) -> SturdyRef.Token.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> SturdyRef.Token.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        def which(self) -> Literal["text", "data"]: ...
        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[SturdyRef.Token.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> SturdyRef.Token.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            text: str | None = None,
            data: bytes | None = None,
        ) -> SturdyRef.Token.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> SturdyRef.Token.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> SturdyRef.Token.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    class Reader:
        @property
        def vat(self) -> VatPath.Reader: ...
        @property
        def localRef(self) -> SturdyRef.Token.Reader: ...
        def as_builder(self) -> SturdyRef.Builder: ...

    class Builder:
        @property
        def vat(self) -> VatPath.Builder: ...
        @vat.setter
        def vat(
            self, value: VatPath.Builder | VatPath.Reader | dict[str, Any]
        ) -> None: ...
        @property
        def localRef(self) -> SturdyRef.Token.Builder: ...
        @localRef.setter
        def localRef(
            self,
            value: SturdyRef.Token.Builder | SturdyRef.Token.Reader | dict[str, Any],
        ) -> None: ...
        @staticmethod
        def from_dict(dictionary: dict[str, Any]) -> SturdyRef.Builder: ...
        @overload
        def init(self: Any, name: Literal["vat"]) -> VatPath.Builder: ...
        @overload
        def init(self: Any, name: Literal["localRef"]) -> SturdyRef.Token.Builder: ...
        def init(self: Any, name: str, size: int = ...) -> Any: ...
        def copy(self) -> SturdyRef.Builder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> SturdyRef.Reader: ...
        @staticmethod
        def write(file: BufferedWriter) -> None: ...
        @staticmethod
        def write_packed(file: BufferedWriter) -> None: ...

    @overload
    def init(self, name: Literal["vat"]) -> VatPath: ...
    @overload
    def init(self, name: Literal["localRef"]) -> SturdyRef.Token: ...
    def init(self: Any, name: str, size: int = ...) -> Any: ...
    @staticmethod
    @contextmanager
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[SturdyRef.Reader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> SturdyRef.Reader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        vat: VatPath.Builder | dict[str, Any] | None = None,
        localRef: SturdyRef.Token.Builder | dict[str, Any] | None = None,
    ) -> SturdyRef.Builder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> SturdyRef.Reader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> SturdyRef.Reader: ...
    def to_dict(self) -> dict[str, Any]: ...

class Heartbeat:
    class BeatRequest(Protocol):
        def send(self) -> None: ...

    @classmethod
    def _new_client(cls, server: Heartbeat.Server) -> "HeartbeatClient": ...
    class Server(Protocol):
        class BeatCallContext(Protocol): ...

        def beat(
            self, _context: Heartbeat.Server.BeatCallContext, **kwargs: Any
        ) -> Awaitable[None]: ...
        def __enter__(self) -> Self: ...
        def __exit__(self, *args: Any) -> None: ...

class HeartbeatClient(Protocol):
    def beat(self) -> None: ...
    def beat_request(self) -> Heartbeat.BeatRequest: ...

class Persistent:
    SaveParamsBuilder: TypeAlias = SaveParams.Builder
    SaveParamsReader: TypeAlias = SaveParams.Reader
    class SaveParams:
        class Reader:
            @property
            def sealFor(self) -> SturdyRef.Owner.Reader: ...
            def as_builder(self) -> Persistent.SaveParams.Builder: ...

        class Builder:
            @property
            def sealFor(self) -> SturdyRef.Owner.Builder: ...
            @sealFor.setter
            def sealFor(
                self,
                value: SturdyRef.Owner.Builder
                | SturdyRef.Owner.Reader
                | dict[str, Any],
            ) -> None: ...
            @staticmethod
            def from_dict(
                dictionary: dict[str, Any],
            ) -> Persistent.SaveParams.Builder: ...
            def init(self, name: Literal["sealFor"]) -> SturdyRef.Owner.Builder: ...
            def copy(self) -> Persistent.SaveParams.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Persistent.SaveParams.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        def init(self, name: Literal["sealFor"]) -> SturdyRef.Owner: ...
        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Persistent.SaveParams.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Persistent.SaveParams.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            sealFor: SturdyRef.Owner.Builder | dict[str, Any] | None = None,
        ) -> Persistent.SaveParams.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Persistent.SaveParams.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Persistent.SaveParams.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    SaveResultsBuilder: TypeAlias = SaveResults.Builder
    SaveResultsReader: TypeAlias = SaveResults.Reader
    class SaveResults:
        class Reader:
            @property
            def sturdyRef(self) -> SturdyRef.Reader: ...
            @property
            def unsaveSR(self) -> SturdyRef.Reader: ...
            def as_builder(self) -> Persistent.SaveResults.Builder: ...

        class Builder:
            @property
            def sturdyRef(self) -> SturdyRef.Builder: ...
            @sturdyRef.setter
            def sturdyRef(
                self, value: SturdyRef.Builder | SturdyRef.Reader | dict[str, Any]
            ) -> None: ...
            @property
            def unsaveSR(self) -> SturdyRef.Builder: ...
            @unsaveSR.setter
            def unsaveSR(
                self, value: SturdyRef.Builder | SturdyRef.Reader | dict[str, Any]
            ) -> None: ...
            @staticmethod
            def from_dict(
                dictionary: dict[str, Any],
            ) -> Persistent.SaveResults.Builder: ...
            @overload
            def init(self: Any, name: Literal["sturdyRef"]) -> SturdyRef.Builder: ...
            @overload
            def init(self: Any, name: Literal["unsaveSR"]) -> SturdyRef.Builder: ...
            def init(self: Any, name: str, size: int = ...) -> Any: ...
            def copy(self) -> Persistent.SaveResults.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Persistent.SaveResults.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        @overload
        def init(self, name: Literal["sturdyRef"]) -> SturdyRef: ...
        @overload
        def init(self, name: Literal["unsaveSR"]) -> SturdyRef: ...
        def init(self: Any, name: str, size: int = ...) -> Any: ...
        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Persistent.SaveResults.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Persistent.SaveResults.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            sturdyRef: SturdyRef.Builder | dict[str, Any] | None = None,
            unsaveSR: SturdyRef.Builder | dict[str, Any] | None = None,
        ) -> Persistent.SaveResults.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Persistent.SaveResults.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Persistent.SaveResults.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    class ReleaseSturdyRef:
        class ReleaseRequest(Protocol):
            def send(self) -> Persistent.ReleaseSturdyRef.ReleaseResult: ...

        class ReleaseResult(Awaitable[ReleaseResult], Protocol):
            success: bool

        @classmethod
        def _new_client(
            cls, server: Persistent.ReleaseSturdyRef.Server
        ) -> "Persistent.ReleaseSturdyRefClient": ...
        class Server(Protocol):
            class ReleaseResultTuple(NamedTuple):
                success: bool

            class ReleaseCallContext(Protocol):
                results: Persistent.ReleaseSturdyRef.ReleaseResult

            def release(
                self,
                _context: Persistent.ReleaseSturdyRef.Server.ReleaseCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                bool | Persistent.ReleaseSturdyRef.Server.ReleaseResultTuple | None
            ]: ...
            def __enter__(self) -> Self: ...
            def __exit__(self, *args: Any) -> None: ...

    class ReleaseSturdyRefClient(Protocol):
        def release(self) -> Persistent.ReleaseSturdyRef.ReleaseResult: ...
        def release_request(self) -> Persistent.ReleaseSturdyRef.ReleaseRequest: ...

    class SaveRequest(Protocol):
        sealFor: SturdyRef.Owner.Builder
        @overload
        def init(self, name: Literal["sealFor"]) -> SturdyRef.Owner.Builder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> Persistent.SaveResult: ...

    class SaveResult(Awaitable[SaveResult], Protocol):
        sturdyRef: SturdyRef.Builder | SturdyRef.Reader
        unsaveSR: SturdyRef.Builder | SturdyRef.Reader

    @classmethod
    def _new_client(cls, server: Persistent.Server) -> "PersistentClient": ...
    class Server(Protocol):
        class SaveResultTuple(NamedTuple):
            sturdyRef: SturdyRef.Builder | SturdyRef.Reader
            unsaveSR: SturdyRef.Builder | SturdyRef.Reader

        class SaveCallContext(Protocol):
            results: Persistent.SaveResult

        def save(
            self,
            sealFor: SturdyRef.Owner.Reader,
            _context: Persistent.Server.SaveCallContext,
            **kwargs: Any,
        ) -> Awaitable[Persistent.Server.SaveResultTuple | None]: ...
        def __enter__(self) -> Self: ...
        def __exit__(self, *args: Any) -> None: ...

class PersistentClient(Protocol):
    def save(
        self, sealFor: SturdyRef.Owner | dict[str, Any] | None = None
    ) -> Persistent.SaveResult: ...
    def save_request(
        self, sealFor: SturdyRef.Owner.Builder | None = None
    ) -> Persistent.SaveRequest: ...

class Restorer:
    RestoreParamsBuilder: TypeAlias = RestoreParams.Builder
    RestoreParamsReader: TypeAlias = RestoreParams.Reader
    class RestoreParams:
        class Reader:
            @property
            def localRef(self) -> SturdyRef.Token.Reader: ...
            @property
            def sealedBy(self) -> SturdyRef.Owner.Reader: ...
            def as_builder(self) -> Restorer.RestoreParams.Builder: ...

        class Builder:
            @property
            def localRef(self) -> SturdyRef.Token.Builder: ...
            @localRef.setter
            def localRef(
                self,
                value: SturdyRef.Token.Builder
                | SturdyRef.Token.Reader
                | dict[str, Any],
            ) -> None: ...
            @property
            def sealedBy(self) -> SturdyRef.Owner.Builder: ...
            @sealedBy.setter
            def sealedBy(
                self,
                value: SturdyRef.Owner.Builder
                | SturdyRef.Owner.Reader
                | dict[str, Any],
            ) -> None: ...
            @staticmethod
            def from_dict(
                dictionary: dict[str, Any],
            ) -> Restorer.RestoreParams.Builder: ...
            @overload
            def init(
                self: Any, name: Literal["localRef"]
            ) -> SturdyRef.Token.Builder: ...
            @overload
            def init(
                self: Any, name: Literal["sealedBy"]
            ) -> SturdyRef.Owner.Builder: ...
            def init(self: Any, name: str, size: int = ...) -> Any: ...
            def copy(self) -> Restorer.RestoreParams.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Restorer.RestoreParams.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        @overload
        def init(self, name: Literal["localRef"]) -> SturdyRef.Token: ...
        @overload
        def init(self, name: Literal["sealedBy"]) -> SturdyRef.Owner: ...
        def init(self: Any, name: str, size: int = ...) -> Any: ...
        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Restorer.RestoreParams.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Restorer.RestoreParams.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            localRef: SturdyRef.Token.Builder | dict[str, Any] | None = None,
            sealedBy: SturdyRef.Owner.Builder | dict[str, Any] | None = None,
        ) -> Restorer.RestoreParams.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Restorer.RestoreParams.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Restorer.RestoreParams.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    class RestoreRequest(Protocol):
        localRef: SturdyRef.Token.Builder
        sealedBy: SturdyRef.Owner.Builder
        @overload
        def init(self, name: Literal["localRef"]) -> SturdyRef.Token.Builder: ...
        @overload
        def init(self, name: Literal["sealedBy"]) -> SturdyRef.Owner.Builder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> Restorer.RestoreResult: ...

    class RestoreResult(Awaitable[RestoreResult], Protocol):
        cap: Any

    @classmethod
    def _new_client(cls, server: Restorer.Server) -> "RestorerClient": ...
    class Server(Protocol):
        class RestoreResultTuple(NamedTuple):
            cap: Any

        class RestoreCallContext(Protocol):
            results: Restorer.RestoreResult

        def restore(
            self,
            localRef: SturdyRef.Token.Reader,
            sealedBy: SturdyRef.Owner.Reader,
            _context: Restorer.Server.RestoreCallContext,
            **kwargs: Any,
        ) -> Awaitable[Restorer.Server.RestoreResultTuple | None]: ...
        def __enter__(self) -> Self: ...
        def __exit__(self, *args: Any) -> None: ...

class RestorerClient(Protocol):
    def restore(
        self,
        localRef: SturdyRef.Token | dict[str, Any] | None = None,
        sealedBy: SturdyRef.Owner | dict[str, Any] | None = None,
    ) -> Restorer.RestoreResult: ...
    def restore_request(
        self,
        localRef: SturdyRef.Token.Builder | None = None,
        sealedBy: SturdyRef.Owner.Builder | None = None,
    ) -> Restorer.RestoreRequest: ...

class HostPortResolver:
    class Registrar:
        RegisterParamsBuilder: TypeAlias = RegisterParams.Builder
        RegisterParamsReader: TypeAlias = RegisterParams.Reader
        class RegisterParams:
            class Reader:
                @property
                def base64VatId(self) -> str: ...
                @property
                def host(self) -> str: ...
                @property
                def port(self) -> int: ...
                @property
                def alias(self) -> str: ...
                @property
                def identityProof(self) -> bytes: ...
                def as_builder(
                    self,
                ) -> HostPortResolver.Registrar.RegisterParams.Builder: ...

            class Builder:
                @property
                def base64VatId(self) -> str: ...
                @base64VatId.setter
                def base64VatId(self, value: str) -> None: ...
                @property
                def host(self) -> str: ...
                @host.setter
                def host(self, value: str) -> None: ...
                @property
                def port(self) -> int: ...
                @port.setter
                def port(self, value: int) -> None: ...
                @property
                def alias(self) -> str: ...
                @alias.setter
                def alias(self, value: str) -> None: ...
                @property
                def identityProof(self) -> bytes: ...
                @identityProof.setter
                def identityProof(self, value: bytes) -> None: ...
                @staticmethod
                def from_dict(
                    dictionary: dict[str, Any],
                ) -> HostPortResolver.Registrar.RegisterParams.Builder: ...
                def copy(self) -> HostPortResolver.Registrar.RegisterParams.Builder: ...
                def to_bytes(self) -> bytes: ...
                def to_bytes_packed(self) -> bytes: ...
                def to_segments(self) -> list[bytes]: ...
                def as_reader(
                    self,
                ) -> HostPortResolver.Registrar.RegisterParams.Reader: ...
                @staticmethod
                def write(file: BufferedWriter) -> None: ...
                @staticmethod
                def write_packed(file: BufferedWriter) -> None: ...

            @staticmethod
            @contextmanager
            def from_bytes(
                data: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> Iterator[HostPortResolver.Registrar.RegisterParams.Reader]: ...
            @staticmethod
            def from_bytes_packed(
                data: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> HostPortResolver.Registrar.RegisterParams.Reader: ...
            @staticmethod
            def new_message(
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
                base64VatId: str | None = None,
                host: str | None = None,
                port: int | None = None,
                alias: str | None = None,
                identityProof: bytes | None = None,
            ) -> HostPortResolver.Registrar.RegisterParams.Builder: ...
            @staticmethod
            def read(
                file: BinaryIO,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> HostPortResolver.Registrar.RegisterParams.Reader: ...
            @staticmethod
            def read_packed(
                file: BinaryIO,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> HostPortResolver.Registrar.RegisterParams.Reader: ...
            def to_dict(self) -> dict[str, Any]: ...

        class RegisterRequest(Protocol):
            base64VatId: str
            host: str
            port: int
            alias: str
            identityProof: bytes
            def send(self) -> HostPortResolver.Registrar.RegisterResult: ...

        class RegisterResult(Awaitable[RegisterResult], Protocol):
            heartbeat: HeartbeatClient
            secsHeartbeatInterval: int

        @classmethod
        def _new_client(
            cls, server: HostPortResolver.Registrar.Server
        ) -> "HostPortResolver.RegistrarClient": ...
        class Server(Protocol):
            class RegisterResultTuple(NamedTuple):
                heartbeat: Heartbeat.Server
                secsHeartbeatInterval: int

            class RegisterCallContext(Protocol):
                results: HostPortResolver.Registrar.RegisterResult

            def register(
                self,
                base64VatId: str,
                host: str,
                port: int,
                alias: str,
                identityProof: bytes,
                _context: HostPortResolver.Registrar.Server.RegisterCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                HostPortResolver.Registrar.Server.RegisterResultTuple | None
            ]: ...
            def __enter__(self) -> Self: ...
            def __exit__(self, *args: Any) -> None: ...

    class RegistrarClient(Protocol):
        def register(
            self,
            base64VatId: str | None = None,
            host: str | None = None,
            port: int | None = None,
            alias: str | None = None,
            identityProof: bytes | None = None,
        ) -> HostPortResolver.Registrar.RegisterResult: ...
        def register_request(
            self,
            base64VatId: str | None = None,
            host: str | None = None,
            port: int | None = None,
            alias: str | None = None,
            identityProof: bytes | None = None,
        ) -> HostPortResolver.Registrar.RegisterRequest: ...

    class ResolveRequest(Protocol):
        id: str
        def send(self) -> HostPortResolver.ResolveResult: ...

    class ResolveResult(Awaitable[ResolveResult], Protocol):
        host: str
        port: int

    @classmethod
    def _new_client(
        cls, server: HostPortResolver.Server | Identifiable.Server | Restorer.Server
    ) -> "HostPortResolverClient": ...
    class Server(Identifiable.Server, Restorer.Server):
        class ResolveResultTuple(NamedTuple):
            host: str
            port: int

        class ResolveCallContext(Protocol):
            results: HostPortResolver.ResolveResult

        def resolve(
            self,
            id: str,
            _context: HostPortResolver.Server.ResolveCallContext,
            **kwargs: Any,
        ) -> Awaitable[HostPortResolver.Server.ResolveResultTuple | None]: ...
        def __enter__(self) -> Self: ...
        def __exit__(self, *args: Any) -> None: ...

class HostPortResolverClient(IdentifiableClient, RestorerClient):
    def resolve(self, id: str | None = None) -> HostPortResolver.ResolveResult: ...
    def resolve_request(
        self, id: str | None = None
    ) -> HostPortResolver.ResolveRequest: ...

class Gateway:
    RegResultsBuilder: TypeAlias = RegResults.Builder
    RegResultsReader: TypeAlias = RegResults.Reader
    class RegResults:
        class Reader:
            @property
            def sturdyRef(self) -> SturdyRef.Reader: ...
            @property
            def heartbeat(self) -> HeartbeatClient: ...
            @property
            def secsHeartbeatInterval(self) -> int: ...
            def as_builder(self) -> Gateway.RegResults.Builder: ...

        class Builder:
            @property
            def sturdyRef(self) -> SturdyRef.Builder: ...
            @sturdyRef.setter
            def sturdyRef(
                self, value: SturdyRef.Builder | SturdyRef.Reader | dict[str, Any]
            ) -> None: ...
            @property
            def heartbeat(self) -> HeartbeatClient: ...
            @heartbeat.setter
            def heartbeat(self, value: HeartbeatClient | Heartbeat.Server) -> None: ...
            @property
            def secsHeartbeatInterval(self) -> int: ...
            @secsHeartbeatInterval.setter
            def secsHeartbeatInterval(self, value: int) -> None: ...
            @staticmethod
            def from_dict(dictionary: dict[str, Any]) -> Gateway.RegResults.Builder: ...
            def init(self, name: Literal["sturdyRef"]) -> SturdyRef.Builder: ...
            def copy(self) -> Gateway.RegResults.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Gateway.RegResults.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        def init(self, name: Literal["sturdyRef"]) -> SturdyRef: ...
        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Gateway.RegResults.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Gateway.RegResults.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            sturdyRef: SturdyRef.Builder | dict[str, Any] | None = None,
            heartbeat: HeartbeatClient | Heartbeat.Server | None = None,
            secsHeartbeatInterval: int | None = None,
        ) -> Gateway.RegResults.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Gateway.RegResults.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Gateway.RegResults.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    class RegisterRequest(Protocol):
        cap: Any
        def send(self) -> Gateway.RegisterResult: ...

    class RegisterResult(Awaitable[RegisterResult], Protocol):
        sturdyRef: SturdyRef.Builder | SturdyRef.Reader
        heartbeat: HeartbeatClient
        secsHeartbeatInterval: int

    @classmethod
    def _new_client(
        cls, server: Gateway.Server | Identifiable.Server | Restorer.Server
    ) -> "GatewayClient": ...
    class Server(Identifiable.Server, Restorer.Server):
        class RegisterResultTuple(NamedTuple):
            sturdyRef: SturdyRef.Builder | SturdyRef.Reader
            heartbeat: Heartbeat.Server
            secsHeartbeatInterval: int

        class RegisterCallContext(Protocol):
            results: Gateway.RegisterResult

        def register(
            self, cap: Any, _context: Gateway.Server.RegisterCallContext, **kwargs: Any
        ) -> Awaitable[Gateway.Server.RegisterResultTuple | None]: ...
        def __enter__(self) -> Self: ...
        def __exit__(self, *args: Any) -> None: ...

class GatewayClient(IdentifiableClient, RestorerClient):
    def register(self, cap: Any | None = None) -> Gateway.RegisterResult: ...
    def register_request(self, cap: Any | None = None) -> Gateway.RegisterRequest: ...
