"""Client helper types for `registry.capnp`."""

from collections.abc import Sequence
from typing import Any

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
)

from mas.schema.common.common_capnp.types.builders import IdInformationBuilder
from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.common.common_capnp.types.readers import IdInformationReader
from mas.schema.registry.registry_capnp.types import builders as builders
from mas.schema.registry.registry_capnp.types import readers as readers
from mas.schema.registry.registry_capnp.types import requests as requests
from mas.schema.registry.registry_capnp.types.results import client as results_client

class RegistryClient(IdentifiableClient):
    def supportedCategories(self) -> results_client.SupportedcategoriesResult: ...
    def categoryInfo(
        self,
        categoryId: str | None = None,
    ) -> results_client.CategoryinfoResult: ...
    def entries(
        self,
        categoryId: str | None = None,
    ) -> results_client.EntriesResult: ...
    def supportedCategories_request(self) -> requests.SupportedcategoriesRequest: ...
    def categoryInfo_request(
        self,
        categoryId: str | None = None,
    ) -> requests.CategoryinfoRequest: ...
    def entries_request(
        self,
        categoryId: str | None = None,
    ) -> requests.EntriesRequest: ...

class AdminClient(IdentifiableClient):
    def addCategory(
        self,
        category: IdInformationBuilder
        | IdInformationReader
        | dict[str, Any]
        | None = None,
        upsert: bool | None = None,
    ) -> results_client.AddcategoryResult: ...
    def removeCategory(
        self,
        categoryId: str | None = None,
        moveObjectsToCategoryId: str | None = None,
    ) -> results_client.RemovecategoryResult: ...
    def moveObjects(
        self,
        objectIds: builders.TextListBuilder
        | readers.TextListReader
        | Sequence[Any]
        | None = None,
        toCatId: str | None = None,
    ) -> results_client.MoveobjectsResult: ...
    def removeObjects(
        self,
        objectIds: builders.TextListBuilder
        | readers.TextListReader
        | Sequence[Any]
        | None = None,
    ) -> results_client.RemoveobjectsResult: ...
    def registry(self) -> results_client.RegistryResult: ...
    def addCategory_request(
        self,
        category: IdInformationBuilder | None = None,
        upsert: bool | None = None,
    ) -> requests.AddcategoryRequest: ...
    def removeCategory_request(
        self,
        categoryId: str | None = None,
        moveObjectsToCategoryId: str | None = None,
    ) -> requests.RemovecategoryRequest: ...
    def moveObjects_request(
        self,
        objectIds: builders.TextListBuilder
        | readers.TextListReader
        | Sequence[Any]
        | None = None,
        toCatId: str | None = None,
    ) -> requests.MoveobjectsRequest: ...
    def removeObjects_request(
        self,
        objectIds: builders.TextListBuilder
        | readers.TextListReader
        | Sequence[Any]
        | None = None,
    ) -> requests.RemoveobjectsRequest: ...
    def registry_request(self) -> requests.RegistryRequest: ...

class UnregisterClient(_DynamicCapabilityClient):
    def unregister(self) -> results_client.UnregisterResult: ...
    def unregister_request(self) -> requests.UnregisterRequest: ...

class RegistrarClient(IdentifiableClient):
    def register(
        self,
        cap: IdentifiableClient | _IdentifiableInterfaceModule.Server | None = None,
        regName: str | None = None,
        categoryId: str | None = None,
        xDomain: builders.CrossDomainRestoreBuilder
        | readers.CrossDomainRestoreReader
        | dict[str, Any]
        | None = None,
    ) -> results_client.RegisterResult: ...
    def register_request(
        self,
        cap: IdentifiableClient | _IdentifiableInterfaceModule.Server | None = None,
        regName: str | None = None,
        categoryId: str | None = None,
        xDomain: builders.CrossDomainRestoreBuilder | None = None,
    ) -> requests.RegisterRequest: ...
