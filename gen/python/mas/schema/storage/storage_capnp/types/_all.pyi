"""This is an automatically generated stub for `storage.capnp`."""

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
from mas.schema.persistence.persistence_capnp.types.clients import PersistentClient
from mas.schema.persistence.persistence_capnp.types.modules import (
    _PersistentInterfaceModule,
)

# Type alias for AnyStruct parameters
type AnyStruct = (
    _DynamicStructBuilder
    | _DynamicStructReader
    | _DynamicObjectReader
    | _DynamicObjectBuilder
)

class _StoreInterfaceModule(_IdentifiableInterfaceModule, _PersistentInterfaceModule):
    class _ContainerInterfaceModule(
        _IdentifiableInterfaceModule,
        _PersistentInterfaceModule,
    ):
        class _EntryInterfaceModule(_InterfaceModule):
            class _ValueStructModule(_StructModule):
                class Reader(_DynamicStructReader): ...
                class Builder(_DynamicStructBuilder): ...

                @override
                def new_message(
                    self,
                    num_first_segment_words: int | None = None,
                    allocate_seg_callable: Callable[[int], bytearray] | None = None,
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
                    **kwargs: object,
                ) -> ValueBuilder: ...
                @override
                @overload
                def from_bytes(
                    self,
                    buf: bytes,
                    traversal_limit_in_words: int | None = None,
                    nesting_limit: int | None = None,
                ) -> AbstractContextManager[ValueReader]: ...
                @overload
                def from_bytes(
                    self,
                    buf: bytes,
                    traversal_limit_in_words: int | None = None,
                    nesting_limit: int | None = None,
                    *,
                    builder: Literal[False],
                ) -> AbstractContextManager[ValueReader]: ...
                @overload
                def from_bytes(
                    self,
                    buf: bytes,
                    traversal_limit_in_words: int | None = None,
                    nesting_limit: int | None = None,
                    *,
                    builder: Literal[True],
                ) -> AbstractContextManager[ValueBuilder]: ...
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
                ) -> ValueReader: ...
                @override
                def read_packed(
                    self,
                    file: IO[str] | IO[bytes],
                    traversal_limit_in_words: int | None = None,
                    nesting_limit: int | None = None,
                ) -> ValueReader: ...

            Value: _ValueStructModule
            @override
            def _new_client(self, server: _DynamicCapabilityServer) -> EntryClient: ...
            class Server(_DynamicCapabilityServer):
                def getKey(
                    self,
                    _context: GetkeyCallContext,
                    **kwargs: object,
                ) -> Awaitable[str | GetkeyResultTuple | None]: ...
                def getKey_context(
                    self,
                    context: GetkeyCallContext,
                ) -> Awaitable[None]: ...
                def getValue(
                    self,
                    _context: GetvalueCallContext,
                    **kwargs: object,
                ) -> Awaitable[GetvalueResultTuple | None]: ...
                def getValue_context(
                    self,
                    context: GetvalueCallContext,
                ) -> Awaitable[None]: ...
                def setValue(
                    self,
                    value: ValueReader,
                    _context: SetvalueCallContext,
                    **kwargs: object,
                ) -> Awaitable[bool | SetvalueResultTuple | None]: ...
                def setValue_context(
                    self,
                    context: SetvalueCallContext,
                ) -> Awaitable[None]: ...

        Entry: _EntryInterfaceModule
        type EntryServer = (
            _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule.Server
        )
        class _KeyAndEntryStructModule(_StructModule):
            class Reader(_DynamicStructReader): ...
            class Builder(_DynamicStructBuilder): ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
                key: str | None = None,
                entry: EntryClient
                | _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule.Server
                | None = None,
                **kwargs: object,
            ) -> KeyAndEntryBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[KeyAndEntryReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[KeyAndEntryReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[KeyAndEntryBuilder]: ...
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
            ) -> KeyAndEntryReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> KeyAndEntryReader: ...

        KeyAndEntry: _KeyAndEntryStructModule
        @override
        def _new_client(self, server: _DynamicCapabilityServer) -> ContainerClient: ...
        class Server(
            _IdentifiableInterfaceModule.Server,
            _PersistentInterfaceModule.Server,
        ):
            def export(
                self,
                _context: ExportCallContext,
                **kwargs: object,
            ) -> Awaitable[str | ExportResultTuple | None]: ...
            def export_context(self, context: ExportCallContext) -> Awaitable[None]: ...
            def downloadEntries(
                self,
                _context: DownloadentriesCallContext,
                **kwargs: object,
            ) -> Awaitable[
                PairListBuilder
                | PairListReader
                | Sequence[Any]
                | DownloadentriesResultTuple
                | None
            ]: ...
            def downloadEntries_context(
                self,
                context: DownloadentriesCallContext,
            ) -> Awaitable[None]: ...
            def listEntries(
                self,
                _context: ListentriesCallContext,
                **kwargs: object,
            ) -> Awaitable[
                KeyAndEntryListBuilder
                | KeyAndEntryListReader
                | Sequence[Any]
                | ListentriesResultTuple
                | None
            ]: ...
            def listEntries_context(
                self,
                context: ListentriesCallContext,
            ) -> Awaitable[None]: ...
            def getEntry(
                self,
                key: str,
                _context: GetentryCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule.Server
                | EntryClient
                | GetentryResultTuple
                | None
            ]: ...
            def getEntry_context(
                self,
                context: GetentryCallContext,
            ) -> Awaitable[None]: ...
            def removeEntry(
                self,
                key: str,
                _context: RemoveentryCallContext,
                **kwargs: object,
            ) -> Awaitable[bool | RemoveentryResultTuple | None]: ...
            def removeEntry_context(
                self,
                context: RemoveentryCallContext,
            ) -> Awaitable[None]: ...
            def clear(
                self,
                _context: ClearCallContext,
                **kwargs: object,
            ) -> Awaitable[bool | ClearResultTuple | None]: ...
            def clear_context(self, context: ClearCallContext) -> Awaitable[None]: ...
            def addEntry(
                self,
                key: str,
                value: ValueReader,
                replaceExisting: bool,
                _context: AddentryCallContext,
                **kwargs: object,
            ) -> Awaitable[AddentryResultTuple | None]: ...
            def addEntry_context(
                self,
                context: AddentryCallContext,
            ) -> Awaitable[None]: ...

    Container: _ContainerInterfaceModule
    type ContainerServer = _StoreInterfaceModule._ContainerInterfaceModule.Server
    class _InfoAndContainerStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            id: str | None = None,
            name: str | None = None,
            container: ContainerClient
            | _StoreInterfaceModule._ContainerInterfaceModule.Server
            | None = None,
            **kwargs: object,
        ) -> InfoAndContainerBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[InfoAndContainerReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[InfoAndContainerReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[InfoAndContainerBuilder]: ...
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
        ) -> InfoAndContainerReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> InfoAndContainerReader: ...

    InfoAndContainer: _InfoAndContainerStructModule
    class _ImportExportDataStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            info: IdInformationBuilder | dict[str, Any] | None = None,
            entries: PairListBuilder | dict[str, Any] | None = None,
            isAnyValue: BoolListBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> ImportExportDataBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[ImportExportDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[ImportExportDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[ImportExportDataBuilder]: ...
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
        ) -> ImportExportDataReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> ImportExportDataReader: ...

    ImportExportData: _ImportExportDataStructModule
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> StoreClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def newContainer(
            self,
            name: str,
            description: str,
            _context: NewcontainerCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _StoreInterfaceModule._ContainerInterfaceModule.Server
            | ContainerClient
            | NewcontainerResultTuple
            | None
        ]: ...
        def newContainer_context(
            self,
            context: NewcontainerCallContext,
        ) -> Awaitable[None]: ...
        def containerWithId(
            self,
            id: str,
            _context: ContainerwithidCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _StoreInterfaceModule._ContainerInterfaceModule.Server
            | ContainerClient
            | ContainerwithidResultTuple
            | None
        ]: ...
        def containerWithId_context(
            self,
            context: ContainerwithidCallContext,
        ) -> Awaitable[None]: ...
        def listContainers(
            self,
            _context: ListcontainersCallContext,
            **kwargs: object,
        ) -> Awaitable[
            InfoAndContainerListBuilder
            | InfoAndContainerListReader
            | Sequence[Any]
            | ListcontainersResultTuple
            | None
        ]: ...
        def listContainers_context(
            self,
            context: ListcontainersCallContext,
        ) -> Awaitable[None]: ...
        def removeContainer(
            self,
            id: str,
            _context: RemovecontainerCallContext,
            **kwargs: object,
        ) -> Awaitable[bool | RemovecontainerResultTuple | None]: ...
        def removeContainer_context(
            self,
            context: RemovecontainerCallContext,
        ) -> Awaitable[None]: ...
        def importContainer(
            self,
            json: str,
            _context: ImportcontainerCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _StoreInterfaceModule._ContainerInterfaceModule.Server
            | ContainerClient
            | ImportcontainerResultTuple
            | None
        ]: ...
        def importContainer_context(
            self,
            context: ImportcontainerCallContext,
        ) -> Awaitable[None]: ...

class _BoolList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> bool: ...
        @override
        def __iter__(self) -> Iterator[bool]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> bool: ...
        @override
        def __setitem__(self, key: int, value: bool) -> None: ...
        @override
        def __iter__(self) -> Iterator[bool]: ...

class _Int8List:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> int: ...
        @override
        def __iter__(self) -> Iterator[int]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> int: ...
        @override
        def __setitem__(self, key: int, value: int) -> None: ...
        @override
        def __iter__(self) -> Iterator[int]: ...

class _Int16List:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> int: ...
        @override
        def __iter__(self) -> Iterator[int]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> int: ...
        @override
        def __setitem__(self, key: int, value: int) -> None: ...
        @override
        def __iter__(self) -> Iterator[int]: ...

class _Int32List:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> int: ...
        @override
        def __iter__(self) -> Iterator[int]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> int: ...
        @override
        def __setitem__(self, key: int, value: int) -> None: ...
        @override
        def __iter__(self) -> Iterator[int]: ...

class _Int64List:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> int: ...
        @override
        def __iter__(self) -> Iterator[int]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> int: ...
        @override
        def __setitem__(self, key: int, value: int) -> None: ...
        @override
        def __iter__(self) -> Iterator[int]: ...

class _Uint8List:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> int: ...
        @override
        def __iter__(self) -> Iterator[int]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> int: ...
        @override
        def __setitem__(self, key: int, value: int) -> None: ...
        @override
        def __iter__(self) -> Iterator[int]: ...

class _Uint16List:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> int: ...
        @override
        def __iter__(self) -> Iterator[int]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> int: ...
        @override
        def __setitem__(self, key: int, value: int) -> None: ...
        @override
        def __iter__(self) -> Iterator[int]: ...

class _Uint32List:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> int: ...
        @override
        def __iter__(self) -> Iterator[int]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> int: ...
        @override
        def __setitem__(self, key: int, value: int) -> None: ...
        @override
        def __iter__(self) -> Iterator[int]: ...

class _Uint64List:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> int: ...
        @override
        def __iter__(self) -> Iterator[int]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> int: ...
        @override
        def __setitem__(self, key: int, value: int) -> None: ...
        @override
        def __iter__(self) -> Iterator[int]: ...

class _Float32List:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> float: ...
        @override
        def __iter__(self) -> Iterator[float]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> float: ...
        @override
        def __setitem__(self, key: int, value: float) -> None: ...
        @override
        def __iter__(self) -> Iterator[float]: ...

class _Float64List:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> float: ...
        @override
        def __iter__(self) -> Iterator[float]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> float: ...
        @override
        def __setitem__(self, key: int, value: float) -> None: ...
        @override
        def __iter__(self) -> Iterator[float]: ...

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

class _DataList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> bytes: ...
        @override
        def __iter__(self) -> Iterator[bytes]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> bytes: ...
        @override
        def __setitem__(self, key: int, value: bytes) -> None: ...
        @override
        def __iter__(self) -> Iterator[bytes]: ...

class ValueReader(_DynamicStructReader):
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> ValueBuilder: ...

class ValueBuilder(_DynamicStructBuilder):
    @property
    def boolValue(self) -> bool: ...
    @boolValue.setter
    def boolValue(self, value: bool) -> None: ...
    @property
    def boolListValue(self) -> BoolListBuilder: ...
    @boolListValue.setter
    def boolListValue(
        self,
        value: BoolListBuilder | BoolListReader | dict[str, Any],
    ) -> None: ...
    @property
    def int8Value(self) -> int: ...
    @int8Value.setter
    def int8Value(self, value: int) -> None: ...
    @property
    def int8ListValue(self) -> Int8ListBuilder: ...
    @int8ListValue.setter
    def int8ListValue(
        self,
        value: Int8ListBuilder | Int8ListReader | dict[str, Any],
    ) -> None: ...
    @property
    def int16Value(self) -> int: ...
    @int16Value.setter
    def int16Value(self, value: int) -> None: ...
    @property
    def int16ListValue(self) -> Int16ListBuilder: ...
    @int16ListValue.setter
    def int16ListValue(
        self,
        value: Int16ListBuilder | Int16ListReader | dict[str, Any],
    ) -> None: ...
    @property
    def int32Value(self) -> int: ...
    @int32Value.setter
    def int32Value(self, value: int) -> None: ...
    @property
    def int32ListValue(self) -> Int32ListBuilder: ...
    @int32ListValue.setter
    def int32ListValue(
        self,
        value: Int32ListBuilder | Int32ListReader | dict[str, Any],
    ) -> None: ...
    @property
    def int64Value(self) -> int: ...
    @int64Value.setter
    def int64Value(self, value: int) -> None: ...
    @property
    def int64ListValue(self) -> Int64ListBuilder: ...
    @int64ListValue.setter
    def int64ListValue(
        self,
        value: Int64ListBuilder | Int64ListReader | dict[str, Any],
    ) -> None: ...
    @property
    def uint8Value(self) -> int: ...
    @uint8Value.setter
    def uint8Value(self, value: int) -> None: ...
    @property
    def uint8ListValue(self) -> Uint8ListBuilder: ...
    @uint8ListValue.setter
    def uint8ListValue(
        self,
        value: Uint8ListBuilder | Uint8ListReader | dict[str, Any],
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
        self,
        value: TextListBuilder | TextListReader | dict[str, Any],
    ) -> None: ...
    @property
    def dataValue(self) -> bytes: ...
    @dataValue.setter
    def dataValue(self, value: bytes) -> None: ...
    @property
    def dataListValue(self) -> DataListBuilder: ...
    @dataListValue.setter
    def dataListValue(
        self,
        value: DataListBuilder | DataListReader | dict[str, Any],
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
    @override
    @overload
    def init(
        self,
        field: Literal["boolListValue"],
        size: int | None = None,
    ) -> BoolListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["int8ListValue"],
        size: int | None = None,
    ) -> Int8ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["int16ListValue"],
        size: int | None = None,
    ) -> Int16ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["int32ListValue"],
        size: int | None = None,
    ) -> Int32ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["int64ListValue"],
        size: int | None = None,
    ) -> Int64ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["uint8ListValue"],
        size: int | None = None,
    ) -> Uint8ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["uint16ListValue"],
        size: int | None = None,
    ) -> Uint16ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["uint32ListValue"],
        size: int | None = None,
    ) -> Uint32ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["uint64ListValue"],
        size: int | None = None,
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
        self,
        field: Literal["textListValue"],
        size: int | None = None,
    ) -> TextListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["dataListValue"],
        size: int | None = None,
    ) -> DataListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> ValueReader: ...

