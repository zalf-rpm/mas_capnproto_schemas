"""Module helper types for `climate.capnp`."""

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

from mas.schema.climate.climate_capnp.types import builders as builders
from mas.schema.climate.climate_capnp.types import clients as clients
from mas.schema.climate.climate_capnp.types import common as common
from mas.schema.climate.climate_capnp.types import contexts as contexts
from mas.schema.climate.climate_capnp.types import enums as enums
from mas.schema.climate.climate_capnp.types import readers as readers
from mas.schema.climate.climate_capnp.types import schemas as schemas
from mas.schema.climate.climate_capnp.types import servers as servers
from mas.schema.climate.climate_capnp.types.results import tuples as results_tuples
from mas.schema.common.common_capnp.types import (
    schemas as _mas_schema_common_common_capnp_schemas,
)
from mas.schema.common.common_capnp.types.builders import IdInformationBuilder
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.common.date_capnp.types import (
    schemas as _mas_schema_common_date_capnp_schemas,
)
from mas.schema.common.date_capnp.types.builders import DateBuilder
from mas.schema.common.date_capnp.types.readers import DateReader
from mas.schema.geo.geo_capnp.types import schemas as _mas_schema_geo_geo_capnp_schemas
from mas.schema.geo.geo_capnp.types.builders import LatLonCoordBuilder
from mas.schema.geo.geo_capnp.types.readers import LatLonCoordReader
from mas.schema.persistence.persistence_capnp.types import (
    schemas as _mas_schema_persistence_persistence_capnp_schemas,
)
from mas.schema.persistence.persistence_capnp.types.modules import (
    _PersistentInterfaceModule,
)

class _GCMEnumModule(_EnumModule):
    cccmaCanEsm2: int
    ichecEcEarth: int
    ipslIpslCm5AMr: int
    mirocMiroc5: int
    mpiMMpiEsmLr: int
    gfdlEsm4: int
    ipslCm6aLr: int
    mpiEsm12Hr: int
    mriEsm20: int
    ukesm10Ll: int
    gswp3W5E5: int
    mohcHadGem2Es: int

    class _GCMSchema(_EnumSchema): ...

    @property
    @override
    def schema(self) -> schemas._GCMEnumSchema: ...

class _RCMEnumModule(_EnumModule):
    clmcomCclm4817: int
    gericsRemo2015: int
    knmiRacmo22E: int
    smhiRca4: int
    clmcomBtuCclm4817: int
    mpiCscRemo2009: int
    uhohWrf361H: int

    class _RCMSchema(_EnumSchema): ...

    @property
    @override
    def schema(self) -> schemas._RCMEnumSchema: ...

class _SSPEnumModule(_EnumModule):
    ssp1: int
    ssp2: int
    ssp3: int
    ssp4: int
    ssp5: int

    class _SSPSchema(_EnumSchema): ...

    @property
    @override
    def schema(self) -> schemas._SSPEnumSchema: ...

class _RCPEnumModule(_EnumModule):
    rcp19: int
    rcp26: int
    rcp34: int
    rcp45: int
    rcp60: int
    rcp70: int
    rcp85: int

    class _RCPSchema(_EnumSchema): ...

    @property
    @override
    def schema(self) -> schemas._RCPEnumSchema: ...

