"""This is an automatically generated stub for `storage.capnp`."""

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
    IdInformationBuilder,
    IdInformationReader,
    PairBuilder,
    PairReader,
    _IdentifiableModule,
)
from .persistence_capnp import _PersistentModule

# Type alias for AnyStruct parameters
type AnyStruct = (
    _DynamicStructBuilder
    | _DynamicStructReader
    | _DynamicObjectReader
    | _DynamicObjectBuilder
)

class _StoreModule(_IdentifiableModule, _PersistentModule):
    class _ContainerModule(_IdentifiableModule, _PersistentModule):
        class _EntryModule(_InterfaceModule):
            class _ValueModule(_StructModule):
                class Reader(_DynamicStructReader):
                    @property
                    def boolValue(self) -> bool: ...
                    @property
                    def boolListValue(self) -> BoolListReader: ...
                    @property
                    def int8Value(self) -> int: ...
                    @property
                    def int8ListValue(self) -> Int8ListReader: ...
                    @property
                    def int16Value(self) -> int: ...
                    @property
                    def int16ListValue(self) -> Int16ListReader: ...
                    @property
                    def int32Value(self) -> int: ...
                    @property
                    def int32ListValue(self) -> Int32ListReader: ...
                    @property
                    def int64Value(self) -> int: ...
                    @property
                    def int64ListValue(self) -> Int64ListReader: ...
                    @property
                    def uint8Value(self) -> int: ...
                    @property
                    def uint8ListValue(self) -> Uint8ListReader: ...
                    @property
                    def uint16Value(self) -> int: ...
                    @property
                    def uint16ListValue(self) -> Uint16ListReader: ...
                    @property
                    def uint32Value(self) -> int: ...
                    @property
                    def uint32ListValue(self) -> Uint32ListReader: ...
                    @property
                    def uint64Value(self) -> int: ...
                    @property
                    def uint64ListValue(self) -> Uint64ListReader: ...
                    @property
                    def float32Value(self) -> float: ...
                    @property
                    def float32ListValue(self) -> Float32ListReader: ...
                    @property
                    def float64Value(self) -> float: ...
                    @property
                    def float64ListValue(self) -> Float64ListReader: ...
                    @property
                    def textValue(self) -> str: ...
                    @property
                    def textListValue(self) -> TextListReader: ...
                    @property
                    def dataValue(self) -> bytes: ...
                    @property
                    def dataListValue(self) -> DataListReader: ...
                    @property
                    def anyValue(self) -> _DynamicObjectReader: ...
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
                    def boolListValue(self) -> BoolListBuilder: ...
                    @boolListValue.setter
                    def boolListValue(
                        self, value: BoolListBuilder | BoolListReader | dict[str, Any]
                    ) -> None: ...
                    @property
                    def int8Value(self) -> int: ...
                    @int8Value.setter
                    def int8Value(self, value: int) -> None: ...
                    @property
                    def int8ListValue(self) -> Int8ListBuilder: ...
                    @int8ListValue.setter
                    def int8ListValue(
                        self, value: Int8ListBuilder | Int8ListReader | dict[str, Any]
                    ) -> None: ...
                    @property
                    def int16Value(self) -> int: ...
                    @int16Value.setter
                    def int16Value(self, value: int) -> None: ...
                    @property
                    def int16ListValue(self) -> Int16ListBuilder: ...
                    @int16ListValue.setter
                    def int16ListValue(
                        self, value: Int16ListBuilder | Int16ListReader | dict[str, Any]
                    ) -> None: ...
                    @property
                    def int32Value(self) -> int: ...
                    @int32Value.setter
                    def int32Value(self, value: int) -> None: ...
                    @property
                    def int32ListValue(self) -> Int32ListBuilder: ...
                    @int32ListValue.setter
                    def int32ListValue(
                        self, value: Int32ListBuilder | Int32ListReader | dict[str, Any]
                    ) -> None: ...
                    @property
                    def int64Value(self) -> int: ...
                    @int64Value.setter
                    def int64Value(self, value: int) -> None: ...
                    @property
                    def int64ListValue(self) -> Int64ListBuilder: ...
                    @int64ListValue.setter
                    def int64ListValue(
                        self, value: Int64ListBuilder | Int64ListReader | dict[str, Any]
                    ) -> None: ...
                    @property
                    def uint8Value(self) -> int: ...
                    @uint8Value.setter
                    def uint8Value(self, value: int) -> None: ...
                    @property
                    def uint8ListValue(self) -> Uint8ListBuilder: ...
                    @uint8ListValue.setter
                    def uint8ListValue(
                        self, value: Uint8ListBuilder | Uint8ListReader | dict[str, Any]
                    ) -> None: ...
                    @property
                    def uint16Value(self) -> int: ...
                    @uint16Value.setter
                    def uint16Value(self, value: int) -> None: ...
                    @property
                    def uint16ListValue(self) -> Uint16ListBuilder: ...
                    @uint16ListValue.setter
                    def uint16ListValue(
                        self,
                        value: Uint16ListBuilder | Uint16ListReader | dict[str, Any],
                    ) -> None: ...
                    @property
                    def uint32Value(self) -> int: ...
                    @uint32Value.setter
                    def uint32Value(self, value: int) -> None: ...
                    @property
                    def uint32ListValue(self) -> Uint32ListBuilder: ...
                    @uint32ListValue.setter
                    def uint32ListValue(
                        self,
                        value: Uint32ListBuilder | Uint32ListReader | dict[str, Any],
                    ) -> None: ...
                    @property
                    def uint64Value(self) -> int: ...
                    @uint64Value.setter
                    def uint64Value(self, value: int) -> None: ...
                    @property
                    def uint64ListValue(self) -> Uint64ListBuilder: ...
                    @uint64ListValue.setter
                    def uint64ListValue(
                        self,
                        value: Uint64ListBuilder | Uint64ListReader | dict[str, Any],
                    ) -> None: ...
                    @property
                    def float32Value(self) -> float: ...
                    @float32Value.setter
                    def float32Value(self, value: float) -> None: ...
                    @property
                    def float32ListValue(self) -> Float32ListBuilder: ...
                    @float32ListValue.setter
                    def float32ListValue(
                        self,
                        value: Float32ListBuilder | Float32ListReader | dict[str, Any],
                    ) -> None: ...
                    @property
                    def float64Value(self) -> float: ...
                    @float64Value.setter
                    def float64Value(self, value: float) -> None: ...
                    @property
                    def float64ListValue(self) -> Float64ListBuilder: ...
                    @float64ListValue.setter
                    def float64ListValue(
                        self,
                        value: Float64ListBuilder | Float64ListReader | dict[str, Any],
                    ) -> None: ...
                    @property
                    def textValue(self) -> str: ...
                    @textValue.setter
                    def textValue(self, value: str) -> None: ...
                    @property
                    def textListValue(self) -> TextListBuilder: ...
                    @textListValue.setter
                    def textListValue(
                        self, value: TextListBuilder | TextListReader | dict[str, Any]
                    ) -> None: ...
                    @property
                    def dataValue(self) -> bytes: ...
                    @dataValue.setter
                    def dataValue(self, value: bytes) -> None: ...
                    @property
                    def dataListValue(self) -> DataListBuilder: ...
                    @dataListValue.setter
                    def dataListValue(
                        self, value: DataListBuilder | DataListReader | dict[str, Any]
                    ) -> None: ...
                    @property
                    def anyValue(self) -> _DynamicStructBuilder: ...
                    @anyValue.setter
                    def anyValue(self, value: AnyStruct | dict[str, Any]) -> None: ...
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
                    ) -> BoolListBuilder: ...
                    @overload
                    def init(
                        self, field: Literal["int8ListValue"], size: int | None = None
                    ) -> Int8ListBuilder: ...
                    @overload
                    def init(
                        self, field: Literal["int16ListValue"], size: int | None = None
                    ) -> Int16ListBuilder: ...
                    @overload
                    def init(
                        self, field: Literal["int32ListValue"], size: int | None = None
                    ) -> Int32ListBuilder: ...
                    @overload
                    def init(
                        self, field: Literal["int64ListValue"], size: int | None = None
                    ) -> Int64ListBuilder: ...
                    @overload
                    def init(
                        self, field: Literal["uint8ListValue"], size: int | None = None
                    ) -> Uint8ListBuilder: ...
                    @overload
                    def init(
                        self, field: Literal["uint16ListValue"], size: int | None = None
                    ) -> Uint16ListBuilder: ...
                    @overload
                    def init(
                        self, field: Literal["uint32ListValue"], size: int | None = None
                    ) -> Uint32ListBuilder: ...
                    @overload
                    def init(
                        self, field: Literal["uint64ListValue"], size: int | None = None
                    ) -> Uint64ListBuilder: ...
                    @overload
                    def init(
                        self,
                        field: Literal["float32ListValue"],
                        size: int | None = None,
                    ) -> Float32ListBuilder: ...
                    @overload
                    def init(
                        self,
                        field: Literal["float64ListValue"],
                        size: int | None = None,
                    ) -> Float64ListBuilder: ...
                    @overload
                    def init(
                        self, field: Literal["textListValue"], size: int | None = None
                    ) -> TextListBuilder: ...
                    @overload
                    def init(
                        self, field: Literal["dataListValue"], size: int | None = None
                    ) -> DataListBuilder: ...
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
                    boolListValue: BoolListBuilder | dict[str, Any] | None = None,
                    int8Value: int | None = None,
                    int8ListValue: Int8ListBuilder | dict[str, Any] | None = None,
                    int16Value: int | None = None,
                    int16ListValue: Int16ListBuilder | dict[str, Any] | None = None,
                    int32Value: int | None = None,
                    int32ListValue: Int32ListBuilder | dict[str, Any] | None = None,
                    int64Value: int | None = None,
                    int64ListValue: Int64ListBuilder | dict[str, Any] | None = None,
                    uint8Value: int | None = None,
                    uint8ListValue: Uint8ListBuilder | dict[str, Any] | None = None,
                    uint16Value: int | None = None,
                    uint16ListValue: Uint16ListBuilder | dict[str, Any] | None = None,
                    uint32Value: int | None = None,
                    uint32ListValue: Uint32ListBuilder | dict[str, Any] | None = None,
                    uint64Value: int | None = None,
                    uint64ListValue: Uint64ListBuilder | dict[str, Any] | None = None,
                    float32Value: float | None = None,
                    float32ListValue: Float32ListBuilder | dict[str, Any] | None = None,
                    float64Value: float | None = None,
                    float64ListValue: Float64ListBuilder | dict[str, Any] | None = None,
                    textValue: str | None = None,
                    textListValue: TextListBuilder | dict[str, Any] | None = None,
                    dataValue: bytes | None = None,
                    dataListValue: DataListBuilder | dict[str, Any] | None = None,
                    anyValue: AnyStruct | dict[str, Any] | None = None,
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
                class GetkeyResult(_DynamicStructBuilder):
                    @property
                    def key(self) -> str: ...
                    @key.setter
                    def key(self, value: str) -> None: ...

                class GetvalueResult(_DynamicStructBuilder):
                    @property
                    def value(self) -> ValueBuilder: ...
                    @value.setter
                    def value(
                        self, value: ValueBuilder | ValueReader | dict[str, Any]
                    ) -> None: ...
                    @property
                    def isUnset(self) -> bool: ...
                    @isUnset.setter
                    def isUnset(self, value: bool) -> None: ...
                    @overload
                    def init(
                        self, field: Literal["value"], size: int | None = None
                    ) -> ValueBuilder: ...
                    @overload
                    def init(self, field: str, size: int | None = None) -> Any: ...

                class SetvalueResult(_DynamicStructBuilder):
                    @property
                    def success(self) -> bool: ...
                    @success.setter
                    def success(self, value: bool) -> None: ...

                class GetkeyResultTuple(NamedTuple):
                    key: str

                class GetvalueResultTuple(NamedTuple):
                    value: ValueBuilder | ValueReader
                    isUnset: bool

                class SetvalueResultTuple(NamedTuple):
                    success: bool

                class GetkeyParams(Protocol): ...

                class GetkeyCallContext(Protocol):
                    params: (
                        _StoreModule._ContainerModule._EntryModule.Server.GetkeyParams
                    )
                    @property
                    def results(
                        self,
                    ) -> (
                        _StoreModule._ContainerModule._EntryModule.Server.GetkeyResult
                    ): ...

                class GetvalueParams(Protocol): ...

                class GetvalueCallContext(Protocol):
                    params: (
                        _StoreModule._ContainerModule._EntryModule.Server.GetvalueParams
                    )
                    @property
                    def results(
                        self,
                    ) -> (
                        _StoreModule._ContainerModule._EntryModule.Server.GetvalueResult
                    ): ...

                class SetvalueParams(Protocol):
                    value: ValueReader

                class SetvalueCallContext(Protocol):
                    params: (
                        _StoreModule._ContainerModule._EntryModule.Server.SetvalueParams
                    )
                    @property
                    def results(
                        self,
                    ) -> (
                        _StoreModule._ContainerModule._EntryModule.Server.SetvalueResult
                    ): ...

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
        type EntryServer = _StoreModule._ContainerModule._EntryModule.Server
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
            class ExportResult(_DynamicStructBuilder):
                @property
                def json(self) -> str: ...
                @json.setter
                def json(self, value: str) -> None: ...

            class DownloadentriesResult(_DynamicStructBuilder):
                @property
                def entries(self) -> PairListBuilder: ...
                @entries.setter
                def entries(
                    self, value: PairListBuilder | PairListReader | Sequence[Any]
                ) -> None: ...
                @overload
                def init(
                    self, field: Literal["entries"], size: int | None = None
                ) -> PairListBuilder: ...
                @overload
                def init(self, field: str, size: int | None = None) -> Any: ...

            class ListentriesResult(_DynamicStructBuilder):
                @property
                def entries(self) -> KeyAndEntryListBuilder: ...
                @entries.setter
                def entries(
                    self,
                    value: KeyAndEntryListBuilder
                    | KeyAndEntryListReader
                    | Sequence[Any],
                ) -> None: ...
                @overload
                def init(
                    self, field: Literal["entries"], size: int | None = None
                ) -> KeyAndEntryListBuilder: ...
                @overload
                def init(self, field: str, size: int | None = None) -> Any: ...

            class GetentryResult(_DynamicStructBuilder):
                @property
                def entry(
                    self,
                ) -> (
                    _StoreModule._ContainerModule._EntryModule.Server
                    | _StoreModule._ContainerModule._EntryModule.EntryClient
                ): ...
                @entry.setter
                def entry(
                    self,
                    value: _StoreModule._ContainerModule._EntryModule.Server
                    | _StoreModule._ContainerModule._EntryModule.EntryClient,
                ) -> None: ...

            class RemoveentryResult(_DynamicStructBuilder):
                @property
                def success(self) -> bool: ...
                @success.setter
                def success(self, value: bool) -> None: ...

            class ClearResult(_DynamicStructBuilder):
                @property
                def success(self) -> bool: ...
                @success.setter
                def success(self, value: bool) -> None: ...

            class AddentryResult(_DynamicStructBuilder):
                @property
                def entry(
                    self,
                ) -> (
                    _StoreModule._ContainerModule._EntryModule.Server
                    | _StoreModule._ContainerModule._EntryModule.EntryClient
                ): ...
                @entry.setter
                def entry(
                    self,
                    value: _StoreModule._ContainerModule._EntryModule.Server
                    | _StoreModule._ContainerModule._EntryModule.EntryClient,
                ) -> None: ...
                @property
                def success(self) -> bool: ...
                @success.setter
                def success(self, value: bool) -> None: ...

            class ExportResultTuple(NamedTuple):
                json: str

            class DownloadentriesResultTuple(NamedTuple):
                entries: PairListBuilder | PairListReader

            class ListentriesResultTuple(NamedTuple):
                entries: KeyAndEntryListBuilder | KeyAndEntryListReader

            class GetentryResultTuple(NamedTuple):
                entry: (
                    _StoreModule._ContainerModule._EntryModule.Server
                    | _StoreModule._ContainerModule._EntryModule.EntryClient
                )

            class RemoveentryResultTuple(NamedTuple):
                success: bool

            class ClearResultTuple(NamedTuple):
                success: bool

            class AddentryResultTuple(NamedTuple):
                entry: (
                    _StoreModule._ContainerModule._EntryModule.Server
                    | _StoreModule._ContainerModule._EntryModule.EntryClient
                )
                success: bool

            class ExportParams(Protocol): ...

            class ExportCallContext(Protocol):
                params: _StoreModule._ContainerModule.Server.ExportParams
                @property
                def results(
                    self,
                ) -> _StoreModule._ContainerModule.Server.ExportResult: ...

            class DownloadentriesParams(Protocol): ...

            class DownloadentriesCallContext(Protocol):
                params: _StoreModule._ContainerModule.Server.DownloadentriesParams
                @property
                def results(
                    self,
                ) -> _StoreModule._ContainerModule.Server.DownloadentriesResult: ...

            class ListentriesParams(Protocol): ...

            class ListentriesCallContext(Protocol):
                params: _StoreModule._ContainerModule.Server.ListentriesParams
                @property
                def results(
                    self,
                ) -> _StoreModule._ContainerModule.Server.ListentriesResult: ...

            class GetentryParams(Protocol):
                key: str

            class GetentryCallContext(Protocol):
                params: _StoreModule._ContainerModule.Server.GetentryParams
                @property
                def results(
                    self,
                ) -> _StoreModule._ContainerModule.Server.GetentryResult: ...

            class RemoveentryParams(Protocol):
                key: str

            class RemoveentryCallContext(Protocol):
                params: _StoreModule._ContainerModule.Server.RemoveentryParams
                @property
                def results(
                    self,
                ) -> _StoreModule._ContainerModule.Server.RemoveentryResult: ...

            class ClearParams(Protocol): ...

            class ClearCallContext(Protocol):
                params: _StoreModule._ContainerModule.Server.ClearParams
                @property
                def results(
                    self,
                ) -> _StoreModule._ContainerModule.Server.ClearResult: ...

            class AddentryParams(Protocol):
                key: str
                value: ValueReader
                replaceExisting: bool

            class AddentryCallContext(Protocol):
                params: _StoreModule._ContainerModule.Server.AddentryParams
                @property
                def results(
                    self,
                ) -> _StoreModule._ContainerModule.Server.AddentryResult: ...

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
                Sequence[PairBuilder | PairReader]
                | _StoreModule._ContainerModule.Server.DownloadentriesResultTuple
                | None
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
                Sequence[KeyAndEntryBuilder | KeyAndEntryReader]
                | _StoreModule._ContainerModule.Server.ListentriesResultTuple
                | None
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
                entries: PairListReader

            class ListentriesResult(Awaitable[ListentriesResult], Protocol):
                entries: KeyAndEntryListReader

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
    type ContainerServer = _StoreModule._ContainerModule.Server
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
            def info(self) -> IdInformationReader: ...
            @property
            def entries(self) -> PairListReader: ...
            @property
            def isAnyValue(self) -> BoolListReader: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> ImportExportDataBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def info(self) -> IdInformationBuilder: ...
            @info.setter
            def info(
                self, value: IdInformationBuilder | IdInformationReader | dict[str, Any]
            ) -> None: ...
            @property
            def entries(self) -> PairListBuilder: ...
            @entries.setter
            def entries(
                self, value: PairListBuilder | PairListReader | dict[str, Any]
            ) -> None: ...
            @property
            def isAnyValue(self) -> BoolListBuilder: ...
            @isAnyValue.setter
            def isAnyValue(
                self, value: BoolListBuilder | BoolListReader | dict[str, Any]
            ) -> None: ...
            @overload
            def init(
                self, field: Literal["info"], size: int | None = None
            ) -> IdInformationBuilder: ...
            @overload
            def init(
                self, field: Literal["entries"], size: int | None = None
            ) -> PairListBuilder: ...
            @overload
            def init(
                self, field: Literal["isAnyValue"], size: int | None = None
            ) -> BoolListBuilder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...
            @override
            def as_reader(self) -> ImportExportDataReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            info: IdInformationBuilder | dict[str, Any] | None = None,
            entries: PairListBuilder | dict[str, Any] | None = None,
            isAnyValue: BoolListBuilder | dict[str, Any] | None = None,
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
        class NewcontainerResult(_DynamicStructBuilder):
            @property
            def container(
                self,
            ) -> (
                _StoreModule._ContainerModule.Server
                | _StoreModule._ContainerModule.ContainerClient
            ): ...
            @container.setter
            def container(
                self,
                value: _StoreModule._ContainerModule.Server
                | _StoreModule._ContainerModule.ContainerClient,
            ) -> None: ...

        class ContainerwithidResult(_DynamicStructBuilder):
            @property
            def container(
                self,
            ) -> (
                _StoreModule._ContainerModule.Server
                | _StoreModule._ContainerModule.ContainerClient
            ): ...
            @container.setter
            def container(
                self,
                value: _StoreModule._ContainerModule.Server
                | _StoreModule._ContainerModule.ContainerClient,
            ) -> None: ...

        class ListcontainersResult(_DynamicStructBuilder):
            @property
            def containers(self) -> InfoAndContainerListBuilder: ...
            @containers.setter
            def containers(
                self,
                value: InfoAndContainerListBuilder
                | InfoAndContainerListReader
                | Sequence[Any],
            ) -> None: ...
            @overload
            def init(
                self, field: Literal["containers"], size: int | None = None
            ) -> InfoAndContainerListBuilder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...

        class RemovecontainerResult(_DynamicStructBuilder):
            @property
            def success(self) -> bool: ...
            @success.setter
            def success(self, value: bool) -> None: ...

        class ImportcontainerResult(_DynamicStructBuilder):
            @property
            def container(
                self,
            ) -> (
                _StoreModule._ContainerModule.Server
                | _StoreModule._ContainerModule.ContainerClient
            ): ...
            @container.setter
            def container(
                self,
                value: _StoreModule._ContainerModule.Server
                | _StoreModule._ContainerModule.ContainerClient,
            ) -> None: ...

        class NewcontainerResultTuple(NamedTuple):
            container: (
                _StoreModule._ContainerModule.Server
                | _StoreModule._ContainerModule.ContainerClient
            )

        class ContainerwithidResultTuple(NamedTuple):
            container: (
                _StoreModule._ContainerModule.Server
                | _StoreModule._ContainerModule.ContainerClient
            )

        class ListcontainersResultTuple(NamedTuple):
            containers: InfoAndContainerListBuilder | InfoAndContainerListReader

        class RemovecontainerResultTuple(NamedTuple):
            success: bool

        class ImportcontainerResultTuple(NamedTuple):
            container: (
                _StoreModule._ContainerModule.Server
                | _StoreModule._ContainerModule.ContainerClient
            )

        class NewcontainerParams(Protocol):
            name: str
            description: str

        class NewcontainerCallContext(Protocol):
            params: _StoreModule.Server.NewcontainerParams
            @property
            def results(self) -> _StoreModule.Server.NewcontainerResult: ...

        class ContainerwithidParams(Protocol):
            id: str

        class ContainerwithidCallContext(Protocol):
            params: _StoreModule.Server.ContainerwithidParams
            @property
            def results(self) -> _StoreModule.Server.ContainerwithidResult: ...

        class ListcontainersParams(Protocol): ...

        class ListcontainersCallContext(Protocol):
            params: _StoreModule.Server.ListcontainersParams
            @property
            def results(self) -> _StoreModule.Server.ListcontainersResult: ...

        class RemovecontainerParams(Protocol):
            id: str

        class RemovecontainerCallContext(Protocol):
            params: _StoreModule.Server.RemovecontainerParams
            @property
            def results(self) -> _StoreModule.Server.RemovecontainerResult: ...

        class ImportcontainerParams(Protocol):
            json: str

        class ImportcontainerCallContext(Protocol):
            params: _StoreModule.Server.ImportcontainerParams
            @property
            def results(self) -> _StoreModule.Server.ImportcontainerResult: ...

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
        ) -> Awaitable[
            Sequence[InfoAndContainerBuilder | InfoAndContainerReader]
            | _StoreModule.Server.ListcontainersResultTuple
            | None
        ]: ...
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
            containers: InfoAndContainerListReader

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

