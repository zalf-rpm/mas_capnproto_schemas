"""This is an automatically generated stub for `storage.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator, Sequence
from contextlib import contextmanager
from io import BufferedWriter
from typing import Any, BinaryIO, Literal, NamedTuple, Protocol, TypeAlias, overload

from .common_capnp import Identifiable, IdentifiableClient, IdInformation, Pair
from .persistence_capnp import Persistent, PersistentClient

class Store:
    class Container:
        class Entry:
            ValueBuilder: TypeAlias = Value.Builder
            ValueReader: TypeAlias = Value.Reader
            class Value:
                class Reader:
                    @property
                    def boolValue(self) -> bool: ...
                    @property
                    def boolListValue(self) -> Sequence[bool]: ...
                    @property
                    def int8Value(self) -> int: ...
                    @property
                    def int8ListValue(self) -> Sequence[int]: ...
                    @property
                    def int16Value(self) -> int: ...
                    @property
                    def int16ListValue(self) -> Sequence[int]: ...
                    @property
                    def int32Value(self) -> int: ...
                    @property
                    def int32ListValue(self) -> Sequence[int]: ...
                    @property
                    def int64Value(self) -> int: ...
                    @property
                    def int64ListValue(self) -> Sequence[int]: ...
                    @property
                    def uint8Value(self) -> int: ...
                    @property
                    def uint8ListValue(self) -> Sequence[int]: ...
                    @property
                    def uint16Value(self) -> int: ...
                    @property
                    def uint16ListValue(self) -> Sequence[int]: ...
                    @property
                    def uint32Value(self) -> int: ...
                    @property
                    def uint32ListValue(self) -> Sequence[int]: ...
                    @property
                    def uint64Value(self) -> int: ...
                    @property
                    def uint64ListValue(self) -> Sequence[int]: ...
                    @property
                    def float32Value(self) -> float: ...
                    @property
                    def float32ListValue(self) -> Sequence[float]: ...
                    @property
                    def float64Value(self) -> float: ...
                    @property
                    def float64ListValue(self) -> Sequence[float]: ...
                    @property
                    def textValue(self) -> str: ...
                    @property
                    def textListValue(self) -> Sequence[str]: ...
                    @property
                    def dataValue(self) -> bytes: ...
                    @property
                    def dataListValue(self) -> Sequence[bytes]: ...
                    @property
                    def anyValue(self) -> Any: ...
                    def which(
                        self,
                    ) -> Literal[
                        "boolValue",
                        "boolListValue",
                        "int8Value",
                        "int8ListValue",
                        "int16Value",
                        "int16ListValue",
                        "int32Value",
                        "int32ListValue",
                        "int64Value",
                        "int64ListValue",
                        "uint8Value",
                        "uint8ListValue",
                        "uint16Value",
                        "uint16ListValue",
                        "uint32Value",
                        "uint32ListValue",
                        "uint64Value",
                        "uint64ListValue",
                        "float32Value",
                        "float32ListValue",
                        "float64Value",
                        "float64ListValue",
                        "textValue",
                        "textListValue",
                        "dataValue",
                        "dataListValue",
                        "anyValue",
                    ]: ...
                    def as_builder(self) -> Store.Container.Entry.Value.Builder: ...

                class Builder:
                    @property
                    def boolValue(self) -> bool: ...
                    @boolValue.setter
                    def boolValue(self, value: bool) -> None: ...
                    @property
                    def boolListValue(self) -> Sequence[bool]: ...
                    @boolListValue.setter
                    def boolListValue(self, value: Sequence[bool]) -> None: ...
                    @property
                    def int8Value(self) -> int: ...
                    @int8Value.setter
                    def int8Value(self, value: int) -> None: ...
                    @property
                    def int8ListValue(self) -> Sequence[int]: ...
                    @int8ListValue.setter
                    def int8ListValue(self, value: Sequence[int]) -> None: ...
                    @property
                    def int16Value(self) -> int: ...
                    @int16Value.setter
                    def int16Value(self, value: int) -> None: ...
                    @property
                    def int16ListValue(self) -> Sequence[int]: ...
                    @int16ListValue.setter
                    def int16ListValue(self, value: Sequence[int]) -> None: ...
                    @property
                    def int32Value(self) -> int: ...
                    @int32Value.setter
                    def int32Value(self, value: int) -> None: ...
                    @property
                    def int32ListValue(self) -> Sequence[int]: ...
                    @int32ListValue.setter
                    def int32ListValue(self, value: Sequence[int]) -> None: ...
                    @property
                    def int64Value(self) -> int: ...
                    @int64Value.setter
                    def int64Value(self, value: int) -> None: ...
                    @property
                    def int64ListValue(self) -> Sequence[int]: ...
                    @int64ListValue.setter
                    def int64ListValue(self, value: Sequence[int]) -> None: ...
                    @property
                    def uint8Value(self) -> int: ...
                    @uint8Value.setter
                    def uint8Value(self, value: int) -> None: ...
                    @property
                    def uint8ListValue(self) -> Sequence[int]: ...
                    @uint8ListValue.setter
                    def uint8ListValue(self, value: Sequence[int]) -> None: ...
                    @property
                    def uint16Value(self) -> int: ...
                    @uint16Value.setter
                    def uint16Value(self, value: int) -> None: ...
                    @property
                    def uint16ListValue(self) -> Sequence[int]: ...
                    @uint16ListValue.setter
                    def uint16ListValue(self, value: Sequence[int]) -> None: ...
                    @property
                    def uint32Value(self) -> int: ...
                    @uint32Value.setter
                    def uint32Value(self, value: int) -> None: ...
                    @property
                    def uint32ListValue(self) -> Sequence[int]: ...
                    @uint32ListValue.setter
                    def uint32ListValue(self, value: Sequence[int]) -> None: ...
                    @property
                    def uint64Value(self) -> int: ...
                    @uint64Value.setter
                    def uint64Value(self, value: int) -> None: ...
                    @property
                    def uint64ListValue(self) -> Sequence[int]: ...
                    @uint64ListValue.setter
                    def uint64ListValue(self, value: Sequence[int]) -> None: ...
                    @property
                    def float32Value(self) -> float: ...
                    @float32Value.setter
                    def float32Value(self, value: float) -> None: ...
                    @property
                    def float32ListValue(self) -> Sequence[float]: ...
                    @float32ListValue.setter
                    def float32ListValue(self, value: Sequence[float]) -> None: ...
                    @property
                    def float64Value(self) -> float: ...
                    @float64Value.setter
                    def float64Value(self, value: float) -> None: ...
                    @property
                    def float64ListValue(self) -> Sequence[float]: ...
                    @float64ListValue.setter
                    def float64ListValue(self, value: Sequence[float]) -> None: ...
                    @property
                    def textValue(self) -> str: ...
                    @textValue.setter
                    def textValue(self, value: str) -> None: ...
                    @property
                    def textListValue(self) -> Sequence[str]: ...
                    @textListValue.setter
                    def textListValue(self, value: Sequence[str]) -> None: ...
                    @property
                    def dataValue(self) -> bytes: ...
                    @dataValue.setter
                    def dataValue(self, value: bytes) -> None: ...
                    @property
                    def dataListValue(self) -> Sequence[bytes]: ...
                    @dataListValue.setter
                    def dataListValue(self, value: Sequence[bytes]) -> None: ...
                    @property
                    def anyValue(self) -> Any: ...
                    @anyValue.setter
                    def anyValue(self, value: Any) -> None: ...
                    def which(
                        self,
                    ) -> Literal[
                        "boolValue",
                        "boolListValue",
                        "int8Value",
                        "int8ListValue",
                        "int16Value",
                        "int16ListValue",
                        "int32Value",
                        "int32ListValue",
                        "int64Value",
                        "int64ListValue",
                        "uint8Value",
                        "uint8ListValue",
                        "uint16Value",
                        "uint16ListValue",
                        "uint32Value",
                        "uint32ListValue",
                        "uint64Value",
                        "uint64ListValue",
                        "float32Value",
                        "float32ListValue",
                        "float64Value",
                        "float64ListValue",
                        "textValue",
                        "textListValue",
                        "dataValue",
                        "dataListValue",
                        "anyValue",
                    ]: ...
                    @staticmethod
                    def from_dict(
                        dictionary: dict[str, Any],
                    ) -> Store.Container.Entry.Value.Builder: ...
                    @overload
                    def init(
                        self: Any, name: Literal["boolListValue"], size: int = ...
                    ) -> Sequence[bool]: ...
                    @overload
                    def init(
                        self: Any, name: Literal["int8ListValue"], size: int = ...
                    ) -> Sequence[int]: ...
                    @overload
                    def init(
                        self: Any, name: Literal["int16ListValue"], size: int = ...
                    ) -> Sequence[int]: ...
                    @overload
                    def init(
                        self: Any, name: Literal["int32ListValue"], size: int = ...
                    ) -> Sequence[int]: ...
                    @overload
                    def init(
                        self: Any, name: Literal["int64ListValue"], size: int = ...
                    ) -> Sequence[int]: ...
                    @overload
                    def init(
                        self: Any, name: Literal["uint8ListValue"], size: int = ...
                    ) -> Sequence[int]: ...
                    @overload
                    def init(
                        self: Any, name: Literal["uint16ListValue"], size: int = ...
                    ) -> Sequence[int]: ...
                    @overload
                    def init(
                        self: Any, name: Literal["uint32ListValue"], size: int = ...
                    ) -> Sequence[int]: ...
                    @overload
                    def init(
                        self: Any, name: Literal["uint64ListValue"], size: int = ...
                    ) -> Sequence[int]: ...
                    @overload
                    def init(
                        self: Any, name: Literal["float32ListValue"], size: int = ...
                    ) -> Sequence[float]: ...
                    @overload
                    def init(
                        self: Any, name: Literal["float64ListValue"], size: int = ...
                    ) -> Sequence[float]: ...
                    @overload
                    def init(
                        self: Any, name: Literal["textListValue"], size: int = ...
                    ) -> Sequence[str]: ...
                    @overload
                    def init(
                        self: Any, name: Literal["dataListValue"], size: int = ...
                    ) -> Sequence[bytes]: ...
                    def init(self: Any, name: str, size: int = ...) -> Any: ...
                    def copy(self) -> Store.Container.Entry.Value.Builder: ...
                    def to_bytes(self) -> bytes: ...
                    def to_bytes_packed(self) -> bytes: ...
                    def to_segments(self) -> list[bytes]: ...
                    def as_reader(self) -> Store.Container.Entry.Value.Reader: ...
                    @staticmethod
                    def write(file: BufferedWriter) -> None: ...
                    @staticmethod
                    def write_packed(file: BufferedWriter) -> None: ...

                def which(
                    self,
                ) -> Literal[
                    "boolValue",
                    "boolListValue",
                    "int8Value",
                    "int8ListValue",
                    "int16Value",
                    "int16ListValue",
                    "int32Value",
                    "int32ListValue",
                    "int64Value",
                    "int64ListValue",
                    "uint8Value",
                    "uint8ListValue",
                    "uint16Value",
                    "uint16ListValue",
                    "uint32Value",
                    "uint32ListValue",
                    "uint64Value",
                    "uint64ListValue",
                    "float32Value",
                    "float32ListValue",
                    "float64Value",
                    "float64ListValue",
                    "textValue",
                    "textListValue",
                    "dataValue",
                    "dataListValue",
                    "anyValue",
                ]: ...
                @staticmethod
                @contextmanager
                def from_bytes(
                    data: bytes,
                    traversal_limit_in_words: int | None = ...,
                    nesting_limit: int | None = ...,
                ) -> Iterator[Store.Container.Entry.Value.Reader]: ...
                @staticmethod
                def from_bytes_packed(
                    data: bytes,
                    traversal_limit_in_words: int | None = ...,
                    nesting_limit: int | None = ...,
                ) -> Store.Container.Entry.Value.Reader: ...
                @staticmethod
                def new_message(
                    num_first_segment_words: int | None = None,
                    allocate_seg_callable: Any = None,
                    boolValue: bool | None = None,
                    boolListValue: Sequence[bool] | None = None,
                    int8Value: int | None = None,
                    int8ListValue: Sequence[int] | None = None,
                    int16Value: int | None = None,
                    int16ListValue: Sequence[int] | None = None,
                    int32Value: int | None = None,
                    int32ListValue: Sequence[int] | None = None,
                    int64Value: int | None = None,
                    int64ListValue: Sequence[int] | None = None,
                    uint8Value: int | None = None,
                    uint8ListValue: Sequence[int] | None = None,
                    uint16Value: int | None = None,
                    uint16ListValue: Sequence[int] | None = None,
                    uint32Value: int | None = None,
                    uint32ListValue: Sequence[int] | None = None,
                    uint64Value: int | None = None,
                    uint64ListValue: Sequence[int] | None = None,
                    float32Value: float | None = None,
                    float32ListValue: Sequence[float] | None = None,
                    float64Value: float | None = None,
                    float64ListValue: Sequence[float] | None = None,
                    textValue: str | None = None,
                    textListValue: Sequence[str] | None = None,
                    dataValue: bytes | None = None,
                    dataListValue: Sequence[bytes] | None = None,
                    anyValue: Any | None = None,
                ) -> Store.Container.Entry.Value.Builder: ...
                @staticmethod
                def read(
                    file: BinaryIO,
                    traversal_limit_in_words: int | None = ...,
                    nesting_limit: int | None = ...,
                ) -> Store.Container.Entry.Value.Reader: ...
                @staticmethod
                def read_packed(
                    file: BinaryIO,
                    traversal_limit_in_words: int | None = ...,
                    nesting_limit: int | None = ...,
                ) -> Store.Container.Entry.Value.Reader: ...
                def to_dict(self) -> dict[str, Any]: ...

            class GetkeyRequest(Protocol):
                def send(self) -> Store.Container.Entry.GetkeyResult: ...

            class GetkeyResult(Awaitable[GetkeyResult], Protocol):
                key: str

            class GetvalueRequest(Protocol):
                def send(self) -> Store.Container.Entry.GetvalueResult: ...

            class GetvalueResult(Awaitable[GetvalueResult], Protocol):
                value: (
                    Store.Container.Entry.Value.Builder
                    | Store.Container.Entry.Value.Reader
                )
                isUnset: bool

            class SetvalueRequest(Protocol):
                value: Store.Container.Entry.Value.Builder
                @overload
                def init(
                    self, name: Literal["value"]
                ) -> Store.Container.Entry.Value.Builder: ...
                @overload
                def init(self, name: str, size: int = ...) -> Any: ...
                def send(self) -> Store.Container.Entry.SetvalueResult: ...

            class SetvalueResult(Awaitable[SetvalueResult], Protocol):
                success: bool

            @classmethod
            def _new_client(
                cls, server: Store.Container.Entry.Server
            ) -> Store.Container.EntryClient: ...
            class Server(Protocol):
                class GetkeyResultTuple(NamedTuple):
                    key: str

                class GetvalueResultTuple(NamedTuple):
                    value: (
                        Store.Container.Entry.Value.Builder
                        | Store.Container.Entry.Value.Reader
                    )
                    isUnset: bool

                class SetvalueResultTuple(NamedTuple):
                    success: bool

                class GetkeyCallContext(Protocol):
                    params: Store.Container.Entry.GetkeyRequest
                    results: Store.Container.Entry.GetkeyResult

                class GetvalueCallContext(Protocol):
                    params: Store.Container.Entry.GetvalueRequest
                    results: Store.Container.Entry.GetvalueResult

                class SetvalueCallContext(Protocol):
                    params: Store.Container.Entry.SetvalueRequest
                    results: Store.Container.Entry.SetvalueResult

                def getKey(
                    self,
                    _context: Store.Container.Entry.Server.GetkeyCallContext,
                    **kwargs: Any,
                ) -> Awaitable[
                    str | Store.Container.Entry.Server.GetkeyResultTuple | None
                ]: ...
                def getKey_context(
                    self, context: Store.Container.Entry.Server.GetkeyCallContext
                ) -> Awaitable[None]: ...
                def getValue(
                    self,
                    _context: Store.Container.Entry.Server.GetvalueCallContext,
                    **kwargs: Any,
                ) -> Awaitable[
                    Store.Container.Entry.Server.GetvalueResultTuple | None
                ]: ...
                def getValue_context(
                    self, context: Store.Container.Entry.Server.GetvalueCallContext
                ) -> Awaitable[None]: ...
                def setValue(
                    self,
                    value: Store.Container.Entry.Value.Reader,
                    _context: Store.Container.Entry.Server.SetvalueCallContext,
                    **kwargs: Any,
                ) -> Awaitable[
                    bool | Store.Container.Entry.Server.SetvalueResultTuple | None
                ]: ...
                def setValue_context(
                    self, context: Store.Container.Entry.Server.SetvalueCallContext
                ) -> Awaitable[None]: ...

        class EntryClient(Protocol):
            def getKey(self) -> Store.Container.Entry.GetkeyResult: ...
            def getValue(self) -> Store.Container.Entry.GetvalueResult: ...
            def setValue(
                self, value: Store.Container.Entry.Value | dict[str, Any] | None = None
            ) -> Store.Container.Entry.SetvalueResult: ...
            def getKey_request(self) -> Store.Container.Entry.GetkeyRequest: ...
            def getValue_request(self) -> Store.Container.Entry.GetvalueRequest: ...
            def setValue_request(
                self, value: Store.Container.Entry.Value.Builder | None = None
            ) -> Store.Container.Entry.SetvalueRequest: ...

        KeyAndEntryBuilder: TypeAlias = KeyAndEntry.Builder
        KeyAndEntryReader: TypeAlias = KeyAndEntry.Reader
        class KeyAndEntry:
            class Reader:
                @property
                def key(self) -> str: ...
                @property
                def entry(self) -> Store.Container.EntryClient: ...
                def as_builder(self) -> Store.Container.KeyAndEntry.Builder: ...

            class Builder:
                @property
                def key(self) -> str: ...
                @key.setter
                def key(self, value: str) -> None: ...
                @property
                def entry(self) -> Store.Container.EntryClient: ...
                @entry.setter
                def entry(
                    self,
                    value: Store.Container.EntryClient | Store.Container.Entry.Server,
                ) -> None: ...
                @staticmethod
                def from_dict(
                    dictionary: dict[str, Any],
                ) -> Store.Container.KeyAndEntry.Builder: ...
                def copy(self) -> Store.Container.KeyAndEntry.Builder: ...
                def to_bytes(self) -> bytes: ...
                def to_bytes_packed(self) -> bytes: ...
                def to_segments(self) -> list[bytes]: ...
                def as_reader(self) -> Store.Container.KeyAndEntry.Reader: ...
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
            ) -> Iterator[Store.Container.KeyAndEntry.Reader]: ...
            @staticmethod
            def from_bytes_packed(
                data: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> Store.Container.KeyAndEntry.Reader: ...
            @staticmethod
            def new_message(
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
                key: str | None = None,
                entry: Store.Container.EntryClient
                | Store.Container.Entry.Server
                | None = None,
            ) -> Store.Container.KeyAndEntry.Builder: ...
            @staticmethod
            def read(
                file: BinaryIO,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> Store.Container.KeyAndEntry.Reader: ...
            @staticmethod
            def read_packed(
                file: BinaryIO,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> Store.Container.KeyAndEntry.Reader: ...
            def to_dict(self) -> dict[str, Any]: ...

        class ExportRequest(Protocol):
            def send(self) -> Store.Container.ExportResult: ...

        class ExportResult(Awaitable[ExportResult], Protocol):
            json: str

        class DownloadentriesRequest(Protocol):
            def send(self) -> Store.Container.DownloadentriesResult: ...

        class DownloadentriesResult(Awaitable[DownloadentriesResult], Protocol):
            entries: Any

        class ListentriesRequest(Protocol):
            def send(self) -> Store.Container.ListentriesResult: ...

        class ListentriesResult(Awaitable[ListentriesResult], Protocol):
            entries: Sequence[
                Store.Container.KeyAndEntry.Builder | Store.Container.KeyAndEntry.Reader
            ]

        class GetentryRequest(Protocol):
            key: str
            def send(self) -> Store.Container.GetentryResult: ...

        class GetentryResult(Awaitable[GetentryResult], Protocol):
            entry: Store.Container.EntryClient

        class RemoveentryRequest(Protocol):
            key: str
            def send(self) -> Store.Container.RemoveentryResult: ...

        class RemoveentryResult(Awaitable[RemoveentryResult], Protocol):
            success: bool

        class ClearRequest(Protocol):
            def send(self) -> Store.Container.ClearResult: ...

        class ClearResult(Awaitable[ClearResult], Protocol):
            success: bool

        class AddentryRequest(Protocol):
            key: str
            value: Store.Container.Entry.Value.Builder
            replaceExisting: bool
            @overload
            def init(
                self, name: Literal["value"]
            ) -> Store.Container.Entry.Value.Builder: ...
            @overload
            def init(self, name: str, size: int = ...) -> Any: ...
            def send(self) -> Store.Container.AddentryResult: ...

        class AddentryResult(Awaitable[AddentryResult], Protocol):
            entry: Store.Container.EntryClient
            success: bool

        @classmethod
        def _new_client(
            cls,
            server: Store.Container.Server | Identifiable.Server | Persistent.Server,
        ) -> Store.ContainerClient: ...
        class Server(Identifiable.Server, Persistent.Server):
            class ExportResultTuple(NamedTuple):
                json: str

            class DownloadentriesResultTuple(NamedTuple):
                pass

            class ListentriesResultTuple(NamedTuple):
                entries: Sequence[Store.Container.KeyAndEntry]

            class GetentryResultTuple(NamedTuple):
                entry: Store.Container.Entry.Server

            class RemoveentryResultTuple(NamedTuple):
                success: bool

            class ClearResultTuple(NamedTuple):
                success: bool

            class AddentryResultTuple(NamedTuple):
                entry: Store.Container.Entry.Server
                success: bool

            class ExportCallContext(Protocol):
                params: Store.Container.ExportRequest
                results: Store.Container.ExportResult

            class DownloadentriesCallContext(Protocol):
                params: Store.Container.DownloadentriesRequest
                results: Store.Container.DownloadentriesResult

            class ListentriesCallContext(Protocol):
                params: Store.Container.ListentriesRequest
                results: Store.Container.ListentriesResult

            class GetentryCallContext(Protocol):
                params: Store.Container.GetentryRequest
                results: Store.Container.GetentryResult

            class RemoveentryCallContext(Protocol):
                params: Store.Container.RemoveentryRequest
                results: Store.Container.RemoveentryResult

            class ClearCallContext(Protocol):
                params: Store.Container.ClearRequest
                results: Store.Container.ClearResult

            class AddentryCallContext(Protocol):
                params: Store.Container.AddentryRequest
                results: Store.Container.AddentryResult

            def export(
                self, _context: Store.Container.Server.ExportCallContext, **kwargs: Any
            ) -> Awaitable[str | Store.Container.Server.ExportResultTuple | None]: ...
            def export_context(
                self, context: Store.Container.Server.ExportCallContext
            ) -> Awaitable[None]: ...
            def downloadEntries(
                self,
                _context: Store.Container.Server.DownloadentriesCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                Store.Container.Server.DownloadentriesResultTuple | None
            ]: ...
            def downloadEntries_context(
                self, context: Store.Container.Server.DownloadentriesCallContext
            ) -> Awaitable[None]: ...
            def listEntries(
                self,
                _context: Store.Container.Server.ListentriesCallContext,
                **kwargs: Any,
            ) -> Awaitable[Store.Container.Server.ListentriesResultTuple | None]: ...
            def listEntries_context(
                self, context: Store.Container.Server.ListentriesCallContext
            ) -> Awaitable[None]: ...
            def getEntry(
                self,
                key: str,
                _context: Store.Container.Server.GetentryCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                Store.Container.Entry.Server
                | Store.Container.Server.GetentryResultTuple
                | None
            ]: ...
            def getEntry_context(
                self, context: Store.Container.Server.GetentryCallContext
            ) -> Awaitable[None]: ...
            def removeEntry(
                self,
                key: str,
                _context: Store.Container.Server.RemoveentryCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                bool | Store.Container.Server.RemoveentryResultTuple | None
            ]: ...
            def removeEntry_context(
                self, context: Store.Container.Server.RemoveentryCallContext
            ) -> Awaitable[None]: ...
            def clear(
                self, _context: Store.Container.Server.ClearCallContext, **kwargs: Any
            ) -> Awaitable[bool | Store.Container.Server.ClearResultTuple | None]: ...
            def clear_context(
                self, context: Store.Container.Server.ClearCallContext
            ) -> Awaitable[None]: ...
            def addEntry(
                self,
                key: str,
                value: Store.Container.Entry.Value.Reader,
                replaceExisting: bool,
                _context: Store.Container.Server.AddentryCallContext,
                **kwargs: Any,
            ) -> Awaitable[Store.Container.Server.AddentryResultTuple | None]: ...
            def addEntry_context(
                self, context: Store.Container.Server.AddentryCallContext
            ) -> Awaitable[None]: ...

    class ContainerClient(IdentifiableClient, PersistentClient):
        def export(self) -> Store.Container.ExportResult: ...
        def downloadEntries(self) -> Store.Container.DownloadentriesResult: ...
        def listEntries(self) -> Store.Container.ListentriesResult: ...
        def getEntry(
            self, key: str | None = None
        ) -> Store.Container.GetentryResult: ...
        def removeEntry(
            self, key: str | None = None
        ) -> Store.Container.RemoveentryResult: ...
        def clear(self) -> Store.Container.ClearResult: ...
        def addEntry(
            self,
            key: str | None = None,
            value: Store.Container.Entry.Value | dict[str, Any] | None = None,
            replaceExisting: bool | None = None,
        ) -> Store.Container.AddentryResult: ...
        def export_request(self) -> Store.Container.ExportRequest: ...
        def downloadEntries_request(self) -> Store.Container.DownloadentriesRequest: ...
        def listEntries_request(self) -> Store.Container.ListentriesRequest: ...
        def getEntry_request(
            self, key: str | None = None
        ) -> Store.Container.GetentryRequest: ...
        def removeEntry_request(
            self, key: str | None = None
        ) -> Store.Container.RemoveentryRequest: ...
        def clear_request(self) -> Store.Container.ClearRequest: ...
        def addEntry_request(
            self,
            key: str | None = None,
            value: Store.Container.Entry.Value.Builder | None = None,
            replaceExisting: bool | None = None,
        ) -> Store.Container.AddentryRequest: ...

    InfoAndContainerBuilder: TypeAlias = InfoAndContainer.Builder
    InfoAndContainerReader: TypeAlias = InfoAndContainer.Reader
    class InfoAndContainer:
        class Reader:
            @property
            def id(self) -> str: ...
            @property
            def name(self) -> str: ...
            @property
            def container(self) -> Store.ContainerClient: ...
            def as_builder(self) -> Store.InfoAndContainer.Builder: ...

        class Builder:
            @property
            def id(self) -> str: ...
            @id.setter
            def id(self, value: str) -> None: ...
            @property
            def name(self) -> str: ...
            @name.setter
            def name(self, value: str) -> None: ...
            @property
            def container(self) -> Store.ContainerClient: ...
            @container.setter
            def container(
                self, value: Store.ContainerClient | Store.Container.Server
            ) -> None: ...
            @staticmethod
            def from_dict(
                dictionary: dict[str, Any],
            ) -> Store.InfoAndContainer.Builder: ...
            def copy(self) -> Store.InfoAndContainer.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Store.InfoAndContainer.Reader: ...
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
        ) -> Iterator[Store.InfoAndContainer.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Store.InfoAndContainer.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            id: str | None = None,
            name: str | None = None,
            container: Store.ContainerClient | Store.Container.Server | None = None,
        ) -> Store.InfoAndContainer.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Store.InfoAndContainer.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Store.InfoAndContainer.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    ImportExportDataBuilder: TypeAlias = ImportExportData.Builder
    ImportExportDataReader: TypeAlias = ImportExportData.Reader
    class ImportExportData:
        class Reader:
            @property
            def info(self) -> IdInformation.Reader: ...
            @property
            def entries(self) -> Sequence[Pair.Reader]: ...
            @property
            def isAnyValue(self) -> Sequence[bool]: ...
            def as_builder(self) -> Store.ImportExportData.Builder: ...

        class Builder:
            @property
            def info(self) -> IdInformation.Builder: ...
            @info.setter
            def info(
                self,
                value: IdInformation.Builder | IdInformation.Reader | dict[str, Any],
            ) -> None: ...
            @property
            def entries(self) -> Sequence[Pair.Builder]: ...
            @entries.setter
            def entries(
                self,
                value: Sequence[Pair.Builder | Pair.Reader] | Sequence[dict[str, Any]],
            ) -> None: ...
            @property
            def isAnyValue(self) -> Sequence[bool]: ...
            @isAnyValue.setter
            def isAnyValue(self, value: Sequence[bool]) -> None: ...
            @staticmethod
            def from_dict(
                dictionary: dict[str, Any],
            ) -> Store.ImportExportData.Builder: ...
            @overload
            def init(self: Any, name: Literal["info"]) -> IdInformation.Builder: ...
            @overload
            def init(
                self: Any, name: Literal["entries"], size: int = ...
            ) -> Sequence[Pair.Builder]: ...
            @overload
            def init(
                self: Any, name: Literal["isAnyValue"], size: int = ...
            ) -> Sequence[bool]: ...
            def init(self: Any, name: str, size: int = ...) -> Any: ...
            def copy(self) -> Store.ImportExportData.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Store.ImportExportData.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        def init(self, name: Literal["info"]) -> IdInformation: ...
        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Store.ImportExportData.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Store.ImportExportData.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            info: IdInformation.Builder | dict[str, Any] | None = None,
            entries: Sequence[Pair.Builder] | Sequence[dict[str, Any]] | None = None,
            isAnyValue: Sequence[bool] | None = None,
        ) -> Store.ImportExportData.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Store.ImportExportData.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Store.ImportExportData.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    class NewcontainerRequest(Protocol):
        name: str
        description: str
        def send(self) -> Store.NewcontainerResult: ...

    class NewcontainerResult(Awaitable[NewcontainerResult], Protocol):
        container: Store.ContainerClient

    class ContainerwithidRequest(Protocol):
        id: str
        def send(self) -> Store.ContainerwithidResult: ...

    class ContainerwithidResult(Awaitable[ContainerwithidResult], Protocol):
        container: Store.ContainerClient

    class ListcontainersRequest(Protocol):
        def send(self) -> Store.ListcontainersResult: ...

    class ListcontainersResult(Awaitable[ListcontainersResult], Protocol):
        containers: Sequence[
            Store.InfoAndContainer.Builder | Store.InfoAndContainer.Reader
        ]

    class RemovecontainerRequest(Protocol):
        id: str
        def send(self) -> Store.RemovecontainerResult: ...

    class RemovecontainerResult(Awaitable[RemovecontainerResult], Protocol):
        success: bool

    class ImportcontainerRequest(Protocol):
        json: str
        def send(self) -> Store.ImportcontainerResult: ...

    class ImportcontainerResult(Awaitable[ImportcontainerResult], Protocol):
        container: Store.ContainerClient

    @classmethod
    def _new_client(
        cls, server: Store.Server | Identifiable.Server | Persistent.Server
    ) -> StoreClient: ...
    class Server(Identifiable.Server, Persistent.Server):
        class NewcontainerResultTuple(NamedTuple):
            container: Store.Container.Server

        class ContainerwithidResultTuple(NamedTuple):
            container: Store.Container.Server

        class ListcontainersResultTuple(NamedTuple):
            containers: Sequence[Store.InfoAndContainer]

        class RemovecontainerResultTuple(NamedTuple):
            success: bool

        class ImportcontainerResultTuple(NamedTuple):
            container: Store.Container.Server

        class NewcontainerCallContext(Protocol):
            params: Store.NewcontainerRequest
            results: Store.NewcontainerResult

        class ContainerwithidCallContext(Protocol):
            params: Store.ContainerwithidRequest
            results: Store.ContainerwithidResult

        class ListcontainersCallContext(Protocol):
            params: Store.ListcontainersRequest
            results: Store.ListcontainersResult

        class RemovecontainerCallContext(Protocol):
            params: Store.RemovecontainerRequest
            results: Store.RemovecontainerResult

        class ImportcontainerCallContext(Protocol):
            params: Store.ImportcontainerRequest
            results: Store.ImportcontainerResult

        def newContainer(
            self,
            name: str,
            description: str,
            _context: Store.Server.NewcontainerCallContext,
            **kwargs: Any,
        ) -> Awaitable[
            Store.Container.Server | Store.Server.NewcontainerResultTuple | None
        ]: ...
        def newContainer_context(
            self, context: Store.Server.NewcontainerCallContext
        ) -> Awaitable[None]: ...
        def containerWithId(
            self,
            id: str,
            _context: Store.Server.ContainerwithidCallContext,
            **kwargs: Any,
        ) -> Awaitable[
            Store.Container.Server | Store.Server.ContainerwithidResultTuple | None
        ]: ...
        def containerWithId_context(
            self, context: Store.Server.ContainerwithidCallContext
        ) -> Awaitable[None]: ...
        def listContainers(
            self, _context: Store.Server.ListcontainersCallContext, **kwargs: Any
        ) -> Awaitable[Store.Server.ListcontainersResultTuple | None]: ...
        def listContainers_context(
            self, context: Store.Server.ListcontainersCallContext
        ) -> Awaitable[None]: ...
        def removeContainer(
            self,
            id: str,
            _context: Store.Server.RemovecontainerCallContext,
            **kwargs: Any,
        ) -> Awaitable[bool | Store.Server.RemovecontainerResultTuple | None]: ...
        def removeContainer_context(
            self, context: Store.Server.RemovecontainerCallContext
        ) -> Awaitable[None]: ...
        def importContainer(
            self,
            json: str,
            _context: Store.Server.ImportcontainerCallContext,
            **kwargs: Any,
        ) -> Awaitable[
            Store.Container.Server | Store.Server.ImportcontainerResultTuple | None
        ]: ...
        def importContainer_context(
            self, context: Store.Server.ImportcontainerCallContext
        ) -> Awaitable[None]: ...

class StoreClient(IdentifiableClient, PersistentClient):
    def newContainer(
        self, name: str | None = None, description: str | None = None
    ) -> Store.NewcontainerResult: ...
    def containerWithId(self, id: str | None = None) -> Store.ContainerwithidResult: ...
    def listContainers(self) -> Store.ListcontainersResult: ...
    def removeContainer(self, id: str | None = None) -> Store.RemovecontainerResult: ...
    def importContainer(
        self, json: str | None = None
    ) -> Store.ImportcontainerResult: ...
    def newContainer_request(
        self, name: str | None = None, description: str | None = None
    ) -> Store.NewcontainerRequest: ...
    def containerWithId_request(
        self, id: str | None = None
    ) -> Store.ContainerwithidRequest: ...
    def listContainers_request(self) -> Store.ListcontainersRequest: ...
    def removeContainer_request(
        self, id: str | None = None
    ) -> Store.RemovecontainerRequest: ...
    def importContainer_request(
        self, json: str | None = None
    ) -> Store.ImportcontainerRequest: ...
