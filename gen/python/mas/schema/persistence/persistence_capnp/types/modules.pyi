"""Module helper types for `persistence.capnp`."""

from collections.abc import Awaitable, Callable
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceMethod,
    _InterfaceModule,
    _InterfaceSchema,
    _StructModule,
    _StructSchema,
    _StructSchemaField,
)

from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.persistence.persistence_capnp.types import builders as builders
from mas.schema.persistence.persistence_capnp.types import clients as clients
from mas.schema.persistence.persistence_capnp.types import common as common
from mas.schema.persistence.persistence_capnp.types import contexts as contexts
from mas.schema.persistence.persistence_capnp.types import readers as readers
from mas.schema.persistence.persistence_capnp.types import schemas as schemas
from mas.schema.persistence.persistence_capnp.types import servers as servers
from mas.schema.persistence.persistence_capnp.types.results import (
    tuples as results_tuples,
)

class _VatIdStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _VatIdSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["publicKey0"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["publicKey1"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["publicKey2"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["publicKey3"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _VatIdStructModule._VatIdSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._VatIdSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        publicKey0: int | None = None,
        publicKey1: int | None = None,
        publicKey2: int | None = None,
        publicKey3: int | None = None,
        **kwargs: object,
    ) -> builders.VatIdBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.VatIdReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.VatIdReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.VatIdBuilder]: ...
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
    ) -> readers.VatIdReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.VatIdReader: ...

class _AddressStructModule(_StructModule):
    class _AddressIp6StructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _AddressIp6Schema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["lower64"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["upper64"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> (
                _AddressStructModule._AddressIp6StructModule._AddressIp6Schema._Fields
            ): ...

        @property
        @override
        def schema(self) -> schemas._AddressAddressIp6Schema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            lower64: int | None = None,
            upper64: int | None = None,
            **kwargs: object,
        ) -> builders.AddressIp6Builder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.AddressIp6Reader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.AddressIp6Reader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.AddressIp6Builder]: ...
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
        ) -> readers.AddressIp6Reader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.AddressIp6Reader: ...

    AddressIp6: _AddressIp6StructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _AddressSchema(_StructSchema):
        class _Ip6Field(_StructSchemaField):
            @property
            @override
            def schema(self) -> _StructSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["ip6"],
            ) -> _AddressStructModule._AddressSchema._Ip6Field: ...
            @overload
            def __getitem__(self, key: Literal["port"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["host"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _AddressStructModule._AddressSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._AddressSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        ip6: builders.AddressIp6Builder | dict[str, Any] | None = None,
        port: int | None = None,
        host: str | None = None,
        **kwargs: object,
    ) -> builders.AddressBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.AddressReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.AddressReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.AddressBuilder]: ...
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
    ) -> readers.AddressReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.AddressReader: ...

class _VatPathStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _VatPathSchema(_StructSchema):
        class _IdField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._VatIdSchema: ...

        class _AddressField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._AddressSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["id"],
            ) -> _VatPathStructModule._VatPathSchema._IdField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["address"],
            ) -> _VatPathStructModule._VatPathSchema._AddressField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _VatPathStructModule._VatPathSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._VatPathSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        id: builders.VatIdBuilder | dict[str, Any] | None = None,
        address: builders.AddressBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> builders.VatPathBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.VatPathReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.VatPathReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.VatPathBuilder]: ...
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
    ) -> readers.VatPathReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.VatPathReader: ...

