"""Client helper types for `jobs.capnp`."""

from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.jobs.jobs_capnp.types import requests as requests
from mas.schema.jobs.jobs_capnp.types.results import client as results_client
from mas.schema.persistence.persistence_capnp.types.clients import PersistentClient

class ServiceClient(IdentifiableClient, PersistentClient):
    def nextJob(self) -> results_client.NextjobResult: ...
    def nextJob_request(self) -> requests.NextjobRequest: ...
