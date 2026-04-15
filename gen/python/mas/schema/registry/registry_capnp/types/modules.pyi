"""Module helper types for `registry.capnp`."""

from collections.abc import Awaitable, Callable, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
    _StructModule,
)

from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.common.common_capnp.types.readers import IdInformationReader
from mas.schema.persistence.persistence_capnp.types.builders import VatIdBuilder
from mas.schema.persistence.persistence_capnp.types.clients import RestorerClient
from mas.schema.persistence.persistence_capnp.types.modules import (
    _RestorerInterfaceModule,
)

from . import _all as _all

class _AdminInterfaceModule(_IdentifiableInterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> _all.AdminClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def addCategory(
            self,
            category: IdInformationReader,
            upsert: bool,
            _context: _all.AddcategoryCallContext,
            **kwargs: object,
        ) -> Awaitable[bool | _all.AddcategoryResultTuple | None]: ...
        def addCategory_context(
            self,
            context: _all.AddcategoryCallContext,
        ) -> Awaitable[None]: ...
        def removeCategory(
            self,
            categoryId: str,
            moveObjectsToCategoryId: str,
            _context: _all.RemovecategoryCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _all.IdentifiableClientListBuilder
            | _all.IdentifiableClientListReader
            | Sequence[Any]
            | _all.RemovecategoryResultTuple
            | None
        ]: ...
        def removeCategory_context(
            self,
            context: _all.RemovecategoryCallContext,
        ) -> Awaitable[None]: ...
        def moveObjects(
            self,
            objectIds: _all.TextListReader,
            toCatId: str,
            _context: _all.MoveobjectsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _all.TextListBuilder
            | _all.TextListReader
            | Sequence[Any]
            | _all.MoveobjectsResultTuple
            | None
        ]: ...
        def moveObjects_context(
            self,
            context: _all.MoveobjectsCallContext,
        ) -> Awaitable[None]: ...
        def removeObjects(
            self,
            objectIds: _all.TextListReader,
            _context: _all.RemoveobjectsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _all.IdentifiableClientListBuilder
            | _all.IdentifiableClientListReader
            | Sequence[Any]
            | _all.RemoveobjectsResultTuple
            | None
        ]: ...
        def removeObjects_context(
            self,
            context: _all.RemoveobjectsCallContext,
        ) -> Awaitable[None]: ...
        def registry(
            self,
            _context: _all.RegistryCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _RegistryInterfaceModule.Server
            | _all.RegistryClient
            | _all.RegistryResultTuple
            | None
        ]: ...
        def registry_context(
            self,
            context: _all.RegistryCallContext,
        ) -> Awaitable[None]: ...

class _RegistryInterfaceModule(_IdentifiableInterfaceModule):
    class _EntryStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            categoryId: str | None = None,
            ref: IdentifiableClient | _IdentifiableInterfaceModule.Server | None = None,
            name: str | None = None,
            id: str | None = None,
            **kwargs: object,
        ) -> _all.EntryBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.EntryReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.EntryReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.EntryBuilder]: ...
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
        ) -> _all.EntryReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.EntryReader: ...

    Entry: _EntryStructModule
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> _all.RegistryClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def supportedCategories(
            self,
            _context: _all.SupportedcategoriesCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _all.IdInformationListBuilder
            | _all.IdInformationListReader
            | Sequence[Any]
            | _all.SupportedcategoriesResultTuple
            | None
        ]: ...
        def supportedCategories_context(
            self,
            context: _all.SupportedcategoriesCallContext,
        ) -> Awaitable[None]: ...
        def categoryInfo(
            self,
            categoryId: str,
            _context: _all.CategoryinfoCallContext,
            **kwargs: object,
        ) -> Awaitable[_all.CategoryinfoResultTuple | None]: ...
        def categoryInfo_context(
            self,
            context: _all.CategoryinfoCallContext,
        ) -> Awaitable[None]: ...
        def entries(
            self,
            categoryId: str,
            _context: _all.EntriesCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _all.EntryListBuilder
            | _all.EntryListReader
            | Sequence[Any]
            | _all.EntriesResultTuple
            | None
        ]: ...
        def entries_context(
            self,
            context: _all.EntriesCallContext,
        ) -> Awaitable[None]: ...

class _RegistrarInterfaceModule(_IdentifiableInterfaceModule):
    class _CrossDomainRestoreStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            vatId: VatIdBuilder | dict[str, Any] | None = None,
            restorer: RestorerClient | _RestorerInterfaceModule.Server | None = None,
            **kwargs: object,
        ) -> _all.CrossDomainRestoreBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.CrossDomainRestoreReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.CrossDomainRestoreReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.CrossDomainRestoreBuilder]: ...
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
        ) -> _all.CrossDomainRestoreReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.CrossDomainRestoreReader: ...

    CrossDomainRestore: _CrossDomainRestoreStructModule
    class _RegParamsStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            cap: IdentifiableClient | _IdentifiableInterfaceModule.Server | None = None,
            regName: str | None = None,
            categoryId: str | None = None,
            xDomain: _all.CrossDomainRestoreBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> _all.RegParamsBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.RegParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.RegParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.RegParamsBuilder]: ...
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
        ) -> _all.RegParamsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.RegParamsReader: ...

    RegParams: _RegParamsStructModule
    class _UnregisterInterfaceModule(_InterfaceModule):
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> _all.UnregisterClient: ...
        class Server(_DynamicCapabilityServer):
            def unregister(
                self,
                _context: _all.UnregisterCallContext,
                **kwargs: object,
            ) -> Awaitable[bool | _all.UnregisterResultTuple | None]: ...
            def unregister_context(
                self,
                context: _all.UnregisterCallContext,
            ) -> Awaitable[None]: ...

    Unregister: _UnregisterInterfaceModule
    type UnregisterServer = _RegistrarInterfaceModule._UnregisterInterfaceModule.Server
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> _all.RegistrarClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def register(
            self,
            cap: IdentifiableClient,
            regName: str,
            categoryId: str,
            xDomain: _all.CrossDomainRestoreReader,
            _context: _all.RegisterCallContext,
            **kwargs: object,
        ) -> Awaitable[_all.RegisterResultTuple | None]: ...
        def register_context(
            self,
            context: _all.RegisterCallContext,
        ) -> Awaitable[None]: ...