class GetkeyRequest(Protocol):
    def send(self) -> GetkeyResult: ...

class GetkeyResult(Awaitable[GetkeyResult], Protocol):
    key: str

class GetkeyServerResult(_DynamicStructBuilder):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str) -> None: ...

class GetkeyParams(Protocol): ...

class GetkeyCallContext(Protocol):
    params: GetkeyParams
    @property
    def results(self) -> GetkeyServerResult: ...

class GetkeyResultTuple(NamedTuple):
    key: str

class GetvalueRequest(Protocol):
    def send(self) -> GetvalueResult: ...

class GetvalueResult(Awaitable[GetvalueResult], Protocol):
    value: ValueReader
    isUnset: bool

class GetvalueServerResult(_DynamicStructBuilder):
    @property
    def value(self) -> ValueBuilder: ...
    @value.setter
    def value(self, value: ValueBuilder | ValueReader | dict[str, Any]) -> None: ...
    @property
    def isUnset(self) -> bool: ...
    @isUnset.setter
    def isUnset(self, value: bool) -> None: ...
    @overload
    def init(
        self,
        field: Literal["value"],
        size: int | None = None,
    ) -> ValueBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class GetvalueParams(Protocol): ...

class GetvalueCallContext(Protocol):
    params: GetvalueParams
    @property
    def results(self) -> GetvalueServerResult: ...

