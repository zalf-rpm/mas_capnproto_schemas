"""Client helper types for `management.capnp`."""

from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.management.management_capnp.types import requests as requests
from mas.schema.management.management_capnp.types.results import (
    client as results_client,
)
from mas.schema.persistence.persistence_capnp.types.clients import PersistentClient
from mas.schema.registry.registry_capnp.types.clients import RegistryClient

class FertilizerClient(IdentifiableClient, PersistentClient):
    def nutrients(self) -> results_client.NutrientsResult: ...
    def parameters(self) -> results_client.ParametersResult: ...
    def nutrients_request(self) -> requests.NutrientsRequest: ...
    def parameters_request(self) -> requests.ParametersRequest: ...

class FertilizerServiceClient(RegistryClient): ...

class ServiceClient(IdentifiableClient):
    def managementAt(
        self,
        lat: float | None = None,
        lon: float | None = None,
    ) -> results_client.ManagementatResult: ...
    def managementAt_request(
        self,
        lat: float | None = None,
        lon: float | None = None,
    ) -> requests.ManagementatRequest: ...
