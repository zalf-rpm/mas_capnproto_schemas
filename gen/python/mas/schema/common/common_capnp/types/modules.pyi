"""Module helper types for `common.capnp`."""

from collections.abc import Awaitable, Callable
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityServer,
    _DynamicObjectReader,
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

from mas.schema.common.common_capnp.types import builders as builders
from mas.schema.common.common_capnp.types import clients as clients
from mas.schema.common.common_capnp.types import common as common
from mas.schema.common.common_capnp.types import contexts as contexts
from mas.schema.common.common_capnp.types import enums as enums
from mas.schema.common.common_capnp.types import readers as readers
from mas.schema.common.common_capnp.types import schemas as schemas
from mas.schema.common.common_capnp.types.results import tuples as results_tuples

class _IdInformationStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _IdInformationSchema(_StructSchema):
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
        ) -> _IdInformationStructModule._IdInformationSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._IdInformationSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        id: str | None = None,
        name: str | None = None,
        description: str | None = None,
        **kwargs: object,
    ) -> builders.IdInformationBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.IdInformationReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.IdInformationReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.IdInformationBuilder]: ...
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
    ) -> readers.IdInformationReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.IdInformationReader: ...

class _IdentifiableInterfaceModule(_InterfaceModule):
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.IdentifiableClient: ...
    class Server(_DynamicCapabilityServer):
        def info(
            self,
            _context: contexts.InfoCallContext,
            **kwargs: object,
        ) -> Awaitable[results_tuples.InfoResultTuple | None]: ...
        def info_context(
            self,
            context: contexts.InfoCallContext,
        ) -> Awaitable[None]: ...

class _StructuredTextStructModule(_StructModule):
    class _TypeEnumModule(_EnumModule):
        unstructured: int
        json: int
        xml: int
        toml: int
        sturdyRef: int

        class _TypeSchema(_EnumSchema): ...

        @property
        @override
        def schema(self) -> schemas._StructuredTextTypeEnumSchema: ...

    Type: _TypeEnumModule
    class _StructuredTextStructureStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _StructuredTextStructureSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["none"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["json"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["xml"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["toml"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _StructuredTextStructModule._StructuredTextStructureStructModule._StructuredTextStructureSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._StructuredTextStructuredTextStructureSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            none: None | None = None,
            json: None | None = None,
            xml: None | None = None,
            toml: None | None = None,
            **kwargs: object,
        ) -> builders.StructuredTextStructureBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.StructuredTextStructureReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.StructuredTextStructureReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.StructuredTextStructureBuilder]: ...
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
        ) -> readers.StructuredTextStructureReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.StructuredTextStructureReader: ...

    StructuredTextStructure: _StructuredTextStructureStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _StructuredTextSchema(_StructSchema):
        class _StructureField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _StructSchema: ...

        class _TypeField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._StructuredTextTypeEnumSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["value"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["structure"],
            ) -> _StructuredTextStructModule._StructuredTextSchema._StructureField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["type"],
            ) -> _StructuredTextStructModule._StructuredTextSchema._TypeField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _StructuredTextStructModule._StructuredTextSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._StructuredTextSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        value: str | None = None,
        structure: builders.StructuredTextStructureBuilder
        | dict[str, Any]
        | None = None,
        type: enums.StructuredTextTypeEnum | None = None,
        **kwargs: object,
    ) -> builders.StructuredTextBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.StructuredTextReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.StructuredTextReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.StructuredTextBuilder]: ...
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
    ) -> readers.StructuredTextReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.StructuredTextReader: ...

class _PairStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _PairSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["fst"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["snd"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _PairStructModule._PairSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._PairSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        fst: common.AnyPointer | None = None,
        snd: common.AnyPointer | None = None,
        **kwargs: object,
    ) -> builders.PairBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.PairReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.PairReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.PairBuilder]: ...
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
    ) -> readers.PairReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.PairReader: ...

