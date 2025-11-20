"""This is an automatically generated stub for `storage.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, MutableSequence, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, NamedTuple, Protocol, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
    _StructModule,
)

from .common_capnp import (
    _IdentifiableModule,
    _IdInformationModule,
    _PairModule,
)
from .persistence_capnp import _PersistentModule

class _StoreModule(_IdentifiableModule, _PersistentModule):
    class _ContainerModule(_IdentifiableModule, _PersistentModule):
        class _EntryModule(_InterfaceModule):
            class _ValueModule(_StructModule):
                class Reader(_DynamicStructReader):
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
                    @override
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
                    @override
                    def as_builder(
                        self,
                        num_first_segment_words: int | None = None,
                        allocate_seg_callable: Any = None,
                    ) -> ValueBuilder: ...

                class Builder(_DynamicStructBuilder):
                    @property
                    def boolValue(self) -> bool: ...
                    @boolValue.setter
                    def boolValue(self, value: bool) -> None: ...
                    @property
                    def boolListValue(self) -> MutableSequence[bool]: ...
                    @boolListValue.setter
                    def boolListValue(self, value: Sequence[bool]) -> None: ...
                    @property
                    def int8Value(self) -> int: ...
                    @int8Value.setter
                    def int8Value(self, value: int) -> None: ...
                    @property
                    def int8ListValue(self) -> MutableSequence[int]: ...
                    @int8ListValue.setter
                    def int8ListValue(self, value: Sequence[int]) -> None: ...
                    @property
                    def int16Value(self) -> int: ...
                    @int16Value.setter
                    def int16Value(self, value: int) -> None: ...
                    @property
                    def int16ListValue(self) -> MutableSequence[int]: ...
                    @int16ListValue.setter
                    def int16ListValue(self, value: Sequence[int]) -> None: ...
                    @property
                    def int32Value(self) -> int: ...
                    @int32Value.setter
                    def int32Value(self, value: int) -> None: ...
                    @property
                    def int32ListValue(self) -> MutableSequence[int]: ...
                    @int32ListValue.setter
                    def int32ListValue(self, value: Sequence[int]) -> None: ...
                    @property
                    def int64Value(self) -> int: ...
                    @int64Value.setter
                    def int64Value(self, value: int) -> None: ...
                    @property
                    def int64ListValue(self) -> MutableSequence[int]: ...
                    @int64ListValue.setter
                    def int64ListValue(self, value: Sequence[int]) -> None: ...
                    @property
                    def uint8Value(self) -> int: ...
                    @uint8Value.setter
                    def uint8Value(self, value: int) -> None: ...
                    @property
                    def uint8ListValue(self) -> MutableSequence[int]: ...
                    @uint8ListValue.setter
                    def uint8ListValue(self, value: Sequence[int]) -> None: ...
                    @property
                    def uint16Value(self) -> int: ...
                    @uint16Value.setter
                    def uint16Value(self, value: int) -> None: ...
                    @property
                    def uint16ListValue(self) -> MutableSequence[int]: ...
                    @uint16ListValue.setter
                    def uint16ListValue(self, value: Sequence[int]) -> None: ...
                    @property
                    def uint32Value(self) -> int: ...
                    @uint32Value.setter
                    def uint32Value(self, value: int) -> None: ...
                    @property
                    def uint32ListValue(self) -> MutableSequence[int]: ...
                    @uint32ListValue.setter
                    def uint32ListValue(self, value: Sequence[int]) -> None: ...
                    @property
                    def uint64Value(self) -> int: ...
                    @uint64Value.setter
                    def uint64Value(self, value: int) -> None: ...
                    @property
                    def uint64ListValue(self) -> MutableSequence[int]: ...
                    @uint64ListValue.setter
                    def uint64ListValue(self, value: Sequence[int]) -> None: ...
                    @property
                    def float32Value(self) -> float: ...
                    @float32Value.setter
                    def float32Value(self, value: float) -> None: ...
                    @property
                    def float32ListValue(self) -> MutableSequence[float]: ...
                    @float32ListValue.setter
                    def float32ListValue(self, value: Sequence[float]) -> None: ...
                    @property
                    def float64Value(self) -> float: ...
                    @float64Value.setter
                    def float64Value(self, value: float) -> None: ...
                    @property
                    def float64ListValue(self) -> MutableSequence[float]: ...
                    @float64ListValue.setter
                    def float64ListValue(self, value: Sequence[float]) -> None: ...
                    @property
                    def textValue(self) -> str: ...
                    @textValue.setter
                    def textValue(self, value: str) -> None: ...
                    @property
                    def textListValue(self) -> MutableSequence[str]: ...
                    @textListValue.setter
                    def textListValue(self, value: Sequence[str]) -> None: ...
                    @property
                    def dataValue(self) -> bytes: ...
                    @dataValue.setter
                    def dataValue(self, value: bytes) -> None: ...
                    @property
                    def dataListValue(self) -> MutableSequence[bytes]: ...
                    @dataListValue.setter
                    def dataListValue(self, value: Sequence[bytes]) -> None: ...
                    @property
                    def anyValue(self) -> Any: ...
                    @anyValue.setter
                    def anyValue(self, value: Any) -> None: ...
                    @override
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
                    @overload
                    def init(
                        self, field: Literal["boolListValue"], size: int | None = None
                    ) -> MutableSequence[bool]: ...
                    @overload
                    def init(
                        self, field: Literal["int8ListValue"], size: int | None = None
                    ) -> MutableSequence[int]: ...
                    @overload
                    def init(
                        self, field: Literal["int16ListValue"], size: int | None = None
                    ) -> MutableSequence[int]: ...
                    @overload
                    def init(
                        self, field: Literal["int32ListValue"], size: int | None = None
                    ) -> MutableSequence[int]: ...
                    @overload
                    def init(
                        self, field: Literal["int64ListValue"], size: int | None = None
                    ) -> MutableSequence[int]: ...
                    @overload
                    def init(
                        self, field: Literal["uint8ListValue"], size: int | None = None
                    ) -> MutableSequence[int]: ...
                    @overload
                    def init(
                        self, field: Literal["uint16ListValue"], size: int | None = None
                    ) -> MutableSequence[int]: ...
                    @overload
                    def init(
                        self, field: Literal["uint32ListValue"], size: int | None = None
                    ) -> MutableSequence[int]: ...
                    @overload
                    def init(
                        self, field: Literal["uint64ListValue"], size: int | None = None
                    ) -> MutableSequence[int]: ...
                    @overload
                    def init(
                        self,
                        field: Literal["float32ListValue"],
                        size: int | None = None,
                    ) -> MutableSequence[float]: ...
                    @overload
                    def init(
                        self,
                        field: Literal["float64ListValue"],
                        size: int | None = None,
                    ) -> MutableSequence[float]: ...
                    @overload
                    def init(
                        self, field: Literal["textListValue"], size: int | None = None
                    ) -> MutableSequence[str]: ...
                    @overload
                    def init(
                        self, field: Literal["dataListValue"], size: int | None = None
                    ) -> MutableSequence[bytes]: ...
                    @overload
                    def init(self, field: str, size: int | None = None) -> Any: ...
                    @override
                    def as_reader(self) -> ValueReader: ...

                @override
                def new_message(
                    self,
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
                    **kwargs: Any,
                ) -> ValueBuilder: ...
                @overload
                def from_bytes(
                    self,
                    buf: bytes,
                    traversal_limit_in_words: int | None = ...,
                    nesting_limit: int | None = ...,
                ) -> AbstractContextManager[ValueReader]: ...
                @overload
                def from_bytes(
                    self,
                    buf: bytes,
                    traversal_limit_in_words: int | None = ...,
                    nesting_limit: int | None = ...,
                    *,
                    builder: Literal[False],
                ) -> AbstractContextManager[ValueReader]: ...
                @overload
                def from_bytes(
                    self,
                    buf: bytes,
                    traversal_limit_in_words: int | None = ...,
                    nesting_limit: int | None = ...,
                    *,
                    builder: Literal[True],
                ) -> AbstractContextManager[ValueBuilder]: ...
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
                ) -> ValueReader: ...
                @override
                def read_packed(
                    self,
                    file: IO[str] | IO[bytes],
                    traversal_limit_in_words: int | None = ...,
                    nesting_limit: int | None = ...,
                ) -> ValueReader: ...

            type ValueReader = _ValueModule.Reader
            type ValueBuilder = _ValueModule.Builder
            Value: _ValueModule
            class GetkeyRequest(Protocol):
                def send(
                    self,
                ) -> (
                    _StoreModule._ContainerModule._EntryModule.EntryClient.GetkeyResult
                ): ...

            class GetvalueRequest(Protocol):
                def send(
                    self,
                ) -> _StoreModule._ContainerModule._EntryModule.EntryClient.GetvalueResult: ...

            class SetvalueRequest(Protocol):
                value: ValueBuilder
                @overload
                def init(self, name: Literal["value"]) -> ValueBuilder: ...
                @overload
                def init(self, name: str, size: int = ...) -> Any: ...
                def send(
                    self,
                ) -> _StoreModule._ContainerModule._EntryModule.EntryClient.SetvalueResult: ...

            def _new_client(
                self, server: _DynamicCapabilityServer
            ) -> _StoreModule._ContainerModule._EntryModule.EntryClient: ...
            class Server(_DynamicCapabilityServer):
                class GetkeyResult(Awaitable[GetkeyResult], Protocol):
                    key: str

                class GetvalueResult(Awaitable[GetvalueResult], Protocol):
                    value: ValueBuilder | ValueReader
                    isUnset: bool

                class SetvalueResult(Awaitable[SetvalueResult], Protocol):
                    success: bool

                class GetkeyResultTuple(NamedTuple):
                    key: str

                class GetvalueResultTuple(NamedTuple):
                    value: (
                        _StoreModule._ContainerModule._EntryModule._ValueModule.Builder
                        | _StoreModule._ContainerModule._EntryModule._ValueModule.Reader
                    )
                    isUnset: bool

                class SetvalueResultTuple(NamedTuple):
                    success: bool

                class GetkeyParams(Protocol): ...

                class GetkeyCallContext(Protocol):
                    params: (
                        _StoreModule._ContainerModule._EntryModule.Server.GetkeyParams
                    )
                    results: (
                        _StoreModule._ContainerModule._EntryModule.Server.GetkeyResult
                    )

                class GetvalueParams(Protocol): ...

                class GetvalueCallContext(Protocol):
                    params: (
                        _StoreModule._ContainerModule._EntryModule.Server.GetvalueParams
                    )
                    results: (
                        _StoreModule._ContainerModule._EntryModule.Server.GetvalueResult
                    )

                class SetvalueParams(Protocol):
                    value: ValueReader

                class SetvalueCallContext(Protocol):
                    params: (
                        _StoreModule._ContainerModule._EntryModule.Server.SetvalueParams
                    )
                    results: (
                        _StoreModule._ContainerModule._EntryModule.Server.SetvalueResult
                    )

                def getKey(
                    self,
                    _context: _StoreModule._ContainerModule._EntryModule.Server.GetkeyCallContext,
                    **kwargs: dict[str, Any],
                ) -> Awaitable[
                    str
                    | _StoreModule._ContainerModule._EntryModule.Server.GetkeyResultTuple
                    | None
                ]: ...
                def getKey_context(
                    self,
                    context: _StoreModule._ContainerModule._EntryModule.Server.GetkeyCallContext,
                ) -> Awaitable[None]: ...
                def getValue(
                    self,
                    _context: _StoreModule._ContainerModule._EntryModule.Server.GetvalueCallContext,
                    **kwargs: dict[str, Any],
                ) -> Awaitable[
                    _StoreModule._ContainerModule._EntryModule.Server.GetvalueResultTuple
                    | None
                ]: ...
                def getValue_context(
                    self,
                    context: _StoreModule._ContainerModule._EntryModule.Server.GetvalueCallContext,
                ) -> Awaitable[None]: ...
                def setValue(
                    self,
                    value: ValueReader,
                    _context: _StoreModule._ContainerModule._EntryModule.Server.SetvalueCallContext,
                    **kwargs: dict[str, Any],
                ) -> Awaitable[
                    bool
                    | _StoreModule._ContainerModule._EntryModule.Server.SetvalueResultTuple
                    | None
                ]: ...
                def setValue_context(
                    self,
                    context: _StoreModule._ContainerModule._EntryModule.Server.SetvalueCallContext,
                ) -> Awaitable[None]: ...

            class EntryClient(_DynamicCapabilityClient):
                class GetkeyResult(Awaitable[GetkeyResult], Protocol):
                    key: str

                class GetvalueResult(Awaitable[GetvalueResult], Protocol):
                    value: ValueReader
                    isUnset: bool

                class SetvalueResult(Awaitable[SetvalueResult], Protocol):
                    success: bool

                def getKey(
                    self,
                ) -> (
                    _StoreModule._ContainerModule._EntryModule.EntryClient.GetkeyResult
                ): ...
                def getValue(
                    self,
                ) -> _StoreModule._ContainerModule._EntryModule.EntryClient.GetvalueResult: ...
                def setValue(
                    self,
                    value: ValueBuilder | ValueReader | dict[str, Any] | None = None,
                ) -> _StoreModule._ContainerModule._EntryModule.EntryClient.SetvalueResult: ...
                def getKey_request(
                    self,
                ) -> _StoreModule._ContainerModule._EntryModule.GetkeyRequest: ...
                def getValue_request(
                    self,
                ) -> _StoreModule._ContainerModule._EntryModule.GetvalueRequest: ...
                def setValue_request(
                    self, value: ValueBuilder | None = None
                ) -> _StoreModule._ContainerModule._EntryModule.SetvalueRequest: ...

        Entry: _EntryModule
        type EntryClient = _StoreModule._ContainerModule._EntryModule.EntryClient
        class _KeyAndEntryModule(_StructModule):
            class Reader(_DynamicStructReader):
                @property
                def key(self) -> str: ...
                @property
                def entry(
                    self,
                ) -> _StoreModule._ContainerModule._EntryModule.EntryClient: ...
                @override
                def as_builder(
                    self,
                    num_first_segment_words: int | None = None,
                    allocate_seg_callable: Any = None,
                ) -> KeyAndEntryBuilder: ...

            class Builder(_DynamicStructBuilder):
                @property
                def key(self) -> str: ...
                @key.setter
                def key(self, value: str) -> None: ...
                @property
                def entry(
                    self,
                ) -> _StoreModule._ContainerModule._EntryModule.EntryClient: ...
                @entry.setter
                def entry(
                    self,
                    value: _StoreModule._ContainerModule._EntryModule.EntryClient
                    | _StoreModule._ContainerModule._EntryModule.Server,
                ) -> None: ...
                @override
                def as_reader(self) -> KeyAndEntryReader: ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
                key: str | None = None,
                entry: _StoreModule._ContainerModule._EntryModule.EntryClient
                | _StoreModule._ContainerModule._EntryModule.Server
                | None = None,
                **kwargs: Any,
            ) -> KeyAndEntryBuilder: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> AbstractContextManager[KeyAndEntryReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[KeyAndEntryReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[KeyAndEntryBuilder]: ...
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
            ) -> KeyAndEntryReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> KeyAndEntryReader: ...

        type KeyAndEntryReader = _KeyAndEntryModule.Reader
        type KeyAndEntryBuilder = _KeyAndEntryModule.Builder
        KeyAndEntry: _KeyAndEntryModule
        class ExportRequest(Protocol):
            def send(
                self,
            ) -> _StoreModule._ContainerModule.ContainerClient.ExportResult: ...

        class DownloadentriesRequest(Protocol):
            def send(
                self,
            ) -> (
                _StoreModule._ContainerModule.ContainerClient.DownloadentriesResult
            ): ...

        class ListentriesRequest(Protocol):
            def send(
                self,
            ) -> _StoreModule._ContainerModule.ContainerClient.ListentriesResult: ...

        class GetentryRequest(Protocol):
            key: str
            def send(
                self,
            ) -> _StoreModule._ContainerModule.ContainerClient.GetentryResult: ...

        class RemoveentryRequest(Protocol):
            key: str
            def send(
                self,
            ) -> _StoreModule._ContainerModule.ContainerClient.RemoveentryResult: ...

        class ClearRequest(Protocol):
            def send(
                self,
            ) -> _StoreModule._ContainerModule.ContainerClient.ClearResult: ...

        class AddentryRequest(Protocol):
            key: str
            value: ValueBuilder
            replaceExisting: bool
            @overload
            def init(self, name: Literal["value"]) -> ValueBuilder: ...
            @overload
            def init(self, name: str, size: int = ...) -> Any: ...
            def send(
                self,
            ) -> _StoreModule._ContainerModule.ContainerClient.AddentryResult: ...

        def _new_client(
            self, server: _DynamicCapabilityServer
        ) -> _StoreModule._ContainerModule.ContainerClient: ...
        class Server(_IdentifiableModule.Server, _PersistentModule.Server):
            class ExportResult(Awaitable[ExportResult], Protocol):
                json: str

            class DownloadentriesResult(Awaitable[DownloadentriesResult], Protocol):
                entries: Any

            class ListentriesResult(Awaitable[ListentriesResult], Protocol):
                entries: Sequence[
                    _StoreModule._ContainerModule._KeyAndEntryModule.Builder
                    | _StoreModule._ContainerModule._KeyAndEntryModule.Reader
                ]

            class GetentryResult(Awaitable[GetentryResult], Protocol):
                entry: _StoreModule._ContainerModule._EntryModule.EntryClient

            class RemoveentryResult(Awaitable[RemoveentryResult], Protocol):
                success: bool

            class ClearResult(Awaitable[ClearResult], Protocol):
                success: bool

            class AddentryResult(Awaitable[AddentryResult], Protocol):
                entry: _StoreModule._ContainerModule._EntryModule.EntryClient
                success: bool

            class ExportResultTuple(NamedTuple):
                json: str

            class DownloadentriesResultTuple(NamedTuple):
                pass

            class ListentriesResultTuple(NamedTuple):
                entries: Sequence[_StoreModule._ContainerModule._KeyAndEntryModule]

            class GetentryResultTuple(NamedTuple):
                entry: _StoreModule._ContainerModule._EntryModule.Server

            class RemoveentryResultTuple(NamedTuple):
                success: bool

            class ClearResultTuple(NamedTuple):
                success: bool

            class AddentryResultTuple(NamedTuple):
                entry: _StoreModule._ContainerModule._EntryModule.Server
                success: bool

            class ExportParams(Protocol): ...

            class ExportCallContext(Protocol):
                params: _StoreModule._ContainerModule.Server.ExportParams
                results: _StoreModule._ContainerModule.Server.ExportResult

            class DownloadentriesParams(Protocol): ...

            class DownloadentriesCallContext(Protocol):
                params: _StoreModule._ContainerModule.Server.DownloadentriesParams
                results: _StoreModule._ContainerModule.Server.DownloadentriesResult

            class ListentriesParams(Protocol): ...

            class ListentriesCallContext(Protocol):
                params: _StoreModule._ContainerModule.Server.ListentriesParams
                results: _StoreModule._ContainerModule.Server.ListentriesResult

            class GetentryParams(Protocol):
                key: str

            class GetentryCallContext(Protocol):
                params: _StoreModule._ContainerModule.Server.GetentryParams
                results: _StoreModule._ContainerModule.Server.GetentryResult

            class RemoveentryParams(Protocol):
                key: str

            class RemoveentryCallContext(Protocol):
                params: _StoreModule._ContainerModule.Server.RemoveentryParams
                results: _StoreModule._ContainerModule.Server.RemoveentryResult

            class ClearParams(Protocol): ...

            class ClearCallContext(Protocol):
                params: _StoreModule._ContainerModule.Server.ClearParams
                results: _StoreModule._ContainerModule.Server.ClearResult

            class AddentryParams(Protocol):
                key: str
                value: ValueReader
                replaceExisting: bool

            class AddentryCallContext(Protocol):
                params: _StoreModule._ContainerModule.Server.AddentryParams
                results: _StoreModule._ContainerModule.Server.AddentryResult

            def export(
                self,
                _context: _StoreModule._ContainerModule.Server.ExportCallContext,
                **kwargs: dict[str, Any],
            ) -> Awaitable[
                str | _StoreModule._ContainerModule.Server.ExportResultTuple | None
            ]: ...
            def export_context(
                self, context: _StoreModule._ContainerModule.Server.ExportCallContext
            ) -> Awaitable[None]: ...
            def downloadEntries(
                self,
                _context: _StoreModule._ContainerModule.Server.DownloadentriesCallContext,
                **kwargs: dict[str, Any],
            ) -> Awaitable[
                _StoreModule._ContainerModule.Server.DownloadentriesResultTuple | None
            ]: ...
            def downloadEntries_context(
                self,
                context: _StoreModule._ContainerModule.Server.DownloadentriesCallContext,
            ) -> Awaitable[None]: ...
            def listEntries(
                self,
                _context: _StoreModule._ContainerModule.Server.ListentriesCallContext,
                **kwargs: dict[str, Any],
            ) -> Awaitable[
                _StoreModule._ContainerModule.Server.ListentriesResultTuple | None
            ]: ...
            def listEntries_context(
                self,
                context: _StoreModule._ContainerModule.Server.ListentriesCallContext,
            ) -> Awaitable[None]: ...
            def getEntry(
                self,
                key: str,
                _context: _StoreModule._ContainerModule.Server.GetentryCallContext,
                **kwargs: dict[str, Any],
            ) -> Awaitable[
                _StoreModule._ContainerModule._EntryModule.Server
                | _StoreModule._ContainerModule.Server.GetentryResultTuple
                | None
            ]: ...
            def getEntry_context(
                self, context: _StoreModule._ContainerModule.Server.GetentryCallContext
            ) -> Awaitable[None]: ...
            def removeEntry(
                self,
                key: str,
                _context: _StoreModule._ContainerModule.Server.RemoveentryCallContext,
                **kwargs: dict[str, Any],
            ) -> Awaitable[
                bool
                | _StoreModule._ContainerModule.Server.RemoveentryResultTuple
                | None
            ]: ...
            def removeEntry_context(
                self,
                context: _StoreModule._ContainerModule.Server.RemoveentryCallContext,
            ) -> Awaitable[None]: ...
            def clear(
                self,
                _context: _StoreModule._ContainerModule.Server.ClearCallContext,
                **kwargs: dict[str, Any],
            ) -> Awaitable[
                bool | _StoreModule._ContainerModule.Server.ClearResultTuple | None
            ]: ...
            def clear_context(
                self, context: _StoreModule._ContainerModule.Server.ClearCallContext
            ) -> Awaitable[None]: ...
            def addEntry(
                self,
                key: str,
                value: ValueReader,
                replaceExisting: bool,
                _context: _StoreModule._ContainerModule.Server.AddentryCallContext,
                **kwargs: dict[str, Any],
            ) -> Awaitable[
                _StoreModule._ContainerModule.Server.AddentryResultTuple | None
            ]: ...
            def addEntry_context(
                self, context: _StoreModule._ContainerModule.Server.AddentryCallContext
            ) -> Awaitable[None]: ...

        class ContainerClient(
            _IdentifiableModule.IdentifiableClient, _PersistentModule.PersistentClient
        ):
            class ExportResult(Awaitable[ExportResult], Protocol):
                json: str

            class DownloadentriesResult(Awaitable[DownloadentriesResult], Protocol):
                entries: Any

            class ListentriesResult(Awaitable[ListentriesResult], Protocol):
                entries: Sequence[
                    _StoreModule._ContainerModule._KeyAndEntryModule.Builder
                    | _StoreModule._ContainerModule._KeyAndEntryModule.Reader
                ]

            class GetentryResult(Awaitable[GetentryResult], Protocol):
                entry: _StoreModule._ContainerModule._EntryModule.EntryClient

            class RemoveentryResult(Awaitable[RemoveentryResult], Protocol):
                success: bool

            class ClearResult(Awaitable[ClearResult], Protocol):
                success: bool

            class AddentryResult(Awaitable[AddentryResult], Protocol):
                entry: _StoreModule._ContainerModule._EntryModule.EntryClient
                success: bool

            def export(
                self,
            ) -> _StoreModule._ContainerModule.ContainerClient.ExportResult: ...
            def downloadEntries(
                self,
            ) -> (
                _StoreModule._ContainerModule.ContainerClient.DownloadentriesResult
            ): ...
            def listEntries(
                self,
            ) -> _StoreModule._ContainerModule.ContainerClient.ListentriesResult: ...
            def getEntry(
                self, key: str | None = None
            ) -> _StoreModule._ContainerModule.ContainerClient.GetentryResult: ...
            def removeEntry(
                self, key: str | None = None
            ) -> _StoreModule._ContainerModule.ContainerClient.RemoveentryResult: ...
            def clear(
                self,
            ) -> _StoreModule._ContainerModule.ContainerClient.ClearResult: ...
            def addEntry(
                self,
                key: str | None = None,
                value: ValueBuilder | ValueReader | dict[str, Any] | None = None,
                replaceExisting: bool | None = None,
            ) -> _StoreModule._ContainerModule.ContainerClient.AddentryResult: ...
            def export_request(self) -> _StoreModule._ContainerModule.ExportRequest: ...
            def downloadEntries_request(
                self,
            ) -> _StoreModule._ContainerModule.DownloadentriesRequest: ...
            def listEntries_request(
                self,
            ) -> _StoreModule._ContainerModule.ListentriesRequest: ...
            def getEntry_request(
                self, key: str | None = None
            ) -> _StoreModule._ContainerModule.GetentryRequest: ...
            def removeEntry_request(
                self, key: str | None = None
            ) -> _StoreModule._ContainerModule.RemoveentryRequest: ...
            def clear_request(self) -> _StoreModule._ContainerModule.ClearRequest: ...
            def addEntry_request(
                self,
                key: str | None = None,
                value: ValueBuilder | None = None,
                replaceExisting: bool | None = None,
            ) -> _StoreModule._ContainerModule.AddentryRequest: ...

    Container: _ContainerModule
    type ContainerClient = _StoreModule._ContainerModule.ContainerClient
    class _InfoAndContainerModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def id(self) -> str: ...
            @property
            def name(self) -> str: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
            @property
            def container(self) -> _StoreModule._ContainerModule.ContainerClient: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> InfoAndContainerBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def id(self) -> str: ...
            @id.setter
            def id(self, value: str) -> None: ...
            @property
            def name(self) -> str: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
            @name.setter
            def name(self, value: str) -> None: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
            @property
            def container(self) -> _StoreModule._ContainerModule.ContainerClient: ...
            @container.setter
            def container(
                self,
                value: _StoreModule._ContainerModule.ContainerClient
                | _StoreModule._ContainerModule.Server,
            ) -> None: ...
            @override
            def as_reader(self) -> InfoAndContainerReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            id: str | None = None,
            name: str | None = None,
            container: _StoreModule._ContainerModule.ContainerClient
            | _StoreModule._ContainerModule.Server
            | None = None,
            **kwargs: Any,
        ) -> InfoAndContainerBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[InfoAndContainerReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[InfoAndContainerReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[InfoAndContainerBuilder]: ...
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
        ) -> InfoAndContainerReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> InfoAndContainerReader: ...

    type InfoAndContainerReader = _InfoAndContainerModule.Reader
    type InfoAndContainerBuilder = _InfoAndContainerModule.Builder
    InfoAndContainer: _InfoAndContainerModule
    class _ImportExportDataModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def info(self) -> _IdInformationModule.Reader: ...
            @property
            def entries(self) -> Sequence[_PairModule.Reader]: ...
            @property
            def isAnyValue(self) -> Sequence[bool]: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> ImportExportDataBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def info(self) -> _IdInformationModule.Builder: ...
            @info.setter
            def info(
                self,
                value: _IdInformationModule.Builder
                | _IdInformationModule.Reader
                | dict[str, Any],
            ) -> None: ...
            @property
            def entries(self) -> MutableSequence[_PairModule.Builder]: ...
            @entries.setter
            def entries(
                self,
                value: Sequence[_PairModule.Builder | _PairModule.Reader]
                | Sequence[dict[str, Any]],
            ) -> None: ...
            @property
            def isAnyValue(self) -> MutableSequence[bool]: ...
            @isAnyValue.setter
            def isAnyValue(self, value: Sequence[bool]) -> None: ...
            @overload
            def init(
                self, field: Literal["info"], size: int | None = None
            ) -> _IdInformationModule.Builder: ...
            @overload
            def init(
                self, field: Literal["entries"], size: int | None = None
            ) -> MutableSequence[_PairModule.Builder]: ...
            @overload
            def init(
                self, field: Literal["isAnyValue"], size: int | None = None
            ) -> MutableSequence[bool]: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...
            @override
            def as_reader(self) -> ImportExportDataReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            info: _IdInformationModule.Builder | dict[str, Any] | None = None,
            entries: Sequence[_PairModule.Builder]
            | Sequence[dict[str, Any]]
            | None = None,
            isAnyValue: Sequence[bool] | None = None,
            **kwargs: Any,
        ) -> ImportExportDataBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[ImportExportDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[ImportExportDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[ImportExportDataBuilder]: ...
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
        ) -> ImportExportDataReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> ImportExportDataReader: ...

    type ImportExportDataReader = _ImportExportDataModule.Reader
    type ImportExportDataBuilder = _ImportExportDataModule.Builder
    ImportExportData: _ImportExportDataModule
    class NewcontainerRequest(Protocol):
        name: str
        description: str
        def send(self) -> _StoreModule.StoreClient.NewcontainerResult: ...

    class ContainerwithidRequest(Protocol):
        id: str
        def send(self) -> _StoreModule.StoreClient.ContainerwithidResult: ...

    class ListcontainersRequest(Protocol):
        def send(self) -> _StoreModule.StoreClient.ListcontainersResult: ...

    class RemovecontainerRequest(Protocol):
        id: str
        def send(self) -> _StoreModule.StoreClient.RemovecontainerResult: ...

    class ImportcontainerRequest(Protocol):
        json: str
        def send(self) -> _StoreModule.StoreClient.ImportcontainerResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _StoreModule.StoreClient: ...
    class Server(_IdentifiableModule.Server, _PersistentModule.Server):
        class NewcontainerResult(Awaitable[NewcontainerResult], Protocol):
            container: _StoreModule._ContainerModule.ContainerClient

        class ContainerwithidResult(Awaitable[ContainerwithidResult], Protocol):
            container: _StoreModule._ContainerModule.ContainerClient

        class ListcontainersResult(Awaitable[ListcontainersResult], Protocol):
            containers: Sequence[
                _StoreModule._InfoAndContainerModule.Builder
                | _StoreModule._InfoAndContainerModule.Reader
            ]

        class RemovecontainerResult(Awaitable[RemovecontainerResult], Protocol):
            success: bool

        class ImportcontainerResult(Awaitable[ImportcontainerResult], Protocol):
            container: _StoreModule._ContainerModule.ContainerClient

        class NewcontainerResultTuple(NamedTuple):
            container: _StoreModule._ContainerModule.Server

        class ContainerwithidResultTuple(NamedTuple):
            container: _StoreModule._ContainerModule.Server

        class ListcontainersResultTuple(NamedTuple):
            containers: Sequence[_StoreModule._InfoAndContainerModule]

        class RemovecontainerResultTuple(NamedTuple):
            success: bool

        class ImportcontainerResultTuple(NamedTuple):
            container: _StoreModule._ContainerModule.Server

        class NewcontainerParams(Protocol):
            name: str
            description: str

        class NewcontainerCallContext(Protocol):
            params: _StoreModule.Server.NewcontainerParams
            results: _StoreModule.Server.NewcontainerResult

        class ContainerwithidParams(Protocol):
            id: str

        class ContainerwithidCallContext(Protocol):
            params: _StoreModule.Server.ContainerwithidParams
            results: _StoreModule.Server.ContainerwithidResult

        class ListcontainersParams(Protocol): ...

        class ListcontainersCallContext(Protocol):
            params: _StoreModule.Server.ListcontainersParams
            results: _StoreModule.Server.ListcontainersResult

        class RemovecontainerParams(Protocol):
            id: str

        class RemovecontainerCallContext(Protocol):
            params: _StoreModule.Server.RemovecontainerParams
            results: _StoreModule.Server.RemovecontainerResult

        class ImportcontainerParams(Protocol):
            json: str

        class ImportcontainerCallContext(Protocol):
            params: _StoreModule.Server.ImportcontainerParams
            results: _StoreModule.Server.ImportcontainerResult

        def newContainer(
            self,
            name: str,
            description: str,
            _context: _StoreModule.Server.NewcontainerCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[
            _StoreModule._ContainerModule.Server
            | _StoreModule.Server.NewcontainerResultTuple
            | None
        ]: ...
        def newContainer_context(
            self, context: _StoreModule.Server.NewcontainerCallContext
        ) -> Awaitable[None]: ...
        def containerWithId(
            self,
            id: str,
            _context: _StoreModule.Server.ContainerwithidCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[
            _StoreModule._ContainerModule.Server
            | _StoreModule.Server.ContainerwithidResultTuple
            | None
        ]: ...
        def containerWithId_context(
            self, context: _StoreModule.Server.ContainerwithidCallContext
        ) -> Awaitable[None]: ...
        def listContainers(
            self,
            _context: _StoreModule.Server.ListcontainersCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_StoreModule.Server.ListcontainersResultTuple | None]: ...
        def listContainers_context(
            self, context: _StoreModule.Server.ListcontainersCallContext
        ) -> Awaitable[None]: ...
        def removeContainer(
            self,
            id: str,
            _context: _StoreModule.Server.RemovecontainerCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[
            bool | _StoreModule.Server.RemovecontainerResultTuple | None
        ]: ...
        def removeContainer_context(
            self, context: _StoreModule.Server.RemovecontainerCallContext
        ) -> Awaitable[None]: ...
        def importContainer(
            self,
            json: str,
            _context: _StoreModule.Server.ImportcontainerCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[
            _StoreModule._ContainerModule.Server
            | _StoreModule.Server.ImportcontainerResultTuple
            | None
        ]: ...
        def importContainer_context(
            self, context: _StoreModule.Server.ImportcontainerCallContext
        ) -> Awaitable[None]: ...

    class StoreClient(
        _IdentifiableModule.IdentifiableClient, _PersistentModule.PersistentClient
    ):
        class NewcontainerResult(Awaitable[NewcontainerResult], Protocol):
            container: _StoreModule._ContainerModule.ContainerClient

        class ContainerwithidResult(Awaitable[ContainerwithidResult], Protocol):
            container: _StoreModule._ContainerModule.ContainerClient

        class ListcontainersResult(Awaitable[ListcontainersResult], Protocol):
            containers: Sequence[
                _StoreModule._InfoAndContainerModule.Builder
                | _StoreModule._InfoAndContainerModule.Reader
            ]

        class RemovecontainerResult(Awaitable[RemovecontainerResult], Protocol):
            success: bool

        class ImportcontainerResult(Awaitable[ImportcontainerResult], Protocol):
            container: _StoreModule._ContainerModule.ContainerClient

        def newContainer(
            self, name: str | None = None, description: str | None = None
        ) -> _StoreModule.StoreClient.NewcontainerResult: ...
        def containerWithId(
            self, id: str | None = None
        ) -> _StoreModule.StoreClient.ContainerwithidResult: ...
        def listContainers(self) -> _StoreModule.StoreClient.ListcontainersResult: ...
        def removeContainer(
            self, id: str | None = None
        ) -> _StoreModule.StoreClient.RemovecontainerResult: ...
        def importContainer(
            self, json: str | None = None
        ) -> _StoreModule.StoreClient.ImportcontainerResult: ...
        def newContainer_request(
            self, name: str | None = None, description: str | None = None
        ) -> _StoreModule.NewcontainerRequest: ...
        def containerWithId_request(
            self, id: str | None = None
        ) -> _StoreModule.ContainerwithidRequest: ...
        def listContainers_request(self) -> _StoreModule.ListcontainersRequest: ...
        def removeContainer_request(
            self, id: str | None = None
        ) -> _StoreModule.RemovecontainerRequest: ...
        def importContainer_request(
            self, json: str | None = None
        ) -> _StoreModule.ImportcontainerRequest: ...

Store: _StoreModule

# Top-level type aliases for use in type annotations
type AddentryResult = _StoreModule._ContainerModule.ContainerClient.AddentryResult
type ClearResult = _StoreModule._ContainerModule.ContainerClient.ClearResult
type ContainerClient = _StoreModule._ContainerModule.ContainerClient
type ContainerwithidResult = _StoreModule.StoreClient.ContainerwithidResult
type DownloadentriesResult = (
    _StoreModule._ContainerModule.ContainerClient.DownloadentriesResult
)
type EntryClient = _StoreModule._ContainerModule._EntryModule.EntryClient
type ExportResult = _StoreModule._ContainerModule.ContainerClient.ExportResult
type GetentryResult = _StoreModule._ContainerModule.ContainerClient.GetentryResult
type GetkeyResult = _StoreModule._ContainerModule._EntryModule.EntryClient.GetkeyResult
type GetvalueResult = (
    _StoreModule._ContainerModule._EntryModule.EntryClient.GetvalueResult
)
type ImportExportDataBuilder = _StoreModule._ImportExportDataModule.Builder
type ImportExportDataReader = _StoreModule._ImportExportDataModule.Reader
type ImportcontainerResult = _StoreModule.StoreClient.ImportcontainerResult
type InfoAndContainerBuilder = _StoreModule._InfoAndContainerModule.Builder
type InfoAndContainerReader = _StoreModule._InfoAndContainerModule.Reader
type KeyAndEntryBuilder = _StoreModule._ContainerModule._KeyAndEntryModule.Builder
type KeyAndEntryReader = _StoreModule._ContainerModule._KeyAndEntryModule.Reader
type ListcontainersResult = _StoreModule.StoreClient.ListcontainersResult
type ListentriesResult = _StoreModule._ContainerModule.ContainerClient.ListentriesResult
type NewcontainerResult = _StoreModule.StoreClient.NewcontainerResult
type RemovecontainerResult = _StoreModule.StoreClient.RemovecontainerResult
type RemoveentryResult = _StoreModule._ContainerModule.ContainerClient.RemoveentryResult
type SetvalueResult = (
    _StoreModule._ContainerModule._EntryModule.EntryClient.SetvalueResult
)
type StoreClient = _StoreModule.StoreClient
type ValueBuilder = _StoreModule._ContainerModule._EntryModule._ValueModule.Builder
type ValueReader = _StoreModule._ContainerModule._EntryModule._ValueModule.Reader
