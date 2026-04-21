"""Module helper types for `x.capnp`."""

from collections.abc import Awaitable, Callable
from contextlib import AbstractContextManager
from typing import IO, Literal, overload, override

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

from mas.schema.test.x_capnp.types import builders as builders
from mas.schema.test.x_capnp.types import clients as clients
from mas.schema.test.x_capnp.types import contexts as contexts
from mas.schema.test.x_capnp.types import readers as readers
from mas.schema.test.x_capnp.types import schemas as schemas
from mas.schema.test.x_capnp.types.results import tuples as results_tuples

class _XInterfaceModule(_InterfaceModule):
    class _XSchema(_InterfaceSchema):
        class _XInterfaceModuleMParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["i"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _XInterfaceModule._XSchema._XInterfaceModuleMParamSchema._Fields: ...

        class _XInterfaceModuleMResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["t"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _XInterfaceModule._XSchema._XInterfaceModuleMResultSchema._Fields: ...

        class _Methods(dict[str, _InterfaceMethod[_StructSchema, _StructSchema]]):
            @overload
            def __getitem__(
                self,
                key: Literal["m"],
            ) -> _InterfaceMethod[
                _XInterfaceModule._XSchema._XInterfaceModuleMParamSchema,
                _XInterfaceModule._XSchema._XInterfaceModuleMResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: str,
            ) -> _InterfaceMethod[_StructSchema, _StructSchema]: ...

        @property
        @override
        def methods(self) -> _XInterfaceModule._XSchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._XSchema: ...
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> clients.XClient: ...
    class Server(_DynamicCapabilityServer):
        def m(
            self,
            i: int,
            _context: contexts.XMCallContext,
            **kwargs: object,
        ) -> Awaitable[str | results_tuples.XMResultTuple | None]: ...
        def m_context(self, context: contexts.XMCallContext) -> Awaitable[None]: ...

class _SStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _SSchema(_StructSchema):
        class _CField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._XSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["c"],
            ) -> _SStructModule._SSchema._CField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _SStructModule._SSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._SSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        c: clients.XClient | _XInterfaceModule.Server | None = None,
        **kwargs: object,
    ) -> builders.SBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.SReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.SReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.SBuilder]: ...
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
    ) -> readers.SReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SReader: ...

class _YInterfaceModule(_InterfaceModule):
    class _YSchema(_InterfaceSchema):
        class _YInterfaceModuleMParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["hello"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _YInterfaceModule._YSchema._YInterfaceModuleMParamSchema._Fields: ...

        class _YInterfaceModuleMResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _YInterfaceModule._YSchema._YInterfaceModuleMResultSchema._Fields: ...

        class _Methods(dict[str, _InterfaceMethod[_StructSchema, _StructSchema]]):
            @overload
            def __getitem__(
                self,
                key: Literal["m"],
            ) -> _InterfaceMethod[
                _YInterfaceModule._YSchema._YInterfaceModuleMParamSchema,
                _YInterfaceModule._YSchema._YInterfaceModuleMResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: str,
            ) -> _InterfaceMethod[_StructSchema, _StructSchema]: ...

        @property
        @override
        def methods(self) -> _YInterfaceModule._YSchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._YSchema: ...
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> clients.YClient: ...
    class Server(_DynamicCapabilityServer):
        def m(
            self,
            hello: str,
            _context: contexts.YMCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def m_context(self, context: contexts.YMCallContext) -> Awaitable[None]: ...

class _ZInterfaceModule(_InterfaceModule):
    class _ZSchema(_InterfaceSchema):
        class _ZInterfaceModuleMParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["n"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ZInterfaceModule._ZSchema._ZInterfaceModuleMParamSchema._Fields: ...

        class _ZInterfaceModuleMResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["r"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ZInterfaceModule._ZSchema._ZInterfaceModuleMResultSchema._Fields: ...

        class _Methods(dict[str, _InterfaceMethod[_StructSchema, _StructSchema]]):
            @overload
            def __getitem__(
                self,
                key: Literal["m"],
            ) -> _InterfaceMethod[
                _ZInterfaceModule._ZSchema._ZInterfaceModuleMParamSchema,
                _ZInterfaceModule._ZSchema._ZInterfaceModuleMResultSchema,
            ]: ...
            @overload
            def __getitem__(
                self,
                key: str,
            ) -> _InterfaceMethod[_StructSchema, _StructSchema]: ...

        @property
        @override
        def methods(self) -> _ZInterfaceModule._ZSchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._ZSchema: ...
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> clients.ZClient: ...
    class Server(_DynamicCapabilityServer):
        def m(
            self,
            n: int,
            _context: contexts.ZMCallContext,
            **kwargs: object,
        ) -> Awaitable[float | results_tuples.ZMResultTuple | None]: ...
        def m_context(self, context: contexts.ZMCallContext) -> Awaitable[None]: ...
