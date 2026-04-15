"""Module helper types for `common.capnp`."""

from collections.abc import Awaitable, Callable
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
    _StructModule,
)

from . import _all as _all

class _IdInformationStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        id: str | None = None,
        name: str | None = None,
        description: str | None = None,
        **kwargs: object,
    ) -> _all.IdInformationBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.IdInformationReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.IdInformationReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.IdInformationBuilder]: ...
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
    ) -> _all.IdInformationReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.IdInformationReader: ...

class _IdentifiableInterfaceModule(_InterfaceModule):
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> _all.IdentifiableClient: ...
    class Server(_DynamicCapabilityServer):
        def info(
            self,
            _context: _all.InfoCallContext,
            **kwargs: object,
        ) -> Awaitable[_all.InfoResultTuple | None]: ...
        def info_context(self, context: _all.InfoCallContext) -> Awaitable[None]: ...

class _StructuredTextStructModule(_StructModule):
    class _TypeEnumModule:
        unstructured: int
        json: int
        xml: int
        toml: int
        sturdyRef: int

    Type: _TypeEnumModule
    class _StructuredTextStructureStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

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
        ) -> _all.StructuredTextStructureBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.StructuredTextStructureReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.StructuredTextStructureReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.StructuredTextStructureBuilder]: ...
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
        ) -> _all.StructuredTextStructureReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.StructuredTextStructureReader: ...

    StructuredTextStructure: _StructuredTextStructureStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        value: str | None = None,
        structure: _all.StructuredTextStructureBuilder | dict[str, Any] | None = None,
        type: _all.StructuredTextTypeEnum | None = None,
        **kwargs: object,
    ) -> _all.StructuredTextBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.StructuredTextReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.StructuredTextReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.StructuredTextBuilder]: ...
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
    ) -> _all.StructuredTextReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.StructuredTextReader: ...

class _PairStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        fst: _all.AnyPointer | None = None,
        snd: _all.AnyPointer | None = None,
        **kwargs: object,
    ) -> _all.PairBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.PairReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.PairReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.PairBuilder]: ...
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
    ) -> _all.PairReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.PairReader: ...

class _ValueStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

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
        p: _all.AnyPointer | None = None,
        cap: _all.Capability | None = None,
        lf64: _all.Float64ListBuilder | dict[str, Any] | None = None,
        lf32: _all.Float32ListBuilder | dict[str, Any] | None = None,
        li64: _all.Int64ListBuilder | dict[str, Any] | None = None,
        li32: _all.Int32ListBuilder | dict[str, Any] | None = None,
        li16: _all.Int16ListBuilder | dict[str, Any] | None = None,
        li8: _all.Int8ListBuilder | dict[str, Any] | None = None,
        lui64: _all.Uint64ListBuilder | dict[str, Any] | None = None,
        lui32: _all.Uint32ListBuilder | dict[str, Any] | None = None,
        lui16: _all.Uint16ListBuilder | dict[str, Any] | None = None,
        lui8: _all.Uint8ListBuilder | dict[str, Any] | None = None,
        lb: _all.BoolListBuilder | dict[str, Any] | None = None,
        lt: _all.TextListBuilder | dict[str, Any] | None = None,
        ld: _all.DataListBuilder | dict[str, Any] | None = None,
        lcap: _all.AnyPointerListBuilder | dict[str, Any] | None = None,
        lpair: _all.PairListBuilder | dict[str, Any] | None = None,
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

class _FactoryInterfaceModule(_IdentifiableInterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> _all.FactoryClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def create(
            self,
            _context: _all.CreateCallContext,
            **kwargs: object,
        ) -> Awaitable[_all.AnyPointer | _all.CreateResultTuple | None]: ...
        def create_context(
            self,
            context: _all.CreateCallContext,
        ) -> Awaitable[None]: ...

class _IOFactoryInterfaceModule(_IdentifiableInterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> _all.IOFactoryClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def produce(
            self,
            in_: _all.AnyPointer,
            _context: _all.ProduceCallContext,
            **kwargs: object,
        ) -> Awaitable[_all.AnyPointer | _all.ProduceResultTuple | None]: ...
        def produce_context(
            self,
            context: _all.ProduceCallContext,
        ) -> Awaitable[None]: ...

class _HolderInterfaceModule(_InterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> _all.HolderClient: ...
    class Server(_DynamicCapabilityServer):
        def value(
            self,
            _context: _all.ValueCallContext,
            **kwargs: object,
        ) -> Awaitable[_all.AnyPointer | _all.ValueResultTuple | None]: ...
        def value_context(self, context: _all.ValueCallContext) -> Awaitable[None]: ...

class _IdentifiableHolderInterfaceModule(
    _IdentifiableInterfaceModule,
    _HolderInterfaceModule,
):
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> _all.IdentifiableHolderClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _HolderInterfaceModule.Server,
    ): ...
