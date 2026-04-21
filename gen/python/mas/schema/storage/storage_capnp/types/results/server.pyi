"""Server result helper types for `storage.capnp`."""

from collections.abc import Sequence
from typing import Any, Literal, overload

from capnp.lib.capnp import (
    _DynamicStructBuilder,
)

from mas.schema.storage.storage_capnp.types import builders as builders
from mas.schema.storage.storage_capnp.types import clients as clients
from mas.schema.storage.storage_capnp.types import modules as modules
from mas.schema.storage.storage_capnp.types import readers as readers

class GetkeyServerResult(_DynamicStructBuilder):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str) -> None: ...

class GetvalueServerResult(_DynamicStructBuilder):
    @property
    def value(self) -> builders.ValueBuilder: ...
    @value.setter
    def value(
        self,
        value: builders.ValueBuilder | readers.ValueReader | dict[str, Any],
    ) -> None: ...
    @property
    def isUnset(self) -> bool: ...
    @isUnset.setter
    def isUnset(self, value: bool) -> None: ...
    @overload
    def init(
        self,
        field: Literal["value"],
        size: int | None = None,
    ) -> builders.ValueBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class SetvalueServerResult(_DynamicStructBuilder):
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class ExportServerResult(_DynamicStructBuilder):
    @property
    def json(self) -> str: ...
    @json.setter
    def json(self, value: str) -> None: ...

class DownloadentriesServerResult(_DynamicStructBuilder):
    @property
    def entries(self) -> builders.PairListBuilder: ...
    @entries.setter
    def entries(
        self,
        value: builders.PairListBuilder | readers.PairListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["entries"],
        size: int | None = None,
    ) -> builders.PairListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class ListentriesServerResult(_DynamicStructBuilder):
    @property
    def entries(self) -> builders.KeyAndEntryListBuilder: ...
    @entries.setter
    def entries(
        self,
        value: builders.KeyAndEntryListBuilder
        | readers.KeyAndEntryListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["entries"],
        size: int | None = None,
    ) -> builders.KeyAndEntryListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class GetentryServerResult(_DynamicStructBuilder):
    @property
    def entry(
        self,
    ) -> (
        modules._StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule.Server
        | clients.EntryClient
    ): ...
    @entry.setter
    def entry(
        self,
        value: modules._StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule.Server
        | clients.EntryClient,
    ) -> None: ...

class RemoveentryServerResult(_DynamicStructBuilder):
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class ClearServerResult(_DynamicStructBuilder):
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class AddentryServerResult(_DynamicStructBuilder):
    @property
    def entry(
        self,
    ) -> (
        modules._StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule.Server
        | clients.EntryClient
    ): ...
    @entry.setter
    def entry(
        self,
        value: modules._StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule.Server
        | clients.EntryClient,
    ) -> None: ...
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class NewcontainerServerResult(_DynamicStructBuilder):
    @property
    def container(
        self,
    ) -> (
        modules._StoreInterfaceModule._ContainerInterfaceModule.Server
        | clients.ContainerClient
    ): ...
    @container.setter
    def container(
        self,
        value: modules._StoreInterfaceModule._ContainerInterfaceModule.Server
        | clients.ContainerClient,
    ) -> None: ...

class ContainerwithidServerResult(_DynamicStructBuilder):
    @property
    def container(
        self,
    ) -> (
        modules._StoreInterfaceModule._ContainerInterfaceModule.Server
        | clients.ContainerClient
    ): ...
    @container.setter
    def container(
        self,
        value: modules._StoreInterfaceModule._ContainerInterfaceModule.Server
        | clients.ContainerClient,
    ) -> None: ...

class ListcontainersServerResult(_DynamicStructBuilder):
    @property
    def containers(self) -> builders.InfoAndContainerListBuilder: ...
    @containers.setter
    def containers(
        self,
        value: builders.InfoAndContainerListBuilder
        | readers.InfoAndContainerListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["containers"],
        size: int | None = None,
    ) -> builders.InfoAndContainerListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class RemovecontainerServerResult(_DynamicStructBuilder):
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class ImportcontainerServerResult(_DynamicStructBuilder):
    @property
    def container(
        self,
    ) -> (
        modules._StoreInterfaceModule._ContainerInterfaceModule.Server
        | clients.ContainerClient
    ): ...
    @container.setter
    def container(
        self,
        value: modules._StoreInterfaceModule._ContainerInterfaceModule.Server
        | clients.ContainerClient,
    ) -> None: ...
