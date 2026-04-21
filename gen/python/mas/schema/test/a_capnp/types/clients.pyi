"""Client helper types for `a.capnp`."""

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
)

from mas.schema.test.a_capnp.types import requests as requests
from mas.schema.test.a_capnp.types.results import client as results_client

class AClient(_DynamicCapabilityClient):
    def method(self, param: str | None = None) -> results_client.MethodResult: ...
    def method_request(self, param: str | None = None) -> requests.MethodRequest: ...
