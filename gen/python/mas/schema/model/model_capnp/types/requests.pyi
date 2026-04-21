"""Request helper types for `model.capnp`."""

from collections.abc import Sequence
from typing import Any, Literal, Protocol, overload

from mas.schema.climate.climate_capnp.types.clients import TimeSeriesClient
from mas.schema.climate.climate_capnp.types.modules import _TimeSeriesInterfaceModule
from mas.schema.model.model_capnp.types import builders as builders
from mas.schema.model.model_capnp.types import clients as clients
from mas.schema.model.model_capnp.types import modules as modules
from mas.schema.model.model_capnp.types import readers as readers
from mas.schema.model.model_capnp.types.results import client as results_client

class ClimateInstanceRunRequest(Protocol):
    timeSeries: TimeSeriesClient | _TimeSeriesInterfaceModule.Server
    def send(self) -> results_client.ClimateInstanceRunResult: ...

class RunsetRequest(Protocol):
    dataset: (
        builders.TimeSeriesClientListBuilder
        | readers.TimeSeriesClientListReader
        | Sequence[Any]
    )
    @overload
    def init(
        self,
        name: Literal["dataset"],
        size: int = ...,
    ) -> builders.TimeSeriesClientListBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.RunsetResult: ...

class EnvInstanceRunRequest(Protocol):
    env: builders.EnvBuilder
    @overload
    def init(self, name: Literal["env"]) -> builders.EnvBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.EnvInstanceRunResult: ...

class UnregisterRequest(Protocol):
    def send(self) -> results_client.UnregisterResult: ...

class RegisterenvinstanceRequest(Protocol):
    instance: clients.EnvInstanceClient | modules._EnvInstanceInterfaceModule.Server
    def send(self) -> results_client.RegisterenvinstanceResult: ...

class ModelinfoRequest(Protocol):
    def send(self) -> results_client.ModelinfoResult: ...

class NewinstanceRequest(Protocol):
    def send(self) -> results_client.NewinstanceResult: ...

class NewinstancesRequest(Protocol):
    numberOfInstances: int
    def send(self) -> results_client.NewinstancesResult: ...
