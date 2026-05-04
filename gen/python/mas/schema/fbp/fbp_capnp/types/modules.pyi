"""Module helper types for `fbp.capnp`."""

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

from mas.schema.common.common_capnp.types import (
    schemas as _mas_schema_common_common_capnp_schemas,
)
from mas.schema.common.common_capnp.types.builders import (
    IdInformationBuilder,
    StructuredTextBuilder,
    ValueBuilder,
)
from mas.schema.common.common_capnp.types.modules import (
    _IdentifiableInterfaceModule,
)
from mas.schema.common.common_capnp.types.readers import ValueReader
from mas.schema.fbp.fbp_capnp.types import builders as builders
from mas.schema.fbp.fbp_capnp.types import clients as clients
from mas.schema.fbp.fbp_capnp.types import common as common
from mas.schema.fbp.fbp_capnp.types import contexts as contexts
from mas.schema.fbp.fbp_capnp.types import enums as enums
from mas.schema.fbp.fbp_capnp.types import readers as readers
from mas.schema.fbp.fbp_capnp.types import schemas as schemas
from mas.schema.fbp.fbp_capnp.types import servers as servers
from mas.schema.fbp.fbp_capnp.types.results import tuples as results_tuples
from mas.schema.persistence.persistence_capnp.types import (
    schemas as _mas_schema_persistence_persistence_capnp_schemas,
)
from mas.schema.persistence.persistence_capnp.types.builders import SturdyRefBuilder
from mas.schema.persistence.persistence_capnp.types.modules import (
    _GatewayRegistrableInterfaceModule,
    _PersistentInterfaceModule,
)
from mas.schema.persistence.persistence_capnp.types.readers import SturdyRefReader

class _IPStructModule(_StructModule):
    class _KVStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _KVSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["key"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["desc"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["value"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(self) -> _IPStructModule._KVStructModule._KVSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._IPKVSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            key: str | None = None,
            desc: str | None = None,
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
    class _TypeEnumModule(_EnumModule):
        standard: int
        openBracket: int
        closeBracket: int

        class _TypeSchema(_EnumSchema): ...

        @property
        @override
        def schema(self) -> schemas._IPTypeEnumSchema: ...

    Type: _TypeEnumModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _IPSchema(_StructSchema):
        class _AttributesField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._IPKVSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _IPStructModule._IPSchema._AttributesField._Schema: ...

        class _TypeField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._IPTypeEnumSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["attributes"],
            ) -> _IPStructModule._IPSchema._AttributesField: ...
            @overload
            def __getitem__(self, key: Literal["content"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["type"],
            ) -> _IPStructModule._IPSchema._TypeField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _IPStructModule._IPSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._IPSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        attributes: builders.KVListBuilder | dict[str, Any] | None = None,
        content: common.AnyPointer | None = None,
        type: enums.IPTypeEnum | None = None,
        **kwargs: object,
    ) -> builders.IPBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.IPReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.IPReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.IPBuilder]: ...
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
    ) -> readers.IPReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.IPReader: ...

class _IIPStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _IIPSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["content"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _IIPStructModule._IIPSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._IIPSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        content: common.AnyPointer | None = None,
        **kwargs: object,
    ) -> builders.IIPBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.IIPReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.IIPReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.IIPBuilder]: ...
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
    ) -> readers.IIPReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.IIPReader: ...

