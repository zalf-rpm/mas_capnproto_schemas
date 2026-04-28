"""Client helper types for `cluster_admin_service.capnp`."""

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
)

from mas.schema.cluster.cluster_admin_service_capnp.types import common as common
from mas.schema.cluster.cluster_admin_service_capnp.types import modules as modules
from mas.schema.cluster.cluster_admin_service_capnp.types import requests as requests
from mas.schema.cluster.cluster_admin_service_capnp.types.results import (
    client as results_client,
)
from mas.schema.common.common_capnp.types.clients import IdentifiableClient

class UnregisterClient(_DynamicCapabilityClient):
    def unregister(self) -> results_client.UnregisterResult: ...
    def unregister_request(self) -> requests.UnregisterRequest: ...

class ValueHolderClient(_DynamicCapabilityClient):
    def value(self) -> results_client.ValueResult: ...
    def release(self) -> results_client.ReleaseResult: ...
    def value_request(self) -> requests.ValueRequest: ...
    def release_request(self) -> requests.ReleaseRequest: ...

class ModelInstanceFactoryClient(IdentifiableClient):
    def newInstance(self) -> results_client.NewinstanceResult: ...
    def newInstances(
        self,
        numberOfInstances: int | None = None,
    ) -> results_client.NewinstancesResult: ...
    def newCloudViaZmqPipelineProxies(
        self,
        numberOfInstances: int | None = None,
    ) -> results_client.NewcloudviazmqpipelineproxiesResult: ...
    def newCloudViaProxy(
        self,
        numberOfInstances: int | None = None,
    ) -> results_client.NewcloudviaproxyResult: ...
    def modelId(self) -> results_client.ModelidResult: ...
    def registerModelInstance(
        self,
        instance: common.Capability | None = None,
        registrationToken: str | None = None,
    ) -> results_client.RegistermodelinstanceResult: ...
    def restoreSturdyRef(
        self,
        sturdyRef: str | None = None,
    ) -> results_client.RestoresturdyrefResult: ...
    def newInstance_request(self) -> requests.NewinstanceRequest: ...
    def newInstances_request(
        self,
        numberOfInstances: int | None = None,
    ) -> requests.NewinstancesRequest: ...
    def newCloudViaZmqPipelineProxies_request(
        self,
        numberOfInstances: int | None = None,
    ) -> requests.NewcloudviazmqpipelineproxiesRequest: ...
    def newCloudViaProxy_request(
        self,
        numberOfInstances: int | None = None,
    ) -> requests.NewcloudviaproxyRequest: ...
    def modelId_request(self) -> requests.ModelidRequest: ...
    def registerModelInstance_request(
        self,
        instance: common.Capability | None = None,
        registrationToken: str | None = None,
    ) -> requests.RegistermodelinstanceRequest: ...
    def restoreSturdyRef_request(
        self,
        sturdyRef: str | None = None,
    ) -> requests.RestoresturdyrefRequest: ...

class AdminMasterClient(IdentifiableClient):
    def registerModelInstanceFactory(
        self,
        aModelId: str | None = None,
        aFactory: ModelInstanceFactoryClient
        | modules._ClusterStructModule._ModelInstanceFactoryInterfaceModule.Server
        | None = None,
    ) -> results_client.AdminMasterRegistermodelinstancefactoryResult: ...
    def availableModels(self) -> results_client.AdminMasterAvailablemodelsResult: ...
    def registerModelInstanceFactory_request(
        self,
        aModelId: str | None = None,
        aFactory: ModelInstanceFactoryClient
        | modules._ClusterStructModule._ModelInstanceFactoryInterfaceModule.Server
        | None = None,
    ) -> requests.AdminMasterRegistermodelinstancefactoryRequest: ...
    def availableModels_request(self) -> requests.AdminMasterAvailablemodelsRequest: ...

class UserMasterClient(IdentifiableClient):
    def availableModels(self) -> results_client.UserMasterAvailablemodelsResult: ...
    def availableModels_request(self) -> requests.UserMasterAvailablemodelsRequest: ...

class RuntimeClient(IdentifiableClient):
    def registerModelInstanceFactory(
        self,
        aModelId: str | None = None,
        aFactory: ModelInstanceFactoryClient
        | modules._ClusterStructModule._ModelInstanceFactoryInterfaceModule.Server
        | None = None,
    ) -> results_client.RuntimeRegistermodelinstancefactoryResult: ...
    def availableModels(self) -> results_client.RuntimeAvailablemodelsResult: ...
    def numberOfCores(self) -> results_client.NumberofcoresResult: ...
    def freeNumberOfCores(self) -> results_client.FreenumberofcoresResult: ...
    def reserveNumberOfCores(
        self,
        reserveCores: int | None = None,
        aModelId: str | None = None,
    ) -> results_client.ReservenumberofcoresResult: ...
    def registerModelInstanceFactory_request(
        self,
        aModelId: str | None = None,
        aFactory: ModelInstanceFactoryClient
        | modules._ClusterStructModule._ModelInstanceFactoryInterfaceModule.Server
        | None = None,
    ) -> requests.RuntimeRegistermodelinstancefactoryRequest: ...
    def availableModels_request(self) -> requests.RuntimeAvailablemodelsRequest: ...
    def numberOfCores_request(self) -> requests.NumberofcoresRequest: ...
    def freeNumberOfCores_request(self) -> requests.FreenumberofcoresRequest: ...
    def reserveNumberOfCores_request(
        self,
        reserveCores: int | None = None,
        aModelId: str | None = None,
    ) -> requests.ReservenumberofcoresRequest: ...
