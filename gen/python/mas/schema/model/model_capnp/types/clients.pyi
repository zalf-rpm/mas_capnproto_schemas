"""Client helper types for `model.capnp`."""

from collections.abc import Sequence
from typing import Any

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
)

from mas.schema.climate.climate_capnp.types.clients import TimeSeriesClient
from mas.schema.climate.climate_capnp.types.modules import _TimeSeriesInterfaceModule
from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.model.model_capnp.types import builders as builders
from mas.schema.model.model_capnp.types import modules as modules
from mas.schema.model.model_capnp.types import readers as readers
from mas.schema.model.model_capnp.types import requests as requests
from mas.schema.model.model_capnp.types.results import client as results_client
from mas.schema.persistence.persistence_capnp.types.clients import PersistentClient
from mas.schema.service.service_capnp.types.clients import StoppableClient

class ClimateInstanceClient(IdentifiableClient):
    def run(
        self,
        timeSeries: TimeSeriesClient | _TimeSeriesInterfaceModule.Server | None = None,
    ) -> results_client.ClimateInstanceRunResult: ...
    def runSet(
        self,
        dataset: builders.TimeSeriesClientListBuilder
        | readers.TimeSeriesClientListReader
        | Sequence[Any]
        | None = None,
    ) -> results_client.RunsetResult: ...
    def run_request(
        self,
        timeSeries: TimeSeriesClient | _TimeSeriesInterfaceModule.Server | None = None,
    ) -> requests.ClimateInstanceRunRequest: ...
    def runSet_request(
        self,
        dataset: builders.TimeSeriesClientListBuilder
        | readers.TimeSeriesClientListReader
        | Sequence[Any]
        | None = None,
    ) -> requests.RunsetRequest: ...

class EnvInstanceClient(IdentifiableClient, PersistentClient, StoppableClient):
    def run(
        self,
        env: builders.EnvBuilder | readers.EnvReader | dict[str, Any] | None = None,
    ) -> results_client.EnvInstanceRunResult: ...
    def run_request(
        self,
        env: builders.EnvBuilder | None = None,
    ) -> requests.EnvInstanceRunRequest: ...

class UnregisterClient(_DynamicCapabilityClient):
    def unregister(self) -> results_client.UnregisterResult: ...
    def unregister_request(self) -> requests.UnregisterRequest: ...

class EnvInstanceProxyClient(EnvInstanceClient):
    def registerEnvInstance(
        self,
        instance: EnvInstanceClient
        | modules._EnvInstanceInterfaceModule.Server
        | None = None,
    ) -> results_client.RegisterenvinstanceResult: ...
    def registerEnvInstance_request(
        self,
        instance: EnvInstanceClient
        | modules._EnvInstanceInterfaceModule.Server
        | None = None,
    ) -> requests.RegisterenvinstanceRequest: ...

class InstanceFactoryClient(IdentifiableClient):
    def modelInfo(self) -> results_client.ModelinfoResult: ...
    def newInstance(self) -> results_client.NewinstanceResult: ...
    def newInstances(
        self,
        numberOfInstances: int | None = None,
    ) -> results_client.NewinstancesResult: ...
    def modelInfo_request(self) -> requests.ModelinfoRequest: ...
    def newInstance_request(self) -> requests.NewinstanceRequest: ...
    def newInstances_request(
        self,
        numberOfInstances: int | None = None,
    ) -> requests.NewinstancesRequest: ...
