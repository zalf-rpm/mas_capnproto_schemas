"""Module helper types for `soil.capnp`."""

from collections.abc import Awaitable, Callable, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _DynamicStructReader,
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
from mas.schema.geo.geo_capnp.types.readers import LatLonCoordReader
from mas.schema.persistence.persistence_capnp.types.modules import (
    _PersistentInterfaceModule,
)
from mas.schema.soil.soil_capnp.types import builders as builders
from mas.schema.soil.soil_capnp.types import clients as clients
from mas.schema.soil.soil_capnp.types import contexts as contexts
from mas.schema.soil.soil_capnp.types import enums as enums
from mas.schema.soil.soil_capnp.types import readers as readers
from mas.schema.soil.soil_capnp.types import schemas as schemas
from mas.schema.soil.soil_capnp.types import servers as servers
from mas.schema.soil.soil_capnp.types.results import tuples as results_tuples

class _LayerStructModule(_StructModule):
    class _PropertyStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _PropertySchema(_StructSchema):
            class _NameField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _EnumSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["name"],
                ) -> (
                    _LayerStructModule._PropertyStructModule._PropertySchema._NameField
                ): ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["f32Value"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["bValue"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["type"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["unset"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _LayerStructModule._PropertyStructModule._PropertySchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._LayerPropertySchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            name: enums.PropertyNameEnum | None = None,
            f32Value: float | None = None,
            bValue: bool | None = None,
            type: str | None = None,
            unset: None | None = None,
            **kwargs: object,
        ) -> builders.PropertyBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.PropertyReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.PropertyReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.PropertyBuilder]: ...
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
        ) -> readers.PropertyReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.PropertyReader: ...

    Property: _PropertyStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _LayerSchema(_StructSchema):
        class _PropertiesField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._LayerPropertySchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _LayerStructModule._LayerSchema._PropertiesField._Schema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["properties"],
            ) -> _LayerStructModule._LayerSchema._PropertiesField: ...
            @overload
            def __getitem__(self, key: Literal["size"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["description"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _LayerStructModule._LayerSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._LayerSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        properties: builders.PropertyListBuilder | dict[str, Any] | None = None,
        size: float | None = None,
        description: str | None = None,
        **kwargs: object,
    ) -> builders.LayerBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.LayerReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.LayerReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.LayerBuilder]: ...
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
    ) -> readers.LayerReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.LayerReader: ...

class _QueryStructModule(_StructModule):
    class _ResultStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _ResultSchema(_StructSchema):
            class _MandatoryField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> _EnumSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _QueryStructModule._ResultStructModule._ResultSchema._MandatoryField._Schema: ...

            class _OptionalField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> _EnumSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _QueryStructModule._ResultStructModule._ResultSchema._OptionalField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["failed"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["mandatory"],
                ) -> (
                    _QueryStructModule._ResultStructModule._ResultSchema._MandatoryField
                ): ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["optional"],
                ) -> (
                    _QueryStructModule._ResultStructModule._ResultSchema._OptionalField
                ): ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _QueryStructModule._ResultStructModule._ResultSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._QueryResultSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            failed: bool | None = None,
            mandatory: builders.PropertyNameEnumListBuilder
            | dict[str, Any]
            | None = None,
            optional: builders.PropertyNameEnumListBuilder
            | dict[str, Any]
            | None = None,
            **kwargs: object,
        ) -> builders.ResultBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.ResultReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.ResultReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.ResultBuilder]: ...
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
        ) -> readers.ResultReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.ResultReader: ...

    Result: _ResultStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _QuerySchema(_StructSchema):
        class _MandatoryField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> _EnumSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _QueryStructModule._QuerySchema._MandatoryField._Schema: ...

        class _OptionalField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> _EnumSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _QueryStructModule._QuerySchema._OptionalField._Schema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["mandatory"],
            ) -> _QueryStructModule._QuerySchema._MandatoryField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["optional"],
            ) -> _QueryStructModule._QuerySchema._OptionalField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["onlyRawData"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _QueryStructModule._QuerySchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._QuerySchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        mandatory: builders.PropertyNameEnumListBuilder | dict[str, Any] | None = None,
        optional: builders.PropertyNameEnumListBuilder | dict[str, Any] | None = None,
        onlyRawData: bool | None = None,
        **kwargs: object,
    ) -> builders.QueryBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.QueryReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.QueryReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.QueryBuilder]: ...
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
    ) -> readers.QueryReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.QueryReader: ...