class _ChannelInterfaceModule(_IdentifiableInterfaceModule, _PersistentInterfaceModule):
    class _CloseSemanticsEnumModule(_EnumModule):
        fbp: int
        no: int

        class _CloseSemanticsSchema(_EnumSchema): ...

        @property
        @override
        def schema(self) -> schemas._ChannelCloseSemanticsEnumSchema: ...

    CloseSemantics: _CloseSemanticsEnumModule
    class _MsgStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _MsgSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["value"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["done"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["noMsg"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ChannelInterfaceModule._MsgStructModule._MsgSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._ChannelMsgSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            value: common.AnyPointer | None = None,
            done: None | None = None,
            noMsg: None | None = None,
            **kwargs: object,
        ) -> builders.MsgBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.MsgReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.MsgReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.MsgBuilder]: ...
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
        ) -> readers.MsgReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.MsgReader: ...

    Msg: _MsgStructModule
    class _ReaderInterfaceModule(
        _IdentifiableInterfaceModule,
        _PersistentInterfaceModule,
    ):
        class _ReaderSchema(_InterfaceSchema):
            class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

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
                ) -> _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

            class _IdentifiableInterfaceModuleInfoMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._IdentifiableInterfaceModuleInfoParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._IdentifiableInterfaceModuleInfoResultSchema: ...

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
                    ) -> _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._PersistentInterfaceModuleSaveParamSchema._SealForField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._PersistentInterfaceModuleSaveParamSchema._Fields: ...

            class _PersistentInterfaceModuleSaveResultSchema(_StructSchema):
                class _SturdyRefField(_StructSchemaField):
                    @property
                    @override
                    def schema(
                        self,
                    ) -> _mas_schema_persistence_persistence_capnp_schemas._SturdyRefSchema: ...

                class _UnsaveSRField(_StructSchemaField):
                    @property
                    @override
                    def schema(
                        self,
                    ) -> _mas_schema_persistence_persistence_capnp_schemas._SturdyRefSchema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["sturdyRef"],
                    ) -> _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._PersistentInterfaceModuleSaveResultSchema._SturdyRefField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["unsaveSR"],
                    ) -> _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._PersistentInterfaceModuleSaveResultSchema._UnsaveSRField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._PersistentInterfaceModuleSaveResultSchema._Fields: ...

            class _PersistentInterfaceModuleSaveMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._PersistentInterfaceModuleSaveParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._PersistentInterfaceModuleSaveResultSchema: ...

            class _ReaderInterfaceModuleReadParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._ReaderInterfaceModuleReadParamSchema._Fields: ...

            class _ReaderInterfaceModuleReadResultSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["value"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["done"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["noMsg"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._ReaderInterfaceModuleReadResultSchema._Fields: ...

            class _ReaderInterfaceModuleReadMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._ReaderInterfaceModuleReadParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._ReaderInterfaceModuleReadResultSchema: ...

            class _ReaderInterfaceModuleCloseParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._ReaderInterfaceModuleCloseParamSchema._Fields: ...

            class _ReaderInterfaceModuleCloseResultSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._ReaderInterfaceModuleCloseResultSchema._Fields: ...

            class _ReaderInterfaceModuleCloseMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._ReaderInterfaceModuleCloseParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._ReaderInterfaceModuleCloseResultSchema: ...

            class _ReaderInterfaceModuleReadIfMsgParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._ReaderInterfaceModuleReadIfMsgParamSchema._Fields: ...

            class _ReaderInterfaceModuleReadIfMsgResultSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["value"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["done"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["noMsg"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._ReaderInterfaceModuleReadIfMsgResultSchema._Fields: ...

            class _ReaderInterfaceModuleReadIfMsgMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._ReaderInterfaceModuleReadIfMsgParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._ReaderInterfaceModuleReadIfMsgResultSchema: ...

            class _Methods(dict[str, _InterfaceMethod]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["info"],
                ) -> _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._IdentifiableInterfaceModuleInfoMethod: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["save"],
                ) -> _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._PersistentInterfaceModuleSaveMethod: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["read"],
                ) -> _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._ReaderInterfaceModuleReadMethod: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["close"],
                ) -> _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._ReaderInterfaceModuleCloseMethod: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["readIfMsg"],
                ) -> _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._ReaderInterfaceModuleReadIfMsgMethod: ...
                @overload
                def __getitem__(self, key: str) -> _InterfaceMethod: ...

            @property
            @override
            def methods(
                self,
            ) -> (
                _ChannelInterfaceModule._ReaderInterfaceModule._ReaderSchema._Methods
            ): ...

        @property
        @override
        def schema(self) -> schemas._ChannelReaderSchema: ...
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> clients.ReaderClient: ...
        class Server(
            _IdentifiableInterfaceModule.Server,
            _PersistentInterfaceModule.Server,
        ):
            def read(
                self,
                _context: contexts.ReadCallContext,
                **kwargs: object,
            ) -> Awaitable[results_tuples.ReadResultTuple | None]: ...
            def read_context(
                self,
                context: contexts.ReadCallContext,
            ) -> Awaitable[None]: ...
            def close(
                self,
                _context: contexts.ReaderCloseCallContext,
                **kwargs: object,
            ) -> Awaitable[None]: ...
            def close_context(
                self,
                context: contexts.ReaderCloseCallContext,
            ) -> Awaitable[None]: ...
            def readIfMsg(
                self,
                _context: contexts.ReadifmsgCallContext,
                **kwargs: object,
            ) -> Awaitable[results_tuples.ReadifmsgResultTuple | None]: ...
            def readIfMsg_context(
                self,
                context: contexts.ReadifmsgCallContext,
            ) -> Awaitable[None]: ...

    Reader: _ReaderInterfaceModule
    type ReaderServer = _ChannelInterfaceModule._ReaderInterfaceModule.Server
    class _WriterInterfaceModule(
        _IdentifiableInterfaceModule,
        _PersistentInterfaceModule,
    ):
        class _WriterSchema(_InterfaceSchema):
            class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

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
                ) -> _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

            class _IdentifiableInterfaceModuleInfoMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._IdentifiableInterfaceModuleInfoParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._IdentifiableInterfaceModuleInfoResultSchema: ...

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
                    ) -> _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._PersistentInterfaceModuleSaveParamSchema._SealForField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._PersistentInterfaceModuleSaveParamSchema._Fields: ...

            class _PersistentInterfaceModuleSaveResultSchema(_StructSchema):
                class _SturdyRefField(_StructSchemaField):
                    @property
                    @override
                    def schema(
                        self,
                    ) -> _mas_schema_persistence_persistence_capnp_schemas._SturdyRefSchema: ...

                class _UnsaveSRField(_StructSchemaField):
                    @property
                    @override
                    def schema(
                        self,
                    ) -> _mas_schema_persistence_persistence_capnp_schemas._SturdyRefSchema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["sturdyRef"],
                    ) -> _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._PersistentInterfaceModuleSaveResultSchema._SturdyRefField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["unsaveSR"],
                    ) -> _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._PersistentInterfaceModuleSaveResultSchema._UnsaveSRField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._PersistentInterfaceModuleSaveResultSchema._Fields: ...

            class _PersistentInterfaceModuleSaveMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._PersistentInterfaceModuleSaveParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._PersistentInterfaceModuleSaveResultSchema: ...

            class _WriterInterfaceModuleWriteParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["value"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["done"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["noMsg"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._WriterInterfaceModuleWriteParamSchema._Fields: ...

            class _WriterInterfaceModuleWriteResultSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._WriterInterfaceModuleWriteResultSchema._Fields: ...

            class _WriterInterfaceModuleWriteMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._WriterInterfaceModuleWriteParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._WriterInterfaceModuleWriteResultSchema: ...

            class _WriterInterfaceModuleCloseParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._WriterInterfaceModuleCloseParamSchema._Fields: ...

            class _WriterInterfaceModuleCloseResultSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._WriterInterfaceModuleCloseResultSchema._Fields: ...

            class _WriterInterfaceModuleCloseMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._WriterInterfaceModuleCloseParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._WriterInterfaceModuleCloseResultSchema: ...

            class _WriterInterfaceModuleWriteIfSpaceParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["value"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["done"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["noMsg"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._WriterInterfaceModuleWriteIfSpaceParamSchema._Fields: ...

            class _WriterInterfaceModuleWriteIfSpaceResultSchema(_StructSchema):
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
                ) -> _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._WriterInterfaceModuleWriteIfSpaceResultSchema._Fields: ...

            class _WriterInterfaceModuleWriteIfSpaceMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._WriterInterfaceModuleWriteIfSpaceParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._WriterInterfaceModuleWriteIfSpaceResultSchema: ...

            class _Methods(dict[str, _InterfaceMethod]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["info"],
                ) -> _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._IdentifiableInterfaceModuleInfoMethod: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["save"],
                ) -> _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._PersistentInterfaceModuleSaveMethod: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["write"],
                ) -> _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._WriterInterfaceModuleWriteMethod: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["close"],
                ) -> _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._WriterInterfaceModuleCloseMethod: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["writeIfSpace"],
                ) -> _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._WriterInterfaceModuleWriteIfSpaceMethod: ...
                @overload
                def __getitem__(self, key: str) -> _InterfaceMethod: ...

            @property
            @override
            def methods(
                self,
            ) -> (
                _ChannelInterfaceModule._WriterInterfaceModule._WriterSchema._Methods
            ): ...

        @property
        @override
        def schema(self) -> schemas._ChannelWriterSchema: ...
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> clients.WriterClient: ...
        class Server(
            _IdentifiableInterfaceModule.Server,
            _PersistentInterfaceModule.Server,
        ):
            def write_context(
                self,
                context: contexts.WriteCallContext,
            ) -> Awaitable[None]: ...
            def close(
                self,
                _context: contexts.WriterCloseCallContext,
                **kwargs: object,
            ) -> Awaitable[None]: ...
            def close_context(
                self,
                context: contexts.WriterCloseCallContext,
            ) -> Awaitable[None]: ...
            def writeIfSpace_context(
                self,
                context: contexts.WriteifspaceCallContext,
            ) -> Awaitable[None]: ...

    Writer: _WriterInterfaceModule
    type WriterServer = _ChannelInterfaceModule._WriterInterfaceModule.Server
    class _StartupInfoStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _StartupInfoSchema(_StructSchema):
            class _CloseSemanticsField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._ChannelCloseSemanticsEnumSchema: ...

            class _ChannelSRField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> (
                    _mas_schema_persistence_persistence_capnp_schemas._SturdyRefSchema
                ): ...

            class _ReaderSRsField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(
                        self,
                    ) -> _mas_schema_persistence_persistence_capnp_schemas._SturdyRefSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _ChannelInterfaceModule._StartupInfoStructModule._StartupInfoSchema._ReaderSRsField._Schema: ...

            class _WriterSRsField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(
                        self,
                    ) -> _mas_schema_persistence_persistence_capnp_schemas._SturdyRefSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _ChannelInterfaceModule._StartupInfoStructModule._StartupInfoSchema._WriterSRsField._Schema: ...

            class _ChannelField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._ChannelSchema: ...

            class _ReadersField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> schemas._ChannelReaderSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _ChannelInterfaceModule._StartupInfoStructModule._StartupInfoSchema._ReadersField._Schema: ...

            class _WritersField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> schemas._ChannelWriterSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _ChannelInterfaceModule._StartupInfoStructModule._StartupInfoSchema._WritersField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["bufferSize"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["closeSemantics"],
                ) -> _ChannelInterfaceModule._StartupInfoStructModule._StartupInfoSchema._CloseSemanticsField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["channelSR"],
                ) -> _ChannelInterfaceModule._StartupInfoStructModule._StartupInfoSchema._ChannelSRField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["readerSRs"],
                ) -> _ChannelInterfaceModule._StartupInfoStructModule._StartupInfoSchema._ReaderSRsField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["writerSRs"],
                ) -> _ChannelInterfaceModule._StartupInfoStructModule._StartupInfoSchema._WriterSRsField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["channel"],
                ) -> _ChannelInterfaceModule._StartupInfoStructModule._StartupInfoSchema._ChannelField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["readers"],
                ) -> _ChannelInterfaceModule._StartupInfoStructModule._StartupInfoSchema._ReadersField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["writers"],
                ) -> _ChannelInterfaceModule._StartupInfoStructModule._StartupInfoSchema._WritersField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ChannelInterfaceModule._StartupInfoStructModule._StartupInfoSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._ChannelStartupInfoSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            bufferSize: int | None = None,
            closeSemantics: enums.ChannelCloseSemanticsEnum | None = None,
            channelSR: SturdyRefBuilder | dict[str, Any] | None = None,
            readerSRs: builders.SturdyRefListBuilder | dict[str, Any] | None = None,
            writerSRs: builders.SturdyRefListBuilder | dict[str, Any] | None = None,
            channel: clients.ChannelClient
            | _ChannelInterfaceModule.Server
            | None = None,
            readers: builders.ReaderClientListBuilder | dict[str, Any] | None = None,
            writers: builders.WriterClientListBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> builders.StartupInfoBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.StartupInfoReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.StartupInfoReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.StartupInfoBuilder]: ...
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
        ) -> readers.StartupInfoReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.StartupInfoReader: ...

    StartupInfo: _StartupInfoStructModule
    class _StatsCallbackInterfaceModule(_InterfaceModule):
        class _StatsStructModule(_StructModule):
            class Reader(_DynamicStructReader): ...
            class Builder(_DynamicStructBuilder): ...

            class _StatsSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["noOfWaitingWriters"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["noOfWaitingReaders"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["noOfIpsInQueue"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["totalNoOfIpsReceived"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["timestamp"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["updateIntervalInMs"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ChannelInterfaceModule._StatsCallbackInterfaceModule._StatsStructModule._StatsSchema._Fields: ...

            @property
            @override
            def schema(self) -> schemas._ChannelStatsCallbackStatsSchema: ...
            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
                noOfWaitingWriters: int | None = None,
                noOfWaitingReaders: int | None = None,
                noOfIpsInQueue: int | None = None,
                totalNoOfIpsReceived: int | None = None,
                timestamp: str | None = None,
                updateIntervalInMs: int | None = None,
                **kwargs: object,
            ) -> builders.StatsBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[readers.StatsReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[readers.StatsReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[builders.StatsBuilder]: ...
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
            ) -> readers.StatsReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> readers.StatsReader: ...

        Stats: _StatsStructModule
        class _UnregisterInterfaceModule(_InterfaceModule):
            class _UnregisterSchema(_InterfaceSchema):
                class _UnregisterInterfaceModuleUnregParamSchema(_StructSchema):
                    class _Fields(dict[str, _StructSchemaField]): ...

                    @property
                    @override
                    def fields(
                        self,
                    ) -> _ChannelInterfaceModule._StatsCallbackInterfaceModule._UnregisterInterfaceModule._UnregisterSchema._UnregisterInterfaceModuleUnregParamSchema._Fields: ...

                class _UnregisterInterfaceModuleUnregResultSchema(_StructSchema):
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
                    ) -> _ChannelInterfaceModule._StatsCallbackInterfaceModule._UnregisterInterfaceModule._UnregisterSchema._UnregisterInterfaceModuleUnregResultSchema._Fields: ...

                class _UnregisterInterfaceModuleUnregMethod(_InterfaceMethod):
                    @property
                    @override
                    def param_type(
                        self,
                    ) -> _ChannelInterfaceModule._StatsCallbackInterfaceModule._UnregisterInterfaceModule._UnregisterSchema._UnregisterInterfaceModuleUnregParamSchema: ...
                    @property
                    @override
                    def result_type(
                        self,
                    ) -> _ChannelInterfaceModule._StatsCallbackInterfaceModule._UnregisterInterfaceModule._UnregisterSchema._UnregisterInterfaceModuleUnregResultSchema: ...

                class _Methods(dict[str, _InterfaceMethod]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["unreg"],
                    ) -> _ChannelInterfaceModule._StatsCallbackInterfaceModule._UnregisterInterfaceModule._UnregisterSchema._UnregisterInterfaceModuleUnregMethod: ...
                    @overload
                    def __getitem__(self, key: str) -> _InterfaceMethod: ...

                @property
                @override
                def methods(
                    self,
                ) -> _ChannelInterfaceModule._StatsCallbackInterfaceModule._UnregisterInterfaceModule._UnregisterSchema._Methods: ...

            @property
            @override
            def schema(self) -> schemas._ChannelStatsCallbackUnregisterSchema: ...
            @override
            def _new_client(
                self,
                server: _DynamicCapabilityServer,
            ) -> clients.UnregisterClient: ...
            class Server(_DynamicCapabilityServer):
                def unreg(
                    self,
                    _context: contexts.UnregCallContext,
                    **kwargs: object,
                ) -> Awaitable[bool | results_tuples.UnregResultTuple | None]: ...
                def unreg_context(
                    self,
                    context: contexts.UnregCallContext,
                ) -> Awaitable[None]: ...

        Unregister: _UnregisterInterfaceModule
        type UnregisterServer = _ChannelInterfaceModule._StatsCallbackInterfaceModule._UnregisterInterfaceModule.Server

        class _StatsCallbackSchema(_InterfaceSchema):
            class _StatsCallbackInterfaceModuleStatusParamSchema(_StructSchema):
                class _StatsField(_StructSchemaField):
                    @property
                    @override
                    def schema(self) -> schemas._ChannelStatsCallbackStatsSchema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["stats"],
                    ) -> _ChannelInterfaceModule._StatsCallbackInterfaceModule._StatsCallbackSchema._StatsCallbackInterfaceModuleStatusParamSchema._StatsField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ChannelInterfaceModule._StatsCallbackInterfaceModule._StatsCallbackSchema._StatsCallbackInterfaceModuleStatusParamSchema._Fields: ...

            class _StatsCallbackInterfaceModuleStatusResultSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ChannelInterfaceModule._StatsCallbackInterfaceModule._StatsCallbackSchema._StatsCallbackInterfaceModuleStatusResultSchema._Fields: ...

            class _StatsCallbackInterfaceModuleStatusMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ChannelInterfaceModule._StatsCallbackInterfaceModule._StatsCallbackSchema._StatsCallbackInterfaceModuleStatusParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ChannelInterfaceModule._StatsCallbackInterfaceModule._StatsCallbackSchema._StatsCallbackInterfaceModuleStatusResultSchema: ...

            class _Methods(dict[str, _InterfaceMethod]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["status"],
                ) -> _ChannelInterfaceModule._StatsCallbackInterfaceModule._StatsCallbackSchema._StatsCallbackInterfaceModuleStatusMethod: ...
                @overload
                def __getitem__(self, key: str) -> _InterfaceMethod: ...

            @property
            @override
            def methods(
                self,
            ) -> _ChannelInterfaceModule._StatsCallbackInterfaceModule._StatsCallbackSchema._Methods: ...

        @property
        @override
        def schema(self) -> schemas._ChannelStatsCallbackSchema: ...
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> clients.StatsCallbackClient: ...
        class Server(_DynamicCapabilityServer):
            def status(
                self,
                stats: readers.StatsReader,
                _context: contexts.StatusCallContext,
                **kwargs: object,
            ) -> Awaitable[None]: ...
            def status_context(
                self,
                context: contexts.StatusCallContext,
            ) -> Awaitable[None]: ...

    StatsCallback: _StatsCallbackInterfaceModule
    type StatsCallbackServer = (
        _ChannelInterfaceModule._StatsCallbackInterfaceModule.Server
    )

    class _ChannelSchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

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
            ) -> _ChannelInterfaceModule._ChannelSchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

        class _IdentifiableInterfaceModuleInfoMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._IdentifiableInterfaceModuleInfoParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._IdentifiableInterfaceModuleInfoResultSchema: ...

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
                ) -> _ChannelInterfaceModule._ChannelSchema._PersistentInterfaceModuleSaveParamSchema._SealForField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._PersistentInterfaceModuleSaveParamSchema._Fields: ...

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
                ) -> _ChannelInterfaceModule._ChannelSchema._PersistentInterfaceModuleSaveResultSchema._SturdyRefField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["unsaveSR"],
                ) -> _ChannelInterfaceModule._ChannelSchema._PersistentInterfaceModuleSaveResultSchema._UnsaveSRField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._PersistentInterfaceModuleSaveResultSchema._Fields: ...

        class _PersistentInterfaceModuleSaveMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._PersistentInterfaceModuleSaveParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._PersistentInterfaceModuleSaveResultSchema: ...

        class _ChannelInterfaceModuleSetBufferSizeParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["size"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleSetBufferSizeParamSchema._Fields: ...

        class _ChannelInterfaceModuleSetBufferSizeResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleSetBufferSizeResultSchema._Fields: ...

        class _ChannelInterfaceModuleSetBufferSizeMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleSetBufferSizeParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleSetBufferSizeResultSchema: ...

        class _ChannelInterfaceModuleReaderParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleReaderParamSchema._Fields: ...

        class _ChannelInterfaceModuleReaderResultSchema(_StructSchema):
            class _RField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._ChannelReaderSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["r"],
                ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleReaderResultSchema._RField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleReaderResultSchema._Fields: ...

        class _ChannelInterfaceModuleReaderMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleReaderParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleReaderResultSchema: ...

        class _ChannelInterfaceModuleWriterParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleWriterParamSchema._Fields: ...

        class _ChannelInterfaceModuleWriterResultSchema(_StructSchema):
            class _WField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._ChannelWriterSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["w"],
                ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleWriterResultSchema._WField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleWriterResultSchema._Fields: ...

        class _ChannelInterfaceModuleWriterMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleWriterParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleWriterResultSchema: ...

        class _ChannelInterfaceModuleEndpointsParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleEndpointsParamSchema._Fields: ...

        class _ChannelInterfaceModuleEndpointsResultSchema(_StructSchema):
            class _RField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._ChannelReaderSchema: ...

            class _WField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._ChannelWriterSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["r"],
                ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleEndpointsResultSchema._RField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["w"],
                ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleEndpointsResultSchema._WField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleEndpointsResultSchema._Fields: ...

        class _ChannelInterfaceModuleEndpointsMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleEndpointsParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleEndpointsResultSchema: ...

        class _ChannelInterfaceModuleSetAutoCloseSemanticsParamSchema(_StructSchema):
            class _CsField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._ChannelCloseSemanticsEnumSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["cs"],
                ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleSetAutoCloseSemanticsParamSchema._CsField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleSetAutoCloseSemanticsParamSchema._Fields: ...

        class _ChannelInterfaceModuleSetAutoCloseSemanticsResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleSetAutoCloseSemanticsResultSchema._Fields: ...

        class _ChannelInterfaceModuleSetAutoCloseSemanticsMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleSetAutoCloseSemanticsParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleSetAutoCloseSemanticsResultSchema: ...

        class _ChannelInterfaceModuleCloseParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["waitForEmptyBuffer"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleCloseParamSchema._Fields: ...

        class _ChannelInterfaceModuleCloseResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleCloseResultSchema._Fields: ...

        class _ChannelInterfaceModuleCloseMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleCloseParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleCloseResultSchema: ...

        class _ChannelInterfaceModuleRegisterStatsCallbackParamSchema(_StructSchema):
            class _CallbackField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._ChannelStatsCallbackSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["callback"],
                ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleRegisterStatsCallbackParamSchema._CallbackField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["updateIntervalInMs"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleRegisterStatsCallbackParamSchema._Fields: ...

        class _ChannelInterfaceModuleRegisterStatsCallbackResultSchema(_StructSchema):
            class _UnregisterCallbackField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._ChannelStatsCallbackUnregisterSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["unregisterCallback"],
                ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleRegisterStatsCallbackResultSchema._UnregisterCallbackField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleRegisterStatsCallbackResultSchema._Fields: ...

        class _ChannelInterfaceModuleRegisterStatsCallbackMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleRegisterStatsCallbackParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleRegisterStatsCallbackResultSchema: ...

        class _Methods(dict[str, _InterfaceMethod]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _ChannelInterfaceModule._ChannelSchema._IdentifiableInterfaceModuleInfoMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["save"],
            ) -> _ChannelInterfaceModule._ChannelSchema._PersistentInterfaceModuleSaveMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["setBufferSize"],
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleSetBufferSizeMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["reader"],
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleReaderMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["writer"],
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleWriterMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["endpoints"],
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleEndpointsMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["setAutoCloseSemantics"],
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleSetAutoCloseSemanticsMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["close"],
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleCloseMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["registerStatsCallback"],
            ) -> _ChannelInterfaceModule._ChannelSchema._ChannelInterfaceModuleRegisterStatsCallbackMethod: ...
            @overload
            def __getitem__(self, key: str) -> _InterfaceMethod: ...

        @property
        @override
        def methods(self) -> _ChannelInterfaceModule._ChannelSchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._ChannelSchema: ...
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.ChannelClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def setBufferSize(
            self,
            size: int,
            _context: contexts.SetbuffersizeCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def setBufferSize_context(
            self,
            context: contexts.SetbuffersizeCallContext,
        ) -> Awaitable[None]: ...
        def reader(
            self,
            _context: contexts.ReaderCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _ChannelInterfaceModule._ReaderInterfaceModule.Server
            | clients.ReaderClient
            | results_tuples.ReaderResultTuple
            | None
        ]: ...
        def reader_context(
            self,
            context: contexts.ReaderCallContext,
        ) -> Awaitable[None]: ...
        def writer(
            self,
            _context: contexts.WriterCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _ChannelInterfaceModule._WriterInterfaceModule.Server
            | clients.WriterClient
            | results_tuples.WriterResultTuple
            | None
        ]: ...
        def writer_context(
            self,
            context: contexts.WriterCallContext,
        ) -> Awaitable[None]: ...
        def endpoints(
            self,
            _context: contexts.EndpointsCallContext,
            **kwargs: object,
        ) -> Awaitable[results_tuples.EndpointsResultTuple | None]: ...
        def endpoints_context(
            self,
            context: contexts.EndpointsCallContext,
        ) -> Awaitable[None]: ...
        def setAutoCloseSemantics(
            self,
            cs: enums.ChannelCloseSemanticsEnum,
            _context: contexts.SetautoclosesemanticsCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def setAutoCloseSemantics_context(
            self,
            context: contexts.SetautoclosesemanticsCallContext,
        ) -> Awaitable[None]: ...
        def close(
            self,
            waitForEmptyBuffer: bool,
            _context: contexts.ChannelCloseCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def close_context(
            self,
            context: contexts.ChannelCloseCallContext,
        ) -> Awaitable[None]: ...
        def registerStatsCallback(
            self,
            callback: clients.StatsCallbackClient,
            updateIntervalInMs: int,
            _context: contexts.RegisterstatscallbackCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _ChannelInterfaceModule._StatsCallbackInterfaceModule._UnregisterInterfaceModule.Server
            | clients.UnregisterClient
            | results_tuples.RegisterstatscallbackResultTuple
            | None
        ]: ...
        def registerStatsCallback_context(
            self,
            context: contexts.RegisterstatscallbackCallContext,
        ) -> Awaitable[None]: ...

class _StartChannelsServiceInterfaceModule(_IdentifiableInterfaceModule):
    class _ParamsStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _ParamsSchema(_StructSchema):
            class _ReaderSrtsField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _ListSchema: ...

            class _WriterSrtsField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _ListSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["name"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["noOfChannels"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["noOfReaders"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["noOfWriters"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["readerSrts"],
                ) -> _StartChannelsServiceInterfaceModule._ParamsStructModule._ParamsSchema._ReaderSrtsField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["writerSrts"],
                ) -> _StartChannelsServiceInterfaceModule._ParamsStructModule._ParamsSchema._WriterSrtsField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["bufferSize"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _StartChannelsServiceInterfaceModule._ParamsStructModule._ParamsSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._StartChannelsServiceParamsSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            name: str | None = None,
            noOfChannels: int | None = None,
            noOfReaders: int | None = None,
            noOfWriters: int | None = None,
            readerSrts: builders.TextListBuilder | dict[str, Any] | None = None,
            writerSrts: builders.TextListBuilder | dict[str, Any] | None = None,
            bufferSize: int | None = None,
            **kwargs: object,
        ) -> builders.ParamsBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.ParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.ParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.ParamsBuilder]: ...
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
        ) -> readers.ParamsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.ParamsReader: ...

    Params: _ParamsStructModule

    class _StartChannelsServiceSchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _StartChannelsServiceInterfaceModule._StartChannelsServiceSchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

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
            ) -> _StartChannelsServiceInterfaceModule._StartChannelsServiceSchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

        class _IdentifiableInterfaceModuleInfoMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _StartChannelsServiceInterfaceModule._StartChannelsServiceSchema._IdentifiableInterfaceModuleInfoParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _StartChannelsServiceInterfaceModule._StartChannelsServiceSchema._IdentifiableInterfaceModuleInfoResultSchema: ...

        class _StartChannelsServiceInterfaceModuleStartParamSchema(_StructSchema):
            class _ReaderSrtsField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _ListSchema: ...

            class _WriterSrtsField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _ListSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["name"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["noOfChannels"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["noOfReaders"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["noOfWriters"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["readerSrts"],
                ) -> _StartChannelsServiceInterfaceModule._StartChannelsServiceSchema._StartChannelsServiceInterfaceModuleStartParamSchema._ReaderSrtsField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["writerSrts"],
                ) -> _StartChannelsServiceInterfaceModule._StartChannelsServiceSchema._StartChannelsServiceInterfaceModuleStartParamSchema._WriterSrtsField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["bufferSize"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _StartChannelsServiceInterfaceModule._StartChannelsServiceSchema._StartChannelsServiceInterfaceModuleStartParamSchema._Fields: ...

        class _StartChannelsServiceInterfaceModuleStartResultSchema(_StructSchema):
            class _StartupInfosField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> schemas._ChannelStartupInfoSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _StartChannelsServiceInterfaceModule._StartChannelsServiceSchema._StartChannelsServiceInterfaceModuleStartResultSchema._StartupInfosField._Schema: ...

            class _StopField(_StructSchemaField):
                @property
                @override
                def schema(self) -> _InterfaceSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["startupInfos"],
                ) -> _StartChannelsServiceInterfaceModule._StartChannelsServiceSchema._StartChannelsServiceInterfaceModuleStartResultSchema._StartupInfosField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["stop"],
                ) -> _StartChannelsServiceInterfaceModule._StartChannelsServiceSchema._StartChannelsServiceInterfaceModuleStartResultSchema._StopField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _StartChannelsServiceInterfaceModule._StartChannelsServiceSchema._StartChannelsServiceInterfaceModuleStartResultSchema._Fields: ...

        class _StartChannelsServiceInterfaceModuleStartMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _StartChannelsServiceInterfaceModule._StartChannelsServiceSchema._StartChannelsServiceInterfaceModuleStartParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _StartChannelsServiceInterfaceModule._StartChannelsServiceSchema._StartChannelsServiceInterfaceModuleStartResultSchema: ...

        class _Methods(dict[str, _InterfaceMethod]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _StartChannelsServiceInterfaceModule._StartChannelsServiceSchema._IdentifiableInterfaceModuleInfoMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["start"],
            ) -> _StartChannelsServiceInterfaceModule._StartChannelsServiceSchema._StartChannelsServiceInterfaceModuleStartMethod: ...
            @overload
            def __getitem__(self, key: str) -> _InterfaceMethod: ...

        @property
        @override
        def methods(
            self,
        ) -> (
            _StartChannelsServiceInterfaceModule._StartChannelsServiceSchema._Methods
        ): ...

    @property
    @override
    def schema(self) -> schemas._StartChannelsServiceSchema: ...
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.StartChannelsServiceClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def start(
            self,
            name: str,
            noOfChannels: int,
            noOfReaders: int,
            noOfWriters: int,
            readerSrts: readers.TextListReader,
            writerSrts: readers.TextListReader,
            bufferSize: int,
            _context: contexts.StartChannelsServiceStartCallContext,
            **kwargs: object,
        ) -> Awaitable[results_tuples.StartChannelsServiceStartResultTuple | None]: ...
        def start_context(
            self,
            context: contexts.StartChannelsServiceStartCallContext,
        ) -> Awaitable[None]: ...

class _PortInfosStructModule(_StructModule):
    class _NameAndSRStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _NameAndSRSchema(_StructSchema):
            class _SrField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> (
                    _mas_schema_persistence_persistence_capnp_schemas._SturdyRefSchema
                ): ...

            class _SrsField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(
                        self,
                    ) -> _mas_schema_persistence_persistence_capnp_schemas._SturdyRefSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _PortInfosStructModule._NameAndSRStructModule._NameAndSRSchema._SrsField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["name"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["sr"],
                ) -> _PortInfosStructModule._NameAndSRStructModule._NameAndSRSchema._SrField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["srs"],
                ) -> _PortInfosStructModule._NameAndSRStructModule._NameAndSRSchema._SrsField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> (
                _PortInfosStructModule._NameAndSRStructModule._NameAndSRSchema._Fields
            ): ...

        @property
        @override
        def schema(self) -> schemas._PortInfosNameAndSRSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            name: str | None = None,
            sr: SturdyRefBuilder | dict[str, Any] | None = None,
            srs: builders.SturdyRefListBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> builders.NameAndSRBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.NameAndSRReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.NameAndSRReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.NameAndSRBuilder]: ...
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
        ) -> readers.NameAndSRReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.NameAndSRReader: ...

    NameAndSR: _NameAndSRStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _PortInfosSchema(_StructSchema):
        class _InPortsField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._PortInfosNameAndSRSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _PortInfosStructModule._PortInfosSchema._InPortsField._Schema: ...

        class _OutPortsField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._PortInfosNameAndSRSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _PortInfosStructModule._PortInfosSchema._OutPortsField._Schema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["inPorts"],
            ) -> _PortInfosStructModule._PortInfosSchema._InPortsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["outPorts"],
            ) -> _PortInfosStructModule._PortInfosSchema._OutPortsField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _PortInfosStructModule._PortInfosSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._PortInfosSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        inPorts: builders.NameAndSRListBuilder | dict[str, Any] | None = None,
        outPorts: builders.NameAndSRListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> builders.PortInfosBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.PortInfosReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.PortInfosReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.PortInfosBuilder]: ...
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
    ) -> readers.PortInfosReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.PortInfosReader: ...

