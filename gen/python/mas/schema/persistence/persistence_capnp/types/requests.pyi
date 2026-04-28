"""Request helper types for `persistence.capnp`."""

from typing import Any, Literal, Protocol, overload

from capnp.lib.capnp import (
    _DynamicObjectBuilder,
)

from mas.schema.persistence.persistence_capnp.types import builders as builders
from mas.schema.persistence.persistence_capnp.types import common as common
from mas.schema.persistence.persistence_capnp.types.results import (
    client as results_client,
)

class BeatRequest(Protocol):
    def send(self) -> results_client.BeatResult: ...

class ReleaseRequest(Protocol):
    def send(self) -> results_client.ReleaseResult: ...

class SaveRequest(Protocol):
    sealFor: builders.OwnerBuilder
    @overload
    def init(self, name: Literal["sealFor"]) -> builders.OwnerBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.SaveResult: ...

class RestoreRequest(Protocol):
    localRef: builders.TokenBuilder
    sealedBy: builders.OwnerBuilder
    @overload
    def init(self, name: Literal["localRef"]) -> builders.TokenBuilder: ...
    @overload
    def init(self, name: Literal["sealedBy"]) -> builders.OwnerBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.RestoreResult: ...

class RegistrarRegisterRequest(Protocol):
    base64VatId: str
    host: str
    port: int
    alias: str
    identityProof: bytes
    def send(self) -> results_client.RegistrarRegisterResult: ...

class ResolveRequest(Protocol):
    id: str
    def send(self) -> results_client.ResolveResult: ...

class GatewayRegisterRequest(Protocol):
    @property
    def cap(self) -> _DynamicObjectBuilder: ...
    @cap.setter
    def cap(self, value: common.Capability) -> None: ...
    secretSeed: str
    def send(self) -> results_client.GatewayRegisterResult: ...

class SturdyrefatgatewayRequest(Protocol):
    gatewaySR: builders.SturdyRefBuilder
    gatewayId: str
    @overload
    def init(self, name: Literal["gatewaySR"]) -> builders.SturdyRefBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.SturdyrefatgatewayResult: ...
