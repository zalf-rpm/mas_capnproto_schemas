"""This is an automatically generated stub for `persistent.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator
from typing import Any, Generic, NamedTuple, Protocol, TypeAlias, TypeVar, override

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

_PersistentModule_Owner = TypeVar("_PersistentModule_Owner")
_PersistentModule_SturdyRef = TypeVar("_PersistentModule_SturdyRef")

class _PersistentModule(_InterfaceModule):
    class _SaveParamsModule(Generic[_PersistentModule_Owner], _StructModule):
        class Reader(_DynamicStructReader):
            @property
            def sealFor(self) -> Any: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _PersistentModule._SaveParamsModule.Builder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def sealFor(self) -> Any: ...
            @sealFor.setter
            def sealFor(self, value: Any) -> None: ...
            @override
            def as_reader(self) -> _PersistentModule._SaveParamsModule.Reader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, sealFor: Any | None = None) -> _PersistentModule._SaveParamsModule.Builder: ...

    SaveParamsReader: TypeAlias = _SaveParamsModule.Reader
    SaveParamsBuilder: TypeAlias = _SaveParamsModule.Builder
    SaveParams: _SaveParamsModule
    class _SaveResultsModule(Generic[_PersistentModule_SturdyRef], _StructModule):
        class Reader(_DynamicStructReader):
            @property
            def sturdyRef(self) -> _PersistentModule_SturdyRef: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _PersistentModule._SaveResultsModule.Builder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def sturdyRef(self) -> _PersistentModule_SturdyRef: ...
            @sturdyRef.setter
            def sturdyRef(self, value: _PersistentModule_SturdyRef) -> None: ...
            @override
            def as_reader(self) -> _PersistentModule._SaveResultsModule.Reader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, sturdyRef: _PersistentModule_SturdyRef | None = None) -> _PersistentModule._SaveResultsModule.Builder: ...

    SaveResultsReader: TypeAlias = _SaveResultsModule.Reader
    SaveResultsBuilder: TypeAlias = _SaveResultsModule.Builder
    SaveResults: _SaveResultsModule
    class SaveRequest(Protocol):
        sealFor: _DynamicObjectReader
        def send(self) -> _PersistentModule.PersistentClient.SaveResult: ...

    @classmethod
    def _new_client(cls, server: _PersistentModule.Server) -> _PersistentModule.PersistentClient: ...
    class Server(_DynamicCapabilityServer):
        class SaveResult(Awaitable[SaveResult], Protocol):
            sturdyRef: str | bytes | _DynamicStructBuilder | _DynamicStructReader | _DynamicCapabilityClient | _DynamicCapabilityServer

        class SaveResultTuple(NamedTuple):
            sturdyRef: str | bytes | _DynamicStructBuilder | _DynamicStructReader | _DynamicCapabilityClient | _DynamicCapabilityServer

        class SaveCallContext(Protocol):
            params: _PersistentModule.SaveRequest
            results: _PersistentModule.Server.SaveResult

        def save(self, sealFor: _DynamicObjectReader, _context: _PersistentModule.Server.SaveCallContext, **kwargs: Any) -> Awaitable[_PersistentModule.Server.SaveResultTuple | None]: ...
        def save_context(self, context: _PersistentModule.Server.SaveCallContext) -> Awaitable[None]: ...

    class PersistentClient(_DynamicCapabilityClient):
        class SaveResult(Awaitable[SaveResult], Protocol):
            sturdyRef: _DynamicObjectReader

        def save(self, sealFor: _DynamicObjectReader | None = None) -> _PersistentModule.PersistentClient.SaveResult: ...
        def save_request(self, sealFor: _DynamicObjectReader | None = None) -> _PersistentModule.SaveRequest: ...

Persistent: _PersistentModule
PersistentClient: TypeAlias = _PersistentModule.PersistentClient

# Top-level type aliases for use in type annotations
SaveParamsBuilder: TypeAlias = _PersistentModule._SaveParamsModule.Builder
SaveParamsReader: TypeAlias = _PersistentModule._SaveParamsModule.Reader
SaveResultsBuilder: TypeAlias = _PersistentModule._SaveResultsModule.Builder
SaveResultsReader: TypeAlias = _PersistentModule._SaveResultsModule.Reader
