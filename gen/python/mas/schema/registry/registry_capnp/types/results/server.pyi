"""Server result helper types for `registry.capnp`."""

from collections.abc import Sequence
from typing import Any, Literal, overload

from capnp.lib.capnp import (
    _DynamicStructBuilder,
)

from mas.schema.persistence.persistence_capnp.types.builders import (
    SturdyRefBuilder,
)
from mas.schema.persistence.persistence_capnp.types.readers import SturdyRefReader
from mas.schema.registry.registry_capnp.types import builders as builders
from mas.schema.registry.registry_capnp.types import clients as clients
from mas.schema.registry.registry_capnp.types import modules as modules
from mas.schema.registry.registry_capnp.types import readers as readers

class AddcategoryServerResult(_DynamicStructBuilder):
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class RemovecategoryServerResult(_DynamicStructBuilder):
    @property
    def removedObjects(self) -> builders.IdentifiableClientListBuilder: ...
    @removedObjects.setter
    def removedObjects(
        self,
        value: builders.IdentifiableClientListBuilder
        | readers.IdentifiableClientListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["removedObjects"],
        size: int | None = None,
    ) -> builders.IdentifiableClientListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class MoveobjectsServerResult(_DynamicStructBuilder):
    @property
    def movedObjectIds(self) -> builders.TextListBuilder: ...
    @movedObjectIds.setter
    def movedObjectIds(
        self,
        value: builders.TextListBuilder | readers.TextListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["movedObjectIds"],
        size: int | None = None,
    ) -> builders.TextListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class RemoveobjectsServerResult(_DynamicStructBuilder):
    @property
    def removedObjects(self) -> builders.IdentifiableClientListBuilder: ...
    @removedObjects.setter
    def removedObjects(
        self,
        value: builders.IdentifiableClientListBuilder
        | readers.IdentifiableClientListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["removedObjects"],
        size: int | None = None,
    ) -> builders.IdentifiableClientListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class SupportedcategoriesServerResult(_DynamicStructBuilder):
    @property
    def cats(self) -> builders.IdInformationListBuilder: ...
    @cats.setter
    def cats(
        self,
        value: builders.IdInformationListBuilder
        | readers.IdInformationListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["cats"],
        size: int | None = None,
    ) -> builders.IdInformationListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class EntriesServerResult(_DynamicStructBuilder):
    @property
    def entries(self) -> builders.EntryListBuilder: ...
    @entries.setter
    def entries(
        self,
        value: builders.EntryListBuilder | readers.EntryListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["entries"],
        size: int | None = None,
    ) -> builders.EntryListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class RegistryServerResult(_DynamicStructBuilder):
    @property
    def registry(
        self,
    ) -> modules._RegistryInterfaceModule.Server | clients.RegistryClient: ...
    @registry.setter
    def registry(
        self,
        value: modules._RegistryInterfaceModule.Server | clients.RegistryClient,
    ) -> None: ...

class UnregisterServerResult(_DynamicStructBuilder):
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class RegisterServerResult(_DynamicStructBuilder):
    @property
    def unreg(
        self,
    ) -> (
        modules._RegistrarInterfaceModule._UnregisterInterfaceModule.Server
        | clients.UnregisterClient
    ): ...
    @unreg.setter
    def unreg(
        self,
        value: modules._RegistrarInterfaceModule._UnregisterInterfaceModule.Server
        | clients.UnregisterClient,
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
