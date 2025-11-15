"""This is an automatically generated stub for `persistent.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator
from typing import Any, NamedTuple, Protocol, override

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

# Type alias for AnyPointer parameters (accepts all Cap'n Proto pointer types)
type AnyPointer = str | bytes | _DynamicStructBuilder | _DynamicStructReader | _DynamicCapabilityClient | _DynamicCapabilityServer

class _PersistentModule(_InterfaceModule):
    class _SaveParamsModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def sealFor(self) -> _DynamicObjectReader: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> SaveParamsBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def sealFor(self) -> _DynamicObjectReader: ...
            @sealFor.setter
            def sealFor(self, value: AnyPointer) -> None: ...
            @override
            def as_reader(self) -> SaveParamsReader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, sealFor: AnyPointer | None = None) -> SaveParamsBuilder: ...

    type SaveParamsReader = _SaveParamsModule.Reader
    type SaveParamsBuilder = _SaveParamsModule.Builder
    SaveParams: _SaveParamsModule
    class _SaveResultsModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def sturdyRef(self) -> _DynamicObjectReader: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> SaveResultsBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def sturdyRef(self) -> _DynamicObjectReader: ...
            @sturdyRef.setter
            def sturdyRef(self, value: AnyPointer) -> None: ...
            @override
            def as_reader(self) -> SaveResultsReader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, sturdyRef: AnyPointer | None = None) -> SaveResultsBuilder: ...

    type SaveResultsReader = _SaveResultsModule.Reader
    type SaveResultsBuilder = _SaveResultsModule.Builder
    SaveResults: _SaveResultsModule
    class SaveRequest(Protocol):
        sealFor: AnyPointer
        def send(self) -> _PersistentModule.PersistentClient.SaveResult: ...

    @classmethod
    def _new_client(cls, server: _PersistentModule.Server) -> _PersistentModule.PersistentClient: ...
    class Server(_DynamicCapabilityServer):
        class SaveResult(Awaitable[SaveResult], Protocol):
            sturdyRef: AnyPointer

        class SaveResultTuple(NamedTuple):
            sturdyRef: AnyPointer

        class SaveCallContext(Protocol):
            params: _PersistentModule.SaveRequest
            results: _PersistentModule.Server.SaveResult

        def save(self, sealFor: AnyPointer, _context: _PersistentModule.Server.SaveCallContext, **kwargs: Any) -> Awaitable[_PersistentModule.Server.SaveResultTuple | None]: ...
        def save_context(self, context: _PersistentModule.Server.SaveCallContext) -> Awaitable[None]: ...

    class PersistentClient(_DynamicCapabilityClient):
        class SaveResult(Awaitable[SaveResult], Protocol):
            sturdyRef: _DynamicObjectReader

        def save(self, sealFor: _DynamicObjectReader | None = None) -> _PersistentModule.PersistentClient.SaveResult: ...
        def save_request(self, sealFor: AnyPointer | None = None) -> _PersistentModule.SaveRequest: ...

Persistent: _PersistentModule

# Top-level type aliases for use in type annotations
type PersistentClient = _PersistentModule.PersistentClient
type SaveParamsBuilder = _PersistentModule._SaveParamsModule.Builder
type SaveParamsReader = _PersistentModule._SaveParamsModule.Reader
type SaveResultsBuilder = _PersistentModule._SaveResultsModule.Builder
type SaveResultsReader = _PersistentModule._SaveResultsModule.Reader
