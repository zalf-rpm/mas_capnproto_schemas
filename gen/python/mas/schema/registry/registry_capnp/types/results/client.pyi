"""Client result helper types for `registry.capnp`."""

from collections.abc import Awaitable
from typing import Protocol

from mas.schema.persistence.persistence_capnp.types.readers import SturdyRefReader
from mas.schema.registry.registry_capnp.types import clients as clients
from mas.schema.registry.registry_capnp.types import readers as readers

class AddcategoryResult(Awaitable[AddcategoryResult], Protocol):
    success: bool

class RemovecategoryResult(Awaitable[RemovecategoryResult], Protocol):
    removedObjects: readers.IdentifiableClientListReader

class MoveobjectsResult(Awaitable[MoveobjectsResult], Protocol):
    movedObjectIds: readers.TextListReader

class RemoveobjectsResult(Awaitable[RemoveobjectsResult], Protocol):
    removedObjects: readers.IdentifiableClientListReader

class SupportedcategoriesResult(Awaitable[SupportedcategoriesResult], Protocol):
    cats: readers.IdInformationListReader

class CategoryinfoResult(Awaitable[CategoryinfoResult], Protocol):
    id: str
    name: str
    description: str

class EntriesResult(Awaitable[EntriesResult], Protocol):
    entries: readers.EntryListReader

class RegistryResult(Awaitable[RegistryResult], Protocol):
    registry: clients.RegistryClient

class UnregisterResult(Awaitable[UnregisterResult], Protocol):
    success: bool

class RegisterResult(Awaitable[RegisterResult], Protocol):
    unreg: clients.UnregisterClient
    reregSR: SturdyRefReader
