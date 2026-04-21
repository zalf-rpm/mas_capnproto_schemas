"""Client helper types for `monica_management.capnp`."""

from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.model.monica.monica_management_capnp.types import requests as requests
from mas.schema.model.monica.monica_management_capnp.types.results import (
    client as results_client,
)

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
