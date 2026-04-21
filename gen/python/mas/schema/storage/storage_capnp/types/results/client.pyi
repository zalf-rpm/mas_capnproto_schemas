"""Client result helper types for `storage.capnp`."""

from collections.abc import Awaitable
from typing import Protocol

from mas.schema.storage.storage_capnp.types import clients as clients
from mas.schema.storage.storage_capnp.types import readers as readers

class GetkeyResult(Awaitable[GetkeyResult], Protocol):
    key: str

class GetvalueResult(Awaitable[GetvalueResult], Protocol):
    value: readers.ValueReader
    isUnset: bool

class SetvalueResult(Awaitable[SetvalueResult], Protocol):
    success: bool

class ExportResult(Awaitable[ExportResult], Protocol):
    json: str

class DownloadentriesResult(Awaitable[DownloadentriesResult], Protocol):
    entries: readers.PairListReader

class ListentriesResult(Awaitable[ListentriesResult], Protocol):
    entries: readers.KeyAndEntryListReader

class GetentryResult(Awaitable[GetentryResult], Protocol):
    entry: clients.EntryClient

class RemoveentryResult(Awaitable[RemoveentryResult], Protocol):
    success: bool

class ClearResult(Awaitable[ClearResult], Protocol):
    success: bool

class AddentryResult(Awaitable[AddentryResult], Protocol):
    entry: clients.EntryClient
    success: bool

class NewcontainerResult(Awaitable[NewcontainerResult], Protocol):
    container: clients.ContainerClient

class ContainerwithidResult(Awaitable[ContainerwithidResult], Protocol):
    container: clients.ContainerClient

class ListcontainersResult(Awaitable[ListcontainersResult], Protocol):
    containers: readers.InfoAndContainerListReader

class RemovecontainerResult(Awaitable[RemovecontainerResult], Protocol):
    success: bool

class ImportcontainerResult(Awaitable[ImportcontainerResult], Protocol):
    container: clients.ContainerClient
