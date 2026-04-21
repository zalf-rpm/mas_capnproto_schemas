"""Request helper types for `storage.capnp`."""

from typing import Any, Literal, Protocol, overload

from mas.schema.storage.storage_capnp.types import builders as builders
from mas.schema.storage.storage_capnp.types.results import client as results_client

class GetkeyRequest(Protocol):
    def send(self) -> results_client.GetkeyResult: ...

class GetvalueRequest(Protocol):
    def send(self) -> results_client.GetvalueResult: ...

class SetvalueRequest(Protocol):
    value: builders.ValueBuilder
    @overload
    def init(self, name: Literal["value"]) -> builders.ValueBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.SetvalueResult: ...

class ExportRequest(Protocol):
    def send(self) -> results_client.ExportResult: ...

class DownloadentriesRequest(Protocol):
    def send(self) -> results_client.DownloadentriesResult: ...

class ListentriesRequest(Protocol):
    def send(self) -> results_client.ListentriesResult: ...

class GetentryRequest(Protocol):
    key: str
    def send(self) -> results_client.GetentryResult: ...

class RemoveentryRequest(Protocol):
    key: str
    def send(self) -> results_client.RemoveentryResult: ...

class ClearRequest(Protocol):
    def send(self) -> results_client.ClearResult: ...

class AddentryRequest(Protocol):
    key: str
    value: builders.ValueBuilder
    replaceExisting: bool
    @overload
    def init(self, name: Literal["value"]) -> builders.ValueBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.AddentryResult: ...

class NewcontainerRequest(Protocol):
    name: str
    description: str
    def send(self) -> results_client.NewcontainerResult: ...

class ContainerwithidRequest(Protocol):
    id: str
    def send(self) -> results_client.ContainerwithidResult: ...

class ListcontainersRequest(Protocol):
    def send(self) -> results_client.ListcontainersResult: ...

class RemovecontainerRequest(Protocol):
    id: str
    def send(self) -> results_client.RemovecontainerResult: ...

class ImportcontainerRequest(Protocol):
    json: str
    def send(self) -> results_client.ImportcontainerResult: ...
