"""Client helper types for `x.capnp`."""

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
)

from mas.schema.test.x_capnp.types import requests as requests
from mas.schema.test.x_capnp.types.results import client as results_client

class XClient(_DynamicCapabilityClient):
    def m(self, i: int | None = None) -> results_client.XMResult: ...
    def m_request(self, i: int | None = None) -> requests.XMRequest: ...

class YClient(_DynamicCapabilityClient):
    def m(self, hello: str | None = None) -> results_client.YMResult: ...
    def m_request(self, hello: str | None = None) -> requests.YMRequest: ...

class ZClient(_DynamicCapabilityClient):
    def m(self, n: int | None = None) -> results_client.ZMResult: ...
    def m_request(self, n: int | None = None) -> requests.ZMRequest: ...