class _EnsembleMemberStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _EnsembleMemberSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["r"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["i"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["p"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["f"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _EnsembleMemberStructModule._EnsembleMemberSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._EnsembleMemberSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        r: int | None = None,
        i: int | None = None,
        p: int | None = None,
        f: int | None = None,
        **kwargs: object,
    ) -> builders.EnsembleMemberBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.EnsembleMemberReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.EnsembleMemberReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.EnsembleMemberBuilder]: ...
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
    ) -> readers.EnsembleMemberReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.EnsembleMemberReader: ...

class _MetadataStructModule(_StructModule):
    class _SupportedInterfaceModule(_InterfaceModule):
        class _SupportedSchema(_InterfaceSchema):
            class _SupportedInterfaceModuleCategoriesParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _MetadataStructModule._SupportedInterfaceModule._SupportedSchema._SupportedInterfaceModuleCategoriesParamSchema._Fields: ...

            class _SupportedInterfaceModuleCategoriesResultSchema(_StructSchema):
                class _TypesField(_StructSchemaField):
                    class _Schema(_ListSchema):
                        @property
                        @override
                        def elementType(
                            self,
                        ) -> (
                            _mas_schema_common_common_capnp_schemas._IdInformationSchema
                        ): ...

                    @property
                    @override
                    def schema(
                        self,
                    ) -> _MetadataStructModule._SupportedInterfaceModule._SupportedSchema._SupportedInterfaceModuleCategoriesResultSchema._TypesField._Schema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["types"],
                    ) -> _MetadataStructModule._SupportedInterfaceModule._SupportedSchema._SupportedInterfaceModuleCategoriesResultSchema._TypesField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _MetadataStructModule._SupportedInterfaceModule._SupportedSchema._SupportedInterfaceModuleCategoriesResultSchema._Fields: ...

            class _SupportedInterfaceModuleSupportedValuesParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["typeId"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _MetadataStructModule._SupportedInterfaceModule._SupportedSchema._SupportedInterfaceModuleSupportedValuesParamSchema._Fields: ...

            class _SupportedInterfaceModuleSupportedValuesResultSchema(_StructSchema):
                class _ValuesField(_StructSchemaField):
                    class _Schema(_ListSchema):
                        @property
                        @override
                        def elementType(
                            self,
                        ) -> (
                            _mas_schema_common_common_capnp_schemas._IdInformationSchema
                        ): ...

                    @property
                    @override
                    def schema(
                        self,
                    ) -> _MetadataStructModule._SupportedInterfaceModule._SupportedSchema._SupportedInterfaceModuleSupportedValuesResultSchema._ValuesField._Schema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["values"],
                    ) -> _MetadataStructModule._SupportedInterfaceModule._SupportedSchema._SupportedInterfaceModuleSupportedValuesResultSchema._ValuesField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _MetadataStructModule._SupportedInterfaceModule._SupportedSchema._SupportedInterfaceModuleSupportedValuesResultSchema._Fields: ...

            class _Methods(dict[str, _InterfaceMethod[_StructSchema, _StructSchema]]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["categories"],
                ) -> _InterfaceMethod[
                    _MetadataStructModule._SupportedInterfaceModule._SupportedSchema._SupportedInterfaceModuleCategoriesParamSchema,
                    _MetadataStructModule._SupportedInterfaceModule._SupportedSchema._SupportedInterfaceModuleCategoriesResultSchema,
                ]: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["supportedValues"],
                ) -> _InterfaceMethod[
                    _MetadataStructModule._SupportedInterfaceModule._SupportedSchema._SupportedInterfaceModuleSupportedValuesParamSchema,
                    _MetadataStructModule._SupportedInterfaceModule._SupportedSchema._SupportedInterfaceModuleSupportedValuesResultSchema,
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
            ) -> _MetadataStructModule._SupportedInterfaceModule._SupportedSchema._Methods: ...

        @property
        @override
        def schema(self) -> schemas._MetadataSupportedSchema: ...
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> clients.SupportedClient: ...
        class Server(_DynamicCapabilityServer):
            def categories(
                self,
                _context: contexts.CategoriesCallContext,
                **kwargs: object,
            ) -> Awaitable[
                builders.IdInformationListBuilder
                | readers.IdInformationListReader
                | Sequence[Any]
                | results_tuples.CategoriesResultTuple
                | None
            ]: ...
            def categories_context(
                self,
                context: contexts.CategoriesCallContext,
            ) -> Awaitable[None]: ...
            def supportedValues(
                self,
                typeId: str,
                _context: contexts.SupportedvaluesCallContext,
                **kwargs: object,
            ) -> Awaitable[
                builders.IdInformationListBuilder
                | readers.IdInformationListReader
                | Sequence[Any]
                | results_tuples.SupportedvaluesResultTuple
                | None
            ]: ...
            def supportedValues_context(
                self,
                context: contexts.SupportedvaluesCallContext,
            ) -> Awaitable[None]: ...

    Supported: _SupportedInterfaceModule
    type SupportedServer = _MetadataStructModule._SupportedInterfaceModule.Server
    class _ValueStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _ValueSchema(_StructSchema):
            class _DateField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_common_date_capnp_schemas._DateSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["text"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["float"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["int"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["bool"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["date"],
                ) -> (
                    _MetadataStructModule._ValueStructModule._ValueSchema._DateField
                ): ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _MetadataStructModule._ValueStructModule._ValueSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._MetadataValueSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            text: str | None = None,
            float: float | None = None,
            int: int | None = None,
            bool: bool | None = None,
            date: DateBuilder | dict[str, Any] | None = None,
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
    class _EntryStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _EntrySchema(_StructSchema):
            class _GcmField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._GCMEnumSchema: ...

            class _RcmField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._RCMEnumSchema: ...

            class _RcpField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._RCPEnumSchema: ...

            class _SspField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._SSPEnumSchema: ...

            class _EnsMemField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._EnsembleMemberSchema: ...

            class _StartField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_common_date_capnp_schemas._DateSchema: ...

            class _EndField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_common_date_capnp_schemas._DateSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["gcm"],
                ) -> (
                    _MetadataStructModule._EntryStructModule._EntrySchema._GcmField
                ): ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["rcm"],
                ) -> (
                    _MetadataStructModule._EntryStructModule._EntrySchema._RcmField
                ): ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["historical"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["rcp"],
                ) -> (
                    _MetadataStructModule._EntryStructModule._EntrySchema._RcpField
                ): ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["ssp"],
                ) -> (
                    _MetadataStructModule._EntryStructModule._EntrySchema._SspField
                ): ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["ensMem"],
                ) -> (
                    _MetadataStructModule._EntryStructModule._EntrySchema._EnsMemField
                ): ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["version"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["start"],
                ) -> (
                    _MetadataStructModule._EntryStructModule._EntrySchema._StartField
                ): ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["end"],
                ) -> (
                    _MetadataStructModule._EntryStructModule._EntrySchema._EndField
                ): ...
                @overload
                def __getitem__(self, key: Literal["co2"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["picontrol"],
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
            ) -> _MetadataStructModule._EntryStructModule._EntrySchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._MetadataEntrySchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            gcm: enums.GCMEnum | None = None,
            rcm: enums.RCMEnum | None = None,
            historical: None | None = None,
            rcp: enums.RCPEnum | None = None,
            ssp: enums.SSPEnum | None = None,
            ensMem: builders.EnsembleMemberBuilder | dict[str, Any] | None = None,
            version: str | None = None,
            start: DateBuilder | dict[str, Any] | None = None,
            end: DateBuilder | dict[str, Any] | None = None,
            co2: float | None = None,
            picontrol: None | None = None,
            description: str | None = None,
            **kwargs: object,
        ) -> builders.EntryBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.EntryReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.EntryReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.EntryBuilder]: ...
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
        ) -> readers.EntryReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.EntryReader: ...

    Entry: _EntryStructModule
    class _InformationInterfaceModule(_InterfaceModule):
        class _InformationSchema(_InterfaceSchema):
            class _InformationInterfaceModuleForOneParamSchema(_StructSchema):
                class _EntryField(_StructSchemaField):
                    @property
                    @override
                    def schema(self) -> schemas._MetadataEntrySchema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["entry"],
                    ) -> _MetadataStructModule._InformationInterfaceModule._InformationSchema._InformationInterfaceModuleForOneParamSchema._EntryField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _MetadataStructModule._InformationInterfaceModule._InformationSchema._InformationInterfaceModuleForOneParamSchema._Fields: ...

            class _InformationInterfaceModuleForOneResultSchema(_StructSchema):
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
                ) -> _MetadataStructModule._InformationInterfaceModule._InformationSchema._InformationInterfaceModuleForOneResultSchema._Fields: ...

            class _InformationInterfaceModuleForAllParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _MetadataStructModule._InformationInterfaceModule._InformationSchema._InformationInterfaceModuleForAllParamSchema._Fields: ...

            class _InformationInterfaceModuleForAllResultSchema(_StructSchema):
                class _AllField(_StructSchemaField):
                    class _Schema(_ListSchema):
                        @property
                        @override
                        def elementType(
                            self,
                        ) -> _mas_schema_common_common_capnp_schemas._PairSchema: ...

                    @property
                    @override
                    def schema(
                        self,
                    ) -> _MetadataStructModule._InformationInterfaceModule._InformationSchema._InformationInterfaceModuleForAllResultSchema._AllField._Schema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["all"],
                    ) -> _MetadataStructModule._InformationInterfaceModule._InformationSchema._InformationInterfaceModuleForAllResultSchema._AllField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _MetadataStructModule._InformationInterfaceModule._InformationSchema._InformationInterfaceModuleForAllResultSchema._Fields: ...

            class _Methods(dict[str, _InterfaceMethod[_StructSchema, _StructSchema]]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["forOne"],
                ) -> _InterfaceMethod[
                    _MetadataStructModule._InformationInterfaceModule._InformationSchema._InformationInterfaceModuleForOneParamSchema,
                    _MetadataStructModule._InformationInterfaceModule._InformationSchema._InformationInterfaceModuleForOneResultSchema,
                ]: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["forAll"],
                ) -> _InterfaceMethod[
                    _MetadataStructModule._InformationInterfaceModule._InformationSchema._InformationInterfaceModuleForAllParamSchema,
                    _MetadataStructModule._InformationInterfaceModule._InformationSchema._InformationInterfaceModuleForAllResultSchema,
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
            ) -> _MetadataStructModule._InformationInterfaceModule._InformationSchema._Methods: ...

        @property
        @override
        def schema(self) -> schemas._MetadataInformationSchema: ...
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> clients.InformationClient: ...
        class Server(_DynamicCapabilityServer):
            def forOne(
                self,
                entry: readers.EntryReader,
                _context: contexts.ForoneCallContext,
                **kwargs: object,
            ) -> Awaitable[results_tuples.ForoneResultTuple | None]: ...
            def forOne_context(
                self,
                context: contexts.ForoneCallContext,
            ) -> Awaitable[None]: ...
            def forAll(
                self,
                _context: contexts.ForallCallContext,
                **kwargs: object,
            ) -> Awaitable[
                builders.PairListBuilder
                | readers.PairListReader
                | Sequence[Any]
                | results_tuples.ForallResultTuple
                | None
            ]: ...
            def forAll_context(
                self,
                context: contexts.ForallCallContext,
            ) -> Awaitable[None]: ...

    Information: _InformationInterfaceModule
    type InformationServer = _MetadataStructModule._InformationInterfaceModule.Server
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _MetadataSchema(_StructSchema):
        class _EntriesField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._MetadataEntrySchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _MetadataStructModule._MetadataSchema._EntriesField._Schema: ...

        class _InfoField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._MetadataInformationSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["entries"],
            ) -> _MetadataStructModule._MetadataSchema._EntriesField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _MetadataStructModule._MetadataSchema._InfoField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _MetadataStructModule._MetadataSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._MetadataSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        entries: builders.EntryListBuilder | dict[str, Any] | None = None,
        info: clients.InformationClient
        | _MetadataStructModule._InformationInterfaceModule.Server
        | None = None,
        **kwargs: object,
    ) -> builders.MetadataBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.MetadataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.MetadataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.MetadataBuilder]: ...
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
    ) -> readers.MetadataReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.MetadataReader: ...

