"""Request helper types for `monica_management.capnp`."""

from typing import Protocol

from mas.schema.model.monica.monica_management_capnp.types.results import (
    client as results_client,
)

class ManagementatRequest(Protocol):
    lat: float
    lon: float
    def send(self) -> results_client.ManagementatResult: ...