class GetvalueResultTuple(NamedTuple):
    value: ValueBuilder | ValueReader | dict[str, Any]
    isUnset: bool

class SetvalueRequest(Protocol):
    value: ValueBuilder
    @overload
    def init(self, name: Literal["value"]) -> ValueBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> SetvalueResult: ...

class SetvalueResult(Awaitable[SetvalueResult], Protocol):
    success: bool

class SetvalueServerResult(_DynamicStructBuilder):
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class SetvalueParams(Protocol):
    value: ValueReader

class SetvalueCallContext(Protocol):
    params: SetvalueParams
    @property
    def results(self) -> SetvalueServerResult: ...

class SetvalueResultTuple(NamedTuple):
    success: bool

class EntryClient(_DynamicCapabilityClient):
    def getKey(self) -> GetkeyResult: ...
    def getValue(self) -> GetvalueResult: ...
    def setValue(
        self,
        value: ValueBuilder | ValueReader | dict[str, Any] | None = None,
    ) -> SetvalueResult: ...
    def getKey_request(self) -> GetkeyRequest: ...
    def getValue_request(self) -> GetvalueRequest: ...
    def setValue_request(
        self,
        value: ValueBuilder | None = None,
    ) -> SetvalueRequest: ...

class KeyAndEntryReader(_DynamicStructReader):
    @property
    def key(self) -> str: ...
    @property
    def entry(self) -> EntryClient: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> KeyAndEntryBuilder: ...

