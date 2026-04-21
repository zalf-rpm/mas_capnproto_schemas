"""Request helper types for `modam.capnp`."""

from typing import Protocol

from mas.schema.dakis.modam.modam_capnp.types.results import client as results_client

class RunaemmodelRequest(Protocol):
    input: str
    def send(self) -> results_client.RunaemmodelResult: ...

class RunfieldmodelRequest(Protocol):
    input: str
    def send(self) -> results_client.RunfieldmodelResult: ...