class _BoolList:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> bool: ...
        def __iter__(self) -> Iterator[bool]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> bool: ...
        def __setitem__(self, key: int, value: bool) -> None: ...
        def __iter__(self) -> Iterator[bool]: ...

class _Int8List:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __iter__(self) -> Iterator[int]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __setitem__(self, key: int, value: int) -> None: ...
        def __iter__(self) -> Iterator[int]: ...

class _Int16List:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __iter__(self) -> Iterator[int]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __setitem__(self, key: int, value: int) -> None: ...
        def __iter__(self) -> Iterator[int]: ...

class _Int32List:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __iter__(self) -> Iterator[int]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __setitem__(self, key: int, value: int) -> None: ...
        def __iter__(self) -> Iterator[int]: ...

class _Int64List:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __iter__(self) -> Iterator[int]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __setitem__(self, key: int, value: int) -> None: ...
        def __iter__(self) -> Iterator[int]: ...

class _Uint8List:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __iter__(self) -> Iterator[int]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __setitem__(self, key: int, value: int) -> None: ...
        def __iter__(self) -> Iterator[int]: ...

class _Uint16List:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __iter__(self) -> Iterator[int]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __setitem__(self, key: int, value: int) -> None: ...
        def __iter__(self) -> Iterator[int]: ...

