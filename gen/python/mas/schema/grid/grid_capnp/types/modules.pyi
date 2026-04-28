"""Module helper types for `grid.capnp`."""

from collections.abc import Awaitable, Callable, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _EnumModule,
    _EnumSchema,
    _InterfaceMethod,
    _InterfaceModule,
    _InterfaceSchema,
    _ListSchema,
    _StructModule,
    _StructSchema,
    _StructSchemaField,
)

from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.geo.geo_capnp.types import schemas as _mas_schema_geo_geo_capnp_schemas
from mas.schema.geo.geo_capnp.types.builders import LatLonCoordBuilder
from mas.schema.geo.geo_capnp.types.readers import LatLonCoordReader
from mas.schema.grid.grid_capnp.types import builders as builders
from mas.schema.grid.grid_capnp.types import clients as clients
from mas.schema.grid.grid_capnp.types import contexts as contexts
from mas.schema.grid.grid_capnp.types import enums as enums
from mas.schema.grid.grid_capnp.types import readers as readers
from mas.schema.grid.grid_capnp.types import schemas as schemas
from mas.schema.grid.grid_capnp.types import servers as servers
from mas.schema.grid.grid_capnp.types.results import tuples as results_tuples
from mas.schema.persistence.persistence_capnp.types import (
    schemas as _mas_schema_persistence_persistence_capnp_schemas,
)
from mas.schema.persistence.persistence_capnp.types.modules import (
    _PersistentInterfaceModule,
)

class _AggregationEnumModule(_EnumModule):
    none: int
    wAvg: int
    wMedian: int
    min: int
    max: int
    sum: int
    iAvg: int
    iMedian: int
    avg: int
    median: int
    wSum: int
    iSum: int
    wMin: int
    iMin: int
    wMax: int
    iMax: int

    class _AggregationSchema(_EnumSchema): ...

    @property
    @override
    def schema(self) -> schemas._AggregationEnumSchema: ...

