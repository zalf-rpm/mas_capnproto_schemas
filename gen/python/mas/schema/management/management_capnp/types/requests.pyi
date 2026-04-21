"""Request helper types for `management.capnp`."""

from typing import Protocol

from mas.schema.management.management_capnp.types.results import (
    client as results_client,
)

class NutrientsRequest(Protocol):
    def send(self) -> results_client.NutrientsResult: ...

class ParametersRequest(Protocol):
    def send(self) -> results_client.ParametersResult: ...

class ManagementatRequest(Protocol):
    lat: float
    lon: float
    def send(self) -> results_client.ManagementatResult: ...
