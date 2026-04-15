"""Module helper types for `storage.capnp`."""

from collections.abc import Awaitable, Callable, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
    _StructModule,
)

from mas.schema.common.common_capnp.types.builders import IdInformationBuilder
from mas.schema.common.common_capnp.types.modules import (
    _IdentifiableInterfaceModule,
)
from mas.schema.persistence.persistence_capnp.types.modules import (
    _PersistentInterfaceModule,
)

from . import _all as _all

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
                    boolListValue: _all.BoolListBuilder | dict[str, Any] | None = None,
                    int8Value: int | None = None,
                    int8ListValue: _all.Int8ListBuilder | dict[str, Any] | None = None,
                    int16Value: int | None = None,
                    int16ListValue: _all.Int16ListBuilder
                    | dict[str, Any]
                    | None = None,
                    int32Value: int | None = None,
                    int32ListValue: _all.Int32ListBuilder
                    | dict[str, Any]
                    | None = None,
                    int64Value: int | None = None,
                    int64ListValue: _all.Int64ListBuilder
                    | dict[str, Any]
                    | None = None,
                    uint8Value: int | None = None,
                    uint8ListValue: _all.Uint8ListBuilder
                    | dict[str, Any]
                    | None = None,
                    uint16Value: int | None = None,
                    uint16ListValue: _all.Uint16ListBuilder
                    | dict[str, Any]
                    | None = None,
                    uint32Value: int | None = None,
                    uint32ListValue: _all.Uint32ListBuilder
                    | dict[str, Any]
                    | None = None,
                    uint64Value: int | None = None,
                    uint64ListValue: _all.Uint64ListBuilder
                    | dict[str, Any]
                    | None = None,
                    float32Value: float | None = None,
                    float32ListValue: _all.Float32ListBuilder
                    | dict[str, Any]
                    | None = None,
                    float64Value: float | None = None,
                    float64ListValue: _all.Float64ListBuilder
                    | dict[str, Any]
                    | None = None,
                    textValue: str | None = None,
                    textListValue: _all.TextListBuilder | dict[str, Any] | None = None,
                    dataValue: bytes | None = None,
                    dataListValue: _all.DataListBuilder | dict[str, Any] | None = None,
                    anyValue: _all.AnyStruct | dict[str, Any] | None = None,
                    **kwargs: object,
                ) -> _all.ValueBuilder: ...
                @override
                @overload
                def from_bytes(
                    self,
                    buf: bytes,
                    traversal_limit_in_words: int | None = None,
                    nesting_limit: int | None = None,
                ) -> AbstractContextManager[_all.ValueReader]: ...
                @overload
                def from_bytes(
                    self,
                    buf: bytes,
                    traversal_limit_in_words: int | None = None,
                    nesting_limit: int | None = None,
                    *,
                    builder: Literal[False],
                ) -> AbstractContextManager[_all.ValueReader]: ...
                @overload
                def from_bytes(
                    self,
                    buf: bytes,
                    traversal_limit_in_words: int | None = None,
                    nesting_limit: int | None = None,
                    *,
                    builder: Literal[True],
                ) -> AbstractContextManager[_all.ValueBuilder]: ...
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
                ) -> _all.ValueReader: ...
                @override
                def read_packed(
                    self,
                    file: IO[str] | IO[bytes],
                    traversal_limit_in_words: int | None = None,
                    nesting_limit: int | None = None,
                ) -> _all.ValueReader: ...

            Value: _ValueStructModule
            @override
            def _new_client(
                self,
                server: _DynamicCapabilityServer,
            ) -> _all.EntryClient: ...
            class Server(_DynamicCapabilityServer):
                def getKey(
                    self,
                    _context: _all.GetkeyCallContext,
                    **kwargs: object,
                ) -> Awaitable[str | _all.GetkeyResultTuple | None]: ...
                def getKey_context(
                    self,
                    context: _all.GetkeyCallContext,
                ) -> Awaitable[None]: ...
                def getValue(
                    self,
                    _context: _all.GetvalueCallContext,
                    **kwargs: object,
                ) -> Awaitable[_all.GetvalueResultTuple | None]: ...
                def getValue_context(
                    self,
                    context: _all.GetvalueCallContext,
                ) -> Awaitable[None]: ...
                def setValue(
                    self,
                    value: _all.ValueReader,
                    _context: _all.SetvalueCallContext,
                    **kwargs: object,
                ) -> Awaitable[bool | _all.SetvalueResultTuple | None]: ...
                def setValue_context(
                    self,
                    context: _all.SetvalueCallContext,
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
                entry: _all.EntryClient
                | _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule.Server
                | None = None,
                **kwargs: object,
            ) -> _all.KeyAndEntryBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[_all.KeyAndEntryReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[_all.KeyAndEntryReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[_all.KeyAndEntryBuilder]: ...
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
            ) -> _all.KeyAndEntryReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> _all.KeyAndEntryReader: ...

        KeyAndEntry: _KeyAndEntryStructModule
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> _all.ContainerClient: ...
        class Server(
            _IdentifiableInterfaceModule.Server,
            _PersistentInterfaceModule.Server,
        ):
            def export(
                self,
                _context: _all.ExportCallContext,
                **kwargs: object,
            ) -> Awaitable[str | _all.ExportResultTuple | None]: ...
            def export_context(
                self,
                context: _all.ExportCallContext,
            ) -> Awaitable[None]: ...
            def downloadEntries(
                self,
                _context: _all.DownloadentriesCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _all.PairListBuilder
                | _all.PairListReader
                | Sequence[Any]
                | _all.DownloadentriesResultTuple
                | None
            ]: ...
            def downloadEntries_context(
                self,
                context: _all.DownloadentriesCallContext,
            ) -> Awaitable[None]: ...
            def listEntries(
                self,
                _context: _all.ListentriesCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _all.KeyAndEntryListBuilder
                | _all.KeyAndEntryListReader
                | Sequence[Any]
                | _all.ListentriesResultTuple
                | None
            ]: ...
            def listEntries_context(
                self,
                context: _all.ListentriesCallContext,
            ) -> Awaitable[None]: ...
            def getEntry(
                self,
                key: str,
                _context: _all.GetentryCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule.Server
                | _all.EntryClient
                | _all.GetentryResultTuple
                | None
            ]: ...
            def getEntry_context(
                self,
                context: _all.GetentryCallContext,
            ) -> Awaitable[None]: ...
            def removeEntry(
                self,
                key: str,
                _context: _all.RemoveentryCallContext,
                **kwargs: object,
            ) -> Awaitable[bool | _all.RemoveentryResultTuple | None]: ...
            def removeEntry_context(
                self,
                context: _all.RemoveentryCallContext,
            ) -> Awaitable[None]: ...
            def clear(
                self,
                _context: _all.ClearCallContext,
                **kwargs: object,
            ) -> Awaitable[bool | _all.ClearResultTuple | None]: ...
            def clear_context(
                self,
                context: _all.ClearCallContext,
            ) -> Awaitable[None]: ...
            def addEntry(
                self,
                key: str,
                value: _all.ValueReader,
                replaceExisting: bool,
                _context: _all.AddentryCallContext,
                **kwargs: object,
            ) -> Awaitable[_all.AddentryResultTuple | None]: ...
            def addEntry_context(
                self,
                context: _all.AddentryCallContext,
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
            container: _all.ContainerClient
            | _StoreInterfaceModule._ContainerInterfaceModule.Server
            | None = None,
            **kwargs: object,
        ) -> _all.InfoAndContainerBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.InfoAndContainerReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.InfoAndContainerReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.InfoAndContainerBuilder]: ...
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
        ) -> _all.InfoAndContainerReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.InfoAndContainerReader: ...

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
            entries: _all.PairListBuilder | dict[str, Any] | None = None,
            isAnyValue: _all.BoolListBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> _all.ImportExportDataBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.ImportExportDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.ImportExportDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.ImportExportDataBuilder]: ...
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
        ) -> _all.ImportExportDataReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.ImportExportDataReader: ...

    ImportExportData: _ImportExportDataStructModule
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> _all.StoreClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def newContainer(
            self,
            name: str,
            description: str,
            _context: _all.NewcontainerCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _StoreInterfaceModule._ContainerInterfaceModule.Server
            | _all.ContainerClient
            | _all.NewcontainerResultTuple
            | None
        ]: ...
        def newContainer_context(
            self,
            context: _all.NewcontainerCallContext,
        ) -> Awaitable[None]: ...
        def containerWithId(
            self,
            id: str,
            _context: _all.ContainerwithidCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _StoreInterfaceModule._ContainerInterfaceModule.Server
            | _all.ContainerClient
            | _all.ContainerwithidResultTuple
            | None
        ]: ...
        def containerWithId_context(
            self,
            context: _all.ContainerwithidCallContext,
        ) -> Awaitable[None]: ...
        def listContainers(
            self,
            _context: _all.ListcontainersCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _all.InfoAndContainerListBuilder
            | _all.InfoAndContainerListReader
            | Sequence[Any]
            | _all.ListcontainersResultTuple
            | None
        ]: ...
        def listContainers_context(
            self,
            context: _all.ListcontainersCallContext,
        ) -> Awaitable[None]: ...
        def removeContainer(
            self,
            id: str,
            _context: _all.RemovecontainerCallContext,
            **kwargs: object,
        ) -> Awaitable[bool | _all.RemovecontainerResultTuple | None]: ...
        def removeContainer_context(
            self,
            context: _all.RemovecontainerCallContext,
        ) -> Awaitable[None]: ...
        def importContainer(
            self,
            json: str,
            _context: _all.ImportcontainerCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _StoreInterfaceModule._ContainerInterfaceModule.Server
            | _all.ContainerClient
            | _all.ImportcontainerResultTuple
            | None
        ]: ...
        def importContainer_context(
            self,
            context: _all.ImportcontainerCallContext,
        ) -> Awaitable[None]: ...
