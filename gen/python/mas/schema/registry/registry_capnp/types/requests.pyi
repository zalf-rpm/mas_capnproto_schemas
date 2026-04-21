"""Request helper types for `registry.capnp`."""

from collections.abc import Sequence
from typing import Any, Literal, Protocol, overload

from mas.schema.common.common_capnp.types.builders import IdInformationBuilder
from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.registry.registry_capnp.types import builders as builders
from mas.schema.registry.registry_capnp.types import readers as readers
from mas.schema.registry.registry_capnp.types.results import client as results_client

class AddcategoryRequest(Protocol):
    category: IdInformationBuilder
    upsert: bool
    @overload
    def init(self, name: Literal["category"]) -> IdInformationBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.AddcategoryResult: ...

class RemovecategoryRequest(Protocol):
    categoryId: str
    moveObjectsToCategoryId: str
    def send(self) -> results_client.RemovecategoryResult: ...

class MoveobjectsRequest(Protocol):
    objectIds: builders.TextListBuilder | readers.TextListReader | Sequence[Any]
    toCatId: str
    @overload
    def init(
        self,
        name: Literal["objectIds"],
        size: int = ...,
    ) -> builders.TextListBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.MoveobjectsResult: ...

class RemoveobjectsRequest(Protocol):
    objectIds: builders.TextListBuilder | readers.TextListReader | Sequence[Any]
    @overload
    def init(
        self,
        name: Literal["objectIds"],
        size: int = ...,
    ) -> builders.TextListBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.RemoveobjectsResult: ...

class RegistryRequest(Protocol):
    def send(self) -> results_client.RegistryResult: ...

class SupportedcategoriesRequest(Protocol):
    def send(self) -> results_client.SupportedcategoriesResult: ...

class CategoryinfoRequest(Protocol):
    categoryId: str
    def send(self) -> results_client.CategoryinfoResult: ...

class EntriesRequest(Protocol):
    categoryId: str
    def send(self) -> results_client.EntriesResult: ...

class UnregisterRequest(Protocol):
    def send(self) -> results_client.UnregisterResult: ...

class RegisterRequest(Protocol):
    cap: IdentifiableClient | _IdentifiableInterfaceModule.Server
    regName: str
    categoryId: str
    xDomain: builders.CrossDomainRestoreBuilder
    @overload
    def init(self, name: Literal["xDomain"]) -> builders.CrossDomainRestoreBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.RegisterResult: ...
