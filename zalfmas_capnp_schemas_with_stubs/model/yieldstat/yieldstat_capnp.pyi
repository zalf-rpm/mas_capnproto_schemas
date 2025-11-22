"""This is an automatically generated stub for `yieldstat.capnp`."""

from __future__ import annotations

from collections.abc import Iterator
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicListBuilder,
    _DynamicListReader,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _StructModule,
)

class _ResultIdModule:
    primaryYield: int
    dryMatter: int
    carbonInAboveGroundBiomass: int
    sumFertilizer: int
    sumIrrigation: int
    primaryYieldCU: int

class _RestInputModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def useDevTrend(self) -> bool: ...
        @property
        def useCO2Increase(self) -> bool: ...
        @property
        def dgm(self) -> float: ...
        @property
        def hft(self) -> int: ...
        @property
        def nft(self) -> int: ...
        @property
        def sft(self) -> int: ...
        @property
        def slope(self) -> int: ...
        @property
        def steino(self) -> int: ...
        @property
        def az(self) -> int: ...
        @property
        def klz(self) -> int: ...
        @property
        def stt(self) -> int: ...
        @property
        def germanFederalStates(self) -> int: ...
        @property
        def getDryYearWaterNeed(self) -> bool: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> RestInputBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def useDevTrend(self) -> bool: ...
        @useDevTrend.setter
        def useDevTrend(self, value: bool) -> None: ...
        @property
        def useCO2Increase(self) -> bool: ...
        @useCO2Increase.setter
        def useCO2Increase(self, value: bool) -> None: ...
        @property
        def dgm(self) -> float: ...
        @dgm.setter
        def dgm(self, value: float) -> None: ...
        @property
        def hft(self) -> int: ...
        @hft.setter
        def hft(self, value: int) -> None: ...
        @property
        def nft(self) -> int: ...
        @nft.setter
        def nft(self, value: int) -> None: ...
        @property
        def sft(self) -> int: ...
        @sft.setter
        def sft(self, value: int) -> None: ...
        @property
        def slope(self) -> int: ...
        @slope.setter
        def slope(self, value: int) -> None: ...
        @property
        def steino(self) -> int: ...
        @steino.setter
        def steino(self, value: int) -> None: ...
        @property
        def az(self) -> int: ...
        @az.setter
        def az(self, value: int) -> None: ...
        @property
        def klz(self) -> int: ...
        @klz.setter
        def klz(self, value: int) -> None: ...
        @property
        def stt(self) -> int: ...
        @stt.setter
        def stt(self, value: int) -> None: ...
        @property
        def germanFederalStates(self) -> int: ...
        @germanFederalStates.setter
        def germanFederalStates(self, value: int) -> None: ...
        @property
        def getDryYearWaterNeed(self) -> bool: ...
        @getDryYearWaterNeed.setter
        def getDryYearWaterNeed(self, value: bool) -> None: ...
        @override
        def as_reader(self) -> RestInputReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        useDevTrend: bool | None = None,
        useCO2Increase: bool | None = None,
        dgm: float | None = None,
        hft: int | None = None,
        nft: int | None = None,
        sft: int | None = None,
        slope: int | None = None,
        steino: int | None = None,
        az: int | None = None,
        klz: int | None = None,
        stt: int | None = None,
        germanFederalStates: int | None = None,
        getDryYearWaterNeed: bool | None = None,
        **kwargs: Any,
    ) -> RestInputBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[RestInputReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[RestInputReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[RestInputBuilder]: ...
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> RestInputReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> RestInputReader: ...

RestInput: _RestInputModule

class _ResultToValueList:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> ResultToValueReader: ...
        def __iter__(self) -> Iterator[ResultToValueReader]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> ResultToValueBuilder: ...
        def __setitem__(
            self,
            key: int,
            value: ResultToValueReader | ResultToValueBuilder | dict[str, Any],
        ) -> None: ...
        def __iter__(self) -> Iterator[ResultToValueBuilder]: ...
        def init(self, index: int, size: int | None = None) -> ResultToValueBuilder: ...

class _ResultModule(_StructModule):
    class _ResultToValueModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def id(self) -> ResultIdEnum: ...
            @property
            def value(self) -> float: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> ResultToValueBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def id(self) -> ResultIdEnum: ...
            @id.setter
            def id(self, value: ResultIdEnum) -> None: ...
            @property
            def value(self) -> float: ...
            @value.setter
            def value(self, value: float) -> None: ...
            @override
            def as_reader(self) -> ResultToValueReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            id: ResultIdEnum | None = None,
            value: float | None = None,
            **kwargs: Any,
        ) -> ResultToValueBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[ResultToValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[ResultToValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[ResultToValueBuilder]: ...
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> ResultToValueReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> ResultToValueReader: ...

    type ResultToValueReader = _ResultToValueModule.Reader
    type ResultToValueBuilder = _ResultToValueModule.Builder
    ResultToValue: _ResultToValueModule
    class Reader(_DynamicStructReader):
        @property
        def cultivar(self) -> str: ...
        @property
        def isNoData(self) -> bool: ...
        @property
        def values(self) -> ResultToValueListReader: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> ResultBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def cultivar(self) -> str: ...
        @cultivar.setter
        def cultivar(self, value: str) -> None: ...
        @property
        def isNoData(self) -> bool: ...
        @isNoData.setter
        def isNoData(self, value: bool) -> None: ...
        @property
        def values(self) -> ResultToValueListBuilder: ...
        @values.setter
        def values(
            self,
            value: ResultToValueListBuilder | ResultToValueListReader | dict[str, Any],
        ) -> None: ...
        def init(
            self, field: Literal["values"], size: int | None = None
        ) -> ResultToValueListBuilder: ...
        @override
        def as_reader(self) -> ResultReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        cultivar: str | None = None,
        isNoData: bool | None = None,
        values: ResultToValueListBuilder | dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> ResultBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[ResultReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[ResultReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[ResultBuilder]: ...
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> ResultReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> ResultReader: ...

Result: _ResultModule

class _YearToResultList:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> YearToResultReader: ...
        def __iter__(self) -> Iterator[YearToResultReader]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> YearToResultBuilder: ...
        def __setitem__(
            self,
            key: int,
            value: YearToResultReader | YearToResultBuilder | dict[str, Any],
        ) -> None: ...
        def __iter__(self) -> Iterator[YearToResultBuilder]: ...
        def init(self, index: int, size: int | None = None) -> YearToResultBuilder: ...

class _OutputModule(_StructModule):
    class _YearToResultModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def year(self) -> int: ...
            @property
            def result(self) -> ResultReader: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> YearToResultBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def year(self) -> int: ...
            @year.setter
            def year(self, value: int) -> None: ...
            @property
            def result(self) -> ResultBuilder: ...
            @result.setter
            def result(
                self, value: ResultBuilder | ResultReader | dict[str, Any]
            ) -> None: ...
            def init(
                self, field: Literal["result"], size: int | None = None
            ) -> ResultBuilder: ...
            @override
            def as_reader(self) -> YearToResultReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            year: int | None = None,
            result: ResultBuilder | dict[str, Any] | None = None,
            **kwargs: Any,
        ) -> YearToResultBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[YearToResultReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[YearToResultReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[YearToResultBuilder]: ...
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> YearToResultReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> YearToResultReader: ...

    type YearToResultReader = _YearToResultModule.Reader
    type YearToResultBuilder = _YearToResultModule.Builder
    YearToResult: _YearToResultModule
    class Reader(_DynamicStructReader):
        @property
        def id(self) -> str: ...
        @property
        def runFailed(self) -> bool: ...
        @property
        def reason(self) -> str: ...
        @property
        def results(self) -> YearToResultListReader: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> OutputBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def id(self) -> str: ...
        @id.setter
        def id(self, value: str) -> None: ...
        @property
        def runFailed(self) -> bool: ...
        @runFailed.setter
        def runFailed(self, value: bool) -> None: ...
        @property
        def reason(self) -> str: ...
        @reason.setter
        def reason(self, value: str) -> None: ...
        @property
        def results(self) -> YearToResultListBuilder: ...
        @results.setter
        def results(
            self,
            value: YearToResultListBuilder | YearToResultListReader | dict[str, Any],
        ) -> None: ...
        def init(
            self, field: Literal["results"], size: int | None = None
        ) -> YearToResultListBuilder: ...
        @override
        def as_reader(self) -> OutputReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        id: str | None = None,
        runFailed: bool | None = None,
        reason: str | None = None,
        results: YearToResultListBuilder | dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> OutputBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[OutputReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[OutputReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[OutputBuilder]: ...
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> OutputReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> OutputReader: ...

Output: _OutputModule

# Top-level type aliases for use in type annotations
type OutputBuilder = _OutputModule.Builder
type OutputReader = _OutputModule.Reader
type RestInputBuilder = _RestInputModule.Builder
type RestInputReader = _RestInputModule.Reader
type ResultBuilder = _ResultModule.Builder
type ResultIdEnum = (
    int
    | Literal[
        "primaryYield",
        "dryMatter",
        "carbonInAboveGroundBiomass",
        "sumFertilizer",
        "sumIrrigation",
        "primaryYieldCU",
    ]
)
type ResultReader = _ResultModule.Reader
type ResultToValueBuilder = _ResultModule._ResultToValueModule.Builder
type ResultToValueListBuilder = _ResultToValueList.Builder
type ResultToValueListReader = _ResultToValueList.Reader
type ResultToValueReader = _ResultModule._ResultToValueModule.Reader
type YearToResultBuilder = _OutputModule._YearToResultModule.Builder
type YearToResultListBuilder = _YearToResultList.Builder
type YearToResultListReader = _YearToResultList.Reader
type YearToResultReader = _OutputModule._YearToResultModule.Reader
