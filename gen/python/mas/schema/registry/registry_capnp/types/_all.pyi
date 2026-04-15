"""This is an automatically generated stub for `registry.capnp`."""

from collections.abc import Awaitable, Callable, Iterator, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, NamedTuple, Protocol, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicListBuilder,
    _DynamicListReader,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
    _StructModule,
)

from mas.schema.common.common_capnp.types.builders import IdInformationBuilder
from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.common.common_capnp.types.readers import IdInformationReader
from mas.schema.persistence.persistence_capnp.types.builders import (
    SturdyRefBuilder,
    VatIdBuilder,
)
from mas.schema.persistence.persistence_capnp.types.clients import RestorerClient
from mas.schema.persistence.persistence_capnp.types.modules import (
    _RestorerInterfaceModule,
)
from mas.schema.persistence.persistence_capnp.types.readers import (
    SturdyRefReader,
    VatIdReader,
)

class _AdminInterfaceModule(_IdentifiableInterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> AdminClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def addCategory(
            self,
            category: IdInformationReader,
            upsert: bool,
            _context: AddcategoryCallContext,
            **kwargs: object,
        ) -> Awaitable[bool | AddcategoryResultTuple | None]: ...
        def addCategory_context(
            self,
            context: AddcategoryCallContext,
        ) -> Awaitable[None]: ...
        def removeCategory(
            self,
            categoryId: str,
            moveObjectsToCategoryId: str,
            _context: RemovecategoryCallContext,
            **kwargs: object,
        ) -> Awaitable[
            IdentifiableClientListBuilder
            | IdentifiableClientListReader
            | Sequence[Any]
            | RemovecategoryResultTuple
            | None
        ]: ...
        def removeCategory_context(
            self,
            context: RemovecategoryCallContext,
        ) -> Awaitable[None]: ...
        def moveObjects(
            self,
            objectIds: TextListReader,
            toCatId: str,
            _context: MoveobjectsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            TextListBuilder
            | TextListReader
            | Sequence[Any]
            | MoveobjectsResultTuple
            | None
        ]: ...
        def moveObjects_context(
            self,
            context: MoveobjectsCallContext,
        ) -> Awaitable[None]: ...
        def removeObjects(
            self,
            objectIds: TextListReader,
            _context: RemoveobjectsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            IdentifiableClientListBuilder
            | IdentifiableClientListReader
            | Sequence[Any]
            | RemoveobjectsResultTuple
            | None
        ]: ...
        def removeObjects_context(
            self,
            context: RemoveobjectsCallContext,
        ) -> Awaitable[None]: ...
        def registry(
            self,
            _context: RegistryCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _RegistryInterfaceModule.Server
            | RegistryClient
            | RegistryResultTuple
            | None
        ]: ...
        def registry_context(self, context: RegistryCallContext) -> Awaitable[None]: ...

class AddcategoryRequest(Protocol):
    category: IdInformationBuilder
    upsert: bool
    @overload
    def init(self, name: Literal["category"]) -> IdInformationBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> AddcategoryResult: ...

class AddcategoryResult(Awaitable[AddcategoryResult], Protocol):
    success: bool

class AddcategoryServerResult(_DynamicStructBuilder):
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class AddcategoryParams(Protocol):
    category: IdInformationReader
    upsert: bool

class AddcategoryCallContext(Protocol):
    params: AddcategoryParams
    @property
    def results(self) -> AddcategoryServerResult: ...

class AddcategoryResultTuple(NamedTuple):
    success: bool

class RemovecategoryRequest(Protocol):
    categoryId: str
    moveObjectsToCategoryId: str
    def send(self) -> RemovecategoryResult: ...

class _IdentifiableClientList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> IdentifiableClient: ...
        @override
        def __iter__(self) -> Iterator[IdentifiableClient]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> IdentifiableClient: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: IdentifiableClient | _IdentifiableInterfaceModule.Server,
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[IdentifiableClient]: ...

class RemovecategoryResult(Awaitable[RemovecategoryResult], Protocol):
    removedObjects: IdentifiableClientListReader

class RemovecategoryServerResult(_DynamicStructBuilder):
    @property
    def removedObjects(self) -> IdentifiableClientListBuilder: ...
    @removedObjects.setter
    def removedObjects(
        self,
        value: IdentifiableClientListBuilder
        | IdentifiableClientListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["removedObjects"],
        size: int | None = None,
    ) -> IdentifiableClientListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class RemovecategoryParams(Protocol):
    categoryId: str
    moveObjectsToCategoryId: str

class RemovecategoryCallContext(Protocol):
    params: RemovecategoryParams
    @property
    def results(self) -> RemovecategoryServerResult: ...

class RemovecategoryResultTuple(NamedTuple):
    removedObjects: (
        IdentifiableClientListBuilder | IdentifiableClientListReader | Sequence[Any]
    )

class _TextList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> str: ...
        @override
        def __iter__(self) -> Iterator[str]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> str: ...
        @override
        def __setitem__(self, key: int, value: str) -> None: ...
        @override
        def __iter__(self) -> Iterator[str]: ...

class MoveobjectsRequest(Protocol):
    objectIds: TextListBuilder | TextListReader | Sequence[Any]
    toCatId: str
    @overload
    def init(self, name: Literal["objectIds"], size: int = ...) -> TextListBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> MoveobjectsResult: ...

class MoveobjectsResult(Awaitable[MoveobjectsResult], Protocol):
    movedObjectIds: TextListReader

class MoveobjectsServerResult(_DynamicStructBuilder):
    @property
    def movedObjectIds(self) -> TextListBuilder: ...
    @movedObjectIds.setter
    def movedObjectIds(
        self,
        value: TextListBuilder | TextListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["movedObjectIds"],
        size: int | None = None,
    ) -> TextListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class MoveobjectsParams(Protocol):
    objectIds: TextListReader
    toCatId: str

class MoveobjectsCallContext(Protocol):
    params: MoveobjectsParams
    @property
    def results(self) -> MoveobjectsServerResult: ...

class MoveobjectsResultTuple(NamedTuple):
    movedObjectIds: TextListBuilder | TextListReader | Sequence[Any]

class RemoveobjectsRequest(Protocol):
    objectIds: TextListBuilder | TextListReader | Sequence[Any]
    @overload
    def init(self, name: Literal["objectIds"], size: int = ...) -> TextListBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> RemoveobjectsResult: ...

class RemoveobjectsResult(Awaitable[RemoveobjectsResult], Protocol):
    removedObjects: IdentifiableClientListReader

class RemoveobjectsServerResult(_DynamicStructBuilder):
    @property
    def removedObjects(self) -> IdentifiableClientListBuilder: ...
    @removedObjects.setter
    def removedObjects(
        self,
        value: IdentifiableClientListBuilder
        | IdentifiableClientListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["removedObjects"],
        size: int | None = None,
    ) -> IdentifiableClientListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class RemoveobjectsParams(Protocol):
    objectIds: TextListReader

class RemoveobjectsCallContext(Protocol):
    params: RemoveobjectsParams
    @property
    def results(self) -> RemoveobjectsServerResult: ...

class RemoveobjectsResultTuple(NamedTuple):
    removedObjects: (
        IdentifiableClientListBuilder | IdentifiableClientListReader | Sequence[Any]
    )

class RegistryRequest(Protocol):
    def send(self) -> RegistryResult: ...

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
        ) -> EntryBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[EntryReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[EntryReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[EntryBuilder]: ...
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
        ) -> EntryReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> EntryReader: ...

    Entry: _EntryStructModule
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> RegistryClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def supportedCategories(
            self,
            _context: SupportedcategoriesCallContext,
            **kwargs: object,
        ) -> Awaitable[
            IdInformationListBuilder
            | IdInformationListReader
            | Sequence[Any]
            | SupportedcategoriesResultTuple
            | None
        ]: ...
        def supportedCategories_context(
            self,
            context: SupportedcategoriesCallContext,
        ) -> Awaitable[None]: ...
        def categoryInfo(
            self,
            categoryId: str,
            _context: CategoryinfoCallContext,
            **kwargs: object,
        ) -> Awaitable[CategoryinfoResultTuple | None]: ...
        def categoryInfo_context(
            self,
            context: CategoryinfoCallContext,
        ) -> Awaitable[None]: ...
        def entries(
            self,
            categoryId: str,
            _context: EntriesCallContext,
            **kwargs: object,
        ) -> Awaitable[
            EntryListBuilder
            | EntryListReader
            | Sequence[Any]
            | EntriesResultTuple
            | None
        ]: ...
        def entries_context(self, context: EntriesCallContext) -> Awaitable[None]: ...

class EntryReader(_DynamicStructReader):
    @property
    def categoryId(self) -> str: ...
    @property
    def ref(self) -> IdentifiableClient: ...
    @property
    def name(self) -> str: ...
    @property
    def id(self) -> str: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> EntryBuilder: ...

class EntryBuilder(_DynamicStructBuilder):
    @property
    def categoryId(self) -> str: ...
    @categoryId.setter
    def categoryId(self, value: str) -> None: ...
    @property
    def ref(self) -> IdentifiableClient: ...
    @ref.setter
    def ref(
        self,
        value: IdentifiableClient | _IdentifiableInterfaceModule.Server,
    ) -> None: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str) -> None: ...
    @override
    def as_reader(self) -> EntryReader: ...

