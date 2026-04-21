"""Request helper types for `jobs.capnp`."""

from typing import Protocol

from mas.schema.jobs.jobs_capnp.types.results import client as results_client

class NextjobRequest(Protocol):
    def send(self) -> results_client.NextjobResult: ...