class _DatasetInterfaceModule(_IdentifiableInterfaceModule, _PersistentInterfaceModule):
    class _GetLocationsCallbackInterfaceModule(_InterfaceModule):
        class _GetLocationsCallbackSchema(_InterfaceSchema):
            class _GetLocationsCallbackInterfaceModuleNextLocationsParamSchema(
                _StructSchema,
            ):
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
                ) -> _DatasetInterfaceModule._GetLocationsCallbackInterfaceModule._GetLocationsCallbackSchema._GetLocationsCallbackInterfaceModuleNextLocationsParamSchema._Fields: ...

            class _GetLocationsCallbackInterfaceModuleNextLocationsResultSchema(
                _StructSchema,
            ):
                class _LocationsField(_StructSchemaField):
                    class _Schema(_ListSchema):
                        @property
                        @override
                        def elementType(self) -> schemas._LocationSchema: ...

                    @property
                    @override
                    def schema(
                        self,
                    ) -> _DatasetInterfaceModule._GetLocationsCallbackInterfaceModule._GetLocationsCallbackSchema._GetLocationsCallbackInterfaceModuleNextLocationsResultSchema._LocationsField._Schema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["locations"],
                    ) -> _DatasetInterfaceModule._GetLocationsCallbackInterfaceModule._GetLocationsCallbackSchema._GetLocationsCallbackInterfaceModuleNextLocationsResultSchema._LocationsField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _DatasetInterfaceModule._GetLocationsCallbackInterfaceModule._GetLocationsCallbackSchema._GetLocationsCallbackInterfaceModuleNextLocationsResultSchema._Fields: ...

            class _Methods(dict[str, _InterfaceMethod[_StructSchema, _StructSchema]]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["nextLocations"],
                ) -> _InterfaceMethod[
                    _DatasetInterfaceModule._GetLocationsCallbackInterfaceModule._GetLocationsCallbackSchema._GetLocationsCallbackInterfaceModuleNextLocationsParamSchema,
                    _DatasetInterfaceModule._GetLocationsCallbackInterfaceModule._GetLocationsCallbackSchema._GetLocationsCallbackInterfaceModuleNextLocationsResultSchema,
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
            ) -> _DatasetInterfaceModule._GetLocationsCallbackInterfaceModule._GetLocationsCallbackSchema._Methods: ...

        @property
        @override
        def schema(self) -> schemas._DatasetGetLocationsCallbackSchema: ...
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> clients.GetLocationsCallbackClient: ...
        class Server(_DynamicCapabilityServer):
            def nextLocations(
                self,
                maxCount: int,
                _context: contexts.NextlocationsCallContext,
                **kwargs: object,
            ) -> Awaitable[
                builders.LocationListBuilder
                | readers.LocationListReader
                | Sequence[Any]
                | results_tuples.NextlocationsResultTuple
                | None
            ]: ...
            def nextLocations_context(
                self,
                context: contexts.NextlocationsCallContext,
            ) -> Awaitable[None]: ...

    GetLocationsCallback: _GetLocationsCallbackInterfaceModule
    type GetLocationsCallbackServer = (
        _DatasetInterfaceModule._GetLocationsCallbackInterfaceModule.Server
    )

    class _DatasetSchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _DatasetInterfaceModule._DatasetSchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

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
            ) -> _DatasetInterfaceModule._DatasetSchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

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
                ) -> _DatasetInterfaceModule._DatasetSchema._PersistentInterfaceModuleSaveParamSchema._SealForField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _DatasetInterfaceModule._DatasetSchema._PersistentInterfaceModuleSaveParamSchema._Fields: ...

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
                ) -> _DatasetInterfaceModule._DatasetSchema._PersistentInterfaceModuleSaveResultSchema._SturdyRefField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["unsaveSR"],
                ) -> _DatasetInterfaceModule._DatasetSchema._PersistentInterfaceModuleSaveResultSchema._UnsaveSRField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _DatasetInterfaceModule._DatasetSchema._PersistentInterfaceModuleSaveResultSchema._Fields: ...

        class _DatasetInterfaceModuleMetadataParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleMetadataParamSchema._Fields: ...

        class _DatasetInterfaceModuleMetadataResultSchema(_StructSchema):
            class _EntriesField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> schemas._MetadataEntrySchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleMetadataResultSchema._EntriesField._Schema: ...

            class _InfoField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._MetadataInformationSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["entries"],
                ) -> _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleMetadataResultSchema._EntriesField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["info"],
                ) -> _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleMetadataResultSchema._InfoField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleMetadataResultSchema._Fields: ...

        class _DatasetInterfaceModuleClosestTimeSeriesAtParamSchema(_StructSchema):
            class _LatlonField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_geo_geo_capnp_schemas._LatLonCoordSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["latlon"],
                ) -> _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleClosestTimeSeriesAtParamSchema._LatlonField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleClosestTimeSeriesAtParamSchema._Fields: ...

        class _DatasetInterfaceModuleClosestTimeSeriesAtResultSchema(_StructSchema):
            class _TimeSeriesField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _InterfaceSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["timeSeries"],
                ) -> _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleClosestTimeSeriesAtResultSchema._TimeSeriesField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleClosestTimeSeriesAtResultSchema._Fields: ...

        class _DatasetInterfaceModuleTimeSeriesAtParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["locationId"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleTimeSeriesAtParamSchema._Fields: ...

        class _DatasetInterfaceModuleTimeSeriesAtResultSchema(_StructSchema):
            class _TimeSeriesField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _InterfaceSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["timeSeries"],
                ) -> _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleTimeSeriesAtResultSchema._TimeSeriesField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleTimeSeriesAtResultSchema._Fields: ...

        class _DatasetInterfaceModuleLocationsParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleLocationsParamSchema._Fields: ...

        class _DatasetInterfaceModuleLocationsResultSchema(_StructSchema):
            class _LocationsField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> schemas._LocationSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleLocationsResultSchema._LocationsField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["locations"],
                ) -> _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleLocationsResultSchema._LocationsField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleLocationsResultSchema._Fields: ...

        class _DatasetInterfaceModuleStreamLocationsParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["startAfterLocationId"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleStreamLocationsParamSchema._Fields: ...

        class _DatasetInterfaceModuleStreamLocationsResultSchema(_StructSchema):
            class _LocationsCallbackField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._DatasetGetLocationsCallbackSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["locationsCallback"],
                ) -> _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleStreamLocationsResultSchema._LocationsCallbackField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleStreamLocationsResultSchema._Fields: ...

        class _Methods(dict[str, _InterfaceMethod[_StructSchema, _StructSchema]]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _InterfaceMethod[
                _DatasetInterfaceModule._DatasetSchema._IdentifiableInterfaceModuleInfoParamSchema,
                _DatasetInterfaceModule._DatasetSchema._IdentifiableInterfaceModuleInfoResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["save"],
            ) -> _InterfaceMethod[
                _DatasetInterfaceModule._DatasetSchema._PersistentInterfaceModuleSaveParamSchema,
                _DatasetInterfaceModule._DatasetSchema._PersistentInterfaceModuleSaveResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["metadata"],
            ) -> _InterfaceMethod[
                _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleMetadataParamSchema,
                _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleMetadataResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["closestTimeSeriesAt"],
            ) -> _InterfaceMethod[
                _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleClosestTimeSeriesAtParamSchema,
                _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleClosestTimeSeriesAtResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["timeSeriesAt"],
            ) -> _InterfaceMethod[
                _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleTimeSeriesAtParamSchema,
                _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleTimeSeriesAtResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["locations"],
            ) -> _InterfaceMethod[
                _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleLocationsParamSchema,
                _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleLocationsResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["streamLocations"],
            ) -> _InterfaceMethod[
                _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleStreamLocationsParamSchema,
                _DatasetInterfaceModule._DatasetSchema._DatasetInterfaceModuleStreamLocationsResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: str,
            ) -> _InterfaceMethod[_StructSchema, _StructSchema]: ...

        @property
        @override
        def methods(self) -> _DatasetInterfaceModule._DatasetSchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._DatasetSchema: ...
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.DatasetClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def metadata(
            self,
            _context: contexts.DatasetMetadataCallContext,
            **kwargs: object,
        ) -> Awaitable[results_tuples.DatasetMetadataResultTuple | None]: ...
        def metadata_context(
            self,
            context: contexts.DatasetMetadataCallContext,
        ) -> Awaitable[None]: ...
        def closestTimeSeriesAt(
            self,
            latlon: LatLonCoordReader,
            _context: contexts.ClosesttimeseriesatCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _TimeSeriesInterfaceModule.Server
            | clients.TimeSeriesClient
            | results_tuples.ClosesttimeseriesatResultTuple
            | None
        ]: ...
        def closestTimeSeriesAt_context(
            self,
            context: contexts.ClosesttimeseriesatCallContext,
        ) -> Awaitable[None]: ...
        def timeSeriesAt(
            self,
            locationId: str,
            _context: contexts.TimeseriesatCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _TimeSeriesInterfaceModule.Server
            | clients.TimeSeriesClient
            | results_tuples.TimeseriesatResultTuple
            | None
        ]: ...
        def timeSeriesAt_context(
            self,
            context: contexts.TimeseriesatCallContext,
        ) -> Awaitable[None]: ...
        def locations(
            self,
            _context: contexts.LocationsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.LocationListBuilder
            | readers.LocationListReader
            | Sequence[Any]
            | results_tuples.LocationsResultTuple
            | None
        ]: ...
        def locations_context(
            self,
            context: contexts.LocationsCallContext,
        ) -> Awaitable[None]: ...
        def streamLocations(
            self,
            startAfterLocationId: str,
            _context: contexts.StreamlocationsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _DatasetInterfaceModule._GetLocationsCallbackInterfaceModule.Server
            | clients.GetLocationsCallbackClient
            | results_tuples.StreamlocationsResultTuple
            | None
        ]: ...
        def streamLocations_context(
            self,
            context: contexts.StreamlocationsCallContext,
        ) -> Awaitable[None]: ...

class _TimeSeriesInterfaceModule(
    _IdentifiableInterfaceModule,
    _PersistentInterfaceModule,
):
    class _ResolutionEnumModule(_EnumModule):
        daily: int
        hourly: int

        class _ResolutionSchema(_EnumSchema): ...

        @property
        @override
        def schema(self) -> schemas._TimeSeriesResolutionEnumSchema: ...

    Resolution: _ResolutionEnumModule
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.TimeSeriesClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def resolution(
            self,
            _context: contexts.ResolutionCallContext,
            **kwargs: object,
        ) -> Awaitable[
            enums.TimeSeriesResolutionEnum | results_tuples.ResolutionResultTuple | None
        ]: ...
        def resolution_context(
            self,
            context: contexts.ResolutionCallContext,
        ) -> Awaitable[None]: ...
        def range(
            self,
            _context: contexts.RangeCallContext,
            **kwargs: object,
        ) -> Awaitable[results_tuples.RangeResultTuple | None]: ...
        def range_context(
            self,
            context: contexts.RangeCallContext,
        ) -> Awaitable[None]: ...
        def header(
            self,
            _context: contexts.HeaderCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.ElementEnumListBuilder
            | readers.ElementEnumListReader
            | Sequence[Any]
            | results_tuples.HeaderResultTuple
            | None
        ]: ...
        def header_context(
            self,
            context: contexts.HeaderCallContext,
        ) -> Awaitable[None]: ...
        def data(
            self,
            _context: contexts.DataCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.Float32ListListBuilder
            | readers.Float32ListListReader
            | Sequence[Any]
            | results_tuples.DataResultTuple
            | None
        ]: ...
        def data_context(
            self,
            context: contexts.DataCallContext,
        ) -> Awaitable[None]: ...
        def dataT(
            self,
            _context: contexts.DatatCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.Float32ListListBuilder
            | readers.Float32ListListReader
            | Sequence[Any]
            | results_tuples.DatatResultTuple
            | None
        ]: ...
        def dataT_context(
            self,
            context: contexts.DatatCallContext,
        ) -> Awaitable[None]: ...
        def subrange(
            self,
            start: DateReader,
            end: DateReader,
            _context: contexts.SubrangeCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _TimeSeriesInterfaceModule.Server
            | clients.TimeSeriesClient
            | results_tuples.SubrangeResultTuple
            | None
        ]: ...
        def subrange_context(
            self,
            context: contexts.SubrangeCallContext,
        ) -> Awaitable[None]: ...
        def subheader(
            self,
            elements: readers.ElementEnumListReader,
            _context: contexts.SubheaderCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _TimeSeriesInterfaceModule.Server
            | clients.TimeSeriesClient
            | results_tuples.SubheaderResultTuple
            | None
        ]: ...
        def subheader_context(
            self,
            context: contexts.SubheaderCallContext,
        ) -> Awaitable[None]: ...
        def metadata(
            self,
            _context: contexts.TimeSeriesMetadataCallContext,
            **kwargs: object,
        ) -> Awaitable[results_tuples.TimeSeriesMetadataResultTuple | None]: ...
        def metadata_context(
            self,
            context: contexts.TimeSeriesMetadataCallContext,
        ) -> Awaitable[None]: ...
        def location(
            self,
            _context: contexts.LocationCallContext,
            **kwargs: object,
        ) -> Awaitable[results_tuples.LocationResultTuple | None]: ...
        def location_context(
            self,
            context: contexts.LocationCallContext,
        ) -> Awaitable[None]: ...

class _ElementEnumModule(_EnumModule):
    tmin: int
    tavg: int
    tmax: int
    precip: int
    globrad: int
    wind: int
    sunhours: int
    cloudamount: int
    relhumid: int
    airpress: int
    vaporpress: int
    co2: int
    o3: int
    et0: int
    dewpointTemp: int
    specificHumidity: int
    snowfallFlux: int
    surfaceDownwellingLongwaveRadiation: int
    potET: int

    class _ElementSchema(_EnumSchema): ...

    @property
    @override
    def schema(self) -> schemas._ElementEnumSchema: ...

class _LocationStructModule(_StructModule):
    class _KVStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _KVSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["key"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["value"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _LocationStructModule._KVStructModule._KVSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._LocationKVSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            key: str | None = None,
            value: common.AnyPointer | None = None,
            **kwargs: object,
        ) -> builders.KVBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.KVReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.KVReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.KVBuilder]: ...
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
        ) -> readers.KVReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.KVReader: ...

    KV: _KVStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _LocationSchema(_StructSchema):
        class _IdField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> _mas_schema_common_common_capnp_schemas._IdInformationSchema: ...

        class _LatlonField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> _mas_schema_geo_geo_capnp_schemas._LatLonCoordSchema: ...

        class _TimeSeriesField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _InterfaceSchema: ...

        class _CustomDataField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._LocationKVSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _LocationStructModule._LocationSchema._CustomDataField._Schema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["id"],
            ) -> _LocationStructModule._LocationSchema._IdField: ...
            @overload
            def __getitem__(self, key: Literal["heightNN"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["latlon"],
            ) -> _LocationStructModule._LocationSchema._LatlonField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["timeSeries"],
            ) -> _LocationStructModule._LocationSchema._TimeSeriesField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["customData"],
            ) -> _LocationStructModule._LocationSchema._CustomDataField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _LocationStructModule._LocationSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._LocationSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        id: IdInformationBuilder | dict[str, Any] | None = None,
        heightNN: float | None = None,
        latlon: LatLonCoordBuilder | dict[str, Any] | None = None,
        timeSeries: clients.TimeSeriesClient
        | _TimeSeriesInterfaceModule.Server
        | None = None,
        customData: builders.KVListBuilder | dict[str, Any] | None = None,
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