class SupportedcategoriesRequest(Protocol):
    def send(self) -> SupportedcategoriesResult: ...

class _IdInformationList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> IdInformationReader: ...
        @override
        def __iter__(self) -> Iterator[IdInformationReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> IdInformationBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: IdInformationReader | IdInformationBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[IdInformationBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> IdInformationBuilder: ...

class SupportedcategoriesResult(Awaitable[SupportedcategoriesResult], Protocol):
    cats: IdInformationListReader

class SupportedcategoriesServerResult(_DynamicStructBuilder):
    @property
    def cats(self) -> IdInformationListBuilder: ...
    @cats.setter
    def cats(
        self,
        value: IdInformationListBuilder | IdInformationListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["cats"],
        size: int | None = None,
    ) -> IdInformationListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class SupportedcategoriesParams(Protocol): ...

class SupportedcategoriesCallContext(Protocol):
    params: SupportedcategoriesParams
    @property
    def results(self) -> SupportedcategoriesServerResult: ...

class SupportedcategoriesResultTuple(NamedTuple):
    cats: IdInformationListBuilder | IdInformationListReader | Sequence[Any]

class CategoryinfoRequest(Protocol):
    categoryId: str
    def send(self) -> CategoryinfoResult: ...

class CategoryinfoResult(Awaitable[CategoryinfoResult], Protocol):
    id: str
    name: str
    description: str

class CategoryinfoParams(Protocol):
    categoryId: str

class CategoryinfoCallContext(Protocol):
    params: CategoryinfoParams
    @property
    def results(self) -> IdInformationBuilder: ...

class CategoryinfoResultTuple(NamedTuple):
    id: str
    name: str
    description: str

class EntriesRequest(Protocol):
    categoryId: str
    def send(self) -> EntriesResult: ...

class _EntryList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> EntryReader: ...
        @override
        def __iter__(self) -> Iterator[EntryReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> EntryBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: EntryReader | EntryBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[EntryBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> EntryBuilder: ...

class EntriesResult(Awaitable[EntriesResult], Protocol):
    entries: EntryListReader

class EntriesServerResult(_DynamicStructBuilder):
    @property
    def entries(self) -> EntryListBuilder: ...
    @entries.setter
    def entries(
        self,
        value: EntryListBuilder | EntryListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["entries"],
        size: int | None = None,
    ) -> EntryListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class EntriesParams(Protocol):
    categoryId: str

class EntriesCallContext(Protocol):
    params: EntriesParams
    @property
    def results(self) -> EntriesServerResult: ...

class EntriesResultTuple(NamedTuple):
    entries: EntryListBuilder | EntryListReader | Sequence[Any]

class RegistryClient(IdentifiableClient):
    def supportedCategories(self) -> SupportedcategoriesResult: ...
    def categoryInfo(self, categoryId: str | None = None) -> CategoryinfoResult: ...
    def entries(self, categoryId: str | None = None) -> EntriesResult: ...
    def supportedCategories_request(self) -> SupportedcategoriesRequest: ...
    def categoryInfo_request(
        self,
        categoryId: str | None = None,
    ) -> CategoryinfoRequest: ...
    def entries_request(self, categoryId: str | None = None) -> EntriesRequest: ...

Registry: _RegistryInterfaceModule

class RegistryResult(Awaitable[RegistryResult], Protocol):
    registry: RegistryClient

class RegistryServerResult(_DynamicStructBuilder):
    @property
    def registry(self) -> _RegistryInterfaceModule.Server | RegistryClient: ...
    @registry.setter
    def registry(
        self,
        value: _RegistryInterfaceModule.Server | RegistryClient,
    ) -> None: ...

class RegistryParams(Protocol): ...

class RegistryCallContext(Protocol):
    params: RegistryParams
    @property
    def results(self) -> RegistryServerResult: ...

class RegistryResultTuple(NamedTuple):
    registry: _RegistryInterfaceModule.Server | RegistryClient

class AdminClient(IdentifiableClient):
    def addCategory(
        self,
        category: IdInformationBuilder
        | IdInformationReader
        | dict[str, Any]
        | None = None,
        upsert: bool | None = None,
    ) -> AddcategoryResult: ...
    def removeCategory(
        self,
        categoryId: str | None = None,
        moveObjectsToCategoryId: str | None = None,
    ) -> RemovecategoryResult: ...
    def moveObjects(
        self,
        objectIds: TextListBuilder | TextListReader | Sequence[Any] | None = None,
        toCatId: str | None = None,
    ) -> MoveobjectsResult: ...
    def removeObjects(
        self,
        objectIds: TextListBuilder | TextListReader | Sequence[Any] | None = None,
    ) -> RemoveobjectsResult: ...
    def registry(self) -> RegistryResult: ...
    def addCategory_request(
        self,
        category: IdInformationBuilder | None = None,
        upsert: bool | None = None,
    ) -> AddcategoryRequest: ...
    def removeCategory_request(
        self,
        categoryId: str | None = None,
        moveObjectsToCategoryId: str | None = None,
    ) -> RemovecategoryRequest: ...
    def moveObjects_request(
        self,
        objectIds: TextListBuilder | TextListReader | Sequence[Any] | None = None,
        toCatId: str | None = None,
    ) -> MoveobjectsRequest: ...
    def removeObjects_request(
        self,
        objectIds: TextListBuilder | TextListReader | Sequence[Any] | None = None,
    ) -> RemoveobjectsRequest: ...
    def registry_request(self) -> RegistryRequest: ...

Admin: _AdminInterfaceModule

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
        ) -> CrossDomainRestoreBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[CrossDomainRestoreReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[CrossDomainRestoreReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[CrossDomainRestoreBuilder]: ...
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
        ) -> CrossDomainRestoreReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> CrossDomainRestoreReader: ...

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
            xDomain: CrossDomainRestoreBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> RegParamsBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[RegParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[RegParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[RegParamsBuilder]: ...
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
        ) -> RegParamsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> RegParamsReader: ...

    RegParams: _RegParamsStructModule
    class _UnregisterInterfaceModule(_InterfaceModule):
        @override
        def _new_client(self, server: _DynamicCapabilityServer) -> UnregisterClient: ...
        class Server(_DynamicCapabilityServer):
            def unregister(
                self,
                _context: UnregisterCallContext,
                **kwargs: object,
            ) -> Awaitable[bool | UnregisterResultTuple | None]: ...
            def unregister_context(
                self,
                context: UnregisterCallContext,
            ) -> Awaitable[None]: ...

    Unregister: _UnregisterInterfaceModule
    type UnregisterServer = _RegistrarInterfaceModule._UnregisterInterfaceModule.Server
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> RegistrarClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def register(
            self,
            cap: IdentifiableClient,
            regName: str,
            categoryId: str,
            xDomain: CrossDomainRestoreReader,
            _context: RegisterCallContext,
            **kwargs: object,
        ) -> Awaitable[RegisterResultTuple | None]: ...
        def register_context(self, context: RegisterCallContext) -> Awaitable[None]: ...

class CrossDomainRestoreReader(_DynamicStructReader):
    @property
    def vatId(self) -> VatIdReader: ...
    @property
    def restorer(self) -> RestorerClient: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> CrossDomainRestoreBuilder: ...

class CrossDomainRestoreBuilder(_DynamicStructBuilder):
    @property
    def vatId(self) -> VatIdBuilder: ...
    @vatId.setter
    def vatId(self, value: VatIdBuilder | VatIdReader | dict[str, Any]) -> None: ...
    @property
    def restorer(self) -> RestorerClient: ...
    @restorer.setter
    def restorer(
        self,
        value: RestorerClient | _RestorerInterfaceModule.Server,
    ) -> None: ...
    @override
    def init(
        self,
        field: Literal["vatId"],
        size: int | None = None,
    ) -> VatIdBuilder: ...
    @override
    def as_reader(self) -> CrossDomainRestoreReader: ...

class RegParamsReader(_DynamicStructReader):
    @property
    def cap(self) -> IdentifiableClient: ...
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> RegParamsBuilder: ...

class RegParamsBuilder(_DynamicStructBuilder):
    @property
    def cap(self) -> IdentifiableClient: ...
    @cap.setter
    def cap(
        self,
        value: IdentifiableClient | _IdentifiableInterfaceModule.Server,
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
        value: CrossDomainRestoreBuilder | CrossDomainRestoreReader | dict[str, Any],
    ) -> None: ...
    @override
    def init(
        self,
        field: Literal["xDomain"],
        size: int | None = None,
    ) -> CrossDomainRestoreBuilder: ...
    @override
    def as_reader(self) -> RegParamsReader: ...

class UnregisterRequest(Protocol):
    def send(self) -> UnregisterResult: ...

class UnregisterResult(Awaitable[UnregisterResult], Protocol):
    success: bool

class UnregisterServerResult(_DynamicStructBuilder):
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class UnregisterParams(Protocol): ...

class UnregisterCallContext(Protocol):
    params: UnregisterParams
    @property
    def results(self) -> UnregisterServerResult: ...

class UnregisterResultTuple(NamedTuple):
    success: bool

class UnregisterClient(_DynamicCapabilityClient):
    def unregister(self) -> UnregisterResult: ...
    def unregister_request(self) -> UnregisterRequest: ...

class RegisterRequest(Protocol):
    cap: IdentifiableClient | _IdentifiableInterfaceModule.Server
    regName: str
    categoryId: str
    xDomain: CrossDomainRestoreBuilder
    @overload
    def init(self, name: Literal["xDomain"]) -> CrossDomainRestoreBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> RegisterResult: ...

class RegisterResult(Awaitable[RegisterResult], Protocol):
    unreg: UnregisterClient
    reregSR: SturdyRefReader

class RegisterServerResult(_DynamicStructBuilder):
    @property
    def unreg(
        self,
    ) -> (
        _RegistrarInterfaceModule._UnregisterInterfaceModule.Server | UnregisterClient
    ): ...
    @unreg.setter
    def unreg(
        self,
        value: _RegistrarInterfaceModule._UnregisterInterfaceModule.Server
        | UnregisterClient,
    ) -> None: ...
    @property
    def reregSR(self) -> SturdyRefBuilder: ...
    @reregSR.setter
    def reregSR(
        self,
        value: SturdyRefBuilder | SturdyRefReader | dict[str, Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["reregSR"],
        size: int | None = None,
    ) -> SturdyRefBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class RegisterCallContext(Protocol):
    params: RegParamsReader
    @property
    def results(self) -> RegisterServerResult: ...

class RegisterResultTuple(NamedTuple):
    unreg: (
        _RegistrarInterfaceModule._UnregisterInterfaceModule.Server | UnregisterClient
    )
    reregSR: SturdyRefBuilder | SturdyRefReader | dict[str, Any]

class RegistrarClient(IdentifiableClient):
    def register(
        self,
        cap: IdentifiableClient | _IdentifiableInterfaceModule.Server | None = None,
        regName: str | None = None,
        categoryId: str | None = None,
        xDomain: CrossDomainRestoreBuilder
        | CrossDomainRestoreReader
        | dict[str, Any]
        | None = None,
    ) -> RegisterResult: ...
    def register_request(
        self,
        cap: IdentifiableClient | _IdentifiableInterfaceModule.Server | None = None,
        regName: str | None = None,
        categoryId: str | None = None,
        xDomain: CrossDomainRestoreBuilder | None = None,
    ) -> RegisterRequest: ...

Registrar: _RegistrarInterfaceModule

# Top-level type aliases for use in type annotations
AdminServer = _AdminInterfaceModule.Server
type EntryListBuilder = _EntryList.Builder
type EntryListReader = _EntryList.Reader
type IdInformationListBuilder = _IdInformationList.Builder
type IdInformationListReader = _IdInformationList.Reader
type IdentifiableClientListBuilder = _IdentifiableClientList.Builder
type IdentifiableClientListReader = _IdentifiableClientList.Reader
RegistrarServer = _RegistrarInterfaceModule.Server
RegistryServer = _RegistryInterfaceModule.Server
type TextListBuilder = _TextList.Builder
type TextListReader = _TextList.Reader
UnregisterServer = _RegistrarInterfaceModule._UnregisterInterfaceModule.Server
