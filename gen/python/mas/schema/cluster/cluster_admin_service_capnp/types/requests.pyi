"""Request helper types for `cluster_admin_service.capnp`."""

from typing import Protocol

from capnp.lib.capnp import (
    _DynamicObjectBuilder,
)

from mas.schema.cluster.cluster_admin_service_capnp.types import clients as clients
from mas.schema.cluster.cluster_admin_service_capnp.types import common as common
from mas.schema.cluster.cluster_admin_service_capnp.types import modules as modules
from mas.schema.cluster.cluster_admin_service_capnp.types.results import (
    client as results_client,
)

class UnregisterRequest(Protocol):
    def send(self) -> results_client.UnregisterResult: ...

class ValueRequest(Protocol):
    def send(self) -> results_client.ValueResult: ...

class ReleaseRequest(Protocol):
    def send(self) -> results_client.ReleaseResult: ...

class NewinstanceRequest(Protocol):
    def send(self) -> results_client.NewinstanceResult: ...

class NewinstancesRequest(Protocol):
    numberOfInstances: int
    def send(self) -> results_client.NewinstancesResult: ...

class NewcloudviazmqpipelineproxiesRequest(Protocol):
    numberOfInstances: int
    def send(self) -> results_client.NewcloudviazmqpipelineproxiesResult: ...

class NewcloudviaproxyRequest(Protocol):
    numberOfInstances: int
    def send(self) -> results_client.NewcloudviaproxyResult: ...

class ModelidRequest(Protocol):
    def send(self) -> results_client.ModelidResult: ...

class RegistermodelinstanceRequest(Protocol):
    @property
    def instance(self) -> _DynamicObjectBuilder: ...
    @instance.setter
    def instance(self, value: common.Capability) -> None: ...
    registrationToken: str
    def send(self) -> results_client.RegistermodelinstanceResult: ...

class RestoresturdyrefRequest(Protocol):
    sturdyRef: str
    def send(self) -> results_client.RestoresturdyrefResult: ...

class AdminMasterRegistermodelinstancefactoryRequest(Protocol):
    aModelId: str
    aFactory: (
        clients.ModelInstanceFactoryClient
        | modules._ClusterStructModule._ModelInstanceFactoryInterfaceModule.Server
    )
    def send(self) -> results_client.AdminMasterRegistermodelinstancefactoryResult: ...

class AdminMasterAvailablemodelsRequest(Protocol):
    def send(self) -> results_client.AdminMasterAvailablemodelsResult: ...

class UserMasterAvailablemodelsRequest(Protocol):
    def send(self) -> results_client.UserMasterAvailablemodelsResult: ...

class RuntimeRegistermodelinstancefactoryRequest(Protocol):
    aModelId: str
    aFactory: (
        clients.ModelInstanceFactoryClient
        | modules._ClusterStructModule._ModelInstanceFactoryInterfaceModule.Server
    )
    def send(self) -> results_client.RuntimeRegistermodelinstancefactoryResult: ...

class RuntimeAvailablemodelsRequest(Protocol):
    def send(self) -> results_client.RuntimeAvailablemodelsResult: ...

class NumberofcoresRequest(Protocol):
    def send(self) -> results_client.NumberofcoresResult: ...

class FreenumberofcoresRequest(Protocol):
    def send(self) -> results_client.FreenumberofcoresResult: ...

class ReservenumberofcoresRequest(Protocol):
    reserveCores: int
    aModelId: str
    def send(self) -> results_client.ReservenumberofcoresResult: ...