class _RunnableInterfaceModule(_IdentifiableInterfaceModule):
    class _FactoryInterfaceModule(_IdentifiableInterfaceModule):
        class _FactorySchema(_InterfaceSchema):
            class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _RunnableInterfaceModule._FactoryInterfaceModule._FactorySchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

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
                ) -> _RunnableInterfaceModule._FactoryInterfaceModule._FactorySchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

            class _IdentifiableInterfaceModuleInfoMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _RunnableInterfaceModule._FactoryInterfaceModule._FactorySchema._IdentifiableInterfaceModuleInfoParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _RunnableInterfaceModule._FactoryInterfaceModule._FactorySchema._IdentifiableInterfaceModuleInfoResultSchema: ...

            class _FactoryInterfaceModuleCreateParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _RunnableInterfaceModule._FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleCreateParamSchema._Fields: ...

            class _FactoryInterfaceModuleCreateResultSchema(_StructSchema):
                class _OutField(_StructSchemaField):
                    @property
                    @override
                    def schema(self) -> schemas._RunnableSchema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["out"],
                    ) -> _RunnableInterfaceModule._FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleCreateResultSchema._OutField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _RunnableInterfaceModule._FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleCreateResultSchema._Fields: ...

            class _FactoryInterfaceModuleCreateMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _RunnableInterfaceModule._FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleCreateParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _RunnableInterfaceModule._FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleCreateResultSchema: ...

            class _Methods(dict[str, _InterfaceMethod]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["info"],
                ) -> _RunnableInterfaceModule._FactoryInterfaceModule._FactorySchema._IdentifiableInterfaceModuleInfoMethod: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["create"],
                ) -> _RunnableInterfaceModule._FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleCreateMethod: ...
                @overload
                def __getitem__(self, key: str) -> _InterfaceMethod: ...

            @property
            @override
            def methods(
                self,
            ) -> (
                _RunnableInterfaceModule._FactoryInterfaceModule._FactorySchema._Methods
            ): ...

        @property
        @override
        def schema(self) -> schemas._RunnableFactorySchema: ...
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> clients.RunnableFactoryClient: ...
        class Server(_IdentifiableInterfaceModule.Server):
            def create(
                self,
                _context: contexts.RunnableFactoryCreateCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _RunnableInterfaceModule.Server
                | clients.RunnableClient
                | results_tuples.RunnableFactoryCreateResultTuple
                | None
            ]: ...
            def create_context(
                self,
                context: contexts.RunnableFactoryCreateCallContext,
            ) -> Awaitable[None]: ...

    Factory: _FactoryInterfaceModule
    type FactoryServer = _RunnableInterfaceModule._FactoryInterfaceModule.Server
    class _StoppedCallbackInterfaceModule(_InterfaceModule):
        class _StoppedCallbackSchema(_InterfaceSchema):
            class _StoppedCallbackInterfaceModuleStoppedParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _RunnableInterfaceModule._StoppedCallbackInterfaceModule._StoppedCallbackSchema._StoppedCallbackInterfaceModuleStoppedParamSchema._Fields: ...

            class _StoppedCallbackInterfaceModuleStoppedResultSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _RunnableInterfaceModule._StoppedCallbackInterfaceModule._StoppedCallbackSchema._StoppedCallbackInterfaceModuleStoppedResultSchema._Fields: ...

            class _StoppedCallbackInterfaceModuleStoppedMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _RunnableInterfaceModule._StoppedCallbackInterfaceModule._StoppedCallbackSchema._StoppedCallbackInterfaceModuleStoppedParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _RunnableInterfaceModule._StoppedCallbackInterfaceModule._StoppedCallbackSchema._StoppedCallbackInterfaceModuleStoppedResultSchema: ...

            class _Methods(dict[str, _InterfaceMethod]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["stopped"],
                ) -> _RunnableInterfaceModule._StoppedCallbackInterfaceModule._StoppedCallbackSchema._StoppedCallbackInterfaceModuleStoppedMethod: ...
                @overload
                def __getitem__(self, key: str) -> _InterfaceMethod: ...

            @property
            @override
            def methods(
                self,
            ) -> _RunnableInterfaceModule._StoppedCallbackInterfaceModule._StoppedCallbackSchema._Methods: ...

        @property
        @override
        def schema(self) -> schemas._RunnableStoppedCallbackSchema: ...
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> clients.StoppedCallbackClient: ...
        class Server(_DynamicCapabilityServer):
            def stopped(
                self,
                _context: contexts.StoppedCallContext,
                **kwargs: object,
            ) -> Awaitable[None]: ...
            def stopped_context(
                self,
                context: contexts.StoppedCallContext,
            ) -> Awaitable[None]: ...

    StoppedCallback: _StoppedCallbackInterfaceModule
    type StoppedCallbackServer = (
        _RunnableInterfaceModule._StoppedCallbackInterfaceModule.Server
    )

    class _RunnableSchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _RunnableInterfaceModule._RunnableSchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

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
            ) -> _RunnableInterfaceModule._RunnableSchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

        class _IdentifiableInterfaceModuleInfoMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _RunnableInterfaceModule._RunnableSchema._IdentifiableInterfaceModuleInfoParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _RunnableInterfaceModule._RunnableSchema._IdentifiableInterfaceModuleInfoResultSchema: ...

        class _RunnableInterfaceModuleStartParamSchema(_StructSchema):
            class _PortInfosReaderSrField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> (
                    _mas_schema_persistence_persistence_capnp_schemas._SturdyRefSchema
                ): ...

            class _StoppedCbField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._RunnableStoppedCallbackSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["portInfosReaderSr"],
                ) -> _RunnableInterfaceModule._RunnableSchema._RunnableInterfaceModuleStartParamSchema._PortInfosReaderSrField: ...
                @overload
                def __getitem__(self, key: Literal["name"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["stoppedCb"],
                ) -> _RunnableInterfaceModule._RunnableSchema._RunnableInterfaceModuleStartParamSchema._StoppedCbField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _RunnableInterfaceModule._RunnableSchema._RunnableInterfaceModuleStartParamSchema._Fields: ...

        class _RunnableInterfaceModuleStartResultSchema(_StructSchema):
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
            ) -> _RunnableInterfaceModule._RunnableSchema._RunnableInterfaceModuleStartResultSchema._Fields: ...

        class _RunnableInterfaceModuleStartMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _RunnableInterfaceModule._RunnableSchema._RunnableInterfaceModuleStartParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _RunnableInterfaceModule._RunnableSchema._RunnableInterfaceModuleStartResultSchema: ...

        class _RunnableInterfaceModuleStopParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _RunnableInterfaceModule._RunnableSchema._RunnableInterfaceModuleStopParamSchema._Fields: ...

        class _RunnableInterfaceModuleStopResultSchema(_StructSchema):
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
            ) -> _RunnableInterfaceModule._RunnableSchema._RunnableInterfaceModuleStopResultSchema._Fields: ...

        class _RunnableInterfaceModuleStopMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _RunnableInterfaceModule._RunnableSchema._RunnableInterfaceModuleStopParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _RunnableInterfaceModule._RunnableSchema._RunnableInterfaceModuleStopResultSchema: ...

        class _Methods(dict[str, _InterfaceMethod]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _RunnableInterfaceModule._RunnableSchema._IdentifiableInterfaceModuleInfoMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["start"],
            ) -> _RunnableInterfaceModule._RunnableSchema._RunnableInterfaceModuleStartMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["stop"],
            ) -> _RunnableInterfaceModule._RunnableSchema._RunnableInterfaceModuleStopMethod: ...
            @overload
            def __getitem__(self, key: str) -> _InterfaceMethod: ...

        @property
        @override
        def methods(self) -> _RunnableInterfaceModule._RunnableSchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._RunnableSchema: ...
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.RunnableClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def start(
            self,
            portInfosReaderSr: SturdyRefReader,
            name: str,
            stoppedCb: clients.StoppedCallbackClient,
            _context: contexts.RunnableStartCallContext,
            **kwargs: object,
        ) -> Awaitable[bool | results_tuples.RunnableStartResultTuple | None]: ...
        def start_context(
            self,
            context: contexts.RunnableStartCallContext,
        ) -> Awaitable[None]: ...
        def stop(
            self,
            _context: contexts.RunnableStopCallContext,
            **kwargs: object,
        ) -> Awaitable[bool | results_tuples.RunnableStopResultTuple | None]: ...
        def stop_context(
            self,
            context: contexts.RunnableStopCallContext,
        ) -> Awaitable[None]: ...

