"""Client helper types for `storage.capnp`."""

from typing import Any

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
)

from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.persistence.persistence_capnp.types.clients import PersistentClient
from mas.schema.storage.storage_capnp.types import builders as builders
from mas.schema.storage.storage_capnp.types import readers as readers
from mas.schema.storage.storage_capnp.types import requests as requests
from mas.schema.storage.storage_capnp.types.results import client as results_client

class EntryClient(_DynamicCapabilityClient):
    def getKey(self) -> results_client.GetkeyResult: ...
    def getValue(self) -> results_client.GetvalueResult: ...
    def setValue(
        self,
        value: builders.ValueBuilder
        | readers.ValueReader
        | dict[str, Any]
        | None = None,
    ) -> results_client.SetvalueResult: ...
    def getKey_request(self) -> requests.GetkeyRequest: ...
    def getValue_request(self) -> requests.GetvalueRequest: ...
    def setValue_request(
        self,
        value: builders.ValueBuilder | None = None,
    ) -> requests.SetvalueRequest: ...

class ContainerClient(IdentifiableClient, PersistentClient):
    def export(self) -> results_client.ExportResult: ...
    def downloadEntries(self) -> results_client.DownloadentriesResult: ...
    def listEntries(self) -> results_client.ListentriesResult: ...
    def getEntry(self, key: str | None = None) -> results_client.GetentryResult: ...
    def removeEntry(
        self,
        key: str | None = None,
    ) -> results_client.RemoveentryResult: ...
    def clear(self) -> results_client.ClearResult: ...
    def addEntry(
        self,
        key: str | None = None,
        value: builders.ValueBuilder
        | readers.ValueReader
        | dict[str, Any]
        | None = None,
        replaceExisting: bool | None = None,
    ) -> results_client.AddentryResult: ...
    def export_request(self) -> requests.ExportRequest: ...
    def downloadEntries_request(self) -> requests.DownloadentriesRequest: ...
    def listEntries_request(self) -> requests.ListentriesRequest: ...
    def getEntry_request(self, key: str | None = None) -> requests.GetentryRequest: ...
    def removeEntry_request(
        self,
        key: str | None = None,
    ) -> requests.RemoveentryRequest: ...
    def clear_request(self) -> requests.ClearRequest: ...
    def addEntry_request(
        self,
        key: str | None = None,
        value: builders.ValueBuilder | None = None,
        replaceExisting: bool | None = None,
    ) -> requests.AddentryRequest: ...

class StoreClient(IdentifiableClient, PersistentClient):
    def newContainer(
        self,
        name: str | None = None,
        description: str | None = None,
    ) -> results_client.NewcontainerResult: ...
    def containerWithId(
        self,
        id: str | None = None,
    ) -> results_client.ContainerwithidResult: ...
    def listContainers(self) -> results_client.ListcontainersResult: ...
    def removeContainer(
        self,
        id: str | None = None,
    ) -> results_client.RemovecontainerResult: ...
    def importContainer(
        self,
        json: str | None = None,
    ) -> results_client.ImportcontainerResult: ...
    def newContainer_request(
        self,
        name: str | None = None,
        description: str | None = None,
    ) -> requests.NewcontainerRequest: ...
    def containerWithId_request(
        self,
        id: str | None = None,
    ) -> requests.ContainerwithidRequest: ...
    def listContainers_request(self) -> requests.ListcontainersRequest: ...
    def removeContainer_request(
        self,
        id: str | None = None,
    ) -> requests.RemovecontainerRequest: ...
    def importContainer_request(
        self,
        json: str | None = None,
    ) -> requests.ImportcontainerRequest: ...
