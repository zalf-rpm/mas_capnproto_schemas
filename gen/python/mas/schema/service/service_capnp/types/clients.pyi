"""Client helper types for `service.capnp`."""

from collections.abc import Sequence
from typing import Any

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
)

from mas.schema.common.common_capnp.types.builders import IdInformationBuilder
from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.common.common_capnp.types.readers import IdInformationReader
from mas.schema.service.service_capnp.types import builders as builders
from mas.schema.service.service_capnp.types import common as common
from mas.schema.service.service_capnp.types import readers as readers
from mas.schema.service.service_capnp.types import requests as requests
from mas.schema.service.service_capnp.types.results import client as results_client

class AdminClient(IdentifiableClient):
    def heartbeat(self) -> results_client.HeartbeatResult: ...
    def setTimeout(
        self,
        seconds: int | None = None,
    ) -> results_client.SettimeoutResult: ...
    def stop(self) -> results_client.AdminStopResult: ...
    def identities(self) -> results_client.IdentitiesResult: ...
    def updateIdentity(
        self,
        oldId: str | None = None,
        newInfo: IdInformationBuilder
        | IdInformationReader
        | dict[str, Any]
        | None = None,
    ) -> results_client.UpdateidentityResult: ...
    def heartbeat_request(self) -> requests.HeartbeatRequest: ...
    def setTimeout_request(
        self,
        seconds: int | None = None,
    ) -> requests.SettimeoutRequest: ...
    def stop_request(self) -> requests.AdminStopRequest: ...
    def identities_request(self) -> requests.IdentitiesRequest: ...
    def updateIdentity_request(
        self,
        oldId: str | None = None,
        newInfo: IdInformationBuilder | None = None,
    ) -> requests.UpdateidentityRequest: ...

class SimpleFactoryClient(IdentifiableClient):
    def create(self) -> results_client.SimpleFactoryCreateResult: ...
    def create_request(self) -> requests.SimpleFactoryCreateRequest: ...

class FactoryClient(IdentifiableClient):
    def create(
        self,
        timeoutSeconds: int | None = None,
        interfaceNameToRegistrySR: builders.PairListBuilder
        | readers.PairListReader
        | Sequence[Any]
        | None = None,
        msgPayload: common.AnyPointer | None = None,
    ) -> results_client.FactoryCreateResult: ...
    def serviceInterfaceNames(self) -> results_client.ServiceinterfacenamesResult: ...
    def create_request(
        self,
        timeoutSeconds: int | None = None,
        interfaceNameToRegistrySR: builders.PairListBuilder
        | readers.PairListReader
        | Sequence[Any]
        | None = None,
        msgPayload: common.AnyPointer | None = None,
    ) -> requests.FactoryCreateRequest: ...
    def serviceInterfaceNames_request(
        self,
    ) -> requests.ServiceinterfacenamesRequest: ...

class StoppableClient(_DynamicCapabilityClient):
    def stop(self) -> results_client.StoppableStopResult: ...
    def stop_request(self) -> requests.StoppableStopRequest: ...