class _Uint32List:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __iter__(self) -> Iterator[int]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __setitem__(self, key: int, value: int) -> None: ...
        def __iter__(self) -> Iterator[int]: ...

class _Uint64List:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __iter__(self) -> Iterator[int]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __setitem__(self, key: int, value: int) -> None: ...
        def __iter__(self) -> Iterator[int]: ...

class _Float32List:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> float: ...
        def __iter__(self) -> Iterator[float]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> float: ...
        def __setitem__(self, key: int, value: float) -> None: ...
        def __iter__(self) -> Iterator[float]: ...

class _Float64List:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> float: ...
        def __iter__(self) -> Iterator[float]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> float: ...
        def __setitem__(self, key: int, value: float) -> None: ...
        def __iter__(self) -> Iterator[float]: ...

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

class _DataList:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> bytes: ...
        def __iter__(self) -> Iterator[bytes]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> bytes: ...
        def __setitem__(self, key: int, value: bytes) -> None: ...
        def __iter__(self) -> Iterator[bytes]: ...

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

class _KeyAndEntryList:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> KeyAndEntryReader: ...
        def __iter__(self) -> Iterator[KeyAndEntryReader]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> KeyAndEntryBuilder: ...
        def __setitem__(
            self,
            key: int,
            value: KeyAndEntryReader | KeyAndEntryBuilder | dict[str, Any],
        ) -> None: ...
        def __iter__(self) -> Iterator[KeyAndEntryBuilder]: ...
        def init(self, index: int, size: int | None = None) -> KeyAndEntryBuilder: ...