class _SturdyRefStructModule(_StructModule):
    class _OwnerStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _OwnerSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["guid"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _SturdyRefStructModule._OwnerStructModule._OwnerSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._SturdyRefOwnerSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            guid: str | None = None,
            **kwargs: object,
        ) -> builders.OwnerBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.OwnerReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.OwnerReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.OwnerBuilder]: ...
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
        ) -> readers.OwnerReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.OwnerReader: ...

    Owner: _OwnerStructModule
    class _TokenStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _TokenSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["text"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["data"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _SturdyRefStructModule._TokenStructModule._TokenSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._SturdyRefTokenSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            text: str | None = None,
            data: bytes | None = None,
            **kwargs: object,
        ) -> builders.TokenBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.TokenReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.TokenReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.TokenBuilder]: ...
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
        ) -> readers.TokenReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.TokenReader: ...

    Token: _TokenStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _SturdyRefSchema(_StructSchema):
        class _VatField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._VatPathSchema: ...

        class _LocalRefField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._SturdyRefTokenSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["vat"],
            ) -> _SturdyRefStructModule._SturdyRefSchema._VatField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["localRef"],
            ) -> _SturdyRefStructModule._SturdyRefSchema._LocalRefField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _SturdyRefStructModule._SturdyRefSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._SturdyRefSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        vat: builders.VatPathBuilder | dict[str, Any] | None = None,
        localRef: builders.TokenBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> builders.SturdyRefBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.SturdyRefReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.SturdyRefReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.SturdyRefBuilder]: ...
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
    ) -> readers.SturdyRefReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SturdyRefReader: ...

class _HeartbeatInterfaceModule(_InterfaceModule):
    class _HeartbeatSchema(_InterfaceSchema):
        class _HeartbeatInterfaceModuleBeatParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _HeartbeatInterfaceModule._HeartbeatSchema._HeartbeatInterfaceModuleBeatParamSchema._Fields: ...

        class _HeartbeatInterfaceModuleBeatResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _HeartbeatInterfaceModule._HeartbeatSchema._HeartbeatInterfaceModuleBeatResultSchema._Fields: ...

        class _Methods(dict[str, _InterfaceMethod[_StructSchema, _StructSchema]]):
            @overload
            def __getitem__(
                self,
                key: Literal["beat"],
            ) -> _InterfaceMethod[
                _HeartbeatInterfaceModule._HeartbeatSchema._HeartbeatInterfaceModuleBeatParamSchema,
                _HeartbeatInterfaceModule._HeartbeatSchema._HeartbeatInterfaceModuleBeatResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: str,
            ) -> _InterfaceMethod[_StructSchema, _StructSchema]: ...

        @property
        @override
        def methods(self) -> _HeartbeatInterfaceModule._HeartbeatSchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._HeartbeatSchema: ...
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.HeartbeatClient: ...
    class Server(_DynamicCapabilityServer):
        def beat(
            self,
            _context: contexts.BeatCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def beat_context(
            self,
            context: contexts.BeatCallContext,
        ) -> Awaitable[None]: ...

class _PersistentInterfaceModule(_InterfaceModule):
    class _SaveParamsStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _SaveParamsSchema(_StructSchema):
            class _SealForField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._SturdyRefOwnerSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["sealFor"],
                ) -> _PersistentInterfaceModule._SaveParamsStructModule._SaveParamsSchema._SealForField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _PersistentInterfaceModule._SaveParamsStructModule._SaveParamsSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._PersistentSaveParamsSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            sealFor: builders.OwnerBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> builders.SaveParamsBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.SaveParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.SaveParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.SaveParamsBuilder]: ...
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
        ) -> readers.SaveParamsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.SaveParamsReader: ...

    SaveParams: _SaveParamsStructModule
    class _SaveResultsStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _SaveResultsSchema(_StructSchema):
            class _SturdyRefField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._SturdyRefSchema: ...

            class _UnsaveSRField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._SturdyRefSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["sturdyRef"],
                ) -> _PersistentInterfaceModule._SaveResultsStructModule._SaveResultsSchema._SturdyRefField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["unsaveSR"],
                ) -> _PersistentInterfaceModule._SaveResultsStructModule._SaveResultsSchema._UnsaveSRField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _PersistentInterfaceModule._SaveResultsStructModule._SaveResultsSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._PersistentSaveResultsSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            sturdyRef: builders.SturdyRefBuilder | dict[str, Any] | None = None,
            unsaveSR: builders.SturdyRefBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> builders.SaveResultsBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.SaveResultsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.SaveResultsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.SaveResultsBuilder]: ...
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
        ) -> readers.SaveResultsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.SaveResultsReader: ...

    SaveResults: _SaveResultsStructModule
    class _ReleaseSturdyRefInterfaceModule(_InterfaceModule):
        class _ReleaseSturdyRefSchema(_InterfaceSchema):
            class _ReleaseSturdyRefInterfaceModuleReleaseParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _PersistentInterfaceModule._ReleaseSturdyRefInterfaceModule._ReleaseSturdyRefSchema._ReleaseSturdyRefInterfaceModuleReleaseParamSchema._Fields: ...

            class _ReleaseSturdyRefInterfaceModuleReleaseResultSchema(_StructSchema):
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
                ) -> _PersistentInterfaceModule._ReleaseSturdyRefInterfaceModule._ReleaseSturdyRefSchema._ReleaseSturdyRefInterfaceModuleReleaseResultSchema._Fields: ...

            class _Methods(dict[str, _InterfaceMethod[_StructSchema, _StructSchema]]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["release"],
                ) -> _InterfaceMethod[
                    _PersistentInterfaceModule._ReleaseSturdyRefInterfaceModule._ReleaseSturdyRefSchema._ReleaseSturdyRefInterfaceModuleReleaseParamSchema,
                    _PersistentInterfaceModule._ReleaseSturdyRefInterfaceModule._ReleaseSturdyRefSchema._ReleaseSturdyRefInterfaceModuleReleaseResultSchema,
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
            ) -> _PersistentInterfaceModule._ReleaseSturdyRefInterfaceModule._ReleaseSturdyRefSchema._Methods: ...

        @property
        @override
        def schema(self) -> schemas._PersistentReleaseSturdyRefSchema: ...
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> clients.ReleaseSturdyRefClient: ...
        class Server(_DynamicCapabilityServer):
            def release(
                self,
                _context: contexts.ReleaseCallContext,
                **kwargs: object,
            ) -> Awaitable[bool | results_tuples.ReleaseResultTuple | None]: ...
            def release_context(
                self,
                context: contexts.ReleaseCallContext,
            ) -> Awaitable[None]: ...

    ReleaseSturdyRef: _ReleaseSturdyRefInterfaceModule
    type ReleaseSturdyRefServer = (
        _PersistentInterfaceModule._ReleaseSturdyRefInterfaceModule.Server
    )
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.PersistentClient: ...
    class Server(_DynamicCapabilityServer):
        def save(
            self,
            sealFor: readers.OwnerReader,
            _context: contexts.SaveCallContext,
            **kwargs: object,
        ) -> Awaitable[results_tuples.SaveResultTuple | None]: ...
        def save_context(
            self,
            context: contexts.SaveCallContext,
        ) -> Awaitable[None]: ...

