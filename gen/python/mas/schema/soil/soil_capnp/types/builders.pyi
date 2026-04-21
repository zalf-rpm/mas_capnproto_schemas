"""Builder helper types for `soil.capnp`."""

from typing import Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicStructBuilder,
)

from mas.schema.soil.soil_capnp.types import enums as enums
from mas.schema.soil.soil_capnp.types import lists as lists
from mas.schema.soil.soil_capnp.types import readers as readers

class PropertyBuilder(_DynamicStructBuilder):
    @property
    def name(self) -> enums.PropertyNameEnum: ...
    @name.setter
    def name(self, value: enums.PropertyNameEnum) -> None: ...
    @property
    def f32Value(self) -> float: ...
    @f32Value.setter
    def f32Value(self, value: float) -> None: ...
    @property
    def bValue(self) -> bool: ...
    @bValue.setter
    def bValue(self, value: bool) -> None: ...
    @property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str) -> None: ...
    @property
    def unset(self) -> None: ...
    @unset.setter
    def unset(self, value: None) -> None: ...
    @override
    def which(self) -> Literal["f32Value", "bValue", "type", "unset"]: ...
    @override
    def as_reader(self) -> readers.PropertyReader: ...

class LayerBuilder(_DynamicStructBuilder):
    @property
    def properties(self) -> PropertyListBuilder: ...
    @properties.setter
    def properties(
        self,
        value: PropertyListBuilder | readers.PropertyListReader | dict[str, Any],
    ) -> None: ...
    @property
    def size(self) -> float: ...
    @size.setter
    def size(self, value: float) -> None: ...
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str) -> None: ...
    @override
    def init(
        self,
        field: Literal["properties"],
        size: int | None = None,
    ) -> PropertyListBuilder: ...
    @override
    def as_reader(self) -> readers.LayerReader: ...

class ResultBuilder(_DynamicStructBuilder):
    @property
    def failed(self) -> bool: ...
    @failed.setter
    def failed(self, value: bool) -> None: ...
    @property
    def mandatory(self) -> PropertyNameEnumListBuilder: ...
    @mandatory.setter
    def mandatory(
        self,
        value: PropertyNameEnumListBuilder
        | readers.PropertyNameEnumListReader
        | dict[str, Any],
    ) -> None: ...
    @property
    def optional(self) -> PropertyNameEnumListBuilder: ...
    @optional.setter
    def optional(
        self,
        value: PropertyNameEnumListBuilder
        | readers.PropertyNameEnumListReader
        | dict[str, Any],
    ) -> None: ...
    @override
    @overload
    def init(
        self,
        field: Literal["mandatory"],
        size: int | None = None,
    ) -> PropertyNameEnumListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["optional"],
        size: int | None = None,
    ) -> PropertyNameEnumListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> readers.ResultReader: ...

class QueryBuilder(_DynamicStructBuilder):
    @property
    def mandatory(self) -> PropertyNameEnumListBuilder: ...
    @mandatory.setter
    def mandatory(
        self,
        value: PropertyNameEnumListBuilder
        | readers.PropertyNameEnumListReader
        | dict[str, Any],
    ) -> None: ...
    @property
    def optional(self) -> PropertyNameEnumListBuilder: ...
    @optional.setter
    def optional(
        self,
        value: PropertyNameEnumListBuilder
        | readers.PropertyNameEnumListReader
        | dict[str, Any],
    ) -> None: ...
    @property
    def onlyRawData(self) -> bool: ...
    @onlyRawData.setter
    def onlyRawData(self, value: bool) -> None: ...
    @override
    @overload
    def init(
        self,
        field: Literal["mandatory"],
        size: int | None = None,
    ) -> PropertyNameEnumListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["optional"],
        size: int | None = None,
    ) -> PropertyNameEnumListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> readers.QueryReader: ...

class ProfileDataBuilder(_DynamicStructBuilder):
    @property
    def layers(self) -> LayerListBuilder: ...
    @layers.setter
    def layers(
        self,
        value: LayerListBuilder | readers.LayerListReader | dict[str, Any],
    ) -> None: ...
    @property
    def percentageOfArea(self) -> float: ...
    @percentageOfArea.setter
    def percentageOfArea(self, value: float) -> None: ...
    @override
    def init(
        self,
        field: Literal["layers"],
        size: int | None = None,
    ) -> LayerListBuilder: ...
    @override
    def as_reader(self) -> readers.ProfileDataReader: ...

type LayerListBuilder = lists._LayerList.Builder

type ProfileClientListBuilder = lists._ProfileClientList.Builder

type PropertyListBuilder = lists._PropertyList.Builder

type PropertyNameEnumListBuilder = lists._PropertyNameEnumList.Builder
