"""Module helper types for `storage.capnp`."""

from collections.abc import Awaitable, Callable, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceMethod,
    _InterfaceModule,
    _InterfaceSchema,
    _ListSchema,
    _StructModule,
    _StructSchema,
    _StructSchemaField,
)

from mas.schema.common.common_capnp.types.builders import IdInformationBuilder
from mas.schema.common.common_capnp.types.modules import (
    _IdentifiableInterfaceModule,
)
from mas.schema.persistence.persistence_capnp.types.modules import (
    _PersistentInterfaceModule,
)
from mas.schema.storage.storage_capnp.types import builders as builders
from mas.schema.storage.storage_capnp.types import clients as clients
from mas.schema.storage.storage_capnp.types import common as common
from mas.schema.storage.storage_capnp.types import contexts as contexts
from mas.schema.storage.storage_capnp.types import readers as readers
from mas.schema.storage.storage_capnp.types import schemas as schemas
from mas.schema.storage.storage_capnp.types import servers as servers
from mas.schema.storage.storage_capnp.types.results import tuples as results_tuples

class _StoreInterfaceModule(_IdentifiableInterfaceModule, _PersistentInterfaceModule):
    class _ContainerInterfaceModule(
        _IdentifiableInterfaceModule,
        _PersistentInterfaceModule,
    ):
        class _EntryInterfaceModule(_InterfaceModule):
            class _ValueStructModule(_StructModule):
                class Reader(_DynamicStructReader): ...
                class Builder(_DynamicStructBuilder): ...

                class _ValueSchema(_StructSchema):
                    class _BoolListValueField(_StructSchemaField):
                        @property
                        @override
                        def schema(self) -> _ListSchema: ...

                    class _Int8ListValueField(_StructSchemaField):
                        @property
                        @override
                        def schema(self) -> _ListSchema: ...

                    class _Int16ListValueField(_StructSchemaField):
                        @property
                        @override
                        def schema(self) -> _ListSchema: ...

                    class _Int32ListValueField(_StructSchemaField):
                        @property
                        @override
                        def schema(self) -> _ListSchema: ...

                    class _Int64ListValueField(_StructSchemaField):
                        @property
                        @override
                        def schema(self) -> _ListSchema: ...

                    class _Uint8ListValueField(_StructSchemaField):
                        @property
                        @override
                        def schema(self) -> _ListSchema: ...

                    class _Uint16ListValueField(_StructSchemaField):
                        @property
                        @override
                        def schema(self) -> _ListSchema: ...

                    class _Uint32ListValueField(_StructSchemaField):
                        @property
                        @override
                        def schema(self) -> _ListSchema: ...

                    class _Uint64ListValueField(_StructSchemaField):
                        @property
                        @override
                        def schema(self) -> _ListSchema: ...

                    class _Float32ListValueField(_StructSchemaField):
                        @property
                        @override
                        def schema(self) -> _ListSchema: ...

                    class _Float64ListValueField(_StructSchemaField):
                        @property
                        @override
                        def schema(self) -> _ListSchema: ...

                    class _TextListValueField(_StructSchemaField):
                        @property
                        @override
                        def schema(self) -> _ListSchema: ...

                    class _DataListValueField(_StructSchemaField):
                        @property
                        @override
                        def schema(self) -> _ListSchema: ...

                    class _Fields(dict[str, _StructSchemaField]):
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["boolValue"],
                        ) -> _StructSchemaField: ...
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["boolListValue"],
                        ) -> _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._ValueStructModule._ValueSchema._BoolListValueField: ...
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["int8Value"],
                        ) -> _StructSchemaField: ...
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["int8ListValue"],
                        ) -> _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._ValueStructModule._ValueSchema._Int8ListValueField: ...
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["int16Value"],
                        ) -> _StructSchemaField: ...
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["int16ListValue"],
                        ) -> _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._ValueStructModule._ValueSchema._Int16ListValueField: ...
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["int32Value"],
                        ) -> _StructSchemaField: ...
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["int32ListValue"],
                        ) -> _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._ValueStructModule._ValueSchema._Int32ListValueField: ...
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["int64Value"],
                        ) -> _StructSchemaField: ...
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["int64ListValue"],
                        ) -> _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._ValueStructModule._ValueSchema._Int64ListValueField: ...
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["uint8Value"],
                        ) -> _StructSchemaField: ...
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["uint8ListValue"],
                        ) -> _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._ValueStructModule._ValueSchema._Uint8ListValueField: ...
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["uint16Value"],
                        ) -> _StructSchemaField: ...
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["uint16ListValue"],
                        ) -> _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._ValueStructModule._ValueSchema._Uint16ListValueField: ...
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["uint32Value"],
                        ) -> _StructSchemaField: ...
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["uint32ListValue"],
                        ) -> _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._ValueStructModule._ValueSchema._Uint32ListValueField: ...
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["uint64Value"],
                        ) -> _StructSchemaField: ...
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["uint64ListValue"],
                        ) -> _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._ValueStructModule._ValueSchema._Uint64ListValueField: ...
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["float32Value"],
                        ) -> _StructSchemaField: ...
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["float32ListValue"],
                        ) -> _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._ValueStructModule._ValueSchema._Float32ListValueField: ...
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["float64Value"],
                        ) -> _StructSchemaField: ...
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["float64ListValue"],
                        ) -> _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._ValueStructModule._ValueSchema._Float64ListValueField: ...
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["textValue"],
                        ) -> _StructSchemaField: ...
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["textListValue"],
                        ) -> _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._ValueStructModule._ValueSchema._TextListValueField: ...
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["dataValue"],
                        ) -> _StructSchemaField: ...
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["dataListValue"],
                        ) -> _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._ValueStructModule._ValueSchema._DataListValueField: ...
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["anyValue"],
                        ) -> _StructSchemaField: ...
                        @overload
                        def __getitem__(self, key: str) -> _StructSchemaField: ...

                    @property
                    @override
                    def fields(
                        self,
                    ) -> _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._ValueStructModule._ValueSchema._Fields: ...

                @property
                @override
                def schema(self) -> schemas._StoreContainerEntryValueSchema: ...
                @override
                def new_message(
                    self,
                    num_first_segment_words: int | None = None,
                    allocate_seg_callable: Callable[[int], bytearray] | None = None,
                    boolValue: bool | None = None,
                    boolListValue: builders.BoolListBuilder
                    | dict[str, Any]
                    | None = None,
                    int8Value: int | None = None,
                    int8ListValue: builders.Int8ListBuilder
                    | dict[str, Any]
                    | None = None,
                    int16Value: int | None = None,
                    int16ListValue: builders.Int16ListBuilder
                    | dict[str, Any]
                    | None = None,
                    int32Value: int | None = None,
                    int32ListValue: builders.Int32ListBuilder
                    | dict[str, Any]
                    | None = None,
                    int64Value: int | None = None,
                    int64ListValue: builders.Int64ListBuilder
                    | dict[str, Any]
                    | None = None,
                    uint8Value: int | None = None,
                    uint8ListValue: builders.Uint8ListBuilder
                    | dict[str, Any]
                    | None = None,
                    uint16Value: int | None = None,
                    uint16ListValue: builders.Uint16ListBuilder
                    | dict[str, Any]
                    | None = None,
                    uint32Value: int | None = None,
                    uint32ListValue: builders.Uint32ListBuilder
                    | dict[str, Any]
                    | None = None,
                    uint64Value: int | None = None,
                    uint64ListValue: builders.Uint64ListBuilder
                    | dict[str, Any]
                    | None = None,
                    float32Value: float | None = None,
                    float32ListValue: builders.Float32ListBuilder
                    | dict[str, Any]
                    | None = None,
                    float64Value: float | None = None,
                    float64ListValue: builders.Float64ListBuilder
                    | dict[str, Any]
                    | None = None,
                    textValue: str | None = None,
                    textListValue: builders.TextListBuilder
                    | dict[str, Any]
                    | None = None,
                    dataValue: bytes | None = None,
                    dataListValue: builders.DataListBuilder
                    | dict[str, Any]
                    | None = None,
                    anyValue: common.AnyStruct | dict[str, Any] | None = None,
                    **kwargs: object,
                ) -> builders.ValueBuilder: ...
                @override
                @overload
                def from_bytes(
                    self,
                    buf: bytes,
                    traversal_limit_in_words: int | None = None,
                    nesting_limit: int | None = None,
                ) -> AbstractContextManager[readers.ValueReader]: ...
                @overload
                def from_bytes(
                    self,
                    buf: bytes,
                    traversal_limit_in_words: int | None = None,
                    nesting_limit: int | None = None,
                    *,
                    builder: Literal[False],
                ) -> AbstractContextManager[readers.ValueReader]: ...
                @overload
                def from_bytes(
                    self,
                    buf: bytes,
                    traversal_limit_in_words: int | None = None,
                    nesting_limit: int | None = None,
                    *,
                    builder: Literal[True],
                ) -> AbstractContextManager[builders.ValueBuilder]: ...
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
                ) -> readers.ValueReader: ...
                @override
                def read_packed(
                    self,
                    file: IO[str] | IO[bytes],
                    traversal_limit_in_words: int | None = None,
                    nesting_limit: int | None = None,
                ) -> readers.ValueReader: ...

            Value: _ValueStructModule

            class _EntrySchema(_InterfaceSchema):
                class _EntryInterfaceModuleGetKeyParamSchema(_StructSchema):
                    class _Fields(dict[str, _StructSchemaField]): ...

                    @property
                    @override
                    def fields(
                        self,
                    ) -> _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._EntrySchema._EntryInterfaceModuleGetKeyParamSchema._Fields: ...

                class _EntryInterfaceModuleGetKeyResultSchema(_StructSchema):
                    class _Fields(dict[str, _StructSchemaField]):
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["key"],
                        ) -> _StructSchemaField: ...
                        @overload
                        def __getitem__(self, key: str) -> _StructSchemaField: ...

                    @property
                    @override
                    def fields(
                        self,
                    ) -> _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._EntrySchema._EntryInterfaceModuleGetKeyResultSchema._Fields: ...

                class _EntryInterfaceModuleGetValueParamSchema(_StructSchema):
                    class _Fields(dict[str, _StructSchemaField]): ...

                    @property
                    @override
                    def fields(
                        self,
                    ) -> _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._EntrySchema._EntryInterfaceModuleGetValueParamSchema._Fields: ...

                class _EntryInterfaceModuleGetValueResultSchema(_StructSchema):
                    class _ValueField(_StructSchemaField):
                        @property
                        @override
                        def schema(self) -> schemas._StoreContainerEntryValueSchema: ...

                    class _Fields(dict[str, _StructSchemaField]):
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["value"],
                        ) -> _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._EntrySchema._EntryInterfaceModuleGetValueResultSchema._ValueField: ...
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["isUnset"],
                        ) -> _StructSchemaField: ...
                        @overload
                        def __getitem__(self, key: str) -> _StructSchemaField: ...

                    @property
                    @override
                    def fields(
                        self,
                    ) -> _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._EntrySchema._EntryInterfaceModuleGetValueResultSchema._Fields: ...

                class _EntryInterfaceModuleSetValueParamSchema(_StructSchema):
                    class _ValueField(_StructSchemaField):
                        @property
                        @override
                        def schema(self) -> schemas._StoreContainerEntryValueSchema: ...

                    class _Fields(dict[str, _StructSchemaField]):
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["value"],
                        ) -> _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._EntrySchema._EntryInterfaceModuleSetValueParamSchema._ValueField: ...
                        @overload
                        def __getitem__(self, key: str) -> _StructSchemaField: ...

                    @property
                    @override
                    def fields(
                        self,
                    ) -> _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._EntrySchema._EntryInterfaceModuleSetValueParamSchema._Fields: ...

                class _EntryInterfaceModuleSetValueResultSchema(_StructSchema):
                    class _Fields(dict[str, _StructSchemaField]):
                        @overload
                        def __getitem__(
                            self,
                            key: Literal["success"],
                        ) -> _StructSchemaField: ...
                        @overload
                        def __getitem__(self, key: str) -> _StructSchemaField: ...

                    @property
                    @override
                    def fields(
                        self,
                    ) -> _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._EntrySchema._EntryInterfaceModuleSetValueResultSchema._Fields: ...

                class _Methods(
                    dict[str, _InterfaceMethod[_StructSchema, _StructSchema]],
                ):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["getKey"],
                    ) -> _InterfaceMethod[
                        _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._EntrySchema._EntryInterfaceModuleGetKeyParamSchema,
                        _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._EntrySchema._EntryInterfaceModuleGetKeyResultSchema,
                    ]: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["getValue"],
                    ) -> _InterfaceMethod[
                        _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._EntrySchema._EntryInterfaceModuleGetValueParamSchema,
                        _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._EntrySchema._EntryInterfaceModuleGetValueResultSchema,
                    ]: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["setValue"],
                    ) -> _InterfaceMethod[
                        _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._EntrySchema._EntryInterfaceModuleSetValueParamSchema,
                        _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._EntrySchema._EntryInterfaceModuleSetValueResultSchema,
                    ]: ...
                    @overload
                    def __getitem__(
                        self,
                        key: str,
                    ) -> _InterfaceMethod[_StructSchema, _StructSchema]: ...

                @property
                @override
                def methods(
                    self,
                ) -> _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._EntrySchema._Methods: ...

            @property
            @override
            def schema(self) -> schemas._StoreContainerEntrySchema: ...
            @override
            def _new_client(
                self,
                server: _DynamicCapabilityServer,
            ) -> clients.EntryClient: ...
            class Server(_DynamicCapabilityServer):
                def getKey(
                    self,
                    _context: contexts.GetkeyCallContext,
                    **kwargs: object,
                ) -> Awaitable[str | results_tuples.GetkeyResultTuple | None]: ...
                def getKey_context(
                    self,
                    context: contexts.GetkeyCallContext,
                ) -> Awaitable[None]: ...
                def getValue(
                    self,
                    _context: contexts.GetvalueCallContext,
                    **kwargs: object,
                ) -> Awaitable[results_tuples.GetvalueResultTuple | None]: ...
                def getValue_context(
                    self,
                    context: contexts.GetvalueCallContext,
                ) -> Awaitable[None]: ...
                def setValue(
                    self,
                    value: readers.ValueReader,
                    _context: contexts.SetvalueCallContext,
                    **kwargs: object,
                ) -> Awaitable[bool | results_tuples.SetvalueResultTuple | None]: ...
                def setValue_context(
                    self,
                    context: contexts.SetvalueCallContext,
                ) -> Awaitable[None]: ...

        Entry: _EntryInterfaceModule
        type EntryServer = (
            _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule.Server
        )
        class _KeyAndEntryStructModule(_StructModule):
            class Reader(_DynamicStructReader): ...
            class Builder(_DynamicStructBuilder): ...

            class _KeyAndEntrySchema(_StructSchema):
                class _EntryField(_StructSchemaField):
                    @property
                    @override
                    def schema(self) -> schemas._StoreContainerEntrySchema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["key"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["entry"],
                    ) -> _StoreInterfaceModule._ContainerInterfaceModule._KeyAndEntryStructModule._KeyAndEntrySchema._EntryField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _StoreInterfaceModule._ContainerInterfaceModule._KeyAndEntryStructModule._KeyAndEntrySchema._Fields: ...

            @property
            @override
            def schema(self) -> schemas._StoreContainerKeyAndEntrySchema: ...
            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
                key: str | None = None,
                entry: clients.EntryClient
                | _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule.Server
                | None = None,
                **kwargs: object,
            ) -> builders.KeyAndEntryBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[readers.KeyAndEntryReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[readers.KeyAndEntryReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[builders.KeyAndEntryBuilder]: ...
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
            ) -> readers.KeyAndEntryReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> readers.KeyAndEntryReader: ...

        KeyAndEntry: _KeyAndEntryStructModule

        class _ContainerSchema(_InterfaceSchema):
            class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

            class _IdentifiableInterfaceModuleInfoResultSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["name"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["description"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

            class _PersistentInterfaceModuleSaveParamSchema(_StructSchema):
                class _SealForField(_StructSchemaField):
                    @property
                    @override
                    def schema(self) -> _StructSchema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["sealFor"],
                    ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._PersistentInterfaceModuleSaveParamSchema._SealForField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._PersistentInterfaceModuleSaveParamSchema._Fields: ...

            class _PersistentInterfaceModuleSaveResultSchema(_StructSchema):
                class _SturdyRefField(_StructSchemaField):
                    @property
                    @override
                    def schema(self) -> _StructSchema: ...

                class _UnsaveSRField(_StructSchemaField):
                    @property
                    @override
                    def schema(self) -> _StructSchema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["sturdyRef"],
                    ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._PersistentInterfaceModuleSaveResultSchema._SturdyRefField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["unsaveSR"],
                    ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._PersistentInterfaceModuleSaveResultSchema._UnsaveSRField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._PersistentInterfaceModuleSaveResultSchema._Fields: ...

            class _ContainerInterfaceModuleExportParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleExportParamSchema._Fields: ...

            class _ContainerInterfaceModuleExportResultSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["json"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleExportResultSchema._Fields: ...

            class _ContainerInterfaceModuleDownloadEntriesParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleDownloadEntriesParamSchema._Fields: ...

            class _ContainerInterfaceModuleDownloadEntriesResultSchema(_StructSchema):
                class _EntriesField(_StructSchemaField):
                    class _Schema(_ListSchema):
                        @property
                        @override
                        def elementType(self) -> _StructSchema: ...

                    @property
                    @override
                    def schema(
                        self,
                    ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleDownloadEntriesResultSchema._EntriesField._Schema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["entries"],
                    ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleDownloadEntriesResultSchema._EntriesField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleDownloadEntriesResultSchema._Fields: ...

            class _ContainerInterfaceModuleListEntriesParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleListEntriesParamSchema._Fields: ...

            class _ContainerInterfaceModuleListEntriesResultSchema(_StructSchema):
                class _EntriesField(_StructSchemaField):
                    class _Schema(_ListSchema):
                        @property
                        @override
                        def elementType(
                            self,
                        ) -> schemas._StoreContainerKeyAndEntrySchema: ...

                    @property
                    @override
                    def schema(
                        self,
                    ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleListEntriesResultSchema._EntriesField._Schema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["entries"],
                    ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleListEntriesResultSchema._EntriesField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleListEntriesResultSchema._Fields: ...

            class _ContainerInterfaceModuleGetEntryParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["key"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleGetEntryParamSchema._Fields: ...

            class _ContainerInterfaceModuleGetEntryResultSchema(_StructSchema):
                class _EntryField(_StructSchemaField):
                    @property
                    @override
                    def schema(self) -> schemas._StoreContainerEntrySchema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["entry"],
                    ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleGetEntryResultSchema._EntryField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleGetEntryResultSchema._Fields: ...

            class _ContainerInterfaceModuleRemoveEntryParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["key"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleRemoveEntryParamSchema._Fields: ...

            class _ContainerInterfaceModuleRemoveEntryResultSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["success"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleRemoveEntryResultSchema._Fields: ...

            class _ContainerInterfaceModuleClearParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleClearParamSchema._Fields: ...

            class _ContainerInterfaceModuleClearResultSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["success"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleClearResultSchema._Fields: ...

            class _ContainerInterfaceModuleAddEntryParamSchema(_StructSchema):
                class _ValueField(_StructSchemaField):
                    @property
                    @override
                    def schema(self) -> schemas._StoreContainerEntryValueSchema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["key"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["value"],
                    ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleAddEntryParamSchema._ValueField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["replaceExisting"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleAddEntryParamSchema._Fields: ...

            class _ContainerInterfaceModuleAddEntryResultSchema(_StructSchema):
                class _EntryField(_StructSchemaField):
                    @property
                    @override
                    def schema(self) -> schemas._StoreContainerEntrySchema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["entry"],
                    ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleAddEntryResultSchema._EntryField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["success"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleAddEntryResultSchema._Fields: ...

            class _Methods(dict[str, _InterfaceMethod[_StructSchema, _StructSchema]]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["info"],
                ) -> _InterfaceMethod[
                    _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._IdentifiableInterfaceModuleInfoParamSchema,
                    _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._IdentifiableInterfaceModuleInfoResultSchema,
                ]: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["save"],
                ) -> _InterfaceMethod[
                    _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._PersistentInterfaceModuleSaveParamSchema,
                    _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._PersistentInterfaceModuleSaveResultSchema,
                ]: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["export"],
                ) -> _InterfaceMethod[
                    _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleExportParamSchema,
                    _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleExportResultSchema,
                ]: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["downloadEntries"],
                ) -> _InterfaceMethod[
                    _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleDownloadEntriesParamSchema,
                    _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleDownloadEntriesResultSchema,
                ]: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["listEntries"],
                ) -> _InterfaceMethod[
                    _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleListEntriesParamSchema,
                    _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleListEntriesResultSchema,
                ]: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["getEntry"],
                ) -> _InterfaceMethod[
                    _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleGetEntryParamSchema,
                    _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleGetEntryResultSchema,
                ]: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["removeEntry"],
                ) -> _InterfaceMethod[
                    _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleRemoveEntryParamSchema,
                    _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleRemoveEntryResultSchema,
                ]: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["clear"],
                ) -> _InterfaceMethod[
                    _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleClearParamSchema,
                    _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleClearResultSchema,
                ]: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["addEntry"],
                ) -> _InterfaceMethod[
                    _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleAddEntryParamSchema,
                    _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._ContainerInterfaceModuleAddEntryResultSchema,
                ]: ...
                @overload
                def __getitem__(
                    self,
                    key: str,
                ) -> _InterfaceMethod[_StructSchema, _StructSchema]: ...

            @property
            @override
            def methods(
                self,
            ) -> _StoreInterfaceModule._ContainerInterfaceModule._ContainerSchema._Methods: ...

        @property
        @override
        def schema(self) -> schemas._StoreContainerSchema: ...
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> clients.ContainerClient: ...
        class Server(
            _IdentifiableInterfaceModule.Server,
            _PersistentInterfaceModule.Server,
        ):
            def export(
                self,
                _context: contexts.ExportCallContext,
                **kwargs: object,
            ) -> Awaitable[str | results_tuples.ExportResultTuple | None]: ...
            def export_context(
                self,
                context: contexts.ExportCallContext,
            ) -> Awaitable[None]: ...
            def downloadEntries(
                self,
                _context: contexts.DownloadentriesCallContext,
                **kwargs: object,
            ) -> Awaitable[
                builders.PairListBuilder
                | readers.PairListReader
                | Sequence[Any]
                | results_tuples.DownloadentriesResultTuple
                | None
            ]: ...
            def downloadEntries_context(
                self,
                context: contexts.DownloadentriesCallContext,
            ) -> Awaitable[None]: ...
            def listEntries(
                self,
                _context: contexts.ListentriesCallContext,
                **kwargs: object,
            ) -> Awaitable[
                builders.KeyAndEntryListBuilder
                | readers.KeyAndEntryListReader
                | Sequence[Any]
                | results_tuples.ListentriesResultTuple
                | None
            ]: ...
            def listEntries_context(
                self,
                context: contexts.ListentriesCallContext,
            ) -> Awaitable[None]: ...
            def getEntry(
                self,
                key: str,
                _context: contexts.GetentryCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule.Server
                | clients.EntryClient
                | results_tuples.GetentryResultTuple
                | None
            ]: ...
            def getEntry_context(
                self,
                context: contexts.GetentryCallContext,
            ) -> Awaitable[None]: ...
            def removeEntry(
                self,
                key: str,
                _context: contexts.RemoveentryCallContext,
                **kwargs: object,
            ) -> Awaitable[bool | results_tuples.RemoveentryResultTuple | None]: ...
            def removeEntry_context(
                self,
                context: contexts.RemoveentryCallContext,
            ) -> Awaitable[None]: ...
            def clear(
                self,
                _context: contexts.ClearCallContext,
                **kwargs: object,
            ) -> Awaitable[bool | results_tuples.ClearResultTuple | None]: ...
            def clear_context(
                self,
                context: contexts.ClearCallContext,
            ) -> Awaitable[None]: ...
            def addEntry(
                self,
                key: str,
                value: readers.ValueReader,
                replaceExisting: bool,
                _context: contexts.AddentryCallContext,
                **kwargs: object,
            ) -> Awaitable[results_tuples.AddentryResultTuple | None]: ...
            def addEntry_context(
                self,
                context: contexts.AddentryCallContext,
            ) -> Awaitable[None]: ...

    Container: _ContainerInterfaceModule
    type ContainerServer = _StoreInterfaceModule._ContainerInterfaceModule.Server
    class _InfoAndContainerStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _InfoAndContainerSchema(_StructSchema):
            class _ContainerField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._StoreContainerSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["name"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["container"],
                ) -> _StoreInterfaceModule._InfoAndContainerStructModule._InfoAndContainerSchema._ContainerField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _StoreInterfaceModule._InfoAndContainerStructModule._InfoAndContainerSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._StoreInfoAndContainerSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            id: str | None = None,
            name: str | None = None,
            container: clients.ContainerClient
            | _StoreInterfaceModule._ContainerInterfaceModule.Server
            | None = None,
            **kwargs: object,
        ) -> builders.InfoAndContainerBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.InfoAndContainerReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.InfoAndContainerReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.InfoAndContainerBuilder]: ...
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
        ) -> readers.InfoAndContainerReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.InfoAndContainerReader: ...

    InfoAndContainer: _InfoAndContainerStructModule
    class _ImportExportDataStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _ImportExportDataSchema(_StructSchema):
            class _InfoField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _StructSchema: ...

            class _EntriesField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> _StructSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _StoreInterfaceModule._ImportExportDataStructModule._ImportExportDataSchema._EntriesField._Schema: ...

            class _IsAnyValueField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _ListSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["info"],
                ) -> _StoreInterfaceModule._ImportExportDataStructModule._ImportExportDataSchema._InfoField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["entries"],
                ) -> _StoreInterfaceModule._ImportExportDataStructModule._ImportExportDataSchema._EntriesField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["isAnyValue"],
                ) -> _StoreInterfaceModule._ImportExportDataStructModule._ImportExportDataSchema._IsAnyValueField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _StoreInterfaceModule._ImportExportDataStructModule._ImportExportDataSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._StoreImportExportDataSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            info: IdInformationBuilder | dict[str, Any] | None = None,
            entries: builders.PairListBuilder | dict[str, Any] | None = None,
            isAnyValue: builders.BoolListBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> builders.ImportExportDataBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.ImportExportDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.ImportExportDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.ImportExportDataBuilder]: ...
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
        ) -> readers.ImportExportDataReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.ImportExportDataReader: ...

    ImportExportData: _ImportExportDataStructModule

    class _StoreSchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _StoreInterfaceModule._StoreSchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

        class _IdentifiableInterfaceModuleInfoResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["name"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["description"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _StoreInterfaceModule._StoreSchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

        class _PersistentInterfaceModuleSaveParamSchema(_StructSchema):
            class _SealForField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _StructSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["sealFor"],
                ) -> _StoreInterfaceModule._StoreSchema._PersistentInterfaceModuleSaveParamSchema._SealForField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _StoreInterfaceModule._StoreSchema._PersistentInterfaceModuleSaveParamSchema._Fields: ...

        class _PersistentInterfaceModuleSaveResultSchema(_StructSchema):
            class _SturdyRefField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _StructSchema: ...

            class _UnsaveSRField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _StructSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["sturdyRef"],
                ) -> _StoreInterfaceModule._StoreSchema._PersistentInterfaceModuleSaveResultSchema._SturdyRefField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["unsaveSR"],
                ) -> _StoreInterfaceModule._StoreSchema._PersistentInterfaceModuleSaveResultSchema._UnsaveSRField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _StoreInterfaceModule._StoreSchema._PersistentInterfaceModuleSaveResultSchema._Fields: ...

        class _StoreInterfaceModuleNewContainerParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["name"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["description"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _StoreInterfaceModule._StoreSchema._StoreInterfaceModuleNewContainerParamSchema._Fields: ...

        class _StoreInterfaceModuleNewContainerResultSchema(_StructSchema):
            class _ContainerField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._StoreContainerSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["container"],
                ) -> _StoreInterfaceModule._StoreSchema._StoreInterfaceModuleNewContainerResultSchema._ContainerField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _StoreInterfaceModule._StoreSchema._StoreInterfaceModuleNewContainerResultSchema._Fields: ...

        class _StoreInterfaceModuleContainerWithIdParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _StoreInterfaceModule._StoreSchema._StoreInterfaceModuleContainerWithIdParamSchema._Fields: ...

        class _StoreInterfaceModuleContainerWithIdResultSchema(_StructSchema):
            class _ContainerField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._StoreContainerSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["container"],
                ) -> _StoreInterfaceModule._StoreSchema._StoreInterfaceModuleContainerWithIdResultSchema._ContainerField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _StoreInterfaceModule._StoreSchema._StoreInterfaceModuleContainerWithIdResultSchema._Fields: ...

        class _StoreInterfaceModuleListContainersParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _StoreInterfaceModule._StoreSchema._StoreInterfaceModuleListContainersParamSchema._Fields: ...

        class _StoreInterfaceModuleListContainersResultSchema(_StructSchema):
            class _ContainersField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> schemas._StoreInfoAndContainerSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _StoreInterfaceModule._StoreSchema._StoreInterfaceModuleListContainersResultSchema._ContainersField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["containers"],
                ) -> _StoreInterfaceModule._StoreSchema._StoreInterfaceModuleListContainersResultSchema._ContainersField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _StoreInterfaceModule._StoreSchema._StoreInterfaceModuleListContainersResultSchema._Fields: ...

        class _StoreInterfaceModuleRemoveContainerParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _StoreInterfaceModule._StoreSchema._StoreInterfaceModuleRemoveContainerParamSchema._Fields: ...

        class _StoreInterfaceModuleRemoveContainerResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["success"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _StoreInterfaceModule._StoreSchema._StoreInterfaceModuleRemoveContainerResultSchema._Fields: ...

        class _StoreInterfaceModuleImportContainerParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["json"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _StoreInterfaceModule._StoreSchema._StoreInterfaceModuleImportContainerParamSchema._Fields: ...

        class _StoreInterfaceModuleImportContainerResultSchema(_StructSchema):
            class _ContainerField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._StoreContainerSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["container"],
                ) -> _StoreInterfaceModule._StoreSchema._StoreInterfaceModuleImportContainerResultSchema._ContainerField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _StoreInterfaceModule._StoreSchema._StoreInterfaceModuleImportContainerResultSchema._Fields: ...

        class _Methods(dict[str, _InterfaceMethod[_StructSchema, _StructSchema]]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _InterfaceMethod[
                _StoreInterfaceModule._StoreSchema._IdentifiableInterfaceModuleInfoParamSchema,
                _StoreInterfaceModule._StoreSchema._IdentifiableInterfaceModuleInfoResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["save"],
            ) -> _InterfaceMethod[
                _StoreInterfaceModule._StoreSchema._PersistentInterfaceModuleSaveParamSchema,
                _StoreInterfaceModule._StoreSchema._PersistentInterfaceModuleSaveResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["newContainer"],
            ) -> _InterfaceMethod[
                _StoreInterfaceModule._StoreSchema._StoreInterfaceModuleNewContainerParamSchema,
                _StoreInterfaceModule._StoreSchema._StoreInterfaceModuleNewContainerResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["containerWithId"],
            ) -> _InterfaceMethod[
                _StoreInterfaceModule._StoreSchema._StoreInterfaceModuleContainerWithIdParamSchema,
                _StoreInterfaceModule._StoreSchema._StoreInterfaceModuleContainerWithIdResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["listContainers"],
            ) -> _InterfaceMethod[
                _StoreInterfaceModule._StoreSchema._StoreInterfaceModuleListContainersParamSchema,
                _StoreInterfaceModule._StoreSchema._StoreInterfaceModuleListContainersResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["removeContainer"],
            ) -> _InterfaceMethod[
                _StoreInterfaceModule._StoreSchema._StoreInterfaceModuleRemoveContainerParamSchema,
                _StoreInterfaceModule._StoreSchema._StoreInterfaceModuleRemoveContainerResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["importContainer"],
            ) -> _InterfaceMethod[
                _StoreInterfaceModule._StoreSchema._StoreInterfaceModuleImportContainerParamSchema,
                _StoreInterfaceModule._StoreSchema._StoreInterfaceModuleImportContainerResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: str,
            ) -> _InterfaceMethod[_StructSchema, _StructSchema]: ...

        @property
        @override
        def methods(self) -> _StoreInterfaceModule._StoreSchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._StoreSchema: ...
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> clients.StoreClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def newContainer(
            self,
            name: str,
            description: str,
            _context: contexts.NewcontainerCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _StoreInterfaceModule._ContainerInterfaceModule.Server
            | clients.ContainerClient
            | results_tuples.NewcontainerResultTuple
            | None
        ]: ...
        def newContainer_context(
            self,
            context: contexts.NewcontainerCallContext,
        ) -> Awaitable[None]: ...
        def containerWithId(
            self,
            id: str,
            _context: contexts.ContainerwithidCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _StoreInterfaceModule._ContainerInterfaceModule.Server
            | clients.ContainerClient
            | results_tuples.ContainerwithidResultTuple
            | None
        ]: ...
        def containerWithId_context(
            self,
            context: contexts.ContainerwithidCallContext,
        ) -> Awaitable[None]: ...
        def listContainers(
            self,
            _context: contexts.ListcontainersCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.InfoAndContainerListBuilder
            | readers.InfoAndContainerListReader
            | Sequence[Any]
            | results_tuples.ListcontainersResultTuple
            | None
        ]: ...
        def listContainers_context(
            self,
            context: contexts.ListcontainersCallContext,
        ) -> Awaitable[None]: ...
        def removeContainer(
            self,
            id: str,
            _context: contexts.RemovecontainerCallContext,
            **kwargs: object,
        ) -> Awaitable[bool | results_tuples.RemovecontainerResultTuple | None]: ...
        def removeContainer_context(
            self,
            context: contexts.RemovecontainerCallContext,
        ) -> Awaitable[None]: ...
        def importContainer(
            self,
            json: str,
            _context: contexts.ImportcontainerCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _StoreInterfaceModule._ContainerInterfaceModule.Server
            | clients.ContainerClient
            | results_tuples.ImportcontainerResultTuple
            | None
        ]: ...
        def importContainer_context(
            self,
            context: contexts.ImportcontainerCallContext,
        ) -> Awaitable[None]: ...
