"""Context helper types for `cluster_admin_service.capnp`."""

from typing import Protocol

from mas.schema.cluster.cluster_admin_service_capnp.types import clients as clients
from mas.schema.cluster.cluster_admin_service_capnp.types import common as common
from mas.schema.cluster.cluster_admin_service_capnp.types.results import (
    server as results_server,
)

class UnregisterParams(Protocol): ...

class UnregisterCallContext(Protocol):
    params: UnregisterParams
    @property
    def results(self) -> results_server.UnregisterServerResult: ...

class ValueParams(Protocol): ...

class ValueCallContext(Protocol):
    params: ValueParams
    @property
    def results(self) -> results_server.ValueServerResult: ...

class ReleaseParams(Protocol): ...

class ReleaseCallContext(Protocol):
    params: ReleaseParams

class NewinstanceParams(Protocol): ...

class NewinstanceCallContext(Protocol):
    params: NewinstanceParams
    @property
    def results(self) -> results_server.NewinstanceServerResult: ...

class NewinstancesParams(Protocol):
    numberOfInstances: int

class NewinstancesCallContext(Protocol):
    params: NewinstancesParams
    @property
    def results(self) -> results_server.NewinstancesServerResult: ...

class NewcloudviazmqpipelineproxiesParams(Protocol):
    numberOfInstances: int

class NewcloudviazmqpipelineproxiesCallContext(Protocol):
    params: NewcloudviazmqpipelineproxiesParams
    @property
    def results(self) -> results_server.NewcloudviazmqpipelineproxiesServerResult: ...

class NewcloudviaproxyParams(Protocol):
    numberOfInstances: int

class NewcloudviaproxyCallContext(Protocol):
    params: NewcloudviaproxyParams
    @property
    def results(self) -> results_server.NewcloudviaproxyServerResult: ...

class ModelidParams(Protocol): ...

class ModelidCallContext(Protocol):
    params: ModelidParams
    @property
    def results(self) -> results_server.ModelidServerResult: ...

class RegistermodelinstanceParams(Protocol):
    instance: common.AnyPointer
    registrationToken: str

class RegistermodelinstanceCallContext(Protocol):
    params: RegistermodelinstanceParams
    @property
    def results(self) -> results_server.RegistermodelinstanceServerResult: ...

class RestoresturdyrefParams(Protocol):
    sturdyRef: str

class RestoresturdyrefCallContext(Protocol):
    params: RestoresturdyrefParams
    @property
    def results(self) -> results_server.RestoresturdyrefServerResult: ...

class AdminMasterRegistermodelinstancefactoryParams(Protocol):
    aModelId: str
    aFactory: clients.ModelInstanceFactoryClient

class AdminMasterRegistermodelinstancefactoryCallContext(Protocol):
    params: AdminMasterRegistermodelinstancefactoryParams
    @property
    def results(
        self,
    ) -> results_server.AdminMasterRegistermodelinstancefactoryServerResult: ...

class AdminMasterAvailablemodelsParams(Protocol): ...

class AdminMasterAvailablemodelsCallContext(Protocol):
    params: AdminMasterAvailablemodelsParams
    @property
    def results(self) -> results_server.AdminMasterAvailablemodelsServerResult: ...

class UserMasterAvailablemodelsParams(Protocol): ...

class UserMasterAvailablemodelsCallContext(Protocol):
    params: UserMasterAvailablemodelsParams
    @property
    def results(self) -> results_server.UserMasterAvailablemodelsServerResult: ...

class RuntimeRegistermodelinstancefactoryParams(Protocol):
    aModelId: str
    aFactory: clients.ModelInstanceFactoryClient

class RuntimeRegistermodelinstancefactoryCallContext(Protocol):
    params: RuntimeRegistermodelinstancefactoryParams
    @property
    def results(
        self,
    ) -> results_server.RuntimeRegistermodelinstancefactoryServerResult: ...

class RuntimeAvailablemodelsParams(Protocol): ...

class RuntimeAvailablemodelsCallContext(Protocol):
    params: RuntimeAvailablemodelsParams
    @property
    def results(self) -> results_server.RuntimeAvailablemodelsServerResult: ...

class NumberofcoresParams(Protocol): ...

class NumberofcoresCallContext(Protocol):
    params: NumberofcoresParams
    @property
    def results(self) -> results_server.NumberofcoresServerResult: ...

class FreenumberofcoresParams(Protocol): ...

class FreenumberofcoresCallContext(Protocol):
    params: FreenumberofcoresParams
    @property
    def results(self) -> results_server.FreenumberofcoresServerResult: ...

class ReservenumberofcoresParams(Protocol):
    reserveCores: int
    aModelId: str

class ReservenumberofcoresCallContext(Protocol):
    params: ReservenumberofcoresParams
    @property
    def results(self) -> results_server.ReservenumberofcoresServerResult: ...
