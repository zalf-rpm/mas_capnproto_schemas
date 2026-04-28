"""Builder helper types for `agmip.capnp`."""

from typing import Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicStructBuilder,
)

from mas.schema.climate.climate_capnp.types.clients import TimeSeriesClient
from mas.schema.climate.climate_capnp.types.modules import _TimeSeriesInterfaceModule
from mas.schema.common.common_capnp.types.builders import StructuredTextBuilder
from mas.schema.common.common_capnp.types.readers import StructuredTextReader
from mas.schema.model.agmip.agmip_capnp.types import readers as readers
from mas.schema.soil.soil_capnp.types.clients import ProfileClient
from mas.schema.soil.soil_capnp.types.modules import _ProfileInterfaceModule

class FieldExperimentDataTemplateBuilder(_DynamicStructBuilder):
    @property
    def soilProfile(self) -> ProfileClient: ...
    @soilProfile.setter
    def soilProfile(
        self,
        value: ProfileClient | _ProfileInterfaceModule.Server,
    ) -> None: ...
    @property
    def soil(self) -> StructuredTextBuilder: ...
    @soil.setter
    def soil(
        self,
        value: StructuredTextBuilder | StructuredTextReader | dict[str, Any],
    ) -> None: ...
    @property
    def plot(self) -> StructuredTextBuilder: ...
    @plot.setter
    def plot(
        self,
        value: StructuredTextBuilder | StructuredTextReader | dict[str, Any],
    ) -> None: ...
    @property
    def timeseries(self) -> TimeSeriesClient: ...
    @timeseries.setter
    def timeseries(
        self,
        value: TimeSeriesClient | _TimeSeriesInterfaceModule.Server,
    ) -> None: ...
    @property
    def treatment(self) -> StructuredTextBuilder: ...
    @treatment.setter
    def treatment(
        self,
        value: StructuredTextBuilder | StructuredTextReader | dict[str, Any],
    ) -> None: ...
    @property
    def experiment(self) -> StructuredTextBuilder: ...
    @experiment.setter
    def experiment(
        self,
        value: StructuredTextBuilder | StructuredTextReader | dict[str, Any],
    ) -> None: ...
    @override
    @overload
    def init(
        self,
        field: Literal["soil"],
        size: int | None = None,
    ) -> StructuredTextBuilder: ...
    @overload
    def init(
        self,
        field: Literal["plot"],
        size: int | None = None,
    ) -> StructuredTextBuilder: ...
    @overload
    def init(
        self,
        field: Literal["treatment"],
        size: int | None = None,
    ) -> StructuredTextBuilder: ...
    @overload
    def init(
        self,
        field: Literal["experiment"],
        size: int | None = None,
    ) -> StructuredTextBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> readers.FieldExperimentDataTemplateReader: ...
