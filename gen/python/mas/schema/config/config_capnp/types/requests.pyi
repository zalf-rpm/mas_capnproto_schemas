"""Request helper types for `config.capnp`."""

from typing import Protocol

from mas.schema.config.config_capnp.types.results import client as results_client

class NextconfigRequest(Protocol):
    def send(self) -> results_client.NextconfigResult: ...