class _ProcessInterfaceModule(
    _IdentifiableInterfaceModule,
    _GatewayRegistrableInterfaceModule,
):
    class _FactoryInterfaceModule(_IdentifiableInterfaceModule):
        class _FactorySchema(_InterfaceSchema):
            class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ProcessInterfaceModule._FactoryInterfaceModule._FactorySchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

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
                ) -> _ProcessInterfaceModule._FactoryInterfaceModule._FactorySchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

            class _IdentifiableInterfaceModuleInfoMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ProcessInterfaceModule._FactoryInterfaceModule._FactorySchema._IdentifiableInterfaceModuleInfoParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ProcessInterfaceModule._FactoryInterfaceModule._FactorySchema._IdentifiableInterfaceModuleInfoResultSchema: ...

            class _FactoryInterfaceModuleCreateParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ProcessInterfaceModule._FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleCreateParamSchema._Fields: ...

            class _FactoryInterfaceModuleCreateResultSchema(_StructSchema):
                class _OutField(_StructSchemaField):
                    @property
                    @override
                    def schema(self) -> schemas._ProcessSchema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["out"],
                    ) -> _ProcessInterfaceModule._FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleCreateResultSchema._OutField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ProcessInterfaceModule._FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleCreateResultSchema._Fields: ...

            class _FactoryInterfaceModuleCreateMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ProcessInterfaceModule._FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleCreateParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ProcessInterfaceModule._FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleCreateResultSchema: ...

            class _Methods(dict[str, _InterfaceMethod]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["info"],
                ) -> _ProcessInterfaceModule._FactoryInterfaceModule._FactorySchema._IdentifiableInterfaceModuleInfoMethod: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["create"],
                ) -> _ProcessInterfaceModule._FactoryInterfaceModule._FactorySchema._FactoryInterfaceModuleCreateMethod: ...
                @overload
                def __getitem__(self, key: str) -> _InterfaceMethod: ...

            @property
            @override
            def methods(
                self,
            ) -> (
                _ProcessInterfaceModule._FactoryInterfaceModule._FactorySchema._Methods
            ): ...

        @property
        @override
        def schema(self) -> schemas._ProcessFactorySchema: ...
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> clients.ProcessFactoryClient: ...
        class Server(_IdentifiableInterfaceModule.Server):
            def create(
                self,
                _context: contexts.ProcessFactoryCreateCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _ProcessInterfaceModule.Server
                | clients.ProcessClient
                | results_tuples.ProcessFactoryCreateResultTuple
                | None
            ]: ...
            def create_context(
                self,
                context: contexts.ProcessFactoryCreateCallContext,
            ) -> Awaitable[None]: ...

    Factory: _FactoryInterfaceModule
    type FactoryServer = _ProcessInterfaceModule._FactoryInterfaceModule.Server
    class _DisconnectInterfaceModule(_InterfaceModule):
        class _DisconnectSchema(_InterfaceSchema):
            class _DisconnectInterfaceModuleDisconnectParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ProcessInterfaceModule._DisconnectInterfaceModule._DisconnectSchema._DisconnectInterfaceModuleDisconnectParamSchema._Fields: ...

            class _DisconnectInterfaceModuleDisconnectResultSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["disconnected"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ProcessInterfaceModule._DisconnectInterfaceModule._DisconnectSchema._DisconnectInterfaceModuleDisconnectResultSchema._Fields: ...

            class _DisconnectInterfaceModuleDisconnectMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ProcessInterfaceModule._DisconnectInterfaceModule._DisconnectSchema._DisconnectInterfaceModuleDisconnectParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ProcessInterfaceModule._DisconnectInterfaceModule._DisconnectSchema._DisconnectInterfaceModuleDisconnectResultSchema: ...

            class _Methods(dict[str, _InterfaceMethod]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["disconnect"],
                ) -> _ProcessInterfaceModule._DisconnectInterfaceModule._DisconnectSchema._DisconnectInterfaceModuleDisconnectMethod: ...
                @overload
                def __getitem__(self, key: str) -> _InterfaceMethod: ...

            @property
            @override
            def methods(
                self,
            ) -> _ProcessInterfaceModule._DisconnectInterfaceModule._DisconnectSchema._Methods: ...

        @property
        @override
        def schema(self) -> schemas._ProcessDisconnectSchema: ...
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> clients.DisconnectClient: ...
        class Server(_DynamicCapabilityServer):
            def disconnect(
                self,
                _context: contexts.DisconnectCallContext,
                **kwargs: object,
            ) -> Awaitable[bool | results_tuples.DisconnectResultTuple | None]: ...
            def disconnect_context(
                self,
                context: contexts.DisconnectCallContext,
            ) -> Awaitable[None]: ...

    Disconnect: _DisconnectInterfaceModule
    type DisconnectServer = _ProcessInterfaceModule._DisconnectInterfaceModule.Server
    class _ConfigEntryStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _ConfigEntrySchema(_StructSchema):
            class _ValField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_common_common_capnp_schemas._ValueSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["name"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["val"],
                ) -> _ProcessInterfaceModule._ConfigEntryStructModule._ConfigEntrySchema._ValField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ProcessInterfaceModule._ConfigEntryStructModule._ConfigEntrySchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._ProcessConfigEntrySchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            name: str | None = None,
            val: ValueBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> builders.ConfigEntryBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.ConfigEntryReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.ConfigEntryReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.ConfigEntryBuilder]: ...
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
        ) -> readers.ConfigEntryReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.ConfigEntryReader: ...

    ConfigEntry: _ConfigEntryStructModule
    class _StopModeEnumModule(_EnumModule):
        soft: int
        hard: int

        class _StopModeSchema(_EnumSchema): ...

        @property
        @override
        def schema(self) -> schemas._ProcessStopModeEnumSchema: ...

    StopMode: _StopModeEnumModule
    class _StateEnumModule(_EnumModule):
        idle: int
        starting: int
        running: int
        stopping: int
        failed: int
        closed: int

        class _StateSchema(_EnumSchema): ...

        @property
        @override
        def schema(self) -> schemas._ProcessStateEnumSchema: ...

    State: _StateEnumModule
    class _StateTransitionInterfaceModule(_InterfaceModule):
        class _StateTransitionSchema(_InterfaceSchema):
            class _StateTransitionInterfaceModuleStateChangedParamSchema(_StructSchema):
                class _OldField(_StructSchemaField):
                    @property
                    @override
                    def schema(self) -> schemas._ProcessStateEnumSchema: ...

                class _NewField(_StructSchemaField):
                    @property
                    @override
                    def schema(self) -> schemas._ProcessStateEnumSchema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["old"],
                    ) -> _ProcessInterfaceModule._StateTransitionInterfaceModule._StateTransitionSchema._StateTransitionInterfaceModuleStateChangedParamSchema._OldField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["new"],
                    ) -> _ProcessInterfaceModule._StateTransitionInterfaceModule._StateTransitionSchema._StateTransitionInterfaceModuleStateChangedParamSchema._NewField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ProcessInterfaceModule._StateTransitionInterfaceModule._StateTransitionSchema._StateTransitionInterfaceModuleStateChangedParamSchema._Fields: ...

            class _StateTransitionInterfaceModuleStateChangedResultSchema(
                _StructSchema,
            ):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ProcessInterfaceModule._StateTransitionInterfaceModule._StateTransitionSchema._StateTransitionInterfaceModuleStateChangedResultSchema._Fields: ...

            class _StateTransitionInterfaceModuleStateChangedMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ProcessInterfaceModule._StateTransitionInterfaceModule._StateTransitionSchema._StateTransitionInterfaceModuleStateChangedParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ProcessInterfaceModule._StateTransitionInterfaceModule._StateTransitionSchema._StateTransitionInterfaceModuleStateChangedResultSchema: ...

            class _Methods(dict[str, _InterfaceMethod]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["stateChanged"],
                ) -> _ProcessInterfaceModule._StateTransitionInterfaceModule._StateTransitionSchema._StateTransitionInterfaceModuleStateChangedMethod: ...
                @overload
                def __getitem__(self, key: str) -> _InterfaceMethod: ...

            @property
            @override
            def methods(
                self,
            ) -> _ProcessInterfaceModule._StateTransitionInterfaceModule._StateTransitionSchema._Methods: ...

        @property
        @override
        def schema(self) -> schemas._ProcessStateTransitionSchema: ...
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> clients.StateTransitionClient: ...
        class Server(_DynamicCapabilityServer):
            def stateChanged(
                self,
                old: enums.ProcessStateEnum,
                new: enums.ProcessStateEnum,
                _context: contexts.StatechangedCallContext,
                **kwargs: object,
            ) -> Awaitable[None]: ...
            def stateChanged_context(
                self,
                context: contexts.StatechangedCallContext,
            ) -> Awaitable[None]: ...

    StateTransition: _StateTransitionInterfaceModule
    type StateTransitionServer = (
        _ProcessInterfaceModule._StateTransitionInterfaceModule.Server
    )

    class _ProcessSchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

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
            ) -> _ProcessInterfaceModule._ProcessSchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

        class _IdentifiableInterfaceModuleInfoMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._IdentifiableInterfaceModuleInfoParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._IdentifiableInterfaceModuleInfoResultSchema: ...

        class _GatewayRegistrableInterfaceModuleSturdyRefAtGatewayParamSchema(
            _StructSchema,
        ):
            class _GatewaySRField(_StructSchemaField):
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
                    key: Literal["gatewaySR"],
                ) -> _ProcessInterfaceModule._ProcessSchema._GatewayRegistrableInterfaceModuleSturdyRefAtGatewayParamSchema._GatewaySRField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["gatewayId"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._GatewayRegistrableInterfaceModuleSturdyRefAtGatewayParamSchema._Fields: ...

        class _GatewayRegistrableInterfaceModuleSturdyRefAtGatewayResultSchema(
            _StructSchema,
        ):
            class _SelfAtGatewaySRField(_StructSchemaField):
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
                    key: Literal["selfAtGatewaySR"],
                ) -> _ProcessInterfaceModule._ProcessSchema._GatewayRegistrableInterfaceModuleSturdyRefAtGatewayResultSchema._SelfAtGatewaySRField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._GatewayRegistrableInterfaceModuleSturdyRefAtGatewayResultSchema._Fields: ...

        class _GatewayRegistrableInterfaceModuleSturdyRefAtGatewayMethod(
            _InterfaceMethod,
        ):
            @property
            @override
            def param_type(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._GatewayRegistrableInterfaceModuleSturdyRefAtGatewayParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._GatewayRegistrableInterfaceModuleSturdyRefAtGatewayResultSchema: ...

        class _ProcessInterfaceModuleInPortsParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleInPortsParamSchema._Fields: ...

        class _ProcessInterfaceModuleInPortsResultSchema(_StructSchema):
            class _PortsField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> schemas._ComponentPortSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleInPortsResultSchema._PortsField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["ports"],
                ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleInPortsResultSchema._PortsField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleInPortsResultSchema._Fields: ...

        class _ProcessInterfaceModuleInPortsMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleInPortsParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleInPortsResultSchema: ...

        class _ProcessInterfaceModuleConnectInPortParamSchema(_StructSchema):
            class _SturdyRefField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> (
                    _mas_schema_persistence_persistence_capnp_schemas._SturdyRefSchema
                ): ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["name"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["sturdyRef"],
                ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleConnectInPortParamSchema._SturdyRefField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleConnectInPortParamSchema._Fields: ...

        class _ProcessInterfaceModuleConnectInPortResultSchema(_StructSchema):
            class _DisconnectField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._ProcessDisconnectSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["connected"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["disconnect"],
                ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleConnectInPortResultSchema._DisconnectField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleConnectInPortResultSchema._Fields: ...

        class _ProcessInterfaceModuleConnectInPortMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleConnectInPortParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleConnectInPortResultSchema: ...

        class _ProcessInterfaceModuleOutPortsParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleOutPortsParamSchema._Fields: ...

        class _ProcessInterfaceModuleOutPortsResultSchema(_StructSchema):
            class _PortsField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> schemas._ComponentPortSchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleOutPortsResultSchema._PortsField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["ports"],
                ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleOutPortsResultSchema._PortsField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleOutPortsResultSchema._Fields: ...

        class _ProcessInterfaceModuleOutPortsMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleOutPortsParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleOutPortsResultSchema: ...

        class _ProcessInterfaceModuleConnectOutPortParamSchema(_StructSchema):
            class _SturdyRefField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> (
                    _mas_schema_persistence_persistence_capnp_schemas._SturdyRefSchema
                ): ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["name"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["sturdyRef"],
                ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleConnectOutPortParamSchema._SturdyRefField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleConnectOutPortParamSchema._Fields: ...

        class _ProcessInterfaceModuleConnectOutPortResultSchema(_StructSchema):
            class _DisconnectField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._ProcessDisconnectSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["connected"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["disconnect"],
                ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleConnectOutPortResultSchema._DisconnectField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleConnectOutPortResultSchema._Fields: ...

        class _ProcessInterfaceModuleConnectOutPortMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleConnectOutPortParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleConnectOutPortResultSchema: ...

        class _ProcessInterfaceModuleConfigEntriesParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleConfigEntriesParamSchema._Fields: ...

        class _ProcessInterfaceModuleConfigEntriesResultSchema(_StructSchema):
            class _ConfigField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(self) -> schemas._ProcessConfigEntrySchema: ...

                @property
                @override
                def schema(
                    self,
                ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleConfigEntriesResultSchema._ConfigField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["config"],
                ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleConfigEntriesResultSchema._ConfigField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleConfigEntriesResultSchema._Fields: ...

        class _ProcessInterfaceModuleConfigEntriesMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleConfigEntriesParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleConfigEntriesResultSchema: ...

        class _ProcessInterfaceModuleStartParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleStartParamSchema._Fields: ...

        class _ProcessInterfaceModuleStartResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleStartResultSchema._Fields: ...

        class _ProcessInterfaceModuleStartMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleStartParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleStartResultSchema: ...

        class _ProcessInterfaceModuleStopParamSchema(_StructSchema):
            class _ModeField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._ProcessStopModeEnumSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["mode"],
                ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleStopParamSchema._ModeField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleStopParamSchema._Fields: ...

        class _ProcessInterfaceModuleStopResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleStopResultSchema._Fields: ...

        class _ProcessInterfaceModuleStopMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleStopParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleStopResultSchema: ...

        class _ProcessInterfaceModuleSetConfigEntryParamSchema(_StructSchema):
            class _ValField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_common_common_capnp_schemas._ValueSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["name"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["val"],
                ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleSetConfigEntryParamSchema._ValField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleSetConfigEntryParamSchema._Fields: ...

        class _ProcessInterfaceModuleSetConfigEntryResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleSetConfigEntryResultSchema._Fields: ...

        class _ProcessInterfaceModuleSetConfigEntryMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleSetConfigEntryParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleSetConfigEntryResultSchema: ...

        class _ProcessInterfaceModuleStateParamSchema(_StructSchema):
            class _TransitionCallbackField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._ProcessStateTransitionSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["transitionCallback"],
                ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleStateParamSchema._TransitionCallbackField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleStateParamSchema._Fields: ...

        class _ProcessInterfaceModuleStateResultSchema(_StructSchema):
            class _CurrentStateField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._ProcessStateEnumSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["currentState"],
                ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleStateResultSchema._CurrentStateField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleStateResultSchema._Fields: ...

        class _ProcessInterfaceModuleStateMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleStateParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleStateResultSchema: ...

        class _ProcessInterfaceModuleCloseParamSchema(_StructSchema):
            class _ModeField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._ProcessStopModeEnumSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["mode"],
                ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleCloseParamSchema._ModeField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleCloseParamSchema._Fields: ...

        class _ProcessInterfaceModuleCloseResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["closed"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleCloseResultSchema._Fields: ...

        class _ProcessInterfaceModuleCloseMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleCloseParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleCloseResultSchema: ...

        class _Methods(dict[str, _InterfaceMethod]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _ProcessInterfaceModule._ProcessSchema._IdentifiableInterfaceModuleInfoMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["sturdyRefAtGateway"],
            ) -> _ProcessInterfaceModule._ProcessSchema._GatewayRegistrableInterfaceModuleSturdyRefAtGatewayMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["inPorts"],
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleInPortsMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["connectInPort"],
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleConnectInPortMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["outPorts"],
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleOutPortsMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["connectOutPort"],
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleConnectOutPortMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["configEntries"],
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleConfigEntriesMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["start"],
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleStartMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["stop"],
            ) -> (
                _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleStopMethod
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["setConfigEntry"],
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleSetConfigEntryMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["state"],
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleStateMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["close"],
            ) -> _ProcessInterfaceModule._ProcessSchema._ProcessInterfaceModuleCloseMethod: ...
            @overload
            def __getitem__(self, key: str) -> _InterfaceMethod: ...

        @property
        @override
        def methods(self) -> _ProcessInterfaceModule._ProcessSchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._ProcessSchema: ...
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.ProcessClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _GatewayRegistrableInterfaceModule.Server,
    ):
        def inPorts(
            self,
            _context: contexts.InportsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.PortListBuilder
            | readers.PortListReader
            | Sequence[Any]
            | results_tuples.InportsResultTuple
            | None
        ]: ...
        def inPorts_context(
            self,
            context: contexts.InportsCallContext,
        ) -> Awaitable[None]: ...
        def connectInPort(
            self,
            name: str,
            sturdyRef: SturdyRefReader,
            _context: contexts.ConnectinportCallContext,
            **kwargs: object,
        ) -> Awaitable[results_tuples.ConnectinportResultTuple | None]: ...
        def connectInPort_context(
            self,
            context: contexts.ConnectinportCallContext,
        ) -> Awaitable[None]: ...
        def outPorts(
            self,
            _context: contexts.OutportsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.PortListBuilder
            | readers.PortListReader
            | Sequence[Any]
            | results_tuples.OutportsResultTuple
            | None
        ]: ...
        def outPorts_context(
            self,
            context: contexts.OutportsCallContext,
        ) -> Awaitable[None]: ...
        def connectOutPort(
            self,
            name: str,
            sturdyRef: SturdyRefReader,
            _context: contexts.ConnectoutportCallContext,
            **kwargs: object,
        ) -> Awaitable[results_tuples.ConnectoutportResultTuple | None]: ...
        def connectOutPort_context(
            self,
            context: contexts.ConnectoutportCallContext,
        ) -> Awaitable[None]: ...
        def configEntries(
            self,
            _context: contexts.ConfigentriesCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.ConfigEntryListBuilder
            | readers.ConfigEntryListReader
            | Sequence[Any]
            | results_tuples.ConfigentriesResultTuple
            | None
        ]: ...
        def configEntries_context(
            self,
            context: contexts.ConfigentriesCallContext,
        ) -> Awaitable[None]: ...
        def start(
            self,
            _context: contexts.ProcessStartCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def start_context(
            self,
            context: contexts.ProcessStartCallContext,
        ) -> Awaitable[None]: ...
        def stop(
            self,
            mode: enums.ProcessStopModeEnum,
            _context: contexts.ProcessStopCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def stop_context(
            self,
            context: contexts.ProcessStopCallContext,
        ) -> Awaitable[None]: ...
        def setConfigEntry(
            self,
            name: str,
            val: ValueReader,
            _context: contexts.SetconfigentryCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def setConfigEntry_context(
            self,
            context: contexts.SetconfigentryCallContext,
        ) -> Awaitable[None]: ...
        def state(
            self,
            transitionCallback: clients.StateTransitionClient,
            _context: contexts.StateCallContext,
            **kwargs: object,
        ) -> Awaitable[
            enums.ProcessStateEnum | results_tuples.StateResultTuple | None
        ]: ...
        def state_context(
            self,
            context: contexts.StateCallContext,
        ) -> Awaitable[None]: ...
        def close(
            self,
            mode: enums.ProcessStopModeEnum,
            _context: contexts.ProcessCloseCallContext,
            **kwargs: object,
        ) -> Awaitable[bool | results_tuples.ProcessCloseResultTuple | None]: ...
        def close_context(
            self,
            context: contexts.ProcessCloseCallContext,
        ) -> Awaitable[None]: ...

class _ComponentStructModule(_StructModule):
    class _ComponentTypeEnumModule(_EnumModule):
        standard: int
        iip: int
        subflow: int
        view: int
        process: int

        class _ComponentTypeSchema(_EnumSchema): ...

        @property
        @override
        def schema(self) -> schemas._ComponentComponentTypeEnumSchema: ...

    ComponentType: _ComponentTypeEnumModule
    class _PortStructModule(_StructModule):
        class _PortTypeEnumModule(_EnumModule):
            standard: int
            array: int

            class _PortTypeSchema(_EnumSchema): ...

            @property
            @override
            def schema(self) -> schemas._ComponentPortPortTypeEnumSchema: ...

        PortType: _PortTypeEnumModule
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _PortSchema(_StructSchema):
            class _TypeField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._ComponentPortPortTypeEnumSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["name"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["contentType"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["type"],
                ) -> (
                    _ComponentStructModule._PortStructModule._PortSchema._TypeField
                ): ...
                @overload
                def __getitem__(self, key: Literal["desc"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ComponentStructModule._PortStructModule._PortSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._ComponentPortSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            name: str | None = None,
            contentType: str | None = None,
            type: enums.ComponentPortPortTypeEnum | None = None,
            desc: str | None = None,
            **kwargs: object,
        ) -> builders.PortBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.PortReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.PortReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.PortBuilder]: ...
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
        ) -> readers.PortReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.PortReader: ...

    Port: _PortStructModule
    class _ComponentFactoryStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _ComponentFactorySchema(_StructSchema):
            class _RunnableField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._RunnableFactorySchema: ...

            class _ProcessField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._ProcessFactorySchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["none"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["runnable"],
                ) -> _ComponentStructModule._ComponentFactoryStructModule._ComponentFactorySchema._RunnableField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["process"],
                ) -> _ComponentStructModule._ComponentFactoryStructModule._ComponentFactorySchema._ProcessField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ComponentStructModule._ComponentFactoryStructModule._ComponentFactorySchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._ComponentComponentFactorySchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            none: None | None = None,
            runnable: clients.RunnableFactoryClient
            | _RunnableInterfaceModule._FactoryInterfaceModule.Server
            | None = None,
            process: clients.ProcessFactoryClient
            | _ProcessInterfaceModule._FactoryInterfaceModule.Server
            | None = None,
            **kwargs: object,
        ) -> builders.ComponentFactoryBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.ComponentFactoryReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.ComponentFactoryReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.ComponentFactoryBuilder]: ...
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
        ) -> readers.ComponentFactoryReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.ComponentFactoryReader: ...

    ComponentFactory: _ComponentFactoryStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _ComponentSchema(_StructSchema):
        class _InfoField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> _mas_schema_common_common_capnp_schemas._IdInformationSchema: ...

        class _TypeField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._ComponentComponentTypeEnumSchema: ...

        class _InPortsField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._ComponentPortSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _ComponentStructModule._ComponentSchema._InPortsField._Schema: ...

        class _OutPortsField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._ComponentPortSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _ComponentStructModule._ComponentSchema._OutPortsField._Schema: ...

        class _DefaultConfigField(_StructSchemaField):
            @property
            @override
            def schema(
                self,
            ) -> _mas_schema_common_common_capnp_schemas._StructuredTextSchema: ...

        class _FactoryField(_StructSchemaField):
            @property
            @override
            def schema(self) -> _StructSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _ComponentStructModule._ComponentSchema._InfoField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["type"],
            ) -> _ComponentStructModule._ComponentSchema._TypeField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["inPorts"],
            ) -> _ComponentStructModule._ComponentSchema._InPortsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["outPorts"],
            ) -> _ComponentStructModule._ComponentSchema._OutPortsField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["defaultConfig"],
            ) -> _ComponentStructModule._ComponentSchema._DefaultConfigField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["factory"],
            ) -> _ComponentStructModule._ComponentSchema._FactoryField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _ComponentStructModule._ComponentSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._ComponentSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        info: IdInformationBuilder | dict[str, Any] | None = None,
        type: enums.ComponentComponentTypeEnum | None = None,
        inPorts: builders.PortListBuilder | dict[str, Any] | None = None,
        outPorts: builders.PortListBuilder | dict[str, Any] | None = None,
        defaultConfig: StructuredTextBuilder | dict[str, Any] | None = None,
        factory: builders.ComponentFactoryBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> builders.ComponentBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.ComponentReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.ComponentReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.ComponentBuilder]: ...
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
    ) -> readers.ComponentReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.ComponentReader: ...