class _MetaPlusDataStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _MetaPlusDataSchema(_StructSchema):
        class _MetaField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._MetadataSchema: ...

        class _DataField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._DatasetSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["meta"],
            ) -> _MetaPlusDataStructModule._MetaPlusDataSchema._MetaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["data"],
            ) -> _MetaPlusDataStructModule._MetaPlusDataSchema._DataField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _MetaPlusDataStructModule._MetaPlusDataSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._MetaPlusDataSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        meta: builders.MetadataBuilder | dict[str, Any] | None = None,
        data: clients.DatasetClient | _DatasetInterfaceModule.Server | None = None,
        **kwargs: object,
    ) -> builders.MetaPlusDataBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.MetaPlusDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.MetaPlusDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.MetaPlusDataBuilder]: ...
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
    ) -> readers.MetaPlusDataReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.MetaPlusDataReader: ...

class _TimeSeriesDataStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _TimeSeriesDataSchema(_StructSchema):
        class _DataField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> _ListSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> (
                _TimeSeriesDataStructModule._TimeSeriesDataSchema._DataField._Schema
            ): ...

        class _HeaderField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._ElementEnumSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> (
                _TimeSeriesDataStructModule._TimeSeriesDataSchema._HeaderField._Schema
            ): ...

        class _StartDateField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _mas_schema_common_date_capnp_schemas._DateSchema: ...

        class _EndDateField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _mas_schema_common_date_capnp_schemas._DateSchema: ...

        class _ResolutionField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._TimeSeriesResolutionEnumSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["data"],
            ) -> _TimeSeriesDataStructModule._TimeSeriesDataSchema._DataField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["isTransposed"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["header"],
            ) -> _TimeSeriesDataStructModule._TimeSeriesDataSchema._HeaderField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["startDate"],
            ) -> _TimeSeriesDataStructModule._TimeSeriesDataSchema._StartDateField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["endDate"],
            ) -> _TimeSeriesDataStructModule._TimeSeriesDataSchema._EndDateField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["resolution"],
            ) -> _TimeSeriesDataStructModule._TimeSeriesDataSchema._ResolutionField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _TimeSeriesDataStructModule._TimeSeriesDataSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._TimeSeriesDataSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        data: builders.Float32ListListBuilder | dict[str, Any] | None = None,
        isTransposed: bool | None = None,
        header: builders.ElementEnumListBuilder | dict[str, Any] | None = None,
        startDate: DateBuilder | dict[str, Any] | None = None,
        endDate: DateBuilder | dict[str, Any] | None = None,
        resolution: enums.TimeSeriesResolutionEnum | None = None,
        **kwargs: object,
    ) -> builders.TimeSeriesDataBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.TimeSeriesDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.TimeSeriesDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.TimeSeriesDataBuilder]: ...
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
    ) -> readers.TimeSeriesDataReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.TimeSeriesDataReader: ...