class _ProfileDataStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _ProfileDataSchema(_StructSchema):
        class _LayersField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._LayerSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _ProfileDataStructModule._ProfileDataSchema._LayersField._Schema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["layers"],
            ) -> _ProfileDataStructModule._ProfileDataSchema._LayersField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["percentageOfArea"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _ProfileDataStructModule._ProfileDataSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._ProfileDataSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        layers: builders.LayerListBuilder | dict[str, Any] | None = None,
        percentageOfArea: float | None = None,
        **kwargs: object,
    ) -> builders.ProfileDataBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.ProfileDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.ProfileDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.ProfileDataBuilder]: ...
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
    ) -> readers.ProfileDataReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.ProfileDataReader: ...

class _ProfileInterfaceModule(_IdentifiableInterfaceModule, _PersistentInterfaceModule):
    class _ProfileSchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _ProfileInterfaceModule._ProfileSchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

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
            ) -> _ProfileInterfaceModule._ProfileSchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

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
                ) -> _ProfileInterfaceModule._ProfileSchema._PersistentInterfaceModuleSaveParamSchema._SealForField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ProfileInterfaceModule._ProfileSchema._PersistentInterfaceModuleSaveParamSchema._Fields: ...

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
                ) -> _ProfileInterfaceModule._ProfileSchema._PersistentInterfaceModuleSaveResultSchema._SturdyRefField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["unsaveSR"],
                ) -> _ProfileInterfaceModule._ProfileSchema._PersistentInterfaceModuleSaveResultSchema._UnsaveSRField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ProfileInterfaceModule._ProfileSchema._PersistentInterfaceModuleSaveResultSchema._Fields: ...

        class _ProfileInterfaceModuleDataParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _ProfileInterfaceModule._ProfileSchema._ProfileInterfaceModuleDataParamSchema._Fields: ...

        class _ProfileInterfaceModuleDataResultSchema(_StructSchema):
            class _LayersField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> schemas._LayerSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _ProfileInterfaceModule._ProfileSchema._ProfileInterfaceModuleDataResultSchema._LayersField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["layers"],
                ) -> _ProfileInterfaceModule._ProfileSchema._ProfileInterfaceModuleDataResultSchema._LayersField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["percentageOfArea"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ProfileInterfaceModule._ProfileSchema._ProfileInterfaceModuleDataResultSchema._Fields: ...

        class _ProfileInterfaceModuleGeoLocationParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _ProfileInterfaceModule._ProfileSchema._ProfileInterfaceModuleGeoLocationParamSchema._Fields: ...

        class _ProfileInterfaceModuleGeoLocationResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["lat"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["lon"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ProfileInterfaceModule._ProfileSchema._ProfileInterfaceModuleGeoLocationResultSchema._Fields: ...

        class _Methods(dict[str, _InterfaceMethod[_StructSchema, _StructSchema]]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _InterfaceMethod[
                _ProfileInterfaceModule._ProfileSchema._IdentifiableInterfaceModuleInfoParamSchema,
                _ProfileInterfaceModule._ProfileSchema._IdentifiableInterfaceModuleInfoResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["save"],
            ) -> _InterfaceMethod[
                _ProfileInterfaceModule._ProfileSchema._PersistentInterfaceModuleSaveParamSchema,
                _ProfileInterfaceModule._ProfileSchema._PersistentInterfaceModuleSaveResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["data"],
            ) -> _InterfaceMethod[
                _ProfileInterfaceModule._ProfileSchema._ProfileInterfaceModuleDataParamSchema,
                _ProfileInterfaceModule._ProfileSchema._ProfileInterfaceModuleDataResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["geoLocation"],
            ) -> _InterfaceMethod[
                _ProfileInterfaceModule._ProfileSchema._ProfileInterfaceModuleGeoLocationParamSchema,
                _ProfileInterfaceModule._ProfileSchema._ProfileInterfaceModuleGeoLocationResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: str,
            ) -> _InterfaceMethod[_StructSchema, _StructSchema]: ...

        @property
        @override
        def methods(self) -> _ProfileInterfaceModule._ProfileSchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._ProfileSchema: ...
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.ProfileClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def data(
            self,
            _context: contexts.DataCallContext,
            **kwargs: object,
        ) -> Awaitable[results_tuples.DataResultTuple | None]: ...
        def data_context(
            self,
            context: contexts.DataCallContext,
        ) -> Awaitable[None]: ...
        def geoLocation(
            self,
            _context: contexts.GeolocationCallContext,
            **kwargs: object,
        ) -> Awaitable[results_tuples.GeolocationResultTuple | None]: ...
        def geoLocation_context(
            self,
            context: contexts.GeolocationCallContext,
        ) -> Awaitable[None]: ...

class _ServiceInterfaceModule(_IdentifiableInterfaceModule, _PersistentInterfaceModule):
    class _StreamInterfaceModule(_InterfaceModule):
        class _StreamSchema(_InterfaceSchema):
            class _StreamInterfaceModuleNextProfilesParamSchema(_StructSchema):
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
                ) -> _ServiceInterfaceModule._StreamInterfaceModule._StreamSchema._StreamInterfaceModuleNextProfilesParamSchema._Fields: ...

            class _StreamInterfaceModuleNextProfilesResultSchema(_StructSchema):
                class _ProfilesField(_StructSchemaField):
                    class _Schema(_ListSchema):
                        @property
                        @override
                        def elementType(self) -> schemas._ProfileSchema: ...

                    @property
                    @override
                    def schema(
                        self,
                    ) -> _ServiceInterfaceModule._StreamInterfaceModule._StreamSchema._StreamInterfaceModuleNextProfilesResultSchema._ProfilesField._Schema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["profiles"],
                    ) -> _ServiceInterfaceModule._StreamInterfaceModule._StreamSchema._StreamInterfaceModuleNextProfilesResultSchema._ProfilesField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ServiceInterfaceModule._StreamInterfaceModule._StreamSchema._StreamInterfaceModuleNextProfilesResultSchema._Fields: ...

            class _Methods(dict[str, _InterfaceMethod[_StructSchema, _StructSchema]]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["nextProfiles"],
                ) -> _InterfaceMethod[
                    _ServiceInterfaceModule._StreamInterfaceModule._StreamSchema._StreamInterfaceModuleNextProfilesParamSchema,
                    _ServiceInterfaceModule._StreamInterfaceModule._StreamSchema._StreamInterfaceModuleNextProfilesResultSchema,
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
                _ServiceInterfaceModule._StreamInterfaceModule._StreamSchema._Methods
            ): ...

        @property
        @override
        def schema(self) -> schemas._ServiceStreamSchema: ...
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> clients.StreamClient: ...
        class Server(_DynamicCapabilityServer):
            def nextProfiles(
                self,
                maxCount: int,
                _context: contexts.NextprofilesCallContext,
                **kwargs: object,
            ) -> Awaitable[
                builders.ProfileClientListBuilder
                | readers.ProfileClientListReader
                | Sequence[Any]
                | results_tuples.NextprofilesResultTuple
                | None
            ]: ...
            def nextProfiles_context(
                self,
                context: contexts.NextprofilesCallContext,
            ) -> Awaitable[None]: ...

    Stream: _StreamInterfaceModule
    type StreamServer = _ServiceInterfaceModule._StreamInterfaceModule.Server

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
                def schema(self) -> _StructSchema: ...

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

        class _ServiceInterfaceModuleCheckAvailableParametersParamSchema(_StructSchema):
            class _MandatoryField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> _EnumSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleCheckAvailableParametersParamSchema._MandatoryField._Schema: ...

            class _OptionalField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> _EnumSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleCheckAvailableParametersParamSchema._OptionalField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["mandatory"],
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleCheckAvailableParametersParamSchema._MandatoryField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["optional"],
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleCheckAvailableParametersParamSchema._OptionalField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["onlyRawData"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleCheckAvailableParametersParamSchema._Fields: ...

        class _ServiceInterfaceModuleCheckAvailableParametersResultSchema(
            _StructSchema,
        ):
            class _MandatoryField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> _EnumSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleCheckAvailableParametersResultSchema._MandatoryField._Schema: ...

            class _OptionalField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> _EnumSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleCheckAvailableParametersResultSchema._OptionalField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["failed"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["mandatory"],
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleCheckAvailableParametersResultSchema._MandatoryField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["optional"],
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleCheckAvailableParametersResultSchema._OptionalField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleCheckAvailableParametersResultSchema._Fields: ...

        class _ServiceInterfaceModuleGetAllAvailableParametersParamSchema(
            _StructSchema,
        ):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["onlyRawData"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleGetAllAvailableParametersParamSchema._Fields: ...

        class _ServiceInterfaceModuleGetAllAvailableParametersResultSchema(
            _StructSchema,
        ):
            class _MandatoryField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> _EnumSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleGetAllAvailableParametersResultSchema._MandatoryField._Schema: ...

            class _OptionalField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> _EnumSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleGetAllAvailableParametersResultSchema._OptionalField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["mandatory"],
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleGetAllAvailableParametersResultSchema._MandatoryField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["optional"],
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleGetAllAvailableParametersResultSchema._OptionalField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleGetAllAvailableParametersResultSchema._Fields: ...

        class _ServiceInterfaceModuleClosestProfilesAtParamSchema(_StructSchema):
            class _CoordField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _StructSchema: ...

            class _QueryField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._QuerySchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["coord"],
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleClosestProfilesAtParamSchema._CoordField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["query"],
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleClosestProfilesAtParamSchema._QueryField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleClosestProfilesAtParamSchema._Fields: ...

        class _ServiceInterfaceModuleClosestProfilesAtResultSchema(_StructSchema):
            class _ProfilesField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> schemas._ProfileSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleClosestProfilesAtResultSchema._ProfilesField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["profiles"],
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleClosestProfilesAtResultSchema._ProfilesField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleClosestProfilesAtResultSchema._Fields: ...

        class _ServiceInterfaceModuleStreamAllProfilesParamSchema(_StructSchema):
            class _MandatoryField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> _EnumSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleStreamAllProfilesParamSchema._MandatoryField._Schema: ...

            class _OptionalField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> _EnumSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleStreamAllProfilesParamSchema._OptionalField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["mandatory"],
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleStreamAllProfilesParamSchema._MandatoryField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["optional"],
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleStreamAllProfilesParamSchema._OptionalField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["onlyRawData"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleStreamAllProfilesParamSchema._Fields: ...

        class _ServiceInterfaceModuleStreamAllProfilesResultSchema(_StructSchema):
            class _AllProfilesField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._ServiceStreamSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["allProfiles"],
                ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleStreamAllProfilesResultSchema._AllProfilesField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleStreamAllProfilesResultSchema._Fields: ...

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
                key: Literal["checkAvailableParameters"],
            ) -> _InterfaceMethod[
                _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleCheckAvailableParametersParamSchema,
                _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleCheckAvailableParametersResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["getAllAvailableParameters"],
            ) -> _InterfaceMethod[
                _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleGetAllAvailableParametersParamSchema,
                _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleGetAllAvailableParametersResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["closestProfilesAt"],
            ) -> _InterfaceMethod[
                _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleClosestProfilesAtParamSchema,
                _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleClosestProfilesAtResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["streamAllProfiles"],
            ) -> _InterfaceMethod[
                _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleStreamAllProfilesParamSchema,
                _ServiceInterfaceModule._ServiceSchema._ServiceInterfaceModuleStreamAllProfilesResultSchema,
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
        def checkAvailableParameters(
            self,
            mandatory: readers.PropertyNameEnumListReader,
            optional: readers.PropertyNameEnumListReader,
            onlyRawData: bool,
            _context: contexts.CheckavailableparametersCallContext,
            **kwargs: object,
        ) -> Awaitable[results_tuples.CheckavailableparametersResultTuple | None]: ...
        def checkAvailableParameters_context(
            self,
            context: contexts.CheckavailableparametersCallContext,
        ) -> Awaitable[None]: ...
        def getAllAvailableParameters(
            self,
            onlyRawData: bool,
            _context: contexts.GetallavailableparametersCallContext,
            **kwargs: object,
        ) -> Awaitable[results_tuples.GetallavailableparametersResultTuple | None]: ...
        def getAllAvailableParameters_context(
            self,
            context: contexts.GetallavailableparametersCallContext,
        ) -> Awaitable[None]: ...
        def closestProfilesAt(
            self,
            coord: LatLonCoordReader,
            query: readers.QueryReader,
            _context: contexts.ClosestprofilesatCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.ProfileClientListBuilder
            | readers.ProfileClientListReader
            | Sequence[Any]
            | results_tuples.ClosestprofilesatResultTuple
            | None
        ]: ...
        def closestProfilesAt_context(
            self,
            context: contexts.ClosestprofilesatCallContext,
        ) -> Awaitable[None]: ...
        def streamAllProfiles(
            self,
            mandatory: readers.PropertyNameEnumListReader,
            optional: readers.PropertyNameEnumListReader,
            onlyRawData: bool,
            _context: contexts.StreamallprofilesCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _ServiceInterfaceModule._StreamInterfaceModule.Server
            | clients.StreamClient
            | results_tuples.StreamallprofilesResultTuple
            | None
        ]: ...
        def streamAllProfiles_context(
            self,
            context: contexts.StreamallprofilesCallContext,
        ) -> Awaitable[None]: ...
