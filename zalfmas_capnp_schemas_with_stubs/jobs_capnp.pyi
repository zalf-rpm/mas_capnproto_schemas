"""This is an automatically generated stub for `jobs.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator
from typing import Any, Generic, NamedTuple, Protocol, TypeAlias, TypeVar, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
    _Request,
    _StructModule,
)

from .common_capnp import Identifiable, IdentifiableClient, _IdentifiableModule
from .persistence_capnp import Persistent, PersistentClient, _PersistentModule

_Payload = TypeVar("_Payload")

class _JobModule(Generic[_Payload], _StructModule):
    class Reader(_DynamicStructReader):
        @property
        def data(self) -> _Payload: ...
        @property
        def noFurtherJobs(self) -> bool: ...
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _JobModule.Builder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def data(self) -> _Payload: ...
        @data.setter
        def data(self, value: _Payload) -> None: ...
        @property
        def noFurtherJobs(self) -> bool: ...
        @noFurtherJobs.setter
        def noFurtherJobs(self, value: bool) -> None: ...
        @override
        def as_reader(self) -> _JobModule.Reader: ...

    @override
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, data: _Payload | None = None, noFurtherJobs: bool | None = None) -> _JobModule.Builder: ...

JobReader: TypeAlias = _JobModule.Reader
JobBuilder: TypeAlias = _JobModule.Builder
Job: _JobModule

class _ServiceModule(_IdentifiableModule, _PersistentModule):
    class NextjobRequest(Protocol):
        def send(self) -> _ServiceModule.ServiceClient.NextjobResult: ...

    @classmethod
    def _new_client(cls, server: _ServiceModule.Server | _IdentifiableModule.Server | _PersistentModule.Server) -> _ServiceModule.ServiceClient: ...
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
ServiceClient: TypeAlias = _ServiceModule.ServiceClient
