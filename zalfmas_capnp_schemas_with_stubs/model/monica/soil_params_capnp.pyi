"""This is an automatically generated stub for `soil_params.capnp`."""

from __future__ import annotations

from collections.abc import MutableSequence, Sequence
from typing import Any, Literal, TypeAlias, override

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
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _SoilCharacteristicDataModule._DataModule.Builder: ...

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
            def as_reader(self) -> _SoilCharacteristicDataModule._DataModule.Reader: ...

        @override
        def new_message(
            self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, soilType: str | None = None, soilRawDensity: int | None = None, airCapacity: int | None = None, fieldCapacity: int | None = None, nFieldCapacity: int | None = None
        ) -> _SoilCharacteristicDataModule._DataModule.Builder: ...

    DataReader: TypeAlias = _DataModule.Reader
    DataBuilder: TypeAlias = _DataModule.Builder
    Data: _DataModule
    class Reader(_DynamicStructReader):
        @property
        def list(self) -> Sequence[_SoilCharacteristicDataModule._DataModule.Reader]: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _SoilCharacteristicDataModule.Builder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def list(self) -> MutableSequence[_SoilCharacteristicDataModule._DataModule.Builder]: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
        @list.setter
        def list(self, value: Sequence[_SoilCharacteristicDataModule._DataModule.Builder | _SoilCharacteristicDataModule._DataModule.Reader] | Sequence[dict[str, Any]]) -> None: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
        def init(self, field: Literal["list"], size: int | None = None) -> MutableSequence[_SoilCharacteristicDataModule._DataModule.Builder]: ...
        @override
        def as_reader(self) -> _SoilCharacteristicDataModule.Reader: ...

    @override
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, list: Sequence[_SoilCharacteristicDataModule._DataModule.Builder] | Sequence[dict[str, Any]] | None = None) -> _SoilCharacteristicDataModule.Builder: ...

SoilCharacteristicDataReader: TypeAlias = _SoilCharacteristicDataModule.Reader
SoilCharacteristicDataBuilder: TypeAlias = _SoilCharacteristicDataModule.Builder
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
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _SoilCharacteristicModifierModule._DataModule.Builder: ...

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
            def as_reader(self) -> _SoilCharacteristicModifierModule._DataModule.Reader: ...

        @override
        def new_message(
            self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, soilType: str | None = None, organicMatter: float | None = None, airCapacity: int | None = None, fieldCapacity: int | None = None, nFieldCapacity: int | None = None
        ) -> _SoilCharacteristicModifierModule._DataModule.Builder: ...

    DataReader: TypeAlias = _DataModule.Reader
    DataBuilder: TypeAlias = _DataModule.Builder
    Data: _DataModule
    class Reader(_DynamicStructReader):
        @property
        def list(self) -> Sequence[_SoilCharacteristicModifierModule._DataModule.Reader]: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _SoilCharacteristicModifierModule.Builder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def list(self) -> MutableSequence[_SoilCharacteristicModifierModule._DataModule.Builder]: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
        @list.setter
        def list(self, value: Sequence[_SoilCharacteristicModifierModule._DataModule.Builder | _SoilCharacteristicModifierModule._DataModule.Reader] | Sequence[dict[str, Any]]) -> None: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
        def init(self, field: Literal["list"], size: int | None = None) -> MutableSequence[_SoilCharacteristicModifierModule._DataModule.Builder]: ...
        @override
        def as_reader(self) -> _SoilCharacteristicModifierModule.Reader: ...

    @override
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, list: Sequence[_SoilCharacteristicModifierModule._DataModule.Builder] | Sequence[dict[str, Any]] | None = None) -> _SoilCharacteristicModifierModule.Builder: ...

SoilCharacteristicModifierReader: TypeAlias = _SoilCharacteristicModifierModule.Reader
SoilCharacteristicModifierBuilder: TypeAlias = _SoilCharacteristicModifierModule.Builder
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
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _CapillaryRiseRateModule._DataModule.Builder: ...

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
            def as_reader(self) -> _CapillaryRiseRateModule._DataModule.Reader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, soilType: str | None = None, distance: int | None = None, rate: float | None = None) -> _CapillaryRiseRateModule._DataModule.Builder: ...

    DataReader: TypeAlias = _DataModule.Reader
    DataBuilder: TypeAlias = _DataModule.Builder
    Data: _DataModule
    class Reader(_DynamicStructReader):
        @property
        def list(self) -> Sequence[_CapillaryRiseRateModule._DataModule.Reader]: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _CapillaryRiseRateModule.Builder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def list(self) -> MutableSequence[_CapillaryRiseRateModule._DataModule.Builder]: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
        @list.setter
        def list(self, value: Sequence[_CapillaryRiseRateModule._DataModule.Builder | _CapillaryRiseRateModule._DataModule.Reader] | Sequence[dict[str, Any]]) -> None: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
        def init(self, field: Literal["list"], size: int | None = None) -> MutableSequence[_CapillaryRiseRateModule._DataModule.Builder]: ...
        @override
        def as_reader(self) -> _CapillaryRiseRateModule.Reader: ...

    @override
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, list: Sequence[_CapillaryRiseRateModule._DataModule.Builder] | Sequence[dict[str, Any]] | None = None) -> _CapillaryRiseRateModule.Builder: ...

CapillaryRiseRateReader: TypeAlias = _CapillaryRiseRateModule.Reader
CapillaryRiseRateBuilder: TypeAlias = _CapillaryRiseRateModule.Builder
CapillaryRiseRate: _CapillaryRiseRateModule

# Top-level type aliases for use in type annotations
DataBuilder: TypeAlias = _CapillaryRiseRateModule._DataModule.Builder
DataReader: TypeAlias = _CapillaryRiseRateModule._DataModule.Reader