class _ValueStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _ValueSchema(_StructSchema):
        class _Lf64Field(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _Lf32Field(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _Li64Field(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _Li32Field(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _Li16Field(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _Li8Field(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _Lui64Field(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _Lui32Field(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _Lui16Field(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _Lui8Field(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _LbField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _LtField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _LdField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _LcapField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _ListSchema: ...

        class _LpairField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._PairSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _ValueStructModule._ValueSchema._LpairField._Schema: ...

        class _LvField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._ValueSchema: ...

            @property
            @override
            def schema(self) -> _ValueStructModule._ValueSchema._LvField._Schema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["f64"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["f32"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["i64"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["i32"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["i16"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["i8"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["ui64"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["ui32"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["ui16"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["ui8"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["b"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["t"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["d"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["p"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["cap"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["lf64"],
            ) -> _ValueStructModule._ValueSchema._Lf64Field: ...
            @overload
            def __getitem__(
                self,
                key: Literal["lf32"],
            ) -> _ValueStructModule._ValueSchema._Lf32Field: ...
            @overload
            def __getitem__(
                self,
                key: Literal["li64"],
            ) -> _ValueStructModule._ValueSchema._Li64Field: ...
            @overload
            def __getitem__(
                self,
                key: Literal["li32"],
            ) -> _ValueStructModule._ValueSchema._Li32Field: ...
            @overload
            def __getitem__(
                self,
                key: Literal["li16"],
            ) -> _ValueStructModule._ValueSchema._Li16Field: ...
            @overload
            def __getitem__(
                self,
                key: Literal["li8"],
            ) -> _ValueStructModule._ValueSchema._Li8Field: ...
            @overload
            def __getitem__(
                self,
                key: Literal["lui64"],
            ) -> _ValueStructModule._ValueSchema._Lui64Field: ...
            @overload
            def __getitem__(
                self,
                key: Literal["lui32"],
            ) -> _ValueStructModule._ValueSchema._Lui32Field: ...
            @overload
            def __getitem__(
                self,
                key: Literal["lui16"],
            ) -> _ValueStructModule._ValueSchema._Lui16Field: ...
            @overload
            def __getitem__(
                self,
                key: Literal["lui8"],
            ) -> _ValueStructModule._ValueSchema._Lui8Field: ...
            @overload
            def __getitem__(
                self,
                key: Literal["lb"],
            ) -> _ValueStructModule._ValueSchema._LbField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["lt"],
            ) -> _ValueStructModule._ValueSchema._LtField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["ld"],
            ) -> _ValueStructModule._ValueSchema._LdField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["lcap"],
            ) -> _ValueStructModule._ValueSchema._LcapField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["lpair"],
            ) -> _ValueStructModule._ValueSchema._LpairField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["lv"],
            ) -> _ValueStructModule._ValueSchema._LvField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _ValueStructModule._ValueSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._ValueSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        f64: float | None = None,
        f32: float | None = None,
        i64: int | None = None,
        i32: int | None = None,
        i16: int | None = None,
        i8: int | None = None,
        ui64: int | None = None,
        ui32: int | None = None,
        ui16: int | None = None,
        ui8: int | None = None,
        b: bool | None = None,
        t: str | None = None,
        d: bytes | None = None,
        p: common.AnyPointer | None = None,
        cap: common.Capability | None = None,
        lf64: builders.Float64ListBuilder | dict[str, Any] | None = None,
        lf32: builders.Float32ListBuilder | dict[str, Any] | None = None,
        li64: builders.Int64ListBuilder | dict[str, Any] | None = None,
        li32: builders.Int32ListBuilder | dict[str, Any] | None = None,
        li16: builders.Int16ListBuilder | dict[str, Any] | None = None,
        li8: builders.Int8ListBuilder | dict[str, Any] | None = None,
        lui64: builders.Uint64ListBuilder | dict[str, Any] | None = None,
        lui32: builders.Uint32ListBuilder | dict[str, Any] | None = None,
        lui16: builders.Uint16ListBuilder | dict[str, Any] | None = None,
        lui8: builders.Uint8ListBuilder | dict[str, Any] | None = None,
        lb: builders.BoolListBuilder | dict[str, Any] | None = None,
        lt: builders.TextListBuilder | dict[str, Any] | None = None,
        ld: builders.DataListBuilder | dict[str, Any] | None = None,
        lcap: builders.AnyPointerListBuilder | dict[str, Any] | None = None,
        lpair: builders.PairListBuilder | dict[str, Any] | None = None,
        lv: builders.ValueListBuilder | dict[str, Any] | None = None,
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

class _FactoryInterfaceModule(_IdentifiableInterfaceModule):
    class _FactorySchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _FactoryInterfaceModule._FactorySchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

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
            ) -> _FactoryInterfaceModule._FactorySchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

        class _IdentifiableInterfaceModuleInfoMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _FactoryInterfaceModule._FactorySchema._IdentifiableInterfaceModuleInfoParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _FactoryInterfaceModule._FactorySchema._IdentifiableInterfaceModuleInfoResultSchema: ...

        class _FactoryInterfaceModuleCreateParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleCreateParamSchema._Fields: ...

        class _FactoryInterfaceModuleCreateResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["out"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleCreateResultSchema._Fields: ...

        class _FactoryInterfaceModuleCreateMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleCreateParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleCreateResultSchema: ...

        class _Methods(dict[str, _InterfaceMethod]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _FactoryInterfaceModule._FactorySchema._IdentifiableInterfaceModuleInfoMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["create"],
            ) -> _FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleCreateMethod: ...
            @overload
            def __getitem__(self, key: str) -> _InterfaceMethod: ...

        @property
        @override
        def methods(self) -> _FactoryInterfaceModule._FactorySchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._FactorySchema: ...
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.FactoryClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def create(
            self,
            _context: contexts.CreateCallContext,
            **kwargs: object,
        ) -> Awaitable[common.AnyPointer | results_tuples.CreateResultTuple | None]: ...
        def create_context(
            self,
            context: contexts.CreateCallContext,
        ) -> Awaitable[None]: ...

class _IOFactoryInterfaceModule(_IdentifiableInterfaceModule):
    class _IOFactorySchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _IOFactoryInterfaceModule._IOFactorySchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

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
            ) -> _IOFactoryInterfaceModule._IOFactorySchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

        class _IdentifiableInterfaceModuleInfoMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _IOFactoryInterfaceModule._IOFactorySchema._IdentifiableInterfaceModuleInfoParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _IOFactoryInterfaceModule._IOFactorySchema._IdentifiableInterfaceModuleInfoResultSchema: ...

        class _IOFactoryInterfaceModuleProduceParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["in"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _IOFactoryInterfaceModule._IOFactorySchema._IOFactoryInterfaceModuleProduceParamSchema._Fields: ...

        class _IOFactoryInterfaceModuleProduceResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["out"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _IOFactoryInterfaceModule._IOFactorySchema._IOFactoryInterfaceModuleProduceResultSchema._Fields: ...

        class _IOFactoryInterfaceModuleProduceMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _IOFactoryInterfaceModule._IOFactorySchema._IOFactoryInterfaceModuleProduceParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _IOFactoryInterfaceModule._IOFactorySchema._IOFactoryInterfaceModuleProduceResultSchema: ...

        class _Methods(dict[str, _InterfaceMethod]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _IOFactoryInterfaceModule._IOFactorySchema._IdentifiableInterfaceModuleInfoMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["produce"],
            ) -> _IOFactoryInterfaceModule._IOFactorySchema._IOFactoryInterfaceModuleProduceMethod: ...
            @overload
            def __getitem__(self, key: str) -> _InterfaceMethod: ...

        @property
        @override
        def methods(self) -> _IOFactoryInterfaceModule._IOFactorySchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._IOFactorySchema: ...
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.IOFactoryClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def produce(
            self,
            in_: _DynamicObjectReader,
            _context: contexts.ProduceCallContext,
            **kwargs: object,
        ) -> Awaitable[
            common.AnyPointer | results_tuples.ProduceResultTuple | None
        ]: ...
        def produce_context(
            self,
            context: contexts.ProduceCallContext,
        ) -> Awaitable[None]: ...

class _HolderInterfaceModule(_InterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> clients.HolderClient: ...
    class Server(_DynamicCapabilityServer):
        def value(
            self,
            _context: contexts.ValueCallContext,
            **kwargs: object,
        ) -> Awaitable[common.AnyPointer | results_tuples.ValueResultTuple | None]: ...
        def value_context(
            self,
            context: contexts.ValueCallContext,
        ) -> Awaitable[None]: ...

class _IdentifiableHolderInterfaceModule(
    _IdentifiableInterfaceModule,
    _HolderInterfaceModule,
):
    class _IdentifiableHolderSchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _IdentifiableHolderInterfaceModule._IdentifiableHolderSchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

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
            ) -> _IdentifiableHolderInterfaceModule._IdentifiableHolderSchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

        class _IdentifiableInterfaceModuleInfoMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _IdentifiableHolderInterfaceModule._IdentifiableHolderSchema._IdentifiableInterfaceModuleInfoParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _IdentifiableHolderInterfaceModule._IdentifiableHolderSchema._IdentifiableInterfaceModuleInfoResultSchema: ...

        class _HolderInterfaceModuleValueParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _IdentifiableHolderInterfaceModule._IdentifiableHolderSchema._HolderInterfaceModuleValueParamSchema._Fields: ...

        class _HolderInterfaceModuleValueResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["value"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _IdentifiableHolderInterfaceModule._IdentifiableHolderSchema._HolderInterfaceModuleValueResultSchema._Fields: ...

        class _HolderInterfaceModuleValueMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _IdentifiableHolderInterfaceModule._IdentifiableHolderSchema._HolderInterfaceModuleValueParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _IdentifiableHolderInterfaceModule._IdentifiableHolderSchema._HolderInterfaceModuleValueResultSchema: ...

        class _Methods(dict[str, _InterfaceMethod]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _IdentifiableHolderInterfaceModule._IdentifiableHolderSchema._IdentifiableInterfaceModuleInfoMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["value"],
            ) -> _IdentifiableHolderInterfaceModule._IdentifiableHolderSchema._HolderInterfaceModuleValueMethod: ...
            @overload
            def __getitem__(self, key: str) -> _InterfaceMethod: ...

        @property
        @override
        def methods(
            self,
        ) -> _IdentifiableHolderInterfaceModule._IdentifiableHolderSchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._IdentifiableHolderSchema: ...
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.IdentifiableHolderClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _HolderInterfaceModule.Server,
    ): ...