class _RestorerInterfaceModule(_InterfaceModule):
    class _RestoreParamsStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _RestoreParamsSchema(_StructSchema):
            class _LocalRefField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._SturdyRefTokenSchema: ...

            class _SealedByField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._SturdyRefOwnerSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["localRef"],
                ) -> _RestorerInterfaceModule._RestoreParamsStructModule._RestoreParamsSchema._LocalRefField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["sealedBy"],
                ) -> _RestorerInterfaceModule._RestoreParamsStructModule._RestoreParamsSchema._SealedByField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _RestorerInterfaceModule._RestoreParamsStructModule._RestoreParamsSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._RestorerRestoreParamsSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            localRef: builders.TokenBuilder | dict[str, Any] | None = None,
            sealedBy: builders.OwnerBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> builders.RestoreParamsBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.RestoreParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.RestoreParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.RestoreParamsBuilder]: ...
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
        ) -> readers.RestoreParamsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.RestoreParamsReader: ...

    RestoreParams: _RestoreParamsStructModule
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.RestorerClient: ...
    class Server(_DynamicCapabilityServer):
        def restore(
            self,
            localRef: readers.TokenReader,
            sealedBy: readers.OwnerReader,
            _context: contexts.RestoreCallContext,
            **kwargs: object,
        ) -> Awaitable[
            common.Capability | results_tuples.RestoreResultTuple | None
        ]: ...
        def restore_context(
            self,
            context: contexts.RestoreCallContext,
        ) -> Awaitable[None]: ...

