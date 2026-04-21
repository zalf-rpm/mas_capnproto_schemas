"""Reader helper types for `yieldstat.capnp`."""

from collections.abc import Callable
from typing import override

from capnp.lib.capnp import (
    _DynamicStructReader,
)

from mas.schema.model.yieldstat.yieldstat_capnp.types import builders as builders
from mas.schema.model.yieldstat.yieldstat_capnp.types import enums as enums
from mas.schema.model.yieldstat.yieldstat_capnp.types import lists as lists

class RestInputReader(_DynamicStructReader):
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.RestInputBuilder: ...

class ResultToValueReader(_DynamicStructReader):
    @property
    def id(self) -> enums.ResultIdEnum: ...
    @property
    def value(self) -> float: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.ResultToValueBuilder: ...

class ResultReader(_DynamicStructReader):
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.ResultBuilder: ...

class YearToResultReader(_DynamicStructReader):
    @property
    def year(self) -> int: ...
    @property
    def result(self) -> ResultReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.YearToResultBuilder: ...

class OutputReader(_DynamicStructReader):
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.OutputBuilder: ...

type ResultToValueListReader = lists._ResultToValueList.Reader

type YearToResultListReader = lists._YearToResultList.Reader
