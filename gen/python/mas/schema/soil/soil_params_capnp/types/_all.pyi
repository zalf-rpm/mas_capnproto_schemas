"""This is an automatically generated stub for `soil_params.capnp`."""

from collections.abc import Callable, Iterator
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicListBuilder,
    _DynamicListReader,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _StructModule,
)

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
    ) -> SoilCharacteristicDataDataBuilder: ...

class SoilCharacteristicDataDataBuilder(_DynamicStructBuilder):
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
    def as_reader(self) -> SoilCharacteristicDataDataReader: ...

class _DataList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(
            self,
            key: int,
        ) -> _SoilCharacteristicDataStructModule._DataStructModule.Reader: ...
        @override
        def __iter__(
            self,
        ) -> Iterator[_SoilCharacteristicDataStructModule._DataStructModule.Reader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(
            self,
            key: int,
        ) -> _SoilCharacteristicDataStructModule._DataStructModule.Builder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: _SoilCharacteristicDataStructModule._DataStructModule.Reader
            | _SoilCharacteristicDataStructModule._DataStructModule.Builder
            | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(
            self,
        ) -> Iterator[
            _SoilCharacteristicDataStructModule._DataStructModule.Builder
        ]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> _SoilCharacteristicDataStructModule._DataStructModule.Builder: ...

class _SoilCharacteristicDataStructModule(_StructModule):
    class _DataStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            soilType: str | None = None,
            soilRawDensity: int | None = None,
            airCapacity: int | None = None,
            fieldCapacity: int | None = None,
            nFieldCapacity: int | None = None,
            **kwargs: object,
        ) -> SoilCharacteristicDataDataBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[SoilCharacteristicDataDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[SoilCharacteristicDataDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[SoilCharacteristicDataDataBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> SoilCharacteristicDataDataReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> SoilCharacteristicDataDataReader: ...

    Data: _DataStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        list: DataListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> SoilCharacteristicDataBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[SoilCharacteristicDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[SoilCharacteristicDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[SoilCharacteristicDataBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> SoilCharacteristicDataReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> SoilCharacteristicDataReader: ...

class SoilCharacteristicDataReader(_DynamicStructReader):
    @property
    def list(self) -> DataListReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> SoilCharacteristicDataBuilder: ...

class SoilCharacteristicDataBuilder(_DynamicStructBuilder):
    @property
    def list(self) -> DataListBuilder: ...
    @list.setter
    def list(
        self,
        value: DataListBuilder | DataListReader | dict[str, Any],
    ) -> None: ...
    @override
    def init(
        self,
        field: Literal["list"],
        size: int | None = None,
    ) -> DataListBuilder: ...
    @override
    def as_reader(self) -> SoilCharacteristicDataReader: ...

SoilCharacteristicData: _SoilCharacteristicDataStructModule

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
    ) -> SoilCharacteristicModifierDataBuilder: ...

class SoilCharacteristicModifierDataBuilder(_DynamicStructBuilder):
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
    def as_reader(self) -> SoilCharacteristicModifierDataReader: ...

class _SoilCharacteristicModifierStructModule(_StructModule):
    class _DataStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            soilType: str | None = None,
            organicMatter: float | None = None,
            airCapacity: int | None = None,
            fieldCapacity: int | None = None,
            nFieldCapacity: int | None = None,
            **kwargs: object,
        ) -> SoilCharacteristicModifierDataBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[SoilCharacteristicModifierDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[SoilCharacteristicModifierDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[SoilCharacteristicModifierDataBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> SoilCharacteristicModifierDataReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> SoilCharacteristicModifierDataReader: ...

    Data: _DataStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        list: DataListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> SoilCharacteristicModifierBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[SoilCharacteristicModifierReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[SoilCharacteristicModifierReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[SoilCharacteristicModifierBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> SoilCharacteristicModifierReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> SoilCharacteristicModifierReader: ...

class SoilCharacteristicModifierReader(_DynamicStructReader):
    @property
    def list(self) -> DataListReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> SoilCharacteristicModifierBuilder: ...

class SoilCharacteristicModifierBuilder(_DynamicStructBuilder):
    @property
    def list(self) -> DataListBuilder: ...
    @list.setter
    def list(
        self,
        value: DataListBuilder | DataListReader | dict[str, Any],
    ) -> None: ...
    @override
    def init(
        self,
        field: Literal["list"],
        size: int | None = None,
    ) -> DataListBuilder: ...
    @override
    def as_reader(self) -> SoilCharacteristicModifierReader: ...

SoilCharacteristicModifier: _SoilCharacteristicModifierStructModule

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
    ) -> CapillaryRiseRateDataBuilder: ...

class CapillaryRiseRateDataBuilder(_DynamicStructBuilder):
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
    def as_reader(self) -> CapillaryRiseRateDataReader: ...

class _CapillaryRiseRateStructModule(_StructModule):
    class _DataStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            soilType: str | None = None,
            distance: int | None = None,
            rate: float | None = None,
            **kwargs: object,
        ) -> CapillaryRiseRateDataBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[CapillaryRiseRateDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[CapillaryRiseRateDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[CapillaryRiseRateDataBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> CapillaryRiseRateDataReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> CapillaryRiseRateDataReader: ...

    Data: _DataStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        list: DataListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> CapillaryRiseRateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[CapillaryRiseRateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[CapillaryRiseRateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[CapillaryRiseRateBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> CapillaryRiseRateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> CapillaryRiseRateReader: ...

class CapillaryRiseRateReader(_DynamicStructReader):
    @property
    def list(self) -> DataListReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> CapillaryRiseRateBuilder: ...

class CapillaryRiseRateBuilder(_DynamicStructBuilder):
    @property
    def list(self) -> DataListBuilder: ...
    @list.setter
    def list(
        self,
        value: DataListBuilder | DataListReader | dict[str, Any],
    ) -> None: ...
    @override
    def init(
        self,
        field: Literal["list"],
        size: int | None = None,
    ) -> DataListBuilder: ...
    @override
    def as_reader(self) -> CapillaryRiseRateReader: ...

CapillaryRiseRate: _CapillaryRiseRateStructModule

# Top-level type aliases for use in type annotations
type DataListBuilder = _DataList.Builder
type DataListReader = _DataList.Reader
