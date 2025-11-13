"""This is an automatically generated stub for `registry.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator, Sequence
from contextlib import contextmanager
from io import BufferedWriter
from typing import (
    Any,
    BinaryIO,
    Literal,
    NamedTuple,
    Protocol,
    Self,
    TypeAlias,
    overload,
)

from .common_capnp import Identifiable, IdentifiableClient
from .persistence_capnp import Restorer, RestorerClient, VatId

class Admin:
    class AddcategoryRequest(Protocol):
        upsert: bool
        def send(self) -> Admin.AddcategoryResult: ...

    class AddcategoryResult(Awaitable[AddcategoryResult], Protocol):
        success: bool

    class RemovecategoryRequest(Protocol):
        categoryId: str
        moveObjectsToCategoryId: str
        def send(self) -> Admin.RemovecategoryResult: ...

    class RemovecategoryResult(Awaitable[RemovecategoryResult], Protocol):
        removedObjects: Sequence[Identifiable]

    class MoveobjectsRequest(Protocol):
        objectIds: Sequence[str]
        toCatId: str
        @overload
        def init(
            self, name: Literal["objectIds"], size: int = ...
        ) -> Sequence[str]: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> Admin.MoveobjectsResult: ...

    class MoveobjectsResult(Awaitable[MoveobjectsResult], Protocol):
        movedObjectIds: Sequence[str]

    class RemoveobjectsRequest(Protocol):
        objectIds: Sequence[str]
        @overload
        def init(
            self, name: Literal["objectIds"], size: int = ...
        ) -> Sequence[str]: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> Admin.RemoveobjectsResult: ...

    class RemoveobjectsResult(Awaitable[RemoveobjectsResult], Protocol):
        removedObjects: Sequence[Identifiable]

    class RegistryRequest(Protocol):
        def send(self) -> Admin.RegistryResult: ...

    class RegistryResult(Awaitable[RegistryResult], Protocol):
        registry: Any

    @classmethod
    def _new_client(
        cls, server: Admin.Server | Identifiable.Server
    ) -> "AdminClient": ...
    class Server(Identifiable.Server):
        class AddcategoryResultTuple(NamedTuple):
            success: bool

        class RemovecategoryResultTuple(NamedTuple):
            removedObjects: Sequence[Identifiable]

        class MoveobjectsResultTuple(NamedTuple):
            movedObjectIds: Sequence[str]

        class RemoveobjectsResultTuple(NamedTuple):
            removedObjects: Sequence[Identifiable]

        class RegistryResultTuple(NamedTuple):
            pass

        class AddcategoryCallContext(Protocol):
            results: Admin.AddcategoryResult

        class RemovecategoryCallContext(Protocol):
            results: Admin.RemovecategoryResult

        class MoveobjectsCallContext(Protocol):
            results: Admin.MoveobjectsResult

        class RemoveobjectsCallContext(Protocol):
            results: Admin.RemoveobjectsResult

        class RegistryCallContext(Protocol):
            results: Admin.RegistryResult

        def addCategory(
            self,
            upsert: bool,
            _context: Admin.Server.AddcategoryCallContext,
            **kwargs: Any,
        ) -> Awaitable[bool | Admin.Server.AddcategoryResultTuple | None]: ...
        def removeCategory(
            self,
            categoryId: str,
            moveObjectsToCategoryId: str,
            _context: Admin.Server.RemovecategoryCallContext,
            **kwargs: Any,
        ) -> Awaitable[Admin.Server.RemovecategoryResultTuple | None]: ...
        def moveObjects(
            self,
            objectIds: Sequence[str],
            toCatId: str,
            _context: Admin.Server.MoveobjectsCallContext,
            **kwargs: Any,
        ) -> Awaitable[Admin.Server.MoveobjectsResultTuple | None]: ...
        def removeObjects(
            self,
            objectIds: Sequence[str],
            _context: Admin.Server.RemoveobjectsCallContext,
            **kwargs: Any,
        ) -> Awaitable[Admin.Server.RemoveobjectsResultTuple | None]: ...
        def registry(
            self, _context: Admin.Server.RegistryCallContext, **kwargs: Any
        ) -> Awaitable[Admin.Server.RegistryResultTuple | None]: ...
        def __enter__(self) -> Self: ...
        def __exit__(self, *args: Any) -> None: ...

class AdminClient(IdentifiableClient):
    def addCategory(self, upsert: bool | None = None) -> Admin.AddcategoryResult: ...
    def removeCategory(
        self, categoryId: str | None = None, moveObjectsToCategoryId: str | None = None
    ) -> Admin.RemovecategoryResult: ...
    def moveObjects(
        self, objectIds: Sequence[str] | None = None, toCatId: str | None = None
    ) -> Admin.MoveobjectsResult: ...
    def removeObjects(
        self, objectIds: Sequence[str] | None = None
    ) -> Admin.RemoveobjectsResult: ...
    def registry(self) -> Admin.RegistryResult: ...
    def addCategory_request(
        self, upsert: bool | None = None
    ) -> Admin.AddcategoryRequest: ...
    def removeCategory_request(
        self, categoryId: str | None = None, moveObjectsToCategoryId: str | None = None
    ) -> Admin.RemovecategoryRequest: ...
    def moveObjects_request(
        self, objectIds: Sequence[str] | None = None, toCatId: str | None = None
    ) -> Admin.MoveobjectsRequest: ...
    def removeObjects_request(
        self, objectIds: Sequence[str] | None = None
    ) -> Admin.RemoveobjectsRequest: ...
    def registry_request(self) -> Admin.RegistryRequest: ...

class Registry:
    EntryBuilder: TypeAlias = Entry.Builder
    EntryReader: TypeAlias = Entry.Reader
    class Entry:
        class Reader:
            @property
            def categoryId(self) -> str: ...
            @property
            def ref(self) -> IdentifiableClient: ...
            @property
            def name(self) -> str: ...
            @property
            def id(self) -> str: ...
            def as_builder(self) -> Registry.Entry.Builder: ...

        class Builder:
            @property
            def categoryId(self) -> str: ...
            @categoryId.setter
            def categoryId(self, value: str) -> None: ...
            @property
            def ref(self) -> IdentifiableClient: ...
            @ref.setter
            def ref(self, value: IdentifiableClient | Identifiable.Server) -> None: ...
            @property
            def name(self) -> str: ...
            @name.setter
            def name(self, value: str) -> None: ...
            @property
            def id(self) -> str: ...
            @id.setter
            def id(self, value: str) -> None: ...
            @staticmethod
            def from_dict(dictionary: dict[str, Any]) -> Registry.Entry.Builder: ...
            def copy(self) -> Registry.Entry.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Registry.Entry.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Registry.Entry.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Registry.Entry.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            categoryId: str | None = None,
            ref: IdentifiableClient | Identifiable.Server | None = None,
            name: str | None = None,
            id: str | None = None,
        ) -> Registry.Entry.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Registry.Entry.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Registry.Entry.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    class SupportedcategoriesRequest(Protocol):
        def send(self) -> Registry.SupportedcategoriesResult: ...

    class SupportedcategoriesResult(Awaitable[SupportedcategoriesResult], Protocol):
        cats: Any

    class CategoryinfoRequest(Protocol):
        categoryId: str
        def send(self) -> Registry.CategoryinfoResult: ...

    class CategoryinfoResult(Awaitable[CategoryinfoResult], Protocol):
        id: str
        name: str
        description: str

    class EntriesRequest(Protocol):
        categoryId: str
        def send(self) -> Registry.EntriesResult: ...

    class EntriesResult(Awaitable[EntriesResult], Protocol):
        entries: Sequence[Registry.Entry.Builder | Registry.Entry.Reader]

    @classmethod
    def _new_client(
        cls, server: Registry.Server | Identifiable.Server
    ) -> "RegistryClient": ...
    class Server(Identifiable.Server):
        class SupportedcategoriesResultTuple(NamedTuple):
            pass

        class CategoryinfoResultTuple(NamedTuple):
            id: str
            name: str
            description: str

        class EntriesResultTuple(NamedTuple):
            entries: Sequence[Registry.Entry]

        class SupportedcategoriesCallContext(Protocol):
            results: Registry.SupportedcategoriesResult

        class CategoryinfoCallContext(Protocol):
            results: Registry.CategoryinfoResult

        class EntriesCallContext(Protocol):
            results: Registry.EntriesResult

        def supportedCategories(
            self,
            _context: Registry.Server.SupportedcategoriesCallContext,
            **kwargs: Any,
        ) -> Awaitable[Registry.Server.SupportedcategoriesResultTuple | None]: ...
        def categoryInfo(
            self,
            categoryId: str,
            _context: Registry.Server.CategoryinfoCallContext,
            **kwargs: Any,
        ) -> Awaitable[Registry.Server.CategoryinfoResultTuple | None]: ...
        def entries(
            self,
            categoryId: str,
            _context: Registry.Server.EntriesCallContext,
            **kwargs: Any,
        ) -> Awaitable[Registry.Server.EntriesResultTuple | None]: ...
        def __enter__(self) -> Self: ...
        def __exit__(self, *args: Any) -> None: ...

class RegistryClient(IdentifiableClient):
    def supportedCategories(self) -> Registry.SupportedcategoriesResult: ...
    def categoryInfo(
        self, categoryId: str | None = None
    ) -> Registry.CategoryinfoResult: ...
    def entries(self, categoryId: str | None = None) -> Registry.EntriesResult: ...
    def supportedCategories_request(self) -> Registry.SupportedcategoriesRequest: ...
    def categoryInfo_request(
        self, categoryId: str | None = None
    ) -> Registry.CategoryinfoRequest: ...
    def entries_request(
        self, categoryId: str | None = None
    ) -> Registry.EntriesRequest: ...

class Registrar:
    CrossDomainRestoreBuilder: TypeAlias = CrossDomainRestore.Builder
    CrossDomainRestoreReader: TypeAlias = CrossDomainRestore.Reader
    class CrossDomainRestore:
        class Reader:
            @property
            def vatId(self) -> VatId.Reader: ...
            @property
            def restorer(self) -> RestorerClient: ...
            def as_builder(self) -> Registrar.CrossDomainRestore.Builder: ...

        class Builder:
            @property
            def vatId(self) -> VatId.Builder: ...
            @vatId.setter
            def vatId(
                self, value: VatId.Builder | VatId.Reader | dict[str, Any]
            ) -> None: ...
            @property
            def restorer(self) -> RestorerClient: ...
            @restorer.setter
            def restorer(self, value: RestorerClient | Restorer.Server) -> None: ...
            @staticmethod
            def from_dict(
                dictionary: dict[str, Any],
            ) -> Registrar.CrossDomainRestore.Builder: ...
            def init(self, name: Literal["vatId"]) -> VatId.Builder: ...
            def copy(self) -> Registrar.CrossDomainRestore.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Registrar.CrossDomainRestore.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        def init(self, name: Literal["vatId"]) -> VatId: ...
        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Registrar.CrossDomainRestore.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Registrar.CrossDomainRestore.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            vatId: VatId.Builder | dict[str, Any] | None = None,
            restorer: RestorerClient | Restorer.Server | None = None,
        ) -> Registrar.CrossDomainRestore.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Registrar.CrossDomainRestore.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Registrar.CrossDomainRestore.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    RegParamsBuilder: TypeAlias = RegParams.Builder
    RegParamsReader: TypeAlias = RegParams.Reader
    class RegParams:
        class Reader:
            @property
            def cap(self) -> IdentifiableClient: ...
            @property
            def regName(self) -> str: ...
            @property
            def categoryId(self) -> str: ...
            @property
            def xDomain(self) -> Registrar.CrossDomainRestore.Reader: ...
            def as_builder(self) -> Registrar.RegParams.Builder: ...

        class Builder:
            @property
            def cap(self) -> IdentifiableClient: ...
            @cap.setter
            def cap(self, value: IdentifiableClient | Identifiable.Server) -> None: ...
            @property
            def regName(self) -> str: ...
            @regName.setter
            def regName(self, value: str) -> None: ...
            @property
            def categoryId(self) -> str: ...
            @categoryId.setter
            def categoryId(self, value: str) -> None: ...
            @property
            def xDomain(self) -> Registrar.CrossDomainRestore.Builder: ...
            @xDomain.setter
            def xDomain(
                self,
                value: Registrar.CrossDomainRestore.Builder
                | Registrar.CrossDomainRestore.Reader
                | dict[str, Any],
            ) -> None: ...
            @staticmethod
            def from_dict(
                dictionary: dict[str, Any],
            ) -> Registrar.RegParams.Builder: ...
            def init(
                self, name: Literal["xDomain"]
            ) -> Registrar.CrossDomainRestore.Builder: ...
            def copy(self) -> Registrar.RegParams.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Registrar.RegParams.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        def init(self, name: Literal["xDomain"]) -> Registrar.CrossDomainRestore: ...
        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Registrar.RegParams.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Registrar.RegParams.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            cap: IdentifiableClient | Identifiable.Server | None = None,
            regName: str | None = None,
            categoryId: str | None = None,
            xDomain: Registrar.CrossDomainRestore.Builder
            | dict[str, Any]
            | None = None,
        ) -> Registrar.RegParams.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Registrar.RegParams.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Registrar.RegParams.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    class Unregister:
        class UnregisterRequest(Protocol):
            def send(self) -> Registrar.Unregister.UnregisterResult: ...

        class UnregisterResult(Awaitable[UnregisterResult], Protocol):
            success: bool

        @classmethod
        def _new_client(
            cls, server: Registrar.Unregister.Server
        ) -> "Registrar.UnregisterClient": ...
        class Server(Protocol):
            class UnregisterResultTuple(NamedTuple):
                success: bool

            class UnregisterCallContext(Protocol):
                results: Registrar.Unregister.UnregisterResult

            def unregister(
                self,
                _context: Registrar.Unregister.Server.UnregisterCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                bool | Registrar.Unregister.Server.UnregisterResultTuple | None
            ]: ...
            def __enter__(self) -> Self: ...
            def __exit__(self, *args: Any) -> None: ...

    class UnregisterClient(Protocol):
        def unregister(self) -> Registrar.Unregister.UnregisterResult: ...
        def unregister_request(self) -> Registrar.Unregister.UnregisterRequest: ...

    class RegisterRequest(Protocol):
        cap: Identifiable | Identifiable.Server
        regName: str
        categoryId: str
        xDomain: Registrar.CrossDomainRestore.Builder
        @overload
        def init(
            self, name: Literal["xDomain"]
        ) -> Registrar.CrossDomainRestore.Builder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> Registrar.RegisterResult: ...

    class RegisterResult(Awaitable[RegisterResult], Protocol):
        unreg: Registrar.UnregisterClient
        reregSR: Any

    @classmethod
    def _new_client(
        cls, server: Registrar.Server | Identifiable.Server
    ) -> "RegistrarClient": ...
    class Server(Identifiable.Server):
        class RegisterResultTuple(NamedTuple):
            unreg: Registrar.Unregister.Server

        class RegisterCallContext(Protocol):
            results: Registrar.RegisterResult

        def register(
            self,
            cap: Identifiable,
            regName: str,
            categoryId: str,
            xDomain: Registrar.CrossDomainRestore.Reader,
            _context: Registrar.Server.RegisterCallContext,
            **kwargs: Any,
        ) -> Awaitable[Registrar.Server.RegisterResultTuple | None]: ...
        def __enter__(self) -> Self: ...
        def __exit__(self, *args: Any) -> None: ...

class RegistrarClient(IdentifiableClient):
    def register(
        self,
        cap: Identifiable | Identifiable.Server | None = None,
        regName: str | None = None,
        categoryId: str | None = None,
        xDomain: Registrar.CrossDomainRestore | dict[str, Any] | None = None,
    ) -> Registrar.RegisterResult: ...
    def register_request(
        self,
        cap: Identifiable | Identifiable.Server | None = None,
        regName: str | None = None,
        categoryId: str | None = None,
        xDomain: Registrar.CrossDomainRestore.Builder | None = None,
    ) -> Registrar.RegisterRequest: ...
