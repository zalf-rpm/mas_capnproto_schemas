"""Module helper types for `yieldstat.capnp`."""

from collections.abc import Callable
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicStructBuilder,
    _DynamicStructReader,
    _EnumModule,
    _EnumSchema,
    _ListSchema,
    _StructModule,
    _StructSchema,
    _StructSchemaField,
)

from mas.schema.model.yieldstat.yieldstat_capnp.types import builders as builders
from mas.schema.model.yieldstat.yieldstat_capnp.types import enums as enums
from mas.schema.model.yieldstat.yieldstat_capnp.types import readers as readers
from mas.schema.model.yieldstat.yieldstat_capnp.types import schemas as schemas

class _ResultIdEnumModule(_EnumModule):
    primaryYield: int
    dryMatter: int
    carbonInAboveGroundBiomass: int
    sumFertilizer: int
    sumIrrigation: int
    primaryYieldCU: int

    class _ResultIdSchema(_EnumSchema): ...

    @property
    @override
    def schema(self) -> schemas._ResultIdEnumSchema: ...

class _RestInputStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _RestInputSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["useDevTrend"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["useCO2Increase"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["dgm"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["hft"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["nft"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["sft"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["slope"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["steino"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["az"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["klz"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["stt"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["germanFederalStates"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["getDryYearWaterNeed"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _RestInputStructModule._RestInputSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._RestInputSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
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
        **kwargs: object,
    ) -> builders.RestInputBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.RestInputReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.RestInputReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.RestInputBuilder]: ...
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
    ) -> readers.RestInputReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.RestInputReader: ...

class _ResultStructModule(_StructModule):
    class _ResultToValueStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _ResultToValueSchema(_StructSchema):
            class _IdField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._ResultIdEnumSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["id"],
                ) -> _ResultStructModule._ResultToValueStructModule._ResultToValueSchema._IdField: ...
                @overload
                def __getitem__(self, key: Literal["value"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ResultStructModule._ResultToValueStructModule._ResultToValueSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._ResultResultToValueSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            id: enums.ResultIdEnum | None = None,
            value: float | None = None,
            **kwargs: object,
        ) -> builders.ResultToValueBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.ResultToValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.ResultToValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.ResultToValueBuilder]: ...
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
        ) -> readers.ResultToValueReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.ResultToValueReader: ...

    ResultToValue: _ResultToValueStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _ResultSchema(_StructSchema):
        class _ValuesField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._ResultResultToValueSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _ResultStructModule._ResultSchema._ValuesField._Schema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["cultivar"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["isNoData"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["values"],
            ) -> _ResultStructModule._ResultSchema._ValuesField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _ResultStructModule._ResultSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._ResultSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        cultivar: str | None = None,
        isNoData: bool | None = None,
        values: builders.ResultToValueListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> builders.ResultBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.ResultReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.ResultReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.ResultBuilder]: ...
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
    ) -> readers.ResultReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.ResultReader: ...

class _OutputStructModule(_StructModule):
    class _YearToResultStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _YearToResultSchema(_StructSchema):
            class _ResultField(_StructSchemaField):
                @property
                @override
                def schema(self) -> schemas._ResultSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["year"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["result"],
                ) -> _OutputStructModule._YearToResultStructModule._YearToResultSchema._ResultField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _OutputStructModule._YearToResultStructModule._YearToResultSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._OutputYearToResultSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            year: int | None = None,
            result: builders.ResultBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> builders.YearToResultBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.YearToResultReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.YearToResultReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.YearToResultBuilder]: ...
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
        ) -> readers.YearToResultReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.YearToResultReader: ...

    YearToResult: _YearToResultStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _OutputSchema(_StructSchema):
        class _ResultsField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._OutputYearToResultSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _OutputStructModule._OutputSchema._ResultsField._Schema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["runFailed"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["reason"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["results"],
            ) -> _OutputStructModule._OutputSchema._ResultsField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _OutputStructModule._OutputSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._OutputSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        id: str | None = None,
        runFailed: bool | None = None,
        reason: str | None = None,
        results: builders.YearToResultListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> builders.OutputBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.OutputReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.OutputReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.OutputBuilder]: ...
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
    ) -> readers.OutputReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.OutputReader: ...