class _ServiceInterfaceModule(_IdentifiableInterfaceModule, _PersistentInterfaceModule):
    class _ServiceSchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

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
            ) -> _ServiceInterfaceModule._ServiceSchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

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
                ) -> _ServiceInterfaceModule._ServiceSchema._PersistentInterfaceModuleSaveParamSchema._SealForField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._PersistentInterfaceModuleSaveParamSchema._Fields: ...

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
                ) -> _ServiceInterfaceModule._ServiceSchema._PersistentInterfaceModuleSaveResultSchema._SturdyRefField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["unsaveSR"],
                ) -> _ServiceInterfaceModule._ServiceSchema._PersistentInterfaceModuleSaveResultSchema._UnsaveSRField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._PersistentInterfaceModuleSaveResultSchema._Fields: ...

        class _ServiceInterfaceModuleGetAvailableDatasetsParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleGetAvailableDatasetsParamSchema._Fields: ...

        class _ServiceInterfaceModuleGetAvailableDatasetsResultSchema(_StructSchema):
            class _DatasetsField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> schemas._MetaPlusDataSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleGetAvailableDatasetsResultSchema._DatasetsField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["datasets"],
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleGetAvailableDatasetsResultSchema._DatasetsField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleGetAvailableDatasetsResultSchema._Fields: ...

        class _ServiceInterfaceModuleGetDatasetsForParamSchema(_StructSchema):
            class _TemplateField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._MetadataSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["template"],
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleGetDatasetsForParamSchema._TemplateField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleGetDatasetsForParamSchema._Fields: ...

        class _ServiceInterfaceModuleGetDatasetsForResultSchema(_StructSchema):
            class _DatasetsField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> schemas._DatasetSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleGetDatasetsForResultSchema._DatasetsField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["datasets"],
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleGetDatasetsForResultSchema._DatasetsField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleGetDatasetsForResultSchema._Fields: ...

        class _Methods(dict[str, _InterfaceMethod[_StructSchema, _StructSchema]]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _InterfaceMethod[
                _ServiceInterfaceModule._ServiceSchema._IdentifiableInterfaceModuleInfoParamSchema,
                _ServiceInterfaceModule._ServiceSchema._IdentifiableInterfaceModuleInfoResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["save"],
            ) -> _InterfaceMethod[
                _ServiceInterfaceModule._ServiceSchema._PersistentInterfaceModuleSaveParamSchema,
                _ServiceInterfaceModule._ServiceSchema._PersistentInterfaceModuleSaveResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["getAvailableDatasets"],
            ) -> _InterfaceMethod[
                _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleGetAvailableDatasetsParamSchema,
                _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleGetAvailableDatasetsResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["getDatasetsFor"],
            ) -> _InterfaceMethod[
                _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleGetDatasetsForParamSchema,
                _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleGetDatasetsForResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: str,
            ) -> _InterfaceMethod[_StructSchema, _StructSchema]: ...

        @property
        @override
        def methods(self) -> _ServiceInterfaceModule._ServiceSchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._ServiceSchema: ...
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.ServiceClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def getAvailableDatasets(
            self,
            _context: contexts.GetavailabledatasetsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.MetaPlusDataListBuilder
            | readers.MetaPlusDataListReader
            | Sequence[Any]
            | results_tuples.GetavailabledatasetsResultTuple
            | None
        ]: ...
        def getAvailableDatasets_context(
            self,
            context: contexts.GetavailabledatasetsCallContext,
        ) -> Awaitable[None]: ...
        def getDatasetsFor(
            self,
            template: readers.MetadataReader,
            _context: contexts.GetdatasetsforCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.DatasetClientListBuilder
            | readers.DatasetClientListReader
            | Sequence[Any]
            | results_tuples.GetdatasetsforResultTuple
            | None
        ]: ...
        def getDatasetsFor_context(
            self,
            context: contexts.GetdatasetsforCallContext,
        ) -> Awaitable[None]: ...

class _CSVTimeSeriesFactoryInterfaceModule(_IdentifiableInterfaceModule):
    class _CSVConfigStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _CSVConfigSchema(_StructSchema):
            class _HeaderMapField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(
                        self,
                    ) -> _mas_schema_common_common_capnp_schemas._PairSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _CSVTimeSeriesFactoryInterfaceModule._CSVConfigStructModule._CSVConfigSchema._HeaderMapField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["sep"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["headerMap"],
                ) -> _CSVTimeSeriesFactoryInterfaceModule._CSVConfigStructModule._CSVConfigSchema._HeaderMapField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["skipLinesToHeader"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["skipLinesFromHeaderToData"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _CSVTimeSeriesFactoryInterfaceModule._CSVConfigStructModule._CSVConfigSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._CSVTimeSeriesFactoryCSVConfigSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            sep: str | None = None,
            headerMap: builders.PairListBuilder | dict[str, Any] | None = None,
            skipLinesToHeader: int | None = None,
            skipLinesFromHeaderToData: int | None = None,
            **kwargs: object,
        ) -> builders.CSVConfigBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.CSVConfigReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.CSVConfigReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.CSVConfigBuilder]: ...
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
        ) -> readers.CSVConfigReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.CSVConfigReader: ...

    CSVConfig: _CSVConfigStructModule

    class _CSVTimeSeriesFactorySchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _CSVTimeSeriesFactoryInterfaceModule._CSVTimeSeriesFactorySchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

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
            ) -> _CSVTimeSeriesFactoryInterfaceModule._CSVTimeSeriesFactorySchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

        class _CSVTimeSeriesFactoryInterfaceModuleCreateParamSchema(_StructSchema):
            class _ConfigField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._CSVTimeSeriesFactoryCSVConfigSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["csvData"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["config"],
                ) -> _CSVTimeSeriesFactoryInterfaceModule._CSVTimeSeriesFactorySchema._CSVTimeSeriesFactoryInterfaceModuleCreateParamSchema._ConfigField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _CSVTimeSeriesFactoryInterfaceModule._CSVTimeSeriesFactorySchema._CSVTimeSeriesFactoryInterfaceModuleCreateParamSchema._Fields: ...

        class _CSVTimeSeriesFactoryInterfaceModuleCreateResultSchema(_StructSchema):
            class _TimeseriesField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _InterfaceSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["timeseries"],
                ) -> _CSVTimeSeriesFactoryInterfaceModule._CSVTimeSeriesFactorySchema._CSVTimeSeriesFactoryInterfaceModuleCreateResultSchema._TimeseriesField: ...
                @overload
                def __getitem__(self, key: Literal["error"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _CSVTimeSeriesFactoryInterfaceModule._CSVTimeSeriesFactorySchema._CSVTimeSeriesFactoryInterfaceModuleCreateResultSchema._Fields: ...

        class _Methods(dict[str, _InterfaceMethod[_StructSchema, _StructSchema]]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _InterfaceMethod[
                _CSVTimeSeriesFactoryInterfaceModule._CSVTimeSeriesFactorySchema._IdentifiableInterfaceModuleInfoParamSchema,
                _CSVTimeSeriesFactoryInterfaceModule._CSVTimeSeriesFactorySchema._IdentifiableInterfaceModuleInfoResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["create"],
            ) -> _InterfaceMethod[
                _CSVTimeSeriesFactoryInterfaceModule._CSVTimeSeriesFactorySchema._CSVTimeSeriesFactoryInterfaceModuleCreateParamSchema,
                _CSVTimeSeriesFactoryInterfaceModule._CSVTimeSeriesFactorySchema._CSVTimeSeriesFactoryInterfaceModuleCreateResultSchema,
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
        ) -> (
            _CSVTimeSeriesFactoryInterfaceModule._CSVTimeSeriesFactorySchema._Methods
        ): ...

    @property
    @override
    def schema(self) -> schemas._CSVTimeSeriesFactorySchema: ...
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.CSVTimeSeriesFactoryClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def create(
            self,
            csvData: str,
            config: readers.CSVConfigReader,
            _context: contexts.CreateCallContext,
            **kwargs: object,
        ) -> Awaitable[results_tuples.CreateResultTuple | None]: ...
        def create_context(
            self,
            context: contexts.CreateCallContext,
        ) -> Awaitable[None]: ...

class _AlterTimeSeriesWrapperInterfaceModule(_TimeSeriesInterfaceModule):
    class _AlterTypeEnumModule(_EnumModule):
        add: int
        mul: int

        class _AlterTypeSchema(_EnumSchema): ...

        @property
        @override
        def schema(self) -> schemas._AlterTimeSeriesWrapperAlterTypeEnumSchema: ...

    AlterType: _AlterTypeEnumModule
    class _AlteredStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _AlteredSchema(_StructSchema):
            class _ElementField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._ElementEnumSchema: ...

            class _TypeField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> schemas._AlterTimeSeriesWrapperAlterTypeEnumSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["element"],
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlteredStructModule._AlteredSchema._ElementField: ...
                @overload
                def __getitem__(self, key: Literal["value"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["type"],
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlteredStructModule._AlteredSchema._TypeField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlteredStructModule._AlteredSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._AlterTimeSeriesWrapperAlteredSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            element: enums.ElementEnum | None = None,
            value: float | None = None,
            type: enums.AlterTimeSeriesWrapperAlterTypeEnum | None = None,
            **kwargs: object,
        ) -> builders.AlteredBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.AlteredReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.AlteredReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.AlteredBuilder]: ...
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
        ) -> readers.AlteredReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.AlteredReader: ...

    Altered: _AlteredStructModule

    class _AlterTimeSeriesWrapperSchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

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
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

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
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._PersistentInterfaceModuleSaveParamSchema._SealForField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._PersistentInterfaceModuleSaveParamSchema._Fields: ...

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
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._PersistentInterfaceModuleSaveResultSchema._SturdyRefField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["unsaveSR"],
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._PersistentInterfaceModuleSaveResultSchema._UnsaveSRField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._PersistentInterfaceModuleSaveResultSchema._Fields: ...

        class _TimeSeriesInterfaceModuleResolutionParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleResolutionParamSchema._Fields: ...

        class _TimeSeriesInterfaceModuleResolutionResultSchema(_StructSchema):
            class _ResolutionField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._TimeSeriesResolutionEnumSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["resolution"],
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleResolutionResultSchema._ResolutionField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleResolutionResultSchema._Fields: ...

        class _TimeSeriesInterfaceModuleRangeParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleRangeParamSchema._Fields: ...

        class _TimeSeriesInterfaceModuleRangeResultSchema(_StructSchema):
            class _StartDateField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_common_date_capnp_schemas._DateSchema: ...

            class _EndDateField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_common_date_capnp_schemas._DateSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["startDate"],
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleRangeResultSchema._StartDateField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["endDate"],
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleRangeResultSchema._EndDateField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleRangeResultSchema._Fields: ...

        class _TimeSeriesInterfaceModuleHeaderParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleHeaderParamSchema._Fields: ...

        class _TimeSeriesInterfaceModuleHeaderResultSchema(_StructSchema):
            class _HeaderField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> schemas._ElementEnumSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleHeaderResultSchema._HeaderField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["header"],
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleHeaderResultSchema._HeaderField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleHeaderResultSchema._Fields: ...

        class _TimeSeriesInterfaceModuleDataParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleDataParamSchema._Fields: ...

        class _TimeSeriesInterfaceModuleDataResultSchema(_StructSchema):
            class _DataField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> _ListSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleDataResultSchema._DataField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["data"],
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleDataResultSchema._DataField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleDataResultSchema._Fields: ...

        class _TimeSeriesInterfaceModuleDataTParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleDataTParamSchema._Fields: ...

        class _TimeSeriesInterfaceModuleDataTResultSchema(_StructSchema):
            class _DataField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> _ListSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleDataTResultSchema._DataField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["data"],
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleDataTResultSchema._DataField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleDataTResultSchema._Fields: ...

        class _TimeSeriesInterfaceModuleSubrangeParamSchema(_StructSchema):
            class _StartField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_common_date_capnp_schemas._DateSchema: ...

            class _EndField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_common_date_capnp_schemas._DateSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["start"],
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleSubrangeParamSchema._StartField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["end"],
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleSubrangeParamSchema._EndField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleSubrangeParamSchema._Fields: ...

        class _TimeSeriesInterfaceModuleSubrangeResultSchema(_StructSchema):
            class _TimeSeriesField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _InterfaceSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["timeSeries"],
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleSubrangeResultSchema._TimeSeriesField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleSubrangeResultSchema._Fields: ...

        class _TimeSeriesInterfaceModuleSubheaderParamSchema(_StructSchema):
            class _ElementsField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> schemas._ElementEnumSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleSubheaderParamSchema._ElementsField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["elements"],
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleSubheaderParamSchema._ElementsField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleSubheaderParamSchema._Fields: ...

        class _TimeSeriesInterfaceModuleSubheaderResultSchema(_StructSchema):
            class _TimeSeriesField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _InterfaceSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["timeSeries"],
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleSubheaderResultSchema._TimeSeriesField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleSubheaderResultSchema._Fields: ...

        class _TimeSeriesInterfaceModuleMetadataParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleMetadataParamSchema._Fields: ...

        class _TimeSeriesInterfaceModuleMetadataResultSchema(_StructSchema):
            class _EntriesField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> schemas._MetadataEntrySchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleMetadataResultSchema._EntriesField._Schema: ...

            class _InfoField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._MetadataInformationSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["entries"],
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleMetadataResultSchema._EntriesField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["info"],
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleMetadataResultSchema._InfoField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleMetadataResultSchema._Fields: ...

        class _TimeSeriesInterfaceModuleLocationParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleLocationParamSchema._Fields: ...

        class _TimeSeriesInterfaceModuleLocationResultSchema(_StructSchema):
            class _IdField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_common_common_capnp_schemas._IdInformationSchema: ...

            class _LatlonField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_geo_geo_capnp_schemas._LatLonCoordSchema: ...

            class _TimeSeriesField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _InterfaceSchema: ...

            class _CustomDataField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> schemas._LocationKVSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleLocationResultSchema._CustomDataField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["id"],
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleLocationResultSchema._IdField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["heightNN"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["latlon"],
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleLocationResultSchema._LatlonField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["timeSeries"],
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleLocationResultSchema._TimeSeriesField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["customData"],
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleLocationResultSchema._CustomDataField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleLocationResultSchema._Fields: ...

        class _AlterTimeSeriesWrapperInterfaceModuleWrappedTimeSeriesParamSchema(
            _StructSchema,
        ):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._AlterTimeSeriesWrapperInterfaceModuleWrappedTimeSeriesParamSchema._Fields: ...

        class _AlterTimeSeriesWrapperInterfaceModuleWrappedTimeSeriesResultSchema(
            _StructSchema,
        ):
            class _TimeSeriesField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _InterfaceSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["timeSeries"],
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._AlterTimeSeriesWrapperInterfaceModuleWrappedTimeSeriesResultSchema._TimeSeriesField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._AlterTimeSeriesWrapperInterfaceModuleWrappedTimeSeriesResultSchema._Fields: ...

        class _AlterTimeSeriesWrapperInterfaceModuleAlteredElementsParamSchema(
            _StructSchema,
        ):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._AlterTimeSeriesWrapperInterfaceModuleAlteredElementsParamSchema._Fields: ...

        class _AlterTimeSeriesWrapperInterfaceModuleAlteredElementsResultSchema(
            _StructSchema,
        ):
            class _ListField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(
                        self,
                    ) -> schemas._AlterTimeSeriesWrapperAlteredSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._AlterTimeSeriesWrapperInterfaceModuleAlteredElementsResultSchema._ListField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["list"],
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._AlterTimeSeriesWrapperInterfaceModuleAlteredElementsResultSchema._ListField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._AlterTimeSeriesWrapperInterfaceModuleAlteredElementsResultSchema._Fields: ...

        class _AlterTimeSeriesWrapperInterfaceModuleAlterParamSchema(_StructSchema):
            class _DescField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._AlterTimeSeriesWrapperAlteredSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["desc"],
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._AlterTimeSeriesWrapperInterfaceModuleAlterParamSchema._DescField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["asNewTimeSeries"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._AlterTimeSeriesWrapperInterfaceModuleAlterParamSchema._Fields: ...

        class _AlterTimeSeriesWrapperInterfaceModuleAlterResultSchema(_StructSchema):
            class _TimeSeriesField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _InterfaceSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["timeSeries"],
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._AlterTimeSeriesWrapperInterfaceModuleAlterResultSchema._TimeSeriesField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._AlterTimeSeriesWrapperInterfaceModuleAlterResultSchema._Fields: ...

        class _AlterTimeSeriesWrapperInterfaceModuleRemoveParamSchema(_StructSchema):
            class _AlteredElementField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._ElementEnumSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["alteredElement"],
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._AlterTimeSeriesWrapperInterfaceModuleRemoveParamSchema._AlteredElementField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._AlterTimeSeriesWrapperInterfaceModuleRemoveParamSchema._Fields: ...

        class _AlterTimeSeriesWrapperInterfaceModuleRemoveResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._AlterTimeSeriesWrapperInterfaceModuleRemoveResultSchema._Fields: ...

        class _AlterTimeSeriesWrapperInterfaceModuleReplaceWrappedTimeSeriesParamSchema(
            _StructSchema,
        ):
            class _TimeSeriesField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _InterfaceSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["timeSeries"],
                ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._AlterTimeSeriesWrapperInterfaceModuleReplaceWrappedTimeSeriesParamSchema._TimeSeriesField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._AlterTimeSeriesWrapperInterfaceModuleReplaceWrappedTimeSeriesParamSchema._Fields: ...

        class _AlterTimeSeriesWrapperInterfaceModuleReplaceWrappedTimeSeriesResultSchema(
            _StructSchema,
        ):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._AlterTimeSeriesWrapperInterfaceModuleReplaceWrappedTimeSeriesResultSchema._Fields: ...

        class _Methods(dict[str, _InterfaceMethod[_StructSchema, _StructSchema]]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _InterfaceMethod[
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._IdentifiableInterfaceModuleInfoParamSchema,
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._IdentifiableInterfaceModuleInfoResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["save"],
            ) -> _InterfaceMethod[
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._PersistentInterfaceModuleSaveParamSchema,
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._PersistentInterfaceModuleSaveResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["resolution"],
            ) -> _InterfaceMethod[
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleResolutionParamSchema,
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleResolutionResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["range"],
            ) -> _InterfaceMethod[
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleRangeParamSchema,
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleRangeResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["header"],
            ) -> _InterfaceMethod[
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleHeaderParamSchema,
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleHeaderResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["data"],
            ) -> _InterfaceMethod[
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleDataParamSchema,
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleDataResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["dataT"],
            ) -> _InterfaceMethod[
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleDataTParamSchema,
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleDataTResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["subrange"],
            ) -> _InterfaceMethod[
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleSubrangeParamSchema,
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleSubrangeResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["subheader"],
            ) -> _InterfaceMethod[
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleSubheaderParamSchema,
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleSubheaderResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["metadata"],
            ) -> _InterfaceMethod[
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleMetadataParamSchema,
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleMetadataResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["location"],
            ) -> _InterfaceMethod[
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleLocationParamSchema,
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._TimeSeriesInterfaceModuleLocationResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["wrappedTimeSeries"],
            ) -> _InterfaceMethod[
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._AlterTimeSeriesWrapperInterfaceModuleWrappedTimeSeriesParamSchema,
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._AlterTimeSeriesWrapperInterfaceModuleWrappedTimeSeriesResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["alteredElements"],
            ) -> _InterfaceMethod[
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._AlterTimeSeriesWrapperInterfaceModuleAlteredElementsParamSchema,
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._AlterTimeSeriesWrapperInterfaceModuleAlteredElementsResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["alter"],
            ) -> _InterfaceMethod[
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._AlterTimeSeriesWrapperInterfaceModuleAlterParamSchema,
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._AlterTimeSeriesWrapperInterfaceModuleAlterResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["remove"],
            ) -> _InterfaceMethod[
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._AlterTimeSeriesWrapperInterfaceModuleRemoveParamSchema,
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._AlterTimeSeriesWrapperInterfaceModuleRemoveResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["replaceWrappedTimeSeries"],
            ) -> _InterfaceMethod[
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._AlterTimeSeriesWrapperInterfaceModuleReplaceWrappedTimeSeriesParamSchema,
                _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._AlterTimeSeriesWrapperInterfaceModuleReplaceWrappedTimeSeriesResultSchema,
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
        ) -> _AlterTimeSeriesWrapperInterfaceModule._AlterTimeSeriesWrapperSchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._AlterTimeSeriesWrapperSchema: ...
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.AlterTimeSeriesWrapperClient: ...
    class Server(_TimeSeriesInterfaceModule.Server):
        def wrappedTimeSeries(
            self,
            _context: contexts.WrappedtimeseriesCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _TimeSeriesInterfaceModule.Server
            | clients.TimeSeriesClient
            | results_tuples.WrappedtimeseriesResultTuple
            | None
        ]: ...
        def wrappedTimeSeries_context(
            self,
            context: contexts.WrappedtimeseriesCallContext,
        ) -> Awaitable[None]: ...
        def alteredElements(
            self,
            _context: contexts.AlteredelementsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.AlteredListBuilder
            | readers.AlteredListReader
            | Sequence[Any]
            | results_tuples.AlteredelementsResultTuple
            | None
        ]: ...
        def alteredElements_context(
            self,
            context: contexts.AlteredelementsCallContext,
        ) -> Awaitable[None]: ...
        def alter(
            self,
            desc: readers.AlteredReader,
            asNewTimeSeries: bool,
            _context: contexts.AlterCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _TimeSeriesInterfaceModule.Server
            | clients.TimeSeriesClient
            | results_tuples.AlterResultTuple
            | None
        ]: ...
        def alter_context(
            self,
            context: contexts.AlterCallContext,
        ) -> Awaitable[None]: ...
        def remove(
            self,
            alteredElement: enums.ElementEnum,
            _context: contexts.RemoveCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def remove_context(
            self,
            context: contexts.RemoveCallContext,
        ) -> Awaitable[None]: ...
        def replaceWrappedTimeSeries(
            self,
            timeSeries: clients.TimeSeriesClient,
            _context: contexts.ReplacewrappedtimeseriesCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def replaceWrappedTimeSeries_context(
            self,
            context: contexts.ReplacewrappedtimeseriesCallContext,
        ) -> Awaitable[None]: ...

class _AlterTimeSeriesWrapperFactoryInterfaceModule(_IdentifiableInterfaceModule):
    class _AlterTimeSeriesWrapperFactorySchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperFactoryInterfaceModule._AlterTimeSeriesWrapperFactorySchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

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
            ) -> _AlterTimeSeriesWrapperFactoryInterfaceModule._AlterTimeSeriesWrapperFactorySchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

        class _AlterTimeSeriesWrapperFactoryInterfaceModuleWrapParamSchema(
            _StructSchema,
        ):
            class _TimeSeriesField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _InterfaceSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["timeSeries"],
                ) -> _AlterTimeSeriesWrapperFactoryInterfaceModule._AlterTimeSeriesWrapperFactorySchema._AlterTimeSeriesWrapperFactoryInterfaceModuleWrapParamSchema._TimeSeriesField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperFactoryInterfaceModule._AlterTimeSeriesWrapperFactorySchema._AlterTimeSeriesWrapperFactoryInterfaceModuleWrapParamSchema._Fields: ...

        class _AlterTimeSeriesWrapperFactoryInterfaceModuleWrapResultSchema(
            _StructSchema,
        ):
            class _WrapperField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._AlterTimeSeriesWrapperSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["wrapper"],
                ) -> _AlterTimeSeriesWrapperFactoryInterfaceModule._AlterTimeSeriesWrapperFactorySchema._AlterTimeSeriesWrapperFactoryInterfaceModuleWrapResultSchema._WrapperField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _AlterTimeSeriesWrapperFactoryInterfaceModule._AlterTimeSeriesWrapperFactorySchema._AlterTimeSeriesWrapperFactoryInterfaceModuleWrapResultSchema._Fields: ...

        class _Methods(dict[str, _InterfaceMethod[_StructSchema, _StructSchema]]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _InterfaceMethod[
                _AlterTimeSeriesWrapperFactoryInterfaceModule._AlterTimeSeriesWrapperFactorySchema._IdentifiableInterfaceModuleInfoParamSchema,
                _AlterTimeSeriesWrapperFactoryInterfaceModule._AlterTimeSeriesWrapperFactorySchema._IdentifiableInterfaceModuleInfoResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["wrap"],
            ) -> _InterfaceMethod[
                _AlterTimeSeriesWrapperFactoryInterfaceModule._AlterTimeSeriesWrapperFactorySchema._AlterTimeSeriesWrapperFactoryInterfaceModuleWrapParamSchema,
                _AlterTimeSeriesWrapperFactoryInterfaceModule._AlterTimeSeriesWrapperFactorySchema._AlterTimeSeriesWrapperFactoryInterfaceModuleWrapResultSchema,
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
        ) -> _AlterTimeSeriesWrapperFactoryInterfaceModule._AlterTimeSeriesWrapperFactorySchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._AlterTimeSeriesWrapperFactorySchema: ...
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.AlterTimeSeriesWrapperFactoryClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def wrap(
            self,
            timeSeries: clients.TimeSeriesClient,
            _context: contexts.WrapCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _AlterTimeSeriesWrapperInterfaceModule.Server
            | clients.AlterTimeSeriesWrapperClient
            | results_tuples.WrapResultTuple
            | None
        ]: ...
        def wrap_context(
            self,
            context: contexts.WrapCallContext,
        ) -> Awaitable[None]: ...
