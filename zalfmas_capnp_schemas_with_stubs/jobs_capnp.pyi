"""This is an automatically generated stub for `jobs.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, NamedTuple, Protocol, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicObjectReader,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
    _Request,
    _StructModule,
)

from .common_capnp import Identifiable, IdentifiableClient, _IdentifiableModule
from .persistence_capnp import Persistent, PersistentClient, _PersistentModule

# Type alias for AnyPointer parameters (accepts all Cap'n Proto pointer types)
type AnyPointer = str | bytes | _DynamicStructBuilder | _DynamicStructReader | _DynamicCapabilityClient | _DynamicCapabilityServer

class _JobModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def data(self) -> _DynamicObjectReader: ...
        @property
        def noFurtherJobs(self) -> bool: ...
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> JobBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def data(self) -> _DynamicObjectReader: ...
        @data.setter
        def data(self, value: AnyPointer) -> None: ...
        @property
        def noFurtherJobs(self) -> bool: ...
        @noFurtherJobs.setter
        def noFurtherJobs(self, value: bool) -> None: ...
        @override
        def as_reader(self) -> JobReader: ...

    @override
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, data: AnyPointer | None = None, noFurtherJobs: bool | None = None, **kwargs: Any) -> JobBuilder: ...
    @overload
    def from_bytes(self, buf: bytes, traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ...) -> AbstractContextManager[JobReader]: ...
    @overload
    def from_bytes(self, buf: bytes, traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ..., *, builder: Literal[False]) -> AbstractContextManager[JobReader]: ...
    @overload
    def from_bytes(self, buf: bytes, traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ..., *, builder: Literal[True]) -> AbstractContextManager[JobBuilder]: ...
    def from_bytes_packed(self, buf: bytes, traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ...) -> _DynamicStructReader: ...
    @override
    def read(self, file: IO[str] | IO[bytes], traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ...) -> JobReader: ...
    @override
    def read_packed(self, file: IO[str] | IO[bytes], traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ...) -> JobReader: ...

Job: _JobModule

class _ServiceModule(_IdentifiableModule, _PersistentModule):
    class NextjobRequest(Protocol):
        def send(self) -> _ServiceModule.ServiceClient.NextjobResult: ...

    @classmethod
    def _new_client(cls, server: _DynamicCapabilityServer) -> _ServiceModule.ServiceClient: ...
    class Server(_IdentifiableModule.Server, _PersistentModule.Server):
        class NextjobResult(Awaitable[NextjobResult], Protocol):
            job: _JobModule.Builder | _JobModule.Reader

        class NextjobResultTuple(NamedTuple):
            job: _JobModule.Builder | _JobModule.Reader

        class NextjobCallContext(Protocol):
            params: _ServiceModule.NextjobRequest
            results: _ServiceModule.Server.NextjobResult

        def nextJob(self, _context: _ServiceModule.Server.NextjobCallContext, **kwargs: Any) -> Awaitable[_ServiceModule.Server.NextjobResultTuple | None]: ...
        def nextJob_context(self, context: _ServiceModule.Server.NextjobCallContext) -> Awaitable[None]: ...

    class ServiceClient(_IdentifiableModule.IdentifiableClient, _PersistentModule.PersistentClient):
        class NextjobResult(Awaitable[NextjobResult], Protocol):
            job: _JobModule.Builder | _JobModule.Reader

        def nextJob(self) -> _ServiceModule.ServiceClient.NextjobResult: ...
        def nextJob_request(self) -> _ServiceModule.NextjobRequest: ...

Service: _ServiceModule

# Top-level type aliases for use in type annotations
type JobBuilder = _JobModule.Builder
type JobReader = _JobModule.Reader
type ServiceClient = _ServiceModule.ServiceClient
