"""Reader helper types for `model.capnp`."""

from collections.abc import Callable
from typing import override

from capnp.lib.capnp import (
    _DynamicObjectReader,
    _DynamicStructReader,
)

from mas.schema.climate.climate_capnp.types.clients import TimeSeriesClient
from mas.schema.model.model_capnp.types import builders as builders
from mas.schema.model.model_capnp.types import enums as enums
from mas.schema.model.model_capnp.types import lists as lists
from mas.schema.soil.soil_capnp.types.clients import ProfileClient

class XYResultReader(_DynamicStructReader):
    @property
    def xs(self) -> Float64ListReader: ...
    @property
    def ys(self) -> Float64ListReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.XYResultBuilder: ...

class StatReader(_DynamicStructReader):
    @property
    def type(self) -> enums.StatTypeEnum: ...
    @property
    def vs(self) -> Float64ListReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.StatBuilder: ...

class XYPlusResultReader(_DynamicStructReader):
    @property
    def xy(self) -> XYResultReader: ...
    @property
    def stats(self) -> StatListReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.XYPlusResultBuilder: ...

class EnvReader(_DynamicStructReader):
    @property
    def rest(self) -> _DynamicObjectReader: ...
    @property
    def timeSeries(self) -> TimeSeriesClient: ...
    @property
    def soilProfile(self) -> ProfileClient: ...
    @property
    def mgmtEvents(self) -> EventListReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.EnvBuilder: ...

type EventListReader = lists._EventList.Reader

type Float64ListReader = lists._Float64List.Reader

type IdentifiableClientListReader = lists._IdentifiableClientList.Reader

type StatListReader = lists._StatList.Reader

type TimeSeriesClientListReader = lists._TimeSeriesClientList.Reader
