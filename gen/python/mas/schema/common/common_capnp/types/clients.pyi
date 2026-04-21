"""Client helper types for `common.capnp`."""

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
)

from mas.schema.common.common_capnp.types import common as common
from mas.schema.common.common_capnp.types import requests as requests
from mas.schema.common.common_capnp.types.results import client as results_client

class IdentifiableClient(_DynamicCapabilityClient):
    def info(self) -> results_client.InfoResult: ...
    def info_request(self) -> requests.InfoRequest: ...

class FactoryClient(IdentifiableClient):
    def create(self) -> results_client.CreateResult: ...
    def create_request(self) -> requests.CreateRequest: ...

class IOFactoryClient(IdentifiableClient):
    def produce(
        self,
        in_: common.AnyPointer | None = None,
    ) -> results_client.ProduceResult: ...
    def produce_request(
        self,
        in_: common.AnyPointer | None = None,
    ) -> requests.ProduceRequest: ...

class HolderClient(_DynamicCapabilityClient):
    def value(self) -> results_client.ValueResult: ...
    def value_request(self) -> requests.ValueRequest: ...

class IdentifiableHolderClient(IdentifiableClient, HolderClient): ...
