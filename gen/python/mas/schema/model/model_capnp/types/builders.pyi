"""Builder helper types for `model.capnp`."""

from typing import Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicObjectReader,
    _DynamicStructBuilder,
)

from mas.schema.climate.climate_capnp.types.clients import TimeSeriesClient
from mas.schema.climate.climate_capnp.types.modules import _TimeSeriesInterfaceModule
from mas.schema.model.model_capnp.types import common as common
from mas.schema.model.model_capnp.types import enums as enums
from mas.schema.model.model_capnp.types import lists as lists
from mas.schema.model.model_capnp.types import readers as readers
from mas.schema.soil.soil_capnp.types.clients import ProfileClient
from mas.schema.soil.soil_capnp.types.modules import _ProfileInterfaceModule

class XYResultBuilder(_DynamicStructBuilder):
    @property
    def xs(self) -> Float64ListBuilder: ...
    @xs.setter
    def xs(
        self,
        value: Float64ListBuilder | readers.Float64ListReader | dict[str, Any],
    ) -> None: ...
    @property
    def ys(self) -> Float64ListBuilder: ...
    @ys.setter
    def ys(
        self,
        value: Float64ListBuilder | readers.Float64ListReader | dict[str, Any],
    ) -> None: ...
    @override
    @overload
    def init(
        self,
        field: Literal["xs"],
        size: int | None = None,
    ) -> Float64ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["ys"],
        size: int | None = None,
    ) -> Float64ListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> readers.XYResultReader: ...

class StatBuilder(_DynamicStructBuilder):
    @property
    def type(self) -> enums.StatTypeEnum: ...
    @type.setter
    def type(self, value: enums.StatTypeEnum) -> None: ...
    @property
    def vs(self) -> Float64ListBuilder: ...
    @vs.setter
    def vs(
        self,
        value: Float64ListBuilder | readers.Float64ListReader | dict[str, Any],
    ) -> None: ...
    @override
    def init(
        self,
        field: Literal["vs"],
        size: int | None = None,
    ) -> Float64ListBuilder: ...
    @override
    def as_reader(self) -> readers.StatReader: ...

class XYPlusResultBuilder(_DynamicStructBuilder):
    @property
    def xy(self) -> XYResultBuilder: ...
    @xy.setter
    def xy(
        self,
        value: XYResultBuilder | readers.XYResultReader | dict[str, Any],
    ) -> None: ...
    @property
    def stats(self) -> StatListBuilder: ...
    @stats.setter
    def stats(
        self,
        value: StatListBuilder | readers.StatListReader | dict[str, Any],
    ) -> None: ...
    @override
    @overload
    def init(
        self,
        field: Literal["xy"],
        size: int | None = None,
    ) -> XYResultBuilder: ...
    @overload
    def init(
        self,
        field: Literal["stats"],
        size: int | None = None,
    ) -> StatListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> readers.XYPlusResultReader: ...

class EnvBuilder(_DynamicStructBuilder):
    @property
    def rest(self) -> _DynamicObjectReader: ...
    @rest.setter
    def rest(self, value: common.AnyPointer) -> None: ...
    @property
    def timeSeries(self) -> TimeSeriesClient: ...
    @timeSeries.setter
    def timeSeries(
        self,
        value: TimeSeriesClient | _TimeSeriesInterfaceModule.Server,
    ) -> None: ...
    @property
    def soilProfile(self) -> ProfileClient: ...
    @soilProfile.setter
    def soilProfile(
        self,
        value: ProfileClient | _ProfileInterfaceModule.Server,
    ) -> None: ...
    @property
    def mgmtEvents(self) -> EventListBuilder: ...
    @mgmtEvents.setter
    def mgmtEvents(
        self,
        value: EventListBuilder | readers.EventListReader | dict[str, Any],
    ) -> None: ...
    @override
    def init(
        self,
        field: Literal["mgmtEvents"],
        size: int | None = None,
    ) -> EventListBuilder: ...
    @override
    def as_reader(self) -> readers.EnvReader: ...

type EventListBuilder = lists._EventList.Builder

type Float64ListBuilder = lists._Float64List.Builder

type IdentifiableClientListBuilder = lists._IdentifiableClientList.Builder

type StatListBuilder = lists._StatList.Builder

type TimeSeriesClientListBuilder = lists._TimeSeriesClientList.Builder