class KeyAndEntryBuilder(_DynamicStructBuilder):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str) -> None: ...
    @property
    def entry(self) -> EntryClient: ...
    @entry.setter
    def entry(
        self,
        value: EntryClient
        | _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule.Server,
    ) -> None: ...
    @override
    def as_reader(self) -> KeyAndEntryReader: ...

class ExportRequest(Protocol):
    def send(self) -> ExportResult: ...

class ExportResult(Awaitable[ExportResult], Protocol):
    json: str

class ExportServerResult(_DynamicStructBuilder):
    @property
    def json(self) -> str: ...
    @json.setter
    def json(self, value: str) -> None: ...

class ExportParams(Protocol): ...

class ExportCallContext(Protocol):
    params: ExportParams
    @property
    def results(self) -> ExportServerResult: ...

class ExportResultTuple(NamedTuple):
    json: str

class DownloadentriesRequest(Protocol):
    def send(self) -> DownloadentriesResult: ...

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

class DownloadentriesResult(Awaitable[DownloadentriesResult], Protocol):
    entries: PairListReader

class DownloadentriesServerResult(_DynamicStructBuilder):
    @property
    def entries(self) -> PairListBuilder: ...
    @entries.setter
    def entries(
        self,
        value: PairListBuilder | PairListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["entries"],
        size: int | None = None,
    ) -> PairListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class DownloadentriesParams(Protocol): ...

