"""Client helper types for `persistence.capnp`."""

from typing import Any

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
)

from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.persistence.persistence_capnp.types import builders as builders
from mas.schema.persistence.persistence_capnp.types import common as common
from mas.schema.persistence.persistence_capnp.types import readers as readers
from mas.schema.persistence.persistence_capnp.types import requests as requests
from mas.schema.persistence.persistence_capnp.types.results import (
    client as results_client,
)

class HeartbeatClient(_DynamicCapabilityClient):
    def beat(self) -> results_client.BeatResult: ...
    def beat_request(self) -> requests.BeatRequest: ...

class ReleaseSturdyRefClient(_DynamicCapabilityClient):
    def release(self) -> results_client.ReleaseResult: ...
    def release_request(self) -> requests.ReleaseRequest: ...

class PersistentClient(_DynamicCapabilityClient):
    def save(
        self,
        sealFor: builders.OwnerBuilder
        | readers.OwnerReader
        | dict[str, Any]
        | None = None,
    ) -> results_client.SaveResult: ...
    def save_request(
        self,
        sealFor: builders.OwnerBuilder | None = None,
    ) -> requests.SaveRequest: ...

class RestorerClient(_DynamicCapabilityClient):
    def restore(
        self,
        localRef: builders.TokenBuilder
        | readers.TokenReader
        | dict[str, Any]
        | None = None,
        sealedBy: builders.OwnerBuilder
        | readers.OwnerReader
        | dict[str, Any]
        | None = None,
    ) -> results_client.RestoreResult: ...
    def restore_request(
        self,
        localRef: builders.TokenBuilder | None = None,
        sealedBy: builders.OwnerBuilder | None = None,
    ) -> requests.RestoreRequest: ...

class RegistrarClient(_DynamicCapabilityClient):
    def register(
        self,
        base64VatId: str | None = None,
        host: str | None = None,
        port: int | None = None,
        alias: str | None = None,
        identityProof: bytes | None = None,
    ) -> results_client.RegistrarRegisterResult: ...
    def register_request(
        self,
        base64VatId: str | None = None,
        host: str | None = None,
        port: int | None = None,
        alias: str | None = None,
        identityProof: bytes | None = None,
    ) -> requests.RegistrarRegisterRequest: ...

class HostPortResolverClient(IdentifiableClient, RestorerClient):
    def resolve(self, id: str | None = None) -> results_client.ResolveResult: ...
    def resolve_request(self, id: str | None = None) -> requests.ResolveRequest: ...

class GatewayClient(IdentifiableClient, RestorerClient):
    def register(
        self,
        cap: common.AnyPointer | None = None,
        secretSeed: str | None = None,
    ) -> results_client.GatewayRegisterResult: ...
    def register_request(
        self,
        cap: common.AnyPointer | None = None,
        secretSeed: str | None = None,
    ) -> requests.GatewayRegisterRequest: ...

class GatewayRegistrableClient(_DynamicCapabilityClient):
    def sturdyRefAtGateway(
        self,
        gatewaySR: builders.SturdyRefBuilder
        | readers.SturdyRefReader
        | dict[str, Any]
        | None = None,
        gatewayId: str | None = None,
    ) -> results_client.SturdyrefatgatewayResult: ...
    def sturdyRefAtGateway_request(
        self,
        gatewaySR: builders.SturdyRefBuilder | None = None,
        gatewayId: str | None = None,
    ) -> requests.SturdyrefatgatewayRequest: ...
