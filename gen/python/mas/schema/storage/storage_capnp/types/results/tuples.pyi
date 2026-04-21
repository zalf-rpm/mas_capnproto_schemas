"""Result tuple helper types for `storage.capnp`."""

from collections.abc import Sequence
from typing import Any, NamedTuple

from mas.schema.storage.storage_capnp.types import builders as builders
from mas.schema.storage.storage_capnp.types import clients as clients
from mas.schema.storage.storage_capnp.types import modules as modules
from mas.schema.storage.storage_capnp.types import readers as readers

class GetkeyResultTuple(NamedTuple):
    key: str

class GetvalueResultTuple(NamedTuple):
    value: builders.ValueBuilder | readers.ValueReader | dict[str, Any]
    isUnset: bool

class SetvalueResultTuple(NamedTuple):
    success: bool

class ExportResultTuple(NamedTuple):
    json: str

class DownloadentriesResultTuple(NamedTuple):
    entries: builders.PairListBuilder | readers.PairListReader | Sequence[Any]

class ListentriesResultTuple(NamedTuple):
    entries: (
        builders.KeyAndEntryListBuilder | readers.KeyAndEntryListReader | Sequence[Any]
    )

class GetentryResultTuple(NamedTuple):
    entry: (
        modules._StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule.Server
        | clients.EntryClient
    )

class RemoveentryResultTuple(NamedTuple):
    success: bool

class ClearResultTuple(NamedTuple):
    success: bool

class AddentryResultTuple(NamedTuple):
    entry: (
        modules._StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule.Server
        | clients.EntryClient
    )
    success: bool

class NewcontainerResultTuple(NamedTuple):
    container: (
        modules._StoreInterfaceModule._ContainerInterfaceModule.Server
        | clients.ContainerClient
    )

class ContainerwithidResultTuple(NamedTuple):
    container: (
        modules._StoreInterfaceModule._ContainerInterfaceModule.Server
        | clients.ContainerClient
    )

class ListcontainersResultTuple(NamedTuple):
    containers: (
        builders.InfoAndContainerListBuilder
        | readers.InfoAndContainerListReader
        | Sequence[Any]
    )

class RemovecontainerResultTuple(NamedTuple):
    success: bool

class ImportcontainerResultTuple(NamedTuple):
    container: (
        modules._StoreInterfaceModule._ContainerInterfaceModule.Server
        | clients.ContainerClient
    )
