"""Reader helper types for `soil_params.capnp`."""

from collections.abc import Callable
from typing import override

from capnp.lib.capnp import (
    _DynamicStructReader,
)

from mas.schema.soil.soil_params_capnp.types import builders as builders
from mas.schema.soil.soil_params_capnp.types import lists as lists

class SoilCharacteristicDataDataReader(_DynamicStructReader):
    @property
    def soilType(self) -> str: ...
    @property
    def soilRawDensity(self) -> int: ...
    @property
    def airCapacity(self) -> int: ...
    @property
    def fieldCapacity(self) -> int: ...
    @property
    def nFieldCapacity(self) -> int: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.SoilCharacteristicDataDataBuilder: ...

class SoilCharacteristicDataReader(_DynamicStructReader):
    @property
    def list(self) -> DataListReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.SoilCharacteristicDataBuilder: ...

class SoilCharacteristicModifierDataReader(_DynamicStructReader):
    @property
    def soilType(self) -> str: ...
    @property
    def organicMatter(self) -> float: ...
    @property
    def airCapacity(self) -> int: ...
    @property
    def fieldCapacity(self) -> int: ...
    @property
    def nFieldCapacity(self) -> int: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.SoilCharacteristicModifierDataBuilder: ...

class SoilCharacteristicModifierReader(_DynamicStructReader):
    @property
    def list(self) -> DataListReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.SoilCharacteristicModifierBuilder: ...

class CapillaryRiseRateDataReader(_DynamicStructReader):
    @property
    def soilType(self) -> str: ...
    @property
    def distance(self) -> int: ...
    @property
    def rate(self) -> float: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.CapillaryRiseRateDataBuilder: ...

class CapillaryRiseRateReader(_DynamicStructReader):
    @property
    def list(self) -> DataListReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.CapillaryRiseRateBuilder: ...

type DataListReader = lists._DataList.Reader
