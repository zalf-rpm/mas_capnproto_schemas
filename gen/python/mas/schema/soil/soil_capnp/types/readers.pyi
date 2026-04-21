"""Reader helper types for `soil.capnp`."""

from collections.abc import Callable
from typing import Literal, override

from capnp.lib.capnp import (
    _DynamicStructReader,
)

from mas.schema.soil.soil_capnp.types import builders as builders
from mas.schema.soil.soil_capnp.types import enums as enums
from mas.schema.soil.soil_capnp.types import lists as lists

class PropertyReader(_DynamicStructReader):
    @property
    def name(self) -> enums.PropertyNameEnum: ...
    @property
    def f32Value(self) -> float: ...
    @property
    def bValue(self) -> bool: ...
    @property
    def type(self) -> str: ...
    @property
    def unset(self) -> None: ...
    @override
    def which(self) -> Literal["f32Value", "bValue", "type", "unset"]: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.PropertyBuilder: ...

class LayerReader(_DynamicStructReader):
    @property
    def properties(self) -> PropertyListReader: ...
    @property
    def size(self) -> float: ...
    @property
    def description(self) -> str: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.LayerBuilder: ...

class ResultReader(_DynamicStructReader):
    @property
    def failed(self) -> bool: ...
    @property
    def mandatory(self) -> PropertyNameEnumListReader: ...
    @property
    def optional(self) -> PropertyNameEnumListReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.ResultBuilder: ...

class QueryReader(_DynamicStructReader):
    @property
    def mandatory(self) -> PropertyNameEnumListReader: ...
    @property
    def optional(self) -> PropertyNameEnumListReader: ...
    @property
    def onlyRawData(self) -> bool: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.QueryBuilder: ...

class ProfileDataReader(_DynamicStructReader):
    @property
    def layers(self) -> LayerListReader: ...
    @property
    def percentageOfArea(self) -> float: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.ProfileDataBuilder: ...

type LayerListReader = lists._LayerList.Reader

type ProfileClientListReader = lists._ProfileClientList.Reader

type PropertyListReader = lists._PropertyList.Reader

type PropertyNameEnumListReader = lists._PropertyNameEnumList.Reader
