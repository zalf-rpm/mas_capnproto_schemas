"""This is an automatically generated stub for `x.capnp`."""

from collections.abc import Awaitable, Callable
from contextlib import AbstractContextManager
from typing import IO, Literal, NamedTuple, Protocol, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
    _StructModule,
)

class _XInterfaceModule(_InterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> XClient: ...
    class Server(_DynamicCapabilityServer):
        def m(
            self,
            i: int,
            _context: XMCallContext,
            **kwargs: object,
        ) -> Awaitable[str | XMResultTuple | None]: ...
        def m_context(self, context: XMCallContext) -> Awaitable[None]: ...

class XMRequest(Protocol):
    i: int
    def send(self) -> XMResult: ...

class XMResult(Awaitable[XMResult], Protocol):
    t: str

class XMServerResult(_DynamicStructBuilder):
    @property
    def t(self) -> str: ...
    @t.setter
    def t(self, value: str) -> None: ...

class XMParams(Protocol):
    i: int

class XMCallContext(Protocol):
    params: XMParams
    @property
    def results(self) -> XMServerResult: ...

class XMResultTuple(NamedTuple):
    t: str

class XClient(_DynamicCapabilityClient):
    def m(self, i: int | None = None) -> XMResult: ...
    def m_request(self, i: int | None = None) -> XMRequest: ...

X: _XInterfaceModule

class _SStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        c: XClient | _XInterfaceModule.Server | None = None,
        **kwargs: object,
    ) -> SBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[SReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[SReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[SBuilder]: ...
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
    ) -> SReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> SReader: ...

class SReader(_DynamicStructReader):
    @property
    def c(self) -> XClient: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> SBuilder: ...

class SBuilder(_DynamicStructBuilder):
    @property
    def c(self) -> XClient: ...
    @c.setter
    def c(self, value: XClient | _XInterfaceModule.Server) -> None: ...
    @override
    def as_reader(self) -> SReader: ...

S: _SStructModule

class _YInterfaceModule(_InterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> YClient: ...
    class Server(_DynamicCapabilityServer):
        def m(
            self,
            hello: str,
            _context: YMCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def m_context(self, context: YMCallContext) -> Awaitable[None]: ...

class YMRequest(Protocol):
    hello: str
    def send(self) -> YMResult: ...

class YMResult(Awaitable[None], Protocol): ...

class YMParams(Protocol):
    hello: str

class YMCallContext(Protocol):
    params: YMParams

class YClient(_DynamicCapabilityClient):
    def m(self, hello: str | None = None) -> YMResult: ...
    def m_request(self, hello: str | None = None) -> YMRequest: ...

Y: _YInterfaceModule

class _ZInterfaceModule(_InterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> ZClient: ...
    class Server(_DynamicCapabilityServer):
        def m(
            self,
            n: int,
            _context: ZMCallContext,
            **kwargs: object,
        ) -> Awaitable[float | ZMResultTuple | None]: ...
        def m_context(self, context: ZMCallContext) -> Awaitable[None]: ...

class ZMRequest(Protocol):
    n: int
    def send(self) -> ZMResult: ...

class ZMResult(Awaitable[ZMResult], Protocol):
    r: float

class ZMServerResult(_DynamicStructBuilder):
    @property
    def r(self) -> float: ...
    @r.setter
    def r(self, value: float) -> None: ...

class ZMParams(Protocol):
    n: int

class ZMCallContext(Protocol):
    params: ZMParams
    @property
    def results(self) -> ZMServerResult: ...

class ZMResultTuple(NamedTuple):
    r: float

class ZClient(_DynamicCapabilityClient):
    def m(self, n: int | None = None) -> ZMResult: ...
    def m_request(self, n: int | None = None) -> ZMRequest: ...

Z: _ZInterfaceModule

# Top-level type aliases for use in type annotations
XServer = _XInterfaceModule.Server
YServer = _YInterfaceModule.Server
ZServer = _ZInterfaceModule.Server
