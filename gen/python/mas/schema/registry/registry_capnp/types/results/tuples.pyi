"""Result tuple helper types for `registry.capnp`."""

from collections.abc import Sequence
from typing import Any, NamedTuple

from mas.schema.persistence.persistence_capnp.types.builders import SturdyRefBuilder
from mas.schema.persistence.persistence_capnp.types.readers import SturdyRefReader
from mas.schema.registry.registry_capnp.types import builders as builders
from mas.schema.registry.registry_capnp.types import clients as clients
from mas.schema.registry.registry_capnp.types import modules as modules
from mas.schema.registry.registry_capnp.types import readers as readers

class AddcategoryResultTuple(NamedTuple):
    success: bool

class RemovecategoryResultTuple(NamedTuple):
    removedObjects: (
        builders.IdentifiableClientListBuilder
        | readers.IdentifiableClientListReader
        | Sequence[Any]
    )

class MoveobjectsResultTuple(NamedTuple):
    movedObjectIds: builders.TextListBuilder | readers.TextListReader | Sequence[Any]

class RemoveobjectsResultTuple(NamedTuple):
    removedObjects: (
        builders.IdentifiableClientListBuilder
        | readers.IdentifiableClientListReader
        | Sequence[Any]
    )

class SupportedcategoriesResultTuple(NamedTuple):
    cats: (
        builders.IdInformationListBuilder
        | readers.IdInformationListReader
        | Sequence[Any]
    )

class CategoryinfoResultTuple(NamedTuple):
    id: str
    name: str
    description: str

class EntriesResultTuple(NamedTuple):
    entries: builders.EntryListBuilder | readers.EntryListReader | Sequence[Any]

class RegistryResultTuple(NamedTuple):
    registry: modules._RegistryInterfaceModule.Server | clients.RegistryClient

class UnregisterResultTuple(NamedTuple):
    success: bool

class RegisterResultTuple(NamedTuple):
    unreg: (
        modules._RegistrarInterfaceModule._UnregisterInterfaceModule.Server
        | clients.UnregisterClient
    )
    reregSR: SturdyRefBuilder | SturdyRefReader | dict[str, Any]
