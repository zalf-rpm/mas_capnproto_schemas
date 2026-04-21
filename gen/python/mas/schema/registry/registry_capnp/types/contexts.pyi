"""Context helper types for `registry.capnp`."""

from typing import Protocol

from mas.schema.common.common_capnp.types.builders import IdInformationBuilder
from mas.schema.common.common_capnp.types.readers import IdInformationReader
from mas.schema.registry.registry_capnp.types import readers as readers
from mas.schema.registry.registry_capnp.types.results import server as results_server

class AddcategoryParams(Protocol):
    category: IdInformationReader
    upsert: bool

class AddcategoryCallContext(Protocol):
    params: AddcategoryParams
    @property
    def results(self) -> results_server.AddcategoryServerResult: ...

class RemovecategoryParams(Protocol):
    categoryId: str
    moveObjectsToCategoryId: str

class RemovecategoryCallContext(Protocol):
    params: RemovecategoryParams
    @property
    def results(self) -> results_server.RemovecategoryServerResult: ...

class MoveobjectsParams(Protocol):
    objectIds: readers.TextListReader
    toCatId: str

class MoveobjectsCallContext(Protocol):
    params: MoveobjectsParams
    @property
    def results(self) -> results_server.MoveobjectsServerResult: ...

class RemoveobjectsParams(Protocol):
    objectIds: readers.TextListReader

class RemoveobjectsCallContext(Protocol):
    params: RemoveobjectsParams
    @property
    def results(self) -> results_server.RemoveobjectsServerResult: ...

class SupportedcategoriesParams(Protocol): ...

class SupportedcategoriesCallContext(Protocol):
    params: SupportedcategoriesParams
    @property
    def results(self) -> results_server.SupportedcategoriesServerResult: ...

class CategoryinfoParams(Protocol):
    categoryId: str

class CategoryinfoCallContext(Protocol):
    params: CategoryinfoParams
    @property
    def results(self) -> IdInformationBuilder: ...

class EntriesParams(Protocol):
    categoryId: str

class EntriesCallContext(Protocol):
    params: EntriesParams
    @property
    def results(self) -> results_server.EntriesServerResult: ...

class RegistryParams(Protocol): ...

class RegistryCallContext(Protocol):
    params: RegistryParams
    @property
    def results(self) -> results_server.RegistryServerResult: ...

class UnregisterParams(Protocol): ...

class UnregisterCallContext(Protocol):
    params: UnregisterParams
    @property
    def results(self) -> results_server.UnregisterServerResult: ...

class RegisterCallContext(Protocol):
    params: readers.RegParamsReader
    @property
    def results(self) -> results_server.RegisterServerResult: ...