class DownloadentriesCallContext(Protocol):
    params: DownloadentriesParams
    @property
    def results(self) -> DownloadentriesServerResult: ...

class DownloadentriesResultTuple(NamedTuple):
    entries: PairListBuilder | PairListReader | Sequence[Any]

class ListentriesRequest(Protocol):
    def send(self) -> ListentriesResult: ...

class _KeyAndEntryList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> KeyAndEntryReader: ...
        @override
        def __iter__(self) -> Iterator[KeyAndEntryReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> KeyAndEntryBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: KeyAndEntryReader | KeyAndEntryBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[KeyAndEntryBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> KeyAndEntryBuilder: ...

class ListentriesResult(Awaitable[ListentriesResult], Protocol):
    entries: KeyAndEntryListReader

class ListentriesServerResult(_DynamicStructBuilder):
    @property
    def entries(self) -> KeyAndEntryListBuilder: ...
    @entries.setter
    def entries(
        self,
        value: KeyAndEntryListBuilder | KeyAndEntryListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["entries"],
        size: int | None = None,
    ) -> KeyAndEntryListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class ListentriesParams(Protocol): ...

class ListentriesCallContext(Protocol):
    params: ListentriesParams
    @property
    def results(self) -> ListentriesServerResult: ...

class ListentriesResultTuple(NamedTuple):
    entries: KeyAndEntryListBuilder | KeyAndEntryListReader | Sequence[Any]

class GetentryRequest(Protocol):
    key: str
    def send(self) -> GetentryResult: ...

class GetentryResult(Awaitable[GetentryResult], Protocol):
    entry: EntryClient

class GetentryServerResult(_DynamicStructBuilder):
    @property
    def entry(
        self,
    ) -> (
        _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule.Server
        | EntryClient
    ): ...
    @entry.setter
    def entry(
        self,
        value: _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule.Server
        | EntryClient,
    ) -> None: ...

class GetentryParams(Protocol):
    key: str

class GetentryCallContext(Protocol):
    params: GetentryParams
    @property
    def results(self) -> GetentryServerResult: ...

class GetentryResultTuple(NamedTuple):
    entry: (
        _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule.Server
        | EntryClient
    )

class RemoveentryRequest(Protocol):
    key: str
    def send(self) -> RemoveentryResult: ...

class RemoveentryResult(Awaitable[RemoveentryResult], Protocol):
    success: bool

class RemoveentryServerResult(_DynamicStructBuilder):
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class RemoveentryParams(Protocol):
    key: str

class RemoveentryCallContext(Protocol):
    params: RemoveentryParams
    @property
    def results(self) -> RemoveentryServerResult: ...

class RemoveentryResultTuple(NamedTuple):
    success: bool

class ClearRequest(Protocol):
    def send(self) -> ClearResult: ...

class ClearResult(Awaitable[ClearResult], Protocol):
    success: bool

class ClearServerResult(_DynamicStructBuilder):
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class ClearParams(Protocol): ...

class ClearCallContext(Protocol):
    params: ClearParams
    @property
    def results(self) -> ClearServerResult: ...

class ClearResultTuple(NamedTuple):
    success: bool

class AddentryRequest(Protocol):
    key: str
    value: ValueBuilder
    replaceExisting: bool
    @overload
    def init(self, name: Literal["value"]) -> ValueBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> AddentryResult: ...

class AddentryResult(Awaitable[AddentryResult], Protocol):
    entry: EntryClient
    success: bool

class AddentryServerResult(_DynamicStructBuilder):
    @property
    def entry(
        self,
    ) -> (
        _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule.Server
        | EntryClient
    ): ...
    @entry.setter
    def entry(
        self,
        value: _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule.Server
        | EntryClient,
    ) -> None: ...
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class AddentryParams(Protocol):
    key: str
    value: ValueReader
    replaceExisting: bool

class AddentryCallContext(Protocol):
    params: AddentryParams
    @property
    def results(self) -> AddentryServerResult: ...

class AddentryResultTuple(NamedTuple):
    entry: (
        _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule.Server
        | EntryClient
    )
    success: bool

class ContainerClient(IdentifiableClient, PersistentClient):
    def export(self) -> ExportResult: ...
    def downloadEntries(self) -> DownloadentriesResult: ...
    def listEntries(self) -> ListentriesResult: ...
    def getEntry(self, key: str | None = None) -> GetentryResult: ...
    def removeEntry(self, key: str | None = None) -> RemoveentryResult: ...
    def clear(self) -> ClearResult: ...
    def addEntry(
        self,
        key: str | None = None,
        value: ValueBuilder | ValueReader | dict[str, Any] | None = None,
        replaceExisting: bool | None = None,
    ) -> AddentryResult: ...
    def export_request(self) -> ExportRequest: ...
    def downloadEntries_request(self) -> DownloadentriesRequest: ...
    def listEntries_request(self) -> ListentriesRequest: ...
    def getEntry_request(self, key: str | None = None) -> GetentryRequest: ...
    def removeEntry_request(self, key: str | None = None) -> RemoveentryRequest: ...
    def clear_request(self) -> ClearRequest: ...
    def addEntry_request(
        self,
        key: str | None = None,
        value: ValueBuilder | None = None,
        replaceExisting: bool | None = None,
    ) -> AddentryRequest: ...

class InfoAndContainerReader(_DynamicStructReader):
    @property
    def id(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def container(self) -> ContainerClient: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> InfoAndContainerBuilder: ...

class InfoAndContainerBuilder(_DynamicStructBuilder):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str) -> None: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def container(self) -> ContainerClient: ...
    @container.setter
    def container(
        self,
        value: ContainerClient | _StoreInterfaceModule._ContainerInterfaceModule.Server,
    ) -> None: ...
    @override
    def as_reader(self) -> InfoAndContainerReader: ...

class ImportExportDataReader(_DynamicStructReader):
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> ImportExportDataBuilder: ...

class ImportExportDataBuilder(_DynamicStructBuilder):
    @property
    def info(self) -> IdInformationBuilder: ...
    @info.setter
    def info(
        self,
        value: IdInformationBuilder | IdInformationReader | dict[str, Any],
    ) -> None: ...
    @property
    def entries(self) -> PairListBuilder: ...
    @entries.setter
    def entries(
        self,
        value: PairListBuilder | PairListReader | dict[str, Any],
    ) -> None: ...
    @property
    def isAnyValue(self) -> BoolListBuilder: ...
    @isAnyValue.setter
    def isAnyValue(
        self,
        value: BoolListBuilder | BoolListReader | dict[str, Any],
    ) -> None: ...
    @override
    @overload
    def init(
        self,
        field: Literal["info"],
        size: int | None = None,
    ) -> IdInformationBuilder: ...
    @overload
    def init(
        self,
        field: Literal["entries"],
        size: int | None = None,
    ) -> PairListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["isAnyValue"],
        size: int | None = None,
    ) -> BoolListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> ImportExportDataReader: ...

class NewcontainerRequest(Protocol):
    name: str
    description: str
    def send(self) -> NewcontainerResult: ...

class NewcontainerResult(Awaitable[NewcontainerResult], Protocol):
    container: ContainerClient

class NewcontainerServerResult(_DynamicStructBuilder):
    @property
    def container(
        self,
    ) -> _StoreInterfaceModule._ContainerInterfaceModule.Server | ContainerClient: ...
    @container.setter
    def container(
        self,
        value: _StoreInterfaceModule._ContainerInterfaceModule.Server | ContainerClient,
    ) -> None: ...

class NewcontainerParams(Protocol):
    name: str
    description: str

class NewcontainerCallContext(Protocol):
    params: NewcontainerParams
    @property
    def results(self) -> NewcontainerServerResult: ...

class NewcontainerResultTuple(NamedTuple):
    container: _StoreInterfaceModule._ContainerInterfaceModule.Server | ContainerClient

class ContainerwithidRequest(Protocol):
    id: str
    def send(self) -> ContainerwithidResult: ...

class ContainerwithidResult(Awaitable[ContainerwithidResult], Protocol):
    container: ContainerClient

class ContainerwithidServerResult(_DynamicStructBuilder):
    @property
    def container(
        self,
    ) -> _StoreInterfaceModule._ContainerInterfaceModule.Server | ContainerClient: ...
    @container.setter
    def container(
        self,
        value: _StoreInterfaceModule._ContainerInterfaceModule.Server | ContainerClient,
    ) -> None: ...

class ContainerwithidParams(Protocol):
    id: str

class ContainerwithidCallContext(Protocol):
    params: ContainerwithidParams
    @property
    def results(self) -> ContainerwithidServerResult: ...

class ContainerwithidResultTuple(NamedTuple):
    container: _StoreInterfaceModule._ContainerInterfaceModule.Server | ContainerClient

class ListcontainersRequest(Protocol):
    def send(self) -> ListcontainersResult: ...

class _InfoAndContainerList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> InfoAndContainerReader: ...
        @override
        def __iter__(self) -> Iterator[InfoAndContainerReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> InfoAndContainerBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: InfoAndContainerReader | InfoAndContainerBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[InfoAndContainerBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> InfoAndContainerBuilder: ...

class ListcontainersResult(Awaitable[ListcontainersResult], Protocol):
    containers: InfoAndContainerListReader

class ListcontainersServerResult(_DynamicStructBuilder):
    @property
    def containers(self) -> InfoAndContainerListBuilder: ...
    @containers.setter
    def containers(
        self,
        value: InfoAndContainerListBuilder | InfoAndContainerListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["containers"],
        size: int | None = None,
    ) -> InfoAndContainerListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class ListcontainersParams(Protocol): ...

class ListcontainersCallContext(Protocol):
    params: ListcontainersParams
    @property
    def results(self) -> ListcontainersServerResult: ...

class ListcontainersResultTuple(NamedTuple):
    containers: InfoAndContainerListBuilder | InfoAndContainerListReader | Sequence[Any]

class RemovecontainerRequest(Protocol):
    id: str
    def send(self) -> RemovecontainerResult: ...

class RemovecontainerResult(Awaitable[RemovecontainerResult], Protocol):
    success: bool

class RemovecontainerServerResult(_DynamicStructBuilder):
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class RemovecontainerParams(Protocol):
    id: str

class RemovecontainerCallContext(Protocol):
    params: RemovecontainerParams
    @property
    def results(self) -> RemovecontainerServerResult: ...

class RemovecontainerResultTuple(NamedTuple):
    success: bool

class ImportcontainerRequest(Protocol):
    json: str
    def send(self) -> ImportcontainerResult: ...

class ImportcontainerResult(Awaitable[ImportcontainerResult], Protocol):
    container: ContainerClient

class ImportcontainerServerResult(_DynamicStructBuilder):
    @property
    def container(
        self,
    ) -> _StoreInterfaceModule._ContainerInterfaceModule.Server | ContainerClient: ...
    @container.setter
    def container(
        self,
        value: _StoreInterfaceModule._ContainerInterfaceModule.Server | ContainerClient,
    ) -> None: ...

class ImportcontainerParams(Protocol):
    json: str

class ImportcontainerCallContext(Protocol):
    params: ImportcontainerParams
    @property
    def results(self) -> ImportcontainerServerResult: ...

class ImportcontainerResultTuple(NamedTuple):
    container: _StoreInterfaceModule._ContainerInterfaceModule.Server | ContainerClient

class StoreClient(IdentifiableClient, PersistentClient):
    def newContainer(
        self,
        name: str | None = None,
        description: str | None = None,
    ) -> NewcontainerResult: ...
    def containerWithId(self, id: str | None = None) -> ContainerwithidResult: ...
    def listContainers(self) -> ListcontainersResult: ...
    def removeContainer(self, id: str | None = None) -> RemovecontainerResult: ...
    def importContainer(self, json: str | None = None) -> ImportcontainerResult: ...
    def newContainer_request(
        self,
        name: str | None = None,
        description: str | None = None,
    ) -> NewcontainerRequest: ...
    def containerWithId_request(
        self,
        id: str | None = None,
    ) -> ContainerwithidRequest: ...
    def listContainers_request(self) -> ListcontainersRequest: ...
    def removeContainer_request(
        self,
        id: str | None = None,
    ) -> RemovecontainerRequest: ...
    def importContainer_request(
        self,
        json: str | None = None,
    ) -> ImportcontainerRequest: ...

Store: _StoreInterfaceModule

# Top-level type aliases for use in type annotations
type BoolListBuilder = _BoolList.Builder
type BoolListReader = _BoolList.Reader
ContainerServer = _StoreInterfaceModule._ContainerInterfaceModule.Server
type DataListBuilder = _DataList.Builder
type DataListReader = _DataList.Reader
EntryServer = (
    _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule.Server
)
type Float32ListBuilder = _Float32List.Builder
type Float32ListReader = _Float32List.Reader
type Float64ListBuilder = _Float64List.Builder
type Float64ListReader = _Float64List.Reader
type InfoAndContainerListBuilder = _InfoAndContainerList.Builder
type InfoAndContainerListReader = _InfoAndContainerList.Reader
type Int16ListBuilder = _Int16List.Builder
type Int16ListReader = _Int16List.Reader
type Int32ListBuilder = _Int32List.Builder
type Int32ListReader = _Int32List.Reader
type Int64ListBuilder = _Int64List.Builder
type Int64ListReader = _Int64List.Reader
type Int8ListBuilder = _Int8List.Builder
type Int8ListReader = _Int8List.Reader
type KeyAndEntryListBuilder = _KeyAndEntryList.Builder
type KeyAndEntryListReader = _KeyAndEntryList.Reader
type PairListBuilder = _PairList.Builder
type PairListReader = _PairList.Reader
StoreServer = _StoreInterfaceModule.Server
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
