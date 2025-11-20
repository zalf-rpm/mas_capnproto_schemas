"""This is an automatically generated stub for `registry.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, MutableSequence, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, NamedTuple, Protocol, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
    _StructModule,
)

from .common_capnp import (
    IdentifiableClient,
    IdInformationBuilder,
    IdInformationReader,
    _IdentifiableModule,
)
from .persistence_capnp import (
    SturdyRefBuilder,
    SturdyRefReader,
    VatIdBuilder,
    VatIdReader,
    _RestorerModule,
)

class _AdminModule(_IdentifiableModule):
    class AddcategoryRequest(Protocol):
        category: IdInformationBuilder
        upsert: bool
        @overload
        def init(self, name: Literal["category"]) -> IdInformationBuilder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> _AdminModule.AdminClient.AddcategoryResult: ...

    class RemovecategoryRequest(Protocol):
        categoryId: str
        moveObjectsToCategoryId: str
        def send(self) -> _AdminModule.AdminClient.RemovecategoryResult: ...

    class MoveobjectsRequest(Protocol):
        objectIds: Sequence[str]
        toCatId: str
        @overload
        def init(
            self, name: Literal["objectIds"], size: int = ...
        ) -> MutableSequence[str]: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> _AdminModule.AdminClient.MoveobjectsResult: ...

    class RemoveobjectsRequest(Protocol):
        objectIds: Sequence[str]
        @overload
        def init(
            self, name: Literal["objectIds"], size: int = ...
        ) -> MutableSequence[str]: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> _AdminModule.AdminClient.RemoveobjectsResult: ...

    class RegistryRequest(Protocol):
        def send(self) -> _AdminModule.AdminClient.RegistryResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _AdminModule.AdminClient: ...
    class Server(_IdentifiableModule.Server):
        class AddcategoryResult(Awaitable[AddcategoryResult], Protocol):
            success: bool

        class RemovecategoryResult(Awaitable[RemovecategoryResult], Protocol):
            removedObjects: Sequence[
                _IdentifiableModule.Server | _IdentifiableModule.IdentifiableClient
            ]

        class MoveobjectsResult(Awaitable[MoveobjectsResult], Protocol):
            movedObjectIds: Sequence[str]

        class RemoveobjectsResult(Awaitable[RemoveobjectsResult], Protocol):
            removedObjects: Sequence[
                _IdentifiableModule.Server | _IdentifiableModule.IdentifiableClient
            ]

        class RegistryResult(Awaitable[RegistryResult], Protocol):
            registry: _RegistryModule.Server | _RegistryModule.RegistryClient

        class AddcategoryResultTuple(NamedTuple):
            success: bool

        class RemovecategoryResultTuple(NamedTuple):
            removedObjects: Sequence[
                _IdentifiableModule.Server | _IdentifiableModule.IdentifiableClient
            ]

        class MoveobjectsResultTuple(NamedTuple):
            movedObjectIds: Sequence[str]

        class RemoveobjectsResultTuple(NamedTuple):
            removedObjects: Sequence[
                _IdentifiableModule.Server | _IdentifiableModule.IdentifiableClient
            ]

        class RegistryResultTuple(NamedTuple):
            registry: _RegistryModule.Server | _RegistryModule.RegistryClient

        class AddcategoryParams(Protocol):
            category: IdInformationReader
            upsert: bool

        class AddcategoryCallContext(Protocol):
            params: _AdminModule.Server.AddcategoryParams
            results: _AdminModule.Server.AddcategoryResult

        class RemovecategoryParams(Protocol):
            categoryId: str
            moveObjectsToCategoryId: str

        class RemovecategoryCallContext(Protocol):
            params: _AdminModule.Server.RemovecategoryParams
            results: _AdminModule.Server.RemovecategoryResult

        class MoveobjectsParams(Protocol):
            objectIds: Sequence[str]
            toCatId: str

        class MoveobjectsCallContext(Protocol):
            params: _AdminModule.Server.MoveobjectsParams
            results: _AdminModule.Server.MoveobjectsResult

        class RemoveobjectsParams(Protocol):
            objectIds: Sequence[str]

        class RemoveobjectsCallContext(Protocol):
            params: _AdminModule.Server.RemoveobjectsParams
            results: _AdminModule.Server.RemoveobjectsResult

        class RegistryParams(Protocol): ...

        class RegistryCallContext(Protocol):
            params: _AdminModule.Server.RegistryParams
            results: _AdminModule.Server.RegistryResult

        def addCategory(
            self,
            category: IdInformationReader,
            upsert: bool,
            _context: _AdminModule.Server.AddcategoryCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[bool | _AdminModule.Server.AddcategoryResultTuple | None]: ...
        def addCategory_context(
            self, context: _AdminModule.Server.AddcategoryCallContext
        ) -> Awaitable[None]: ...
        def removeCategory(
            self,
            categoryId: str,
            moveObjectsToCategoryId: str,
            _context: _AdminModule.Server.RemovecategoryCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_AdminModule.Server.RemovecategoryResultTuple | None]: ...
        def removeCategory_context(
            self, context: _AdminModule.Server.RemovecategoryCallContext
        ) -> Awaitable[None]: ...
        def moveObjects(
            self,
            objectIds: Sequence[str],
            toCatId: str,
            _context: _AdminModule.Server.MoveobjectsCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_AdminModule.Server.MoveobjectsResultTuple | None]: ...
        def moveObjects_context(
            self, context: _AdminModule.Server.MoveobjectsCallContext
        ) -> Awaitable[None]: ...
        def removeObjects(
            self,
            objectIds: Sequence[str],
            _context: _AdminModule.Server.RemoveobjectsCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_AdminModule.Server.RemoveobjectsResultTuple | None]: ...
        def removeObjects_context(
            self, context: _AdminModule.Server.RemoveobjectsCallContext
        ) -> Awaitable[None]: ...
        def registry(
            self,
            _context: _AdminModule.Server.RegistryCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[
            _RegistryModule.Server | _AdminModule.Server.RegistryResultTuple | None
        ]: ...
        def registry_context(
            self, context: _AdminModule.Server.RegistryCallContext
        ) -> Awaitable[None]: ...

    class AdminClient(_IdentifiableModule.IdentifiableClient):
        class AddcategoryResult(Awaitable[AddcategoryResult], Protocol):
            success: bool

        class RemovecategoryResult(Awaitable[RemovecategoryResult], Protocol):
            removedObjects: Sequence[_IdentifiableModule.IdentifiableClient]

        class MoveobjectsResult(Awaitable[MoveobjectsResult], Protocol):
            movedObjectIds: Sequence[str]

        class RemoveobjectsResult(Awaitable[RemoveobjectsResult], Protocol):
            removedObjects: Sequence[_IdentifiableModule.IdentifiableClient]

        class RegistryResult(Awaitable[RegistryResult], Protocol):
            registry: _RegistryModule.RegistryClient

        def addCategory(
            self,
            category: IdInformationBuilder
            | IdInformationReader
            | dict[str, Any]
            | None = None,
            upsert: bool | None = None,
        ) -> _AdminModule.AdminClient.AddcategoryResult: ...
        def removeCategory(
            self,
            categoryId: str | None = None,
            moveObjectsToCategoryId: str | None = None,
        ) -> _AdminModule.AdminClient.RemovecategoryResult: ...
        def moveObjects(
            self, objectIds: Sequence[str] | None = None, toCatId: str | None = None
        ) -> _AdminModule.AdminClient.MoveobjectsResult: ...
        def removeObjects(
            self, objectIds: Sequence[str] | None = None
        ) -> _AdminModule.AdminClient.RemoveobjectsResult: ...
        def registry(self) -> _AdminModule.AdminClient.RegistryResult: ...
        def addCategory_request(
            self,
            category: IdInformationBuilder | None = None,
            upsert: bool | None = None,
        ) -> _AdminModule.AddcategoryRequest: ...
        def removeCategory_request(
            self,
            categoryId: str | None = None,
            moveObjectsToCategoryId: str | None = None,
        ) -> _AdminModule.RemovecategoryRequest: ...
        def moveObjects_request(
            self, objectIds: Sequence[str] | None = None, toCatId: str | None = None
        ) -> _AdminModule.MoveobjectsRequest: ...
        def removeObjects_request(
            self, objectIds: Sequence[str] | None = None
        ) -> _AdminModule.RemoveobjectsRequest: ...
        def registry_request(self) -> _AdminModule.RegistryRequest: ...

class _RegistryModule(_IdentifiableModule):
    class _EntryModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def categoryId(self) -> str: ...
            @property
            def ref(self) -> _IdentifiableModule.IdentifiableClient: ...
            @property
            def name(self) -> str: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
            @property
            def id(self) -> str: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> EntryBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def categoryId(self) -> str: ...
            @categoryId.setter
            def categoryId(self, value: str) -> None: ...
            @property
            def ref(self) -> _IdentifiableModule.IdentifiableClient: ...
            @ref.setter
            def ref(
                self,
                value: _IdentifiableModule.IdentifiableClient
                | _IdentifiableModule.Server,
            ) -> None: ...
            @property
            def name(self) -> str: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
            @name.setter
            def name(self, value: str) -> None: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
            @property
            def id(self) -> str: ...
            @id.setter
            def id(self, value: str) -> None: ...
            @override
            def as_reader(self) -> EntryReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            categoryId: str | None = None,
            ref: _IdentifiableModule.IdentifiableClient
            | _IdentifiableModule.Server
            | None = None,
            name: str | None = None,
            id: str | None = None,
            **kwargs: Any,
        ) -> EntryBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[EntryReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[EntryReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[EntryBuilder]: ...
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> EntryReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> EntryReader: ...

    type EntryReader = _EntryModule.Reader
    type EntryBuilder = _EntryModule.Builder
    Entry: _EntryModule
    class SupportedcategoriesRequest(Protocol):
        def send(self) -> _RegistryModule.RegistryClient.SupportedcategoriesResult: ...

    class CategoryinfoRequest(Protocol):
        categoryId: str
        def send(self) -> _RegistryModule.RegistryClient.CategoryinfoResult: ...

    class EntriesRequest(Protocol):
        categoryId: str
        def send(self) -> _RegistryModule.RegistryClient.EntriesResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _RegistryModule.RegistryClient: ...
    class Server(_IdentifiableModule.Server):
        class SupportedcategoriesResult(Awaitable[SupportedcategoriesResult], Protocol):
            cats: Sequence[IdInformationBuilder | IdInformationReader]

        class CategoryinfoResult(Awaitable[CategoryinfoResult], Protocol):
            id: str
            name: str
            description: str

        class EntriesResult(Awaitable[EntriesResult], Protocol):
            entries: Sequence[EntryBuilder | EntryReader]

        class SupportedcategoriesResultTuple(NamedTuple):
            cats: Sequence[IdInformationBuilder | IdInformationReader]

        class CategoryinfoResultTuple(NamedTuple):
            id: str
            name: str
            description: str

        class EntriesResultTuple(NamedTuple):
            entries: Sequence[EntryBuilder | EntryReader]

        class SupportedcategoriesParams(Protocol): ...

        class SupportedcategoriesCallContext(Protocol):
            params: _RegistryModule.Server.SupportedcategoriesParams
            results: _RegistryModule.Server.SupportedcategoriesResult

        class CategoryinfoParams(Protocol):
            categoryId: str

        class CategoryinfoCallContext(Protocol):
            params: _RegistryModule.Server.CategoryinfoParams
            results: _RegistryModule.Server.CategoryinfoResult

        class EntriesParams(Protocol):
            categoryId: str

        class EntriesCallContext(Protocol):
            params: _RegistryModule.Server.EntriesParams
            results: _RegistryModule.Server.EntriesResult

        def supportedCategories(
            self,
            _context: _RegistryModule.Server.SupportedcategoriesCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[
            _RegistryModule.Server.SupportedcategoriesResultTuple | None
        ]: ...
        def supportedCategories_context(
            self, context: _RegistryModule.Server.SupportedcategoriesCallContext
        ) -> Awaitable[None]: ...
        def categoryInfo(
            self,
            categoryId: str,
            _context: _RegistryModule.Server.CategoryinfoCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_RegistryModule.Server.CategoryinfoResultTuple | None]: ...
        def categoryInfo_context(
            self, context: _RegistryModule.Server.CategoryinfoCallContext
        ) -> Awaitable[None]: ...
        def entries(
            self,
            categoryId: str,
            _context: _RegistryModule.Server.EntriesCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_RegistryModule.Server.EntriesResultTuple | None]: ...
        def entries_context(
            self, context: _RegistryModule.Server.EntriesCallContext
        ) -> Awaitable[None]: ...

    class RegistryClient(_IdentifiableModule.IdentifiableClient):
        class SupportedcategoriesResult(Awaitable[SupportedcategoriesResult], Protocol):
            cats: Sequence[IdInformationReader]

        class CategoryinfoResult(Awaitable[CategoryinfoResult], Protocol):
            id: str
            name: str
            description: str

        class EntriesResult(Awaitable[EntriesResult], Protocol):
            entries: Sequence[EntryReader]

        def supportedCategories(
            self,
        ) -> _RegistryModule.RegistryClient.SupportedcategoriesResult: ...
        def categoryInfo(
            self, categoryId: str | None = None
        ) -> _RegistryModule.RegistryClient.CategoryinfoResult: ...
        def entries(
            self, categoryId: str | None = None
        ) -> _RegistryModule.RegistryClient.EntriesResult: ...
        def supportedCategories_request(
            self,
        ) -> _RegistryModule.SupportedcategoriesRequest: ...
        def categoryInfo_request(
            self, categoryId: str | None = None
        ) -> _RegistryModule.CategoryinfoRequest: ...
        def entries_request(
            self, categoryId: str | None = None
        ) -> _RegistryModule.EntriesRequest: ...

Registry: _RegistryModule
Admin: _AdminModule

class _RegistrarModule(_IdentifiableModule):
    class _CrossDomainRestoreModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def vatId(self) -> VatIdReader: ...
            @property
            def restorer(self) -> _RestorerModule.RestorerClient: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> CrossDomainRestoreBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def vatId(self) -> VatIdBuilder: ...
            @vatId.setter
            def vatId(
                self, value: VatIdBuilder | VatIdReader | dict[str, Any]
            ) -> None: ...
            @property
            def restorer(self) -> _RestorerModule.RestorerClient: ...
            @restorer.setter
            def restorer(
                self, value: _RestorerModule.RestorerClient | _RestorerModule.Server
            ) -> None: ...
            def init(
                self, field: Literal["vatId"], size: int | None = None
            ) -> VatIdBuilder: ...
            @override
            def as_reader(self) -> CrossDomainRestoreReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            vatId: VatIdBuilder | dict[str, Any] | None = None,
            restorer: _RestorerModule.RestorerClient
            | _RestorerModule.Server
            | None = None,
            **kwargs: Any,
        ) -> CrossDomainRestoreBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[CrossDomainRestoreReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[CrossDomainRestoreReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[CrossDomainRestoreBuilder]: ...
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> CrossDomainRestoreReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> CrossDomainRestoreReader: ...

    type CrossDomainRestoreReader = _CrossDomainRestoreModule.Reader
    type CrossDomainRestoreBuilder = _CrossDomainRestoreModule.Builder
    CrossDomainRestore: _CrossDomainRestoreModule
    class _RegParamsModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def cap(self) -> _IdentifiableModule.IdentifiableClient: ...
            @property
            def regName(self) -> str: ...
            @property
            def categoryId(self) -> str: ...
            @property
            def xDomain(self) -> CrossDomainRestoreReader: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> RegParamsBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def cap(self) -> _IdentifiableModule.IdentifiableClient: ...
            @cap.setter
            def cap(
                self,
                value: _IdentifiableModule.IdentifiableClient
                | _IdentifiableModule.Server,
            ) -> None: ...
            @property
            def regName(self) -> str: ...
            @regName.setter
            def regName(self, value: str) -> None: ...
            @property
            def categoryId(self) -> str: ...
            @categoryId.setter
            def categoryId(self, value: str) -> None: ...
            @property
            def xDomain(self) -> CrossDomainRestoreBuilder: ...
            @xDomain.setter
            def xDomain(
                self,
                value: CrossDomainRestoreBuilder
                | CrossDomainRestoreReader
                | dict[str, Any],
            ) -> None: ...
            def init(
                self, field: Literal["xDomain"], size: int | None = None
            ) -> CrossDomainRestoreBuilder: ...
            @override
            def as_reader(self) -> RegParamsReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            cap: _IdentifiableModule.IdentifiableClient
            | _IdentifiableModule.Server
            | None = None,
            regName: str | None = None,
            categoryId: str | None = None,
            xDomain: CrossDomainRestoreBuilder | dict[str, Any] | None = None,
            **kwargs: Any,
        ) -> RegParamsBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[RegParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[RegParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[RegParamsBuilder]: ...
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> RegParamsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> RegParamsReader: ...

    type RegParamsReader = _RegParamsModule.Reader
    type RegParamsBuilder = _RegParamsModule.Builder
    RegParams: _RegParamsModule
    class _UnregisterModule(_InterfaceModule):
        class UnregisterRequest(Protocol):
            def send(
                self,
            ) -> (
                _RegistrarModule._UnregisterModule.UnregisterClient.UnregisterResult
            ): ...

        def _new_client(
            self, server: _DynamicCapabilityServer
        ) -> _RegistrarModule._UnregisterModule.UnregisterClient: ...
        class Server(_DynamicCapabilityServer):
            class UnregisterResult(Awaitable[UnregisterResult], Protocol):
                success: bool

            class UnregisterResultTuple(NamedTuple):
                success: bool

            class UnregisterParams(Protocol): ...

            class UnregisterCallContext(Protocol):
                params: _RegistrarModule._UnregisterModule.Server.UnregisterParams
                results: _RegistrarModule._UnregisterModule.Server.UnregisterResult

            def unregister(
                self,
                _context: _RegistrarModule._UnregisterModule.Server.UnregisterCallContext,
                **kwargs: dict[str, Any],
            ) -> Awaitable[
                bool
                | _RegistrarModule._UnregisterModule.Server.UnregisterResultTuple
                | None
            ]: ...
            def unregister_context(
                self,
                context: _RegistrarModule._UnregisterModule.Server.UnregisterCallContext,
            ) -> Awaitable[None]: ...

        class UnregisterClient(_DynamicCapabilityClient):
            class UnregisterResult(Awaitable[UnregisterResult], Protocol):
                success: bool

            def unregister(
                self,
            ) -> (
                _RegistrarModule._UnregisterModule.UnregisterClient.UnregisterResult
            ): ...
            def unregister_request(
                self,
            ) -> _RegistrarModule._UnregisterModule.UnregisterRequest: ...

    Unregister: _UnregisterModule
    type UnregisterClient = _RegistrarModule._UnregisterModule.UnregisterClient
    class RegisterRequest(Protocol):
        cap: IdentifiableClient | _IdentifiableModule.Server
        regName: str
        categoryId: str
        xDomain: CrossDomainRestoreBuilder
        @overload
        def init(self, name: Literal["xDomain"]) -> CrossDomainRestoreBuilder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> _RegistrarModule.RegistrarClient.RegisterResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _RegistrarModule.RegistrarClient: ...
    class Server(_IdentifiableModule.Server):
        class RegisterResult(Awaitable[RegisterResult], Protocol):
            unreg: (
                _RegistrarModule._UnregisterModule.Server
                | _RegistrarModule._UnregisterModule.UnregisterClient
            )
            reregSR: SturdyRefBuilder | SturdyRefReader

        class RegisterResultTuple(NamedTuple):
            unreg: (
                _RegistrarModule._UnregisterModule.Server
                | _RegistrarModule._UnregisterModule.UnregisterClient
            )
            reregSR: SturdyRefBuilder | SturdyRefReader

        class RegisterParams(Protocol):
            cap: IdentifiableClient
            regName: str
            categoryId: str
            xDomain: CrossDomainRestoreReader

        class RegisterCallContext(Protocol):
            params: _RegistrarModule.Server.RegisterParams
            results: _RegistrarModule.Server.RegisterResult

        def register(
            self,
            cap: IdentifiableClient,
            regName: str,
            categoryId: str,
            xDomain: CrossDomainRestoreReader,
            _context: _RegistrarModule.Server.RegisterCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_RegistrarModule.Server.RegisterResultTuple | None]: ...
        def register_context(
            self, context: _RegistrarModule.Server.RegisterCallContext
        ) -> Awaitable[None]: ...

    class RegistrarClient(_IdentifiableModule.IdentifiableClient):
        class RegisterResult(Awaitable[RegisterResult], Protocol):
            unreg: _RegistrarModule._UnregisterModule.UnregisterClient
            reregSR: SturdyRefReader

        def register(
            self,
            cap: IdentifiableClient | _IdentifiableModule.Server | None = None,
            regName: str | None = None,
            categoryId: str | None = None,
            xDomain: CrossDomainRestoreBuilder
            | CrossDomainRestoreReader
            | dict[str, Any]
            | None = None,
        ) -> _RegistrarModule.RegistrarClient.RegisterResult: ...
        def register_request(
            self,
            cap: IdentifiableClient | _IdentifiableModule.Server | None = None,
            regName: str | None = None,
            categoryId: str | None = None,
            xDomain: CrossDomainRestoreBuilder | None = None,
        ) -> _RegistrarModule.RegisterRequest: ...

Registrar: _RegistrarModule

# Top-level type aliases for use in type annotations
type AddcategoryResult = _AdminModule.AdminClient.AddcategoryResult
type AdminClient = _AdminModule.AdminClient
type CategoryinfoResult = _RegistryModule.RegistryClient.CategoryinfoResult
type CrossDomainRestoreBuilder = _RegistrarModule._CrossDomainRestoreModule.Builder
type CrossDomainRestoreReader = _RegistrarModule._CrossDomainRestoreModule.Reader
type EntriesResult = _RegistryModule.RegistryClient.EntriesResult
type EntryBuilder = _RegistryModule._EntryModule.Builder
type EntryReader = _RegistryModule._EntryModule.Reader
type MoveobjectsResult = _AdminModule.AdminClient.MoveobjectsResult
type RegParamsBuilder = _RegistrarModule._RegParamsModule.Builder
type RegParamsReader = _RegistrarModule._RegParamsModule.Reader
type RegisterResult = _RegistrarModule.RegistrarClient.RegisterResult
type RegistrarClient = _RegistrarModule.RegistrarClient
type RegistryClient = _RegistryModule.RegistryClient
type RegistryResult = _AdminModule.AdminClient.RegistryResult
type RemovecategoryResult = _AdminModule.AdminClient.RemovecategoryResult
type RemoveobjectsResult = _AdminModule.AdminClient.RemoveobjectsResult
type SupportedcategoriesResult = (
    _RegistryModule.RegistryClient.SupportedcategoriesResult
)
type UnregisterClient = _RegistrarModule._UnregisterModule.UnregisterClient
type UnregisterResult = (
    _RegistrarModule._UnregisterModule.UnregisterClient.UnregisterResult
)
