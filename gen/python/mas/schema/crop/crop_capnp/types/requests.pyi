"""Request helper types for `crop.capnp`."""

from typing import Protocol

from mas.schema.crop.crop_capnp.types.results import client as results_client

class ParametersRequest(Protocol):
    def send(self) -> results_client.ParametersResult: ...

class CultivarRequest(Protocol):
    def send(self) -> results_client.CultivarResult: ...

class SpeciesRequest(Protocol):
    def send(self) -> results_client.SpeciesResult: ...
