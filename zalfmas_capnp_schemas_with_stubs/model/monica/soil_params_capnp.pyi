"""This is an automatically generated stub for `soil_params.capnp`."""

from __future__ import annotations

from collections.abc import MutableSequence, Sequence
from typing import Any, Literal, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
    _Request,
    _StructModule,
)

class _SoilCharacteristicDataModule(_StructModule):
    class _DataModule(_StructModule):
        class Reader(_DynamicStructReader):
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
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> DataBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def soilType(self) -> str: ...
            @soilType.setter
            def soilType(self, value: str) -> None: ...
            @property
            def soilRawDensity(self) -> int: ...
            @soilRawDensity.setter
            def soilRawDensity(self, value: int) -> None: ...
            @property
            def airCapacity(self) -> int: ...
            @airCapacity.setter
            def airCapacity(self, value: int) -> None: ...
            @property
            def fieldCapacity(self) -> int: ...
            @fieldCapacity.setter
            def fieldCapacity(self, value: int) -> None: ...
            @property
            def nFieldCapacity(self) -> int: ...
            @nFieldCapacity.setter
            def nFieldCapacity(self, value: int) -> None: ...
            @override
            def as_reader(self) -> DataReader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, soilType: str | None = None, soilRawDensity: int | None = None, airCapacity: int | None = None, fieldCapacity: int | None = None, nFieldCapacity: int | None = None) -> DataBuilder: ...

    type DataReader = _DataModule.Reader
    type DataBuilder = _DataModule.Builder
    Data: _DataModule
    class Reader(_DynamicStructReader):
        @property
        def list(self) -> Sequence[DataReader]: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> SoilCharacteristicDataBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def list(self) -> MutableSequence[DataBuilder]: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
        @list.setter
        def list(self, value: Sequence[DataBuilder | DataReader] | Sequence[dict[str, Any]]) -> None: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
        def init(self, field: Literal["list"], size: int | None = None) -> MutableSequence[_SoilCharacteristicDataModule._DataModule.Builder]: ...
        @override
        def as_reader(self) -> SoilCharacteristicDataReader: ...

    @override
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, list: Sequence[DataBuilder] | Sequence[dict[str, Any]] | None = None) -> SoilCharacteristicDataBuilder: ...

SoilCharacteristicData: _SoilCharacteristicDataModule

class _SoilCharacteristicModifierModule(_StructModule):
    class _DataModule(_StructModule):
        class Reader(_DynamicStructReader):
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
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> DataBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def soilType(self) -> str: ...
            @soilType.setter
            def soilType(self, value: str) -> None: ...
            @property
            def organicMatter(self) -> float: ...
            @organicMatter.setter
            def organicMatter(self, value: float) -> None: ...
            @property
            def airCapacity(self) -> int: ...
            @airCapacity.setter
            def airCapacity(self, value: int) -> None: ...
            @property
            def fieldCapacity(self) -> int: ...
            @fieldCapacity.setter
            def fieldCapacity(self, value: int) -> None: ...
            @property
            def nFieldCapacity(self) -> int: ...
            @nFieldCapacity.setter
            def nFieldCapacity(self, value: int) -> None: ...
            @override
            def as_reader(self) -> DataReader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, soilType: str | None = None, organicMatter: float | None = None, airCapacity: int | None = None, fieldCapacity: int | None = None, nFieldCapacity: int | None = None) -> DataBuilder: ...

    type DataReader = _DataModule.Reader
    type DataBuilder = _DataModule.Builder
    Data: _DataModule
    class Reader(_DynamicStructReader):
        @property
        def list(self) -> Sequence[DataReader]: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> SoilCharacteristicModifierBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def list(self) -> MutableSequence[DataBuilder]: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
        @list.setter
        def list(self, value: Sequence[DataBuilder | DataReader] | Sequence[dict[str, Any]]) -> None: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
        def init(self, field: Literal["list"], size: int | None = None) -> MutableSequence[_SoilCharacteristicModifierModule._DataModule.Builder]: ...
        @override
        def as_reader(self) -> SoilCharacteristicModifierReader: ...

    @override
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, list: Sequence[DataBuilder] | Sequence[dict[str, Any]] | None = None) -> SoilCharacteristicModifierBuilder: ...

SoilCharacteristicModifier: _SoilCharacteristicModifierModule

class _CapillaryRiseRateModule(_StructModule):
    class _DataModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def soilType(self) -> str: ...
            @property
            def distance(self) -> int: ...
            @property
            def rate(self) -> float: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> DataBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def soilType(self) -> str: ...
            @soilType.setter
            def soilType(self, value: str) -> None: ...
            @property
            def distance(self) -> int: ...
            @distance.setter
            def distance(self, value: int) -> None: ...
            @property
            def rate(self) -> float: ...
            @rate.setter
            def rate(self, value: float) -> None: ...
            @override
            def as_reader(self) -> DataReader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, soilType: str | None = None, distance: int | None = None, rate: float | None = None) -> DataBuilder: ...

    type DataReader = _DataModule.Reader
    type DataBuilder = _DataModule.Builder
    Data: _DataModule
    class Reader(_DynamicStructReader):
        @property
        def list(self) -> Sequence[DataReader]: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> CapillaryRiseRateBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def list(self) -> MutableSequence[DataBuilder]: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
        @list.setter
        def list(self, value: Sequence[DataBuilder | DataReader] | Sequence[dict[str, Any]]) -> None: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
        def init(self, field: Literal["list"], size: int | None = None) -> MutableSequence[_CapillaryRiseRateModule._DataModule.Builder]: ...
        @override
        def as_reader(self) -> CapillaryRiseRateReader: ...

    @override
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, list: Sequence[DataBuilder] | Sequence[dict[str, Any]] | None = None) -> CapillaryRiseRateBuilder: ...

CapillaryRiseRate: _CapillaryRiseRateModule

# Top-level type aliases for use in type annotations
type CapillaryRiseRateBuilder = _CapillaryRiseRateModule.Builder
type CapillaryRiseRateReader = _CapillaryRiseRateModule.Reader
type DataBuilder = _CapillaryRiseRateModule._DataModule.Builder
type DataReader = _CapillaryRiseRateModule._DataModule.Reader
type SoilCharacteristicDataBuilder = _SoilCharacteristicDataModule.Builder
type SoilCharacteristicDataReader = _SoilCharacteristicDataModule.Reader
type SoilCharacteristicModifierBuilder = _SoilCharacteristicModifierModule.Builder
type SoilCharacteristicModifierReader = _SoilCharacteristicModifierModule.Reader