class _HostPortResolverInterfaceModule(
    _IdentifiableInterfaceModule,
    _RestorerInterfaceModule,
):
    class _RegistrarInterfaceModule(_InterfaceModule):
        class _RegisterParamsStructModule(_StructModule):
            class Reader(_DynamicStructReader): ...
            class Builder(_DynamicStructBuilder): ...

            class _RegisterParamsSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["base64VatId"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["host"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["port"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["alias"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["identityProof"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _HostPortResolverInterfaceModule._RegistrarInterfaceModule._RegisterParamsStructModule._RegisterParamsSchema._Fields: ...

            @property
            @override
            def schema(
                self,
            ) -> schemas._HostPortResolverRegistrarRegisterParamsSchema: ...
            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
                base64VatId: str | None = None,
                host: str | None = None,
                port: int | None = None,
                alias: str | None = None,
                identityProof: bytes | None = None,
                **kwargs: object,
            ) -> builders.RegisterParamsBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[readers.RegisterParamsReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[readers.RegisterParamsReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[builders.RegisterParamsBuilder]: ...
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
            ) -> readers.RegisterParamsReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> readers.RegisterParamsReader: ...

        RegisterParams: _RegisterParamsStructModule

        class _RegistrarSchema(_InterfaceSchema):
            class _RegistrarInterfaceModuleRegisterParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["base64VatId"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["host"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["port"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["alias"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["identityProof"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _HostPortResolverInterfaceModule._RegistrarInterfaceModule._RegistrarSchema._RegistrarInterfaceModuleRegisterParamSchema._Fields: ...

            class _RegistrarInterfaceModuleRegisterResultSchema(_StructSchema):
                class _HeartbeatField(_StructSchemaField):
                    @property
                    @override
                    def schema(self) -> schemas._HeartbeatSchema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["heartbeat"],
                    ) -> _HostPortResolverInterfaceModule._RegistrarInterfaceModule._RegistrarSchema._RegistrarInterfaceModuleRegisterResultSchema._HeartbeatField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["secsHeartbeatInterval"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _HostPortResolverInterfaceModule._RegistrarInterfaceModule._RegistrarSchema._RegistrarInterfaceModuleRegisterResultSchema._Fields: ...

            class _Methods(dict[str, _InterfaceMethod[_StructSchema, _StructSchema]]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["register"],
                ) -> _InterfaceMethod[
                    _HostPortResolverInterfaceModule._RegistrarInterfaceModule._RegistrarSchema._RegistrarInterfaceModuleRegisterParamSchema,
                    _HostPortResolverInterfaceModule._RegistrarInterfaceModule._RegistrarSchema._RegistrarInterfaceModuleRegisterResultSchema,
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
            ) -> _HostPortResolverInterfaceModule._RegistrarInterfaceModule._RegistrarSchema._Methods: ...

        @property
        @override
        def schema(self) -> schemas._HostPortResolverRegistrarSchema: ...
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> clients.RegistrarClient: ...
        class Server(_DynamicCapabilityServer):
            def register(
                self,
                base64VatId: str,
                host: str,
                port: int,
                alias: str,
                identityProof: bytes,
                _context: contexts.RegistrarRegisterCallContext,
                **kwargs: object,
            ) -> Awaitable[results_tuples.RegistrarRegisterResultTuple | None]: ...
            def register_context(
                self,
                context: contexts.RegistrarRegisterCallContext,
            ) -> Awaitable[None]: ...

    Registrar: _RegistrarInterfaceModule
    type RegistrarServer = (
        _HostPortResolverInterfaceModule._RegistrarInterfaceModule.Server
    )

    class _HostPortResolverSchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _HostPortResolverInterfaceModule._HostPortResolverSchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

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
            ) -> _HostPortResolverInterfaceModule._HostPortResolverSchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

        class _RestorerInterfaceModuleRestoreParamSchema(_StructSchema):
            class _LocalRefField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._SturdyRefTokenSchema: ...

            class _SealedByField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._SturdyRefOwnerSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["localRef"],
                ) -> _HostPortResolverInterfaceModule._HostPortResolverSchema._RestorerInterfaceModuleRestoreParamSchema._LocalRefField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["sealedBy"],
                ) -> _HostPortResolverInterfaceModule._HostPortResolverSchema._RestorerInterfaceModuleRestoreParamSchema._SealedByField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _HostPortResolverInterfaceModule._HostPortResolverSchema._RestorerInterfaceModuleRestoreParamSchema._Fields: ...

        class _RestorerInterfaceModuleRestoreResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["cap"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _HostPortResolverInterfaceModule._HostPortResolverSchema._RestorerInterfaceModuleRestoreResultSchema._Fields: ...

        class _HostPortResolverInterfaceModuleResolveParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _HostPortResolverInterfaceModule._HostPortResolverSchema._HostPortResolverInterfaceModuleResolveParamSchema._Fields: ...

        class _HostPortResolverInterfaceModuleResolveResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["host"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["port"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _HostPortResolverInterfaceModule._HostPortResolverSchema._HostPortResolverInterfaceModuleResolveResultSchema._Fields: ...

        class _Methods(dict[str, _InterfaceMethod[_StructSchema, _StructSchema]]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _InterfaceMethod[
                _HostPortResolverInterfaceModule._HostPortResolverSchema._IdentifiableInterfaceModuleInfoParamSchema,
                _HostPortResolverInterfaceModule._HostPortResolverSchema._IdentifiableInterfaceModuleInfoResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["restore"],
            ) -> _InterfaceMethod[
                _HostPortResolverInterfaceModule._HostPortResolverSchema._RestorerInterfaceModuleRestoreParamSchema,
                _HostPortResolverInterfaceModule._HostPortResolverSchema._RestorerInterfaceModuleRestoreResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["resolve"],
            ) -> _InterfaceMethod[
                _HostPortResolverInterfaceModule._HostPortResolverSchema._HostPortResolverInterfaceModuleResolveParamSchema,
                _HostPortResolverInterfaceModule._HostPortResolverSchema._HostPortResolverInterfaceModuleResolveResultSchema,
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
        ) -> _HostPortResolverInterfaceModule._HostPortResolverSchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._HostPortResolverSchema: ...
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.HostPortResolverClient: ...
    class Server(_IdentifiableInterfaceModule.Server, _RestorerInterfaceModule.Server):
        def resolve(
            self,
            id: str,
            _context: contexts.ResolveCallContext,
            **kwargs: object,
        ) -> Awaitable[results_tuples.ResolveResultTuple | None]: ...
        def resolve_context(
            self,
            context: contexts.ResolveCallContext,
        ) -> Awaitable[None]: ...

class _GatewayInterfaceModule(_IdentifiableInterfaceModule, _RestorerInterfaceModule):
    class _RegResultsStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _RegResultsSchema(_StructSchema):
            class _SturdyRefField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._SturdyRefSchema: ...

            class _HeartbeatField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._HeartbeatSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["sturdyRef"],
                ) -> _GatewayInterfaceModule._RegResultsStructModule._RegResultsSchema._SturdyRefField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["heartbeat"],
                ) -> _GatewayInterfaceModule._RegResultsStructModule._RegResultsSchema._HeartbeatField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["secsHeartbeatInterval"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _GatewayInterfaceModule._RegResultsStructModule._RegResultsSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._GatewayRegResultsSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            sturdyRef: builders.SturdyRefBuilder | dict[str, Any] | None = None,
            heartbeat: clients.HeartbeatClient
            | _HeartbeatInterfaceModule.Server
            | None = None,
            secsHeartbeatInterval: int | None = None,
            **kwargs: object,
        ) -> builders.RegResultsBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.RegResultsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.RegResultsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.RegResultsBuilder]: ...
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
        ) -> readers.RegResultsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.RegResultsReader: ...

    RegResults: _RegResultsStructModule

    class _GatewaySchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _GatewayInterfaceModule._GatewaySchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

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
            ) -> _GatewayInterfaceModule._GatewaySchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

        class _RestorerInterfaceModuleRestoreParamSchema(_StructSchema):
            class _LocalRefField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._SturdyRefTokenSchema: ...

            class _SealedByField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._SturdyRefOwnerSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["localRef"],
                ) -> _GatewayInterfaceModule._GatewaySchema._RestorerInterfaceModuleRestoreParamSchema._LocalRefField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["sealedBy"],
                ) -> _GatewayInterfaceModule._GatewaySchema._RestorerInterfaceModuleRestoreParamSchema._SealedByField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _GatewayInterfaceModule._GatewaySchema._RestorerInterfaceModuleRestoreParamSchema._Fields: ...

        class _RestorerInterfaceModuleRestoreResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["cap"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _GatewayInterfaceModule._GatewaySchema._RestorerInterfaceModuleRestoreResultSchema._Fields: ...

        class _GatewayInterfaceModuleRegisterParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["cap"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["secretSeed"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _GatewayInterfaceModule._GatewaySchema._GatewayInterfaceModuleRegisterParamSchema._Fields: ...

        class _GatewayInterfaceModuleRegisterResultSchema(_StructSchema):
            class _SturdyRefField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._SturdyRefSchema: ...

            class _HeartbeatField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._HeartbeatSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["sturdyRef"],
                ) -> _GatewayInterfaceModule._GatewaySchema._GatewayInterfaceModuleRegisterResultSchema._SturdyRefField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["heartbeat"],
                ) -> _GatewayInterfaceModule._GatewaySchema._GatewayInterfaceModuleRegisterResultSchema._HeartbeatField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["secsHeartbeatInterval"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _GatewayInterfaceModule._GatewaySchema._GatewayInterfaceModuleRegisterResultSchema._Fields: ...

        class _Methods(dict[str, _InterfaceMethod[_StructSchema, _StructSchema]]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _InterfaceMethod[
                _GatewayInterfaceModule._GatewaySchema._IdentifiableInterfaceModuleInfoParamSchema,
                _GatewayInterfaceModule._GatewaySchema._IdentifiableInterfaceModuleInfoResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["restore"],
            ) -> _InterfaceMethod[
                _GatewayInterfaceModule._GatewaySchema._RestorerInterfaceModuleRestoreParamSchema,
                _GatewayInterfaceModule._GatewaySchema._RestorerInterfaceModuleRestoreResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: Literal["register"],
            ) -> _InterfaceMethod[
                _GatewayInterfaceModule._GatewaySchema._GatewayInterfaceModuleRegisterParamSchema,
                _GatewayInterfaceModule._GatewaySchema._GatewayInterfaceModuleRegisterResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: str,
            ) -> _InterfaceMethod[_StructSchema, _StructSchema]: ...

        @property
        @override
        def methods(self) -> _GatewayInterfaceModule._GatewaySchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._GatewaySchema: ...
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.GatewayClient: ...
    class Server(_IdentifiableInterfaceModule.Server, _RestorerInterfaceModule.Server):
        def register(
            self,
            cap: common.AnyPointer,
            secretSeed: str,
            _context: contexts.GatewayRegisterCallContext,
            **kwargs: object,
        ) -> Awaitable[results_tuples.GatewayRegisterResultTuple | None]: ...
        def register_context(
            self,
            context: contexts.GatewayRegisterCallContext,
        ) -> Awaitable[None]: ...

class _GatewayRegistrableInterfaceModule(_InterfaceModule):
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.GatewayRegistrableClient: ...
    class Server(_DynamicCapabilityServer):
        def sturdyRefAtGateway(
            self,
            gatewaySR: readers.SturdyRefReader,
            gatewayId: str,
            _context: contexts.SturdyrefatgatewayCallContext,
            **kwargs: object,
        ) -> Awaitable[
            builders.SturdyRefBuilder
            | readers.SturdyRefReader
            | dict[str, Any]
            | results_tuples.SturdyrefatgatewayResultTuple
            | None
        ]: ...
        def sturdyRefAtGateway_context(
            self,
            context: contexts.SturdyrefatgatewayCallContext,
        ) -> Awaitable[None]: ...
