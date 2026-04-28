"""Reader helper types for `agmip.capnp`."""

from collections.abc import Callable
from typing import override

from capnp.lib.capnp import (
    _DynamicStructReader,
)

from mas.schema.climate.climate_capnp.types.clients import TimeSeriesClient
from mas.schema.common.common_capnp.types.readers import StructuredTextReader
from mas.schema.model.agmip.agmip_capnp.types import builders as builders
from mas.schema.soil.soil_capnp.types.clients import ProfileClient

class FieldExperimentDataTemplateReader(_DynamicStructReader):
    @property
    def soilProfile(self) -> ProfileClient: ...
    @property
    def soil(self) -> StructuredTextReader: ...
    @property
    def plot(self) -> StructuredTextReader: ...
    @property
    def timeseries(self) -> TimeSeriesClient: ...
    @property
    def treatment(self) -> StructuredTextReader: ...
    @property
    def experiment(self) -> StructuredTextReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.FieldExperimentDataTemplateBuilder: ...
