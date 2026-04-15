"""Module helper types for `x.capnp`."""

from collections.abc import Awaitable, Callable
from contextlib import AbstractContextManager
from typing import IO, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
    _StructModule,
)

from . import _all as _all

class _XInterfaceModule(_InterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> _all.XClient: ...
    class Server(_DynamicCapabilityServer):
        def m(
            self,
            i: int,
            _context: _all.XMCallContext,
            **kwargs: object,
        ) -> Awaitable[str | _all.XMResultTuple | None]: ...
        def m_context(self, context: _all.XMCallContext) -> Awaitable[None]: ...

class _SStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        c: _all.XClient | _XInterfaceModule.Server | None = None,
        **kwargs: object,
    ) -> _all.SBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.SReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.SReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.SBuilder]: ...
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
    ) -> _all.SReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.SReader: ...

class _YInterfaceModule(_InterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> _all.YClient: ...
    class Server(_DynamicCapabilityServer):
        def m(
            self,
            hello: str,
            _context: _all.YMCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def m_context(self, context: _all.YMCallContext) -> Awaitable[None]: ...

class _ZInterfaceModule(_InterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> _all.ZClient: ...
    class Server(_DynamicCapabilityServer):
        def m(
            self,
            n: int,
            _context: _all.ZMCallContext,
            **kwargs: object,
        ) -> Awaitable[float | _all.ZMResultTuple | None]: ...
        def m_context(self, context: _all.ZMCallContext) -> Awaitable[None]: ...
