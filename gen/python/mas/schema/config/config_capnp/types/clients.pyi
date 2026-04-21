"""Client helper types for `config.capnp`."""

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
)

from mas.schema.config.config_capnp.types import requests as requests
from mas.schema.config.config_capnp.types.results import client as results_client

class ServiceClient(_DynamicCapabilityClient):
    def nextConfig(self) -> results_client.NextconfigResult: ...
    def nextConfig_request(self) -> requests.NextconfigRequest: ...
