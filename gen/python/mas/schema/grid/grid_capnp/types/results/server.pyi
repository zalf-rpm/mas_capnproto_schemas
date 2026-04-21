"""Server result helper types for `grid.capnp`."""

from collections.abc import Sequence
from typing import Any, Literal, overload

from capnp.lib.capnp import (
    _DynamicStructBuilder,
)

from mas.schema.geo.geo_capnp.types.builders import LatLonCoordBuilder
from mas.schema.geo.geo_capnp.types.readers import LatLonCoordReader
from mas.schema.grid.grid_capnp.types import builders as builders
from mas.schema.grid.grid_capnp.types import clients as clients
from mas.schema.grid.grid_capnp.types import modules as modules
from mas.schema.grid.grid_capnp.types import readers as readers

class SendcellsServerResult(_DynamicStructBuilder):
    @property
    def locations(self) -> builders.LocationListBuilder: ...
    @locations.setter
    def locations(
        self,
        value: builders.LocationListBuilder
        | readers.LocationListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["locations"],
        size: int | None = None,
    ) -> builders.LocationListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class ClosestvalueatServerResult(_DynamicStructBuilder):
    @property
    def val(self) -> builders.ValueBuilder: ...
    @val.setter
    def val(
        self,
        value: builders.ValueBuilder | readers.ValueReader | dict[str, Any],
    ) -> None: ...
    @property
    def tl(self) -> builders.RowColBuilder: ...
    @tl.setter
    def tl(
        self,
        value: builders.RowColBuilder | readers.RowColReader | dict[str, Any],
    ) -> None: ...
    @property
    def br(self) -> builders.RowColBuilder: ...
    @br.setter
    def br(
        self,
        value: builders.RowColBuilder | readers.RowColReader | dict[str, Any],
    ) -> None: ...
    @property
    def aggParts(self) -> builders.AggregationPartListBuilder: ...
    @aggParts.setter
    def aggParts(
        self,
        value: builders.AggregationPartListBuilder
        | readers.AggregationPartListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["val"],
        size: int | None = None,
    ) -> builders.ValueBuilder: ...
    @overload
    def init(
        self,
        field: Literal["tl"],
        size: int | None = None,
    ) -> builders.RowColBuilder: ...
    @overload
    def init(
        self,
        field: Literal["br"],
        size: int | None = None,
    ) -> builders.RowColBuilder: ...
    @overload
    def init(
        self,
        field: Literal["aggParts"],
        size: int | None = None,
    ) -> builders.AggregationPartListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class ResolutionServerResult(_DynamicStructBuilder):
    @property
    def res(self) -> builders.ResolutionBuilder: ...
    @res.setter
    def res(
        self,
        value: builders.ResolutionBuilder | readers.ResolutionReader | dict[str, Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["res"],
        size: int | None = None,
    ) -> builders.ResolutionBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class DimensionServerResult(_DynamicStructBuilder):
    @property
    def rows(self) -> int: ...
    @rows.setter
    def rows(self, value: int) -> None: ...
    @property
    def cols(self) -> int: ...
    @cols.setter
    def cols(self, value: int) -> None: ...

class NodatavalueServerResult(_DynamicStructBuilder):
    @property
    def nodata(self) -> builders.ValueBuilder: ...
    @nodata.setter
    def nodata(
        self,
        value: builders.ValueBuilder | readers.ValueReader | dict[str, Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["nodata"],
        size: int | None = None,
    ) -> builders.ValueBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class ValueatServerResult(_DynamicStructBuilder):
    @property
    def val(self) -> builders.ValueBuilder: ...
    @val.setter
    def val(
        self,
        value: builders.ValueBuilder | readers.ValueReader | dict[str, Any],
    ) -> None: ...
    @property
    def aggParts(self) -> builders.AggregationPartListBuilder: ...
    @aggParts.setter
    def aggParts(
        self,
        value: builders.AggregationPartListBuilder
        | readers.AggregationPartListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["val"],
        size: int | None = None,
    ) -> builders.ValueBuilder: ...
    @overload
    def init(
        self,
        field: Literal["aggParts"],
        size: int | None = None,
    ) -> builders.AggregationPartListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class LatlonboundsServerResult(_DynamicStructBuilder):
    @property
    def tl(self) -> LatLonCoordBuilder: ...
    @tl.setter
    def tl(
        self,
        value: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any],
    ) -> None: ...
    @property
    def tr(self) -> LatLonCoordBuilder: ...
    @tr.setter
    def tr(
        self,
        value: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any],
    ) -> None: ...
    @property
    def br(self) -> LatLonCoordBuilder: ...
    @br.setter
    def br(
        self,
        value: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any],
    ) -> None: ...
    @property
    def bl(self) -> LatLonCoordBuilder: ...
    @bl.setter
    def bl(
        self,
        value: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["tl"],
        size: int | None = None,
    ) -> LatLonCoordBuilder: ...
    @overload
    def init(
        self,
        field: Literal["tr"],
        size: int | None = None,
    ) -> LatLonCoordBuilder: ...
    @overload
    def init(
        self,
        field: Literal["br"],
        size: int | None = None,
    ) -> LatLonCoordBuilder: ...
    @overload
    def init(
        self,
        field: Literal["bl"],
        size: int | None = None,
    ) -> LatLonCoordBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class StreamcellsServerResult(_DynamicStructBuilder):
    @property
    def callback(
        self,
    ) -> (
        modules._GridInterfaceModule._CallbackInterfaceModule.Server
        | clients.CallbackClient
    ): ...
    @callback.setter
    def callback(
        self,
        value: modules._GridInterfaceModule._CallbackInterfaceModule.Server
        | clients.CallbackClient,
    ) -> None: ...

class UnitServerResult(_DynamicStructBuilder):
    @property
    def unit(self) -> str: ...
    @unit.setter
    def unit(self, value: str) -> None: ...
