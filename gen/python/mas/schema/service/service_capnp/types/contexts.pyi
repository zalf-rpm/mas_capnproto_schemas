"""Context helper types for `service.capnp`."""

from typing import Protocol

from mas.schema.common.common_capnp.types.readers import IdInformationReader
from mas.schema.service.service_capnp.types import builders as builders
from mas.schema.service.service_capnp.types import readers as readers
from mas.schema.service.service_capnp.types.results import server as results_server

class HeartbeatParams(Protocol): ...

class HeartbeatCallContext(Protocol):
    params: HeartbeatParams

class SettimeoutParams(Protocol):
    seconds: int

class SettimeoutCallContext(Protocol):
    params: SettimeoutParams

class AdminStopParams(Protocol): ...

class AdminStopCallContext(Protocol):
    params: AdminStopParams

class IdentitiesParams(Protocol): ...

class IdentitiesCallContext(Protocol):
    params: IdentitiesParams
    @property
    def results(self) -> results_server.IdentitiesServerResult: ...

class UpdateidentityParams(Protocol):
    oldId: str
    newInfo: IdInformationReader

class UpdateidentityCallContext(Protocol):
    params: UpdateidentityParams

class SimpleFactoryCreateParams(Protocol): ...

class SimpleFactoryCreateCallContext(Protocol):
    params: SimpleFactoryCreateParams
    @property
    def results(self) -> results_server.SimpleFactoryCreateServerResult: ...

class FactoryCreateCallContext(Protocol):
    params: readers.CreateParamsReader
    @property
    def results(self) -> builders.AccessInfoBuilder: ...

class ServiceinterfacenamesParams(Protocol): ...

class ServiceinterfacenamesCallContext(Protocol):
    params: ServiceinterfacenamesParams
    @property
    def results(self) -> results_server.ServiceinterfacenamesServerResult: ...

class StoppableStopParams(Protocol): ...

class StoppableStopCallContext(Protocol):
    params: StoppableStopParams
    @property
    def results(self) -> results_server.StoppableStopServerResult: ...
