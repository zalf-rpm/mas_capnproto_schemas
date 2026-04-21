"""Request helper types for `service.capnp`."""

from collections.abc import Sequence
from typing import Any, Literal, Protocol, overload

from mas.schema.common.common_capnp.types.builders import IdInformationBuilder
from mas.schema.service.service_capnp.types import builders as builders
from mas.schema.service.service_capnp.types import common as common
from mas.schema.service.service_capnp.types import readers as readers
from mas.schema.service.service_capnp.types.results import client as results_client

class HeartbeatRequest(Protocol):
    def send(self) -> results_client.HeartbeatResult: ...

class SettimeoutRequest(Protocol):
    seconds: int
    def send(self) -> results_client.SettimeoutResult: ...

class AdminStopRequest(Protocol):
    def send(self) -> results_client.AdminStopResult: ...

class IdentitiesRequest(Protocol):
    def send(self) -> results_client.IdentitiesResult: ...

class UpdateidentityRequest(Protocol):
    oldId: str
    newInfo: IdInformationBuilder
    @overload
    def init(self, name: Literal["newInfo"]) -> IdInformationBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.UpdateidentityResult: ...

class SimpleFactoryCreateRequest(Protocol):
    def send(self) -> results_client.SimpleFactoryCreateResult: ...

class FactoryCreateRequest(Protocol):
    timeoutSeconds: int
    interfaceNameToRegistrySR: (
        builders.PairListBuilder | readers.PairListReader | Sequence[Any]
    )
    msgPayload: common.AnyPointer
    @overload
    def init(
        self,
        name: Literal["interfaceNameToRegistrySR"],
        size: int = ...,
    ) -> builders.PairListBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.FactoryCreateResult: ...

class ServiceinterfacenamesRequest(Protocol):
    def send(self) -> results_client.ServiceinterfacenamesResult: ...

class StoppableStopRequest(Protocol):
    def send(self) -> results_client.StoppableStopResult: ...