class _GridInterfaceModule(_IdentifiableInterfaceModule, _PersistentInterfaceModule):
    class _ValueStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _ValueSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["f"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["i"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["ui"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["no"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _GridInterfaceModule._ValueStructModule._ValueSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._GridValueSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            f: float | None = None,
            i: int | None = None,
            ui: int | None = None,
            no: bool | None = None,
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
    class _ResolutionStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _ResolutionSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["meter"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["degree"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> (
                _GridInterfaceModule._ResolutionStructModule._ResolutionSchema._Fields
            ): ...

        @property
        @override
        def schema(self) -> schemas._GridResolutionSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            meter: int | None = None,
            degree: float | None = None,
            **kwargs: object,
        ) -> builders.ResolutionBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.ResolutionReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.ResolutionReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.ResolutionBuilder]: ...
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
        ) -> readers.ResolutionReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.ResolutionReader: ...

    Resolution: _ResolutionStructModule
    class _RowColStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _RowColSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["row"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["col"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _GridInterfaceModule._RowColStructModule._RowColSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._GridRowColSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            row: int | None = None,
            col: int | None = None,
            **kwargs: object,
        ) -> builders.RowColBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.RowColReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.RowColReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.RowColBuilder]: ...
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
        ) -> readers.RowColReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.RowColReader: ...

    RowCol: _RowColStructModule
    class _AggregationPartStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _AggregationPartSchema(_StructSchema):
            class _ValueField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._GridValueSchema: ...

            class _RowColField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._GridRowColSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["value"],
                ) -> _GridInterfaceModule._AggregationPartStructModule._AggregationPartSchema._ValueField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["rowCol"],
                ) -> _GridInterfaceModule._AggregationPartStructModule._AggregationPartSchema._RowColField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["areaFrac"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["iValue"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _GridInterfaceModule._AggregationPartStructModule._AggregationPartSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._GridAggregationPartSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            value: builders.ValueBuilder | dict[str, Any] | None = None,
            rowCol: builders.RowColBuilder | dict[str, Any] | None = None,
            areaFrac: float | None = None,
            iValue: float | None = None,
            **kwargs: object,
        ) -> builders.AggregationPartBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.AggregationPartReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.AggregationPartReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.AggregationPartBuilder]: ...
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
        ) -> readers.AggregationPartReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.AggregationPartReader: ...

    AggregationPart: _AggregationPartStructModule
    class _LocationStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _LocationSchema(_StructSchema):
            class _LatLonCoordField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_geo_geo_capnp_schemas._LatLonCoordSchema: ...

            class _RowColField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._GridRowColSchema: ...

            class _ValueField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._GridValueSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["latLonCoord"],
                ) -> _GridInterfaceModule._LocationStructModule._LocationSchema._LatLonCoordField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["rowCol"],
                ) -> _GridInterfaceModule._LocationStructModule._LocationSchema._RowColField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["value"],
                ) -> _GridInterfaceModule._LocationStructModule._LocationSchema._ValueField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _GridInterfaceModule._LocationStructModule._LocationSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._GridLocationSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            latLonCoord: LatLonCoordBuilder | dict[str, Any] | None = None,
            rowCol: builders.RowColBuilder | dict[str, Any] | None = None,
            value: builders.ValueBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> builders.LocationBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.LocationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.LocationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.LocationBuilder]: ...
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
        ) -> readers.LocationReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.LocationReader: ...

    Location: _LocationStructModule
    class _CallbackInterfaceModule(_InterfaceModule):
        class _CallbackSchema(_InterfaceSchema):
            class _CallbackInterfaceModuleSendCellsParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["maxCount"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _GridInterfaceModule._CallbackInterfaceModule._CallbackSchema._CallbackInterfaceModuleSendCellsParamSchema._Fields: ...

            class _CallbackInterfaceModuleSendCellsResultSchema(_StructSchema):
                class _LocationsField(_StructSchemaField):
                    class _Schema(_ListSchema):
                        @property
                        @override
                        def elementType(self) -> schemas._GridLocationSchema: ...

                    @property
                    @override
                    def schema(
                        self,
                    ) -> _GridInterfaceModule._CallbackInterfaceModule._CallbackSchema._CallbackInterfaceModuleSendCellsResultSchema._LocationsField._Schema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["locations"],
                    ) -> _GridInterfaceModule._CallbackInterfaceModule._CallbackSchema._CallbackInterfaceModuleSendCellsResultSchema._LocationsField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _GridInterfaceModule._CallbackInterfaceModule._CallbackSchema._CallbackInterfaceModuleSendCellsResultSchema._Fields: ...

            class _CallbackInterfaceModuleSendCellsMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _GridInterfaceModule._CallbackInterfaceModule._CallbackSchema._CallbackInterfaceModuleSendCellsParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _GridInterfaceModule._CallbackInterfaceModule._CallbackSchema._CallbackInterfaceModuleSendCellsResultSchema: ...

            class _Methods(dict[str, _InterfaceMethod]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["sendCells"],
                ) -> _GridInterfaceModule._CallbackInterfaceModule._CallbackSchema._CallbackInterfaceModuleSendCellsMethod: ...
                @overload
                def __getitem__(self, key: str) -> _InterfaceMethod: ...

            @property
            @override
            def methods(
                self,
            ) -> (
                _GridInterfaceModule._CallbackInterfaceModule._CallbackSchema._Methods
            ): ...

        @property
        @override
        def schema(self) -> schemas._GridCallbackSchema: ...
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> clients.CallbackClient: ...
        class Server(_DynamicCapabilityServer):
            def sendCells(
                self,
                maxCount: int,
                _context: contexts.SendcellsCallContext,
                **kwargs: object,
            ) -> Awaitable[
                builders.LocationListBuilder
                | readers.LocationListReader
                | Sequence[Any]
                | results_tuples.SendcellsResultTuple
                | None
            ]: ...
            def sendCells_context(
                self,
                context: contexts.SendcellsCallContext,
            ) -> Awaitable[None]: ...

    Callback: _CallbackInterfaceModule
    type CallbackServer = _GridInterfaceModule._CallbackInterfaceModule.Server

    class _GridSchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _GridInterfaceModule._GridSchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

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
            ) -> _GridInterfaceModule._GridSchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

        class _IdentifiableInterfaceModuleInfoMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _GridInterfaceModule._GridSchema._IdentifiableInterfaceModuleInfoParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _GridInterfaceModule._GridSchema._IdentifiableInterfaceModuleInfoResultSchema: ...

        class _PersistentInterfaceModuleSaveParamSchema(_StructSchema):
            class _SealForField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_persistence_persistence_capnp_schemas._SturdyRefOwnerSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["sealFor"],
                ) -> _GridInterfaceModule._GridSchema._PersistentInterfaceModuleSaveParamSchema._SealForField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _GridInterfaceModule._GridSchema._PersistentInterfaceModuleSaveParamSchema._Fields: ...

        class _PersistentInterfaceModuleSaveResultSchema(_StructSchema):
            class _SturdyRefField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> (
                    _mas_schema_persistence_persistence_capnp_schemas._SturdyRefSchema
                ): ...

            class _UnsaveSRField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> (
                    _mas_schema_persistence_persistence_capnp_schemas._SturdyRefSchema
                ): ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["sturdyRef"],
                ) -> _GridInterfaceModule._GridSchema._PersistentInterfaceModuleSaveResultSchema._SturdyRefField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["unsaveSR"],
                ) -> _GridInterfaceModule._GridSchema._PersistentInterfaceModuleSaveResultSchema._UnsaveSRField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _GridInterfaceModule._GridSchema._PersistentInterfaceModuleSaveResultSchema._Fields: ...

        class _PersistentInterfaceModuleSaveMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _GridInterfaceModule._GridSchema._PersistentInterfaceModuleSaveParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _GridInterfaceModule._GridSchema._PersistentInterfaceModuleSaveResultSchema: ...

        class _GridInterfaceModuleClosestValueAtParamSchema(_StructSchema):
            class _LatlonCoordField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_geo_geo_capnp_schemas._LatLonCoordSchema: ...

            class _ResolutionField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._GridResolutionSchema: ...

            class _AggField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._AggregationEnumSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["latlonCoord"],
                ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleClosestValueAtParamSchema._LatlonCoordField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["ignoreNoData"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["resolution"],
                ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleClosestValueAtParamSchema._ResolutionField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["agg"],
                ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleClosestValueAtParamSchema._AggField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["returnRowCols"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["includeAggParts"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleClosestValueAtParamSchema._Fields: ...

        class _GridInterfaceModuleClosestValueAtResultSchema(_StructSchema):
            class _ValField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._GridValueSchema: ...

            class _TlField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._GridRowColSchema: ...

            class _BrField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._GridRowColSchema: ...

            class _AggPartsField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> schemas._GridAggregationPartSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleClosestValueAtResultSchema._AggPartsField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["val"],
                ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleClosestValueAtResultSchema._ValField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["tl"],
                ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleClosestValueAtResultSchema._TlField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["br"],
                ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleClosestValueAtResultSchema._BrField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["aggParts"],
                ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleClosestValueAtResultSchema._AggPartsField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleClosestValueAtResultSchema._Fields: ...

        class _GridInterfaceModuleClosestValueAtMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleClosestValueAtParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleClosestValueAtResultSchema: ...

        class _GridInterfaceModuleResolutionParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleResolutionParamSchema._Fields: ...

        class _GridInterfaceModuleResolutionResultSchema(_StructSchema):
            class _ResField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._GridResolutionSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["res"],
                ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleResolutionResultSchema._ResField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleResolutionResultSchema._Fields: ...

        class _GridInterfaceModuleResolutionMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleResolutionParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleResolutionResultSchema: ...

        class _GridInterfaceModuleDimensionParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleDimensionParamSchema._Fields: ...

        class _GridInterfaceModuleDimensionResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["rows"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["cols"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleDimensionResultSchema._Fields: ...

        class _GridInterfaceModuleDimensionMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleDimensionParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleDimensionResultSchema: ...

        class _GridInterfaceModuleNoDataValueParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleNoDataValueParamSchema._Fields: ...

        class _GridInterfaceModuleNoDataValueResultSchema(_StructSchema):
            class _NodataField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._GridValueSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["nodata"],
                ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleNoDataValueResultSchema._NodataField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleNoDataValueResultSchema._Fields: ...

        class _GridInterfaceModuleNoDataValueMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleNoDataValueParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleNoDataValueResultSchema: ...

        class _GridInterfaceModuleValueAtParamSchema(_StructSchema):
            class _ResolutionField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._GridResolutionSchema: ...

            class _AggField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._AggregationEnumSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["row"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["col"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["resolution"],
                ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleValueAtParamSchema._ResolutionField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["agg"],
                ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleValueAtParamSchema._AggField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["includeAggParts"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleValueAtParamSchema._Fields: ...

        class _GridInterfaceModuleValueAtResultSchema(_StructSchema):
            class _ValField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._GridValueSchema: ...

            class _AggPartsField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> schemas._GridAggregationPartSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleValueAtResultSchema._AggPartsField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["val"],
                ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleValueAtResultSchema._ValField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["aggParts"],
                ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleValueAtResultSchema._AggPartsField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleValueAtResultSchema._Fields: ...

        class _GridInterfaceModuleValueAtMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> (
                _GridInterfaceModule._GridSchema._GridInterfaceModuleValueAtParamSchema
            ): ...
            @property
            @override
            def result_type(
                self,
            ) -> (
                _GridInterfaceModule._GridSchema._GridInterfaceModuleValueAtResultSchema
            ): ...

        class _GridInterfaceModuleLatLonBoundsParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["useCellCenter"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleLatLonBoundsParamSchema._Fields: ...

        class _GridInterfaceModuleLatLonBoundsResultSchema(_StructSchema):
            class _TlField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_geo_geo_capnp_schemas._LatLonCoordSchema: ...

            class _TrField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_geo_geo_capnp_schemas._LatLonCoordSchema: ...

            class _BrField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_geo_geo_capnp_schemas._LatLonCoordSchema: ...

            class _BlField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_geo_geo_capnp_schemas._LatLonCoordSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["tl"],
                ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleLatLonBoundsResultSchema._TlField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["tr"],
                ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleLatLonBoundsResultSchema._TrField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["br"],
                ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleLatLonBoundsResultSchema._BrField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["bl"],
                ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleLatLonBoundsResultSchema._BlField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleLatLonBoundsResultSchema._Fields: ...

        class _GridInterfaceModuleLatLonBoundsMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleLatLonBoundsParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleLatLonBoundsResultSchema: ...

        class _GridInterfaceModuleStreamCellsParamSchema(_StructSchema):
            class _TopLeftField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._GridRowColSchema: ...

            class _BottomRightField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._GridRowColSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["topLeft"],
                ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleStreamCellsParamSchema._TopLeftField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["bottomRight"],
                ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleStreamCellsParamSchema._BottomRightField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleStreamCellsParamSchema._Fields: ...

        class _GridInterfaceModuleStreamCellsResultSchema(_StructSchema):
            class _CallbackField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._GridCallbackSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["callback"],
                ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleStreamCellsResultSchema._CallbackField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleStreamCellsResultSchema._Fields: ...

        class _GridInterfaceModuleStreamCellsMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleStreamCellsParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleStreamCellsResultSchema: ...

        class _GridInterfaceModuleUnitParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleUnitParamSchema._Fields: ...

        class _GridInterfaceModuleUnitResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["unit"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleUnitResultSchema._Fields: ...

        class _GridInterfaceModuleUnitMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> (
                _GridInterfaceModule._GridSchema._GridInterfaceModuleUnitParamSchema
            ): ...
            @property
            @override
            def result_type(
                self,
            ) -> (
                _GridInterfaceModule._GridSchema._GridInterfaceModuleUnitResultSchema
            ): ...

        class _Methods(dict[str, _InterfaceMethod]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> (
                _GridInterfaceModule._GridSchema._IdentifiableInterfaceModuleInfoMethod
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["save"],
            ) -> (
                _GridInterfaceModule._GridSchema._PersistentInterfaceModuleSaveMethod
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["closestValueAt"],
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleClosestValueAtMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["resolution"],
            ) -> (
                _GridInterfaceModule._GridSchema._GridInterfaceModuleResolutionMethod
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["dimension"],
            ) -> (
                _GridInterfaceModule._GridSchema._GridInterfaceModuleDimensionMethod
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["noDataValue"],
            ) -> (
                _GridInterfaceModule._GridSchema._GridInterfaceModuleNoDataValueMethod
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["valueAt"],
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleValueAtMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["latLonBounds"],
            ) -> (
                _GridInterfaceModule._GridSchema._GridInterfaceModuleLatLonBoundsMethod
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["streamCells"],
            ) -> (
                _GridInterfaceModule._GridSchema._GridInterfaceModuleStreamCellsMethod
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["unit"],
            ) -> _GridInterfaceModule._GridSchema._GridInterfaceModuleUnitMethod: ...
            @overload
            def __getitem__(self, key: str) -> _InterfaceMethod: ...

        @property
        @override
        def methods(self) -> _GridInterfaceModule._GridSchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._GridSchema: ...
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> clients.GridClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def closestValueAt(
            self,
            latlonCoord: LatLonCoordReader,
            ignoreNoData: bool,
            resolution: readers.ResolutionReader,
            agg: enums.AggregationEnum,
            returnRowCols: bool,
            includeAggParts: bool,
            _context: contexts.ClosestvalueatCallContext,
            **kwargs: object,
        ) -> Awaitable[results_tuples.ClosestvalueatResultTuple | None]: ...
        def closestValueAt_context(
            self,
            context: contexts.ClosestvalueatCallContext,
        ) -> Awaitable[None]: ...
        def resolution(
            self,
            _context: contexts.ResolutionCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.ResolutionBuilder
            | readers.ResolutionReader
            | dict[str, Any]
            | results_tuples.ResolutionResultTuple
            | None
        ]: ...
        def resolution_context(
            self,
            context: contexts.ResolutionCallContext,
        ) -> Awaitable[None]: ...
        def dimension(
            self,
            _context: contexts.DimensionCallContext,
            **kwargs: object,
        ) -> Awaitable[results_tuples.DimensionResultTuple | None]: ...
        def dimension_context(
            self,
            context: contexts.DimensionCallContext,
        ) -> Awaitable[None]: ...
        def noDataValue(
            self,
            _context: contexts.NodatavalueCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.ValueBuilder
            | readers.ValueReader
            | dict[str, Any]
            | results_tuples.NodatavalueResultTuple
            | None
        ]: ...
        def noDataValue_context(
            self,
            context: contexts.NodatavalueCallContext,
        ) -> Awaitable[None]: ...
        def valueAt(
            self,
            row: int,
            col: int,
            resolution: readers.ResolutionReader,
            agg: enums.AggregationEnum,
            includeAggParts: bool,
            _context: contexts.ValueatCallContext,
            **kwargs: object,
        ) -> Awaitable[results_tuples.ValueatResultTuple | None]: ...
        def valueAt_context(
            self,
            context: contexts.ValueatCallContext,
        ) -> Awaitable[None]: ...
        def latLonBounds(
            self,
            useCellCenter: bool,
            _context: contexts.LatlonboundsCallContext,
            **kwargs: object,
        ) -> Awaitable[results_tuples.LatlonboundsResultTuple | None]: ...
        def latLonBounds_context(
            self,
            context: contexts.LatlonboundsCallContext,
        ) -> Awaitable[None]: ...
        def streamCells(
            self,
            topLeft: readers.RowColReader,
            bottomRight: readers.RowColReader,
            _context: contexts.StreamcellsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _GridInterfaceModule._CallbackInterfaceModule.Server
            | clients.CallbackClient
            | results_tuples.StreamcellsResultTuple
            | None
        ]: ...
        def streamCells_context(
            self,
            context: contexts.StreamcellsCallContext,
        ) -> Awaitable[None]: ...
        def unit(
            self,
            _context: contexts.UnitCallContext,
            **kwargs: object,
        ) -> Awaitable[str | results_tuples.UnitResultTuple | None]: ...
        def unit_context(
            self,
            context: contexts.UnitCallContext,
        ) -> Awaitable[None]: ...