class _InfoAndContainerList:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> InfoAndContainerReader: ...
        def __iter__(self) -> Iterator[InfoAndContainerReader]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> InfoAndContainerBuilder: ...
        def __setitem__(
            self,
            key: int,
            value: InfoAndContainerReader | InfoAndContainerBuilder | dict[str, Any],
        ) -> None: ...
        def __iter__(self) -> Iterator[InfoAndContainerBuilder]: ...
        def init(
            self, index: int, size: int | None = None
        ) -> InfoAndContainerBuilder: ...

Store: _StoreModule

# Top-level type aliases for use in type annotations
type AddentryResult = _StoreModule._ContainerModule.ContainerClient.AddentryResult
type BoolListBuilder = _BoolList.Builder
type BoolListReader = _BoolList.Reader
type ClearResult = _StoreModule._ContainerModule.ContainerClient.ClearResult
type ContainerClient = _StoreModule._ContainerModule.ContainerClient
type ContainerServer = _StoreModule._ContainerModule.Server
type ContainerwithidResult = _StoreModule.StoreClient.ContainerwithidResult
type DataListBuilder = _DataList.Builder
type DataListReader = _DataList.Reader
type DownloadentriesResult = (
    _StoreModule._ContainerModule.ContainerClient.DownloadentriesResult
)
type EntryClient = _StoreModule._ContainerModule._EntryModule.EntryClient
type EntryServer = _StoreModule._ContainerModule._EntryModule.Server
type ExportResult = _StoreModule._ContainerModule.ContainerClient.ExportResult
type Float32ListBuilder = _Float32List.Builder
type Float32ListReader = _Float32List.Reader
type Float64ListBuilder = _Float64List.Builder
type Float64ListReader = _Float64List.Reader
type GetentryResult = _StoreModule._ContainerModule.ContainerClient.GetentryResult
type GetkeyResult = _StoreModule._ContainerModule._EntryModule.EntryClient.GetkeyResult
type GetvalueResult = (
    _StoreModule._ContainerModule._EntryModule.EntryClient.GetvalueResult
)
type ImportExportDataBuilder = _StoreModule._ImportExportDataModule.Builder
type ImportExportDataReader = _StoreModule._ImportExportDataModule.Reader
type ImportcontainerResult = _StoreModule.StoreClient.ImportcontainerResult
type InfoAndContainerBuilder = _StoreModule._InfoAndContainerModule.Builder
type InfoAndContainerListBuilder = _InfoAndContainerList.Builder
type InfoAndContainerListReader = _InfoAndContainerList.Reader
type InfoAndContainerReader = _StoreModule._InfoAndContainerModule.Reader
type Int16ListBuilder = _Int16List.Builder
type Int16ListReader = _Int16List.Reader
type Int32ListBuilder = _Int32List.Builder
type Int32ListReader = _Int32List.Reader
type Int64ListBuilder = _Int64List.Builder
type Int64ListReader = _Int64List.Reader
type Int8ListBuilder = _Int8List.Builder
type Int8ListReader = _Int8List.Reader
type KeyAndEntryBuilder = _StoreModule._ContainerModule._KeyAndEntryModule.Builder
type KeyAndEntryListBuilder = _KeyAndEntryList.Builder
type KeyAndEntryListReader = _KeyAndEntryList.Reader
type KeyAndEntryReader = _StoreModule._ContainerModule._KeyAndEntryModule.Reader
type ListcontainersResult = _StoreModule.StoreClient.ListcontainersResult
type ListentriesResult = _StoreModule._ContainerModule.ContainerClient.ListentriesResult
type NewcontainerResult = _StoreModule.StoreClient.NewcontainerResult
type PairListBuilder = _PairList.Builder
type PairListReader = _PairList.Reader
type RemovecontainerResult = _StoreModule.StoreClient.RemovecontainerResult
type RemoveentryResult = _StoreModule._ContainerModule.ContainerClient.RemoveentryResult
type SetvalueResult = (
    _StoreModule._ContainerModule._EntryModule.EntryClient.SetvalueResult
)
type StoreClient = _StoreModule.StoreClient
type StoreServer = _StoreModule.Server
type TextListBuilder = _TextList.Builder
type TextListReader = _TextList.Reader
type Uint16ListBuilder = _Uint16List.Builder
type Uint16ListReader = _Uint16List.Reader
type Uint32ListBuilder = _Uint32List.Builder
type Uint32ListReader = _Uint32List.Reader
type Uint64ListBuilder = _Uint64List.Builder
type Uint64ListReader = _Uint64List.Reader
type Uint8ListBuilder = _Uint8List.Builder
type Uint8ListReader = _Uint8List.Reader
type ValueBuilder = _StoreModule._ContainerModule._EntryModule._ValueModule.Builder
type ValueReader = _StoreModule._ContainerModule._EntryModule._ValueModule.Reader
