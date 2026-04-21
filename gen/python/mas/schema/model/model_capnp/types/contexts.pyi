"""Context helper types for `model.capnp`."""

from typing import Protocol

from mas.schema.climate.climate_capnp.types.clients import TimeSeriesClient
from mas.schema.common.common_capnp.types.builders import IdInformationBuilder
from mas.schema.model.model_capnp.types import clients as clients
from mas.schema.model.model_capnp.types import readers as readers
from mas.schema.model.model_capnp.types.results import server as results_server

class ClimateInstanceRunParams(Protocol):
    timeSeries: TimeSeriesClient

class ClimateInstanceRunCallContext(Protocol):
    params: ClimateInstanceRunParams
    @property
    def results(self) -> results_server.ClimateInstanceRunServerResult: ...

class RunsetParams(Protocol):
    dataset: readers.TimeSeriesClientListReader

class RunsetCallContext(Protocol):
    params: RunsetParams
    @property
    def results(self) -> results_server.RunsetServerResult: ...

class EnvInstanceRunParams(Protocol):
    env: readers.EnvReader

class EnvInstanceRunCallContext(Protocol):
    params: EnvInstanceRunParams
    @property
    def results(self) -> results_server.EnvInstanceRunServerResult: ...

class UnregisterParams(Protocol): ...

class UnregisterCallContext(Protocol):
    params: UnregisterParams
    @property
    def results(self) -> results_server.UnregisterServerResult: ...

class RegisterenvinstanceParams(Protocol):
    instance: clients.EnvInstanceClient

class RegisterenvinstanceCallContext(Protocol):
    params: RegisterenvinstanceParams
    @property
    def results(self) -> results_server.RegisterenvinstanceServerResult: ...

class ModelinfoParams(Protocol): ...

class ModelinfoCallContext(Protocol):
    params: ModelinfoParams
    @property
    def results(self) -> IdInformationBuilder: ...

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
