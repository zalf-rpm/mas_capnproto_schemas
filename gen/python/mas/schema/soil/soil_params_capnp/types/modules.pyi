"""Module helper types for `soil_params.capnp`."""

from collections.abc import Callable, Iterator, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _AsyncIoStream,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _ListSchema,
    _StructModule,
    _StructSchema,
    _StructSchemaField,
)

from mas.schema.soil.soil_params_capnp.types import builders as builders
from mas.schema.soil.soil_params_capnp.types import readers as readers
from mas.schema.soil.soil_params_capnp.types import schemas as schemas

class _SoilCharacteristicDataStructModule(_StructModule):
    class _DataStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _DataSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["soilType"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["soilRawDensity"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["airCapacity"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["fieldCapacity"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["nFieldCapacity"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _SoilCharacteristicDataStructModule._DataStructModule._DataSchema._Fields: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], Any] | None = None,
            soilType: str | None = None,
            soilRawDensity: int | None = None,
            airCapacity: int | None = None,
            fieldCapacity: int | None = None,
            nFieldCapacity: int | None = None,
            **kwargs: object,
        ) -> builders.SoilCharacteristicDataDataBuilder: ...
        @override
        def __call__(
            self,
            num_first_segment_words: int | None = None,
            **kwargs: object,
        ) -> builders.SoilCharacteristicDataDataBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.SoilCharacteristicDataDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            builder: Literal[False] = False,
        ) -> AbstractContextManager[readers.SoilCharacteristicDataDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.SoilCharacteristicDataDataBuilder]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None,
            nesting_limit: int | None,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.SoilCharacteristicDataDataBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.SoilCharacteristicDataDataReader: ...
        @override
        def from_segments(
            self,
            segments: Sequence[Any],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.SoilCharacteristicDataDataReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.SoilCharacteristicDataDataReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.SoilCharacteristicDataDataReader: ...
        @override
        async def read_async(
            self,
            stream: _AsyncIoStream,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.SoilCharacteristicDataDataReader | None: ...
        @override
        def read_multiple(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.SoilCharacteristicDataDataReader]: ...
        @override
        def read_multiple_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.SoilCharacteristicDataDataReader]: ...
        @override
        def read_multiple_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.SoilCharacteristicDataDataReader]: ...
        @override
        def read_multiple_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.SoilCharacteristicDataDataReader]: ...

    Data: _DataStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _SoilCharacteristicDataSchema(_StructSchema):
        class _ListField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._SoilCharacteristicDataDataSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _SoilCharacteristicDataStructModule._SoilCharacteristicDataSchema._ListField._Schema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["list"],
            ) -> _SoilCharacteristicDataStructModule._SoilCharacteristicDataSchema._ListField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> (
            _SoilCharacteristicDataStructModule._SoilCharacteristicDataSchema._Fields
        ): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], Any] | None = None,
        list: builders.DataListBuilder
        | readers.DataListReader
        | Sequence[
            _SoilCharacteristicDataStructModule._DataStructModule.Reader
            | _SoilCharacteristicDataStructModule._DataStructModule.Builder
            | dict[str, Any]
        ]
        | None = None,
        **kwargs: object,
    ) -> builders.SoilCharacteristicDataBuilder: ...
    @override
    def __call__(
        self,
        num_first_segment_words: int | None = None,
        **kwargs: object,
    ) -> builders.SoilCharacteristicDataBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.SoilCharacteristicDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        builder: Literal[False] = False,
    ) -> AbstractContextManager[readers.SoilCharacteristicDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.SoilCharacteristicDataBuilder]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None,
        nesting_limit: int | None,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.SoilCharacteristicDataBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SoilCharacteristicDataReader: ...
    @override
    def from_segments(
        self,
        segments: Sequence[Any],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SoilCharacteristicDataReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SoilCharacteristicDataReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SoilCharacteristicDataReader: ...
    @override
    async def read_async(
        self,
        stream: _AsyncIoStream,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SoilCharacteristicDataReader | None: ...
    @override
    def read_multiple(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.SoilCharacteristicDataReader]: ...
    @override
    def read_multiple_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.SoilCharacteristicDataReader]: ...
    @override
    def read_multiple_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.SoilCharacteristicDataReader]: ...
    @override
    def read_multiple_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.SoilCharacteristicDataReader]: ...

class _SoilCharacteristicModifierStructModule(_StructModule):
    class _DataStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _DataSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["soilType"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["organicMatter"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["airCapacity"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["fieldCapacity"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["nFieldCapacity"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _SoilCharacteristicModifierStructModule._DataStructModule._DataSchema._Fields: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], Any] | None = None,
            soilType: str | None = None,
            organicMatter: float | None = None,
            airCapacity: int | None = None,
            fieldCapacity: int | None = None,
            nFieldCapacity: int | None = None,
            **kwargs: object,
        ) -> builders.SoilCharacteristicModifierDataBuilder: ...
        @override
        def __call__(
            self,
            num_first_segment_words: int | None = None,
            **kwargs: object,
        ) -> builders.SoilCharacteristicModifierDataBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.SoilCharacteristicModifierDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            builder: Literal[False] = False,
        ) -> AbstractContextManager[readers.SoilCharacteristicModifierDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.SoilCharacteristicModifierDataBuilder]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None,
            nesting_limit: int | None,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.SoilCharacteristicModifierDataBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.SoilCharacteristicModifierDataReader: ...
        @override
        def from_segments(
            self,
            segments: Sequence[Any],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.SoilCharacteristicModifierDataReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.SoilCharacteristicModifierDataReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.SoilCharacteristicModifierDataReader: ...
        @override
        async def read_async(
            self,
            stream: _AsyncIoStream,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.SoilCharacteristicModifierDataReader | None: ...
        @override
        def read_multiple(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.SoilCharacteristicModifierDataReader]: ...
        @override
        def read_multiple_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.SoilCharacteristicModifierDataReader]: ...
        @override
        def read_multiple_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.SoilCharacteristicModifierDataReader]: ...
        @override
        def read_multiple_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.SoilCharacteristicModifierDataReader]: ...

    Data: _DataStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _SoilCharacteristicModifierSchema(_StructSchema):
        class _ListField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(
                    self,
                ) -> schemas._SoilCharacteristicModifierDataSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _SoilCharacteristicModifierStructModule._SoilCharacteristicModifierSchema._ListField._Schema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["list"],
            ) -> _SoilCharacteristicModifierStructModule._SoilCharacteristicModifierSchema._ListField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _SoilCharacteristicModifierStructModule._SoilCharacteristicModifierSchema._Fields: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], Any] | None = None,
        list: builders.DataListBuilder
        | readers.DataListReader
        | Sequence[
            _SoilCharacteristicModifierStructModule._DataStructModule.Reader
            | _SoilCharacteristicModifierStructModule._DataStructModule.Builder
            | dict[str, Any]
        ]
        | None = None,
        **kwargs: object,
    ) -> builders.SoilCharacteristicModifierBuilder: ...
    @override
    def __call__(
        self,
        num_first_segment_words: int | None = None,
        **kwargs: object,
    ) -> builders.SoilCharacteristicModifierBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.SoilCharacteristicModifierReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        builder: Literal[False] = False,
    ) -> AbstractContextManager[readers.SoilCharacteristicModifierReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.SoilCharacteristicModifierBuilder]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None,
        nesting_limit: int | None,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.SoilCharacteristicModifierBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SoilCharacteristicModifierReader: ...
    @override
    def from_segments(
        self,
        segments: Sequence[Any],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SoilCharacteristicModifierReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SoilCharacteristicModifierReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SoilCharacteristicModifierReader: ...
    @override
    async def read_async(
        self,
        stream: _AsyncIoStream,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.SoilCharacteristicModifierReader | None: ...
    @override
    def read_multiple(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.SoilCharacteristicModifierReader]: ...
    @override
    def read_multiple_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.SoilCharacteristicModifierReader]: ...
    @override
    def read_multiple_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.SoilCharacteristicModifierReader]: ...
    @override
    def read_multiple_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.SoilCharacteristicModifierReader]: ...

class _CapillaryRiseRateStructModule(_StructModule):
    class _DataStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _DataSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["soilType"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["distance"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["rate"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> (
                _CapillaryRiseRateStructModule._DataStructModule._DataSchema._Fields
            ): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], Any] | None = None,
            soilType: str | None = None,
            distance: int | None = None,
            rate: float | None = None,
            **kwargs: object,
        ) -> builders.CapillaryRiseRateDataBuilder: ...
        @override
        def __call__(
            self,
            num_first_segment_words: int | None = None,
            **kwargs: object,
        ) -> builders.CapillaryRiseRateDataBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.CapillaryRiseRateDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            builder: Literal[False] = False,
        ) -> AbstractContextManager[readers.CapillaryRiseRateDataReader]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.CapillaryRiseRateDataBuilder]: ...
        @overload
        def from_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None,
            nesting_limit: int | None,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.CapillaryRiseRateDataBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.CapillaryRiseRateDataReader: ...
        @override
        def from_segments(
            self,
            segments: Sequence[Any],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.CapillaryRiseRateDataReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.CapillaryRiseRateDataReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.CapillaryRiseRateDataReader: ...
        @override
        async def read_async(
            self,
            stream: _AsyncIoStream,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.CapillaryRiseRateDataReader | None: ...
        @override
        def read_multiple(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.CapillaryRiseRateDataReader]: ...
        @override
        def read_multiple_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            skip_copy: bool = False,
        ) -> Iterator[readers.CapillaryRiseRateDataReader]: ...
        @override
        def read_multiple_bytes(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.CapillaryRiseRateDataReader]: ...
        @override
        def read_multiple_bytes_packed(
            self,
            buf: Any,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> Iterator[readers.CapillaryRiseRateDataReader]: ...

    Data: _DataStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _CapillaryRiseRateSchema(_StructSchema):
        class _ListField(_StructSchemaField):
            class _Schema(_ListSchema):
                @property
                @override
                def elementType(self) -> schemas._CapillaryRiseRateDataSchema: ...

            @property
            @override
            def schema(
                self,
            ) -> _CapillaryRiseRateStructModule._CapillaryRiseRateSchema._ListField._Schema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["list"],
            ) -> _CapillaryRiseRateStructModule._CapillaryRiseRateSchema._ListField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(
            self,
        ) -> _CapillaryRiseRateStructModule._CapillaryRiseRateSchema._Fields: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], Any] | None = None,
        list: builders.DataListBuilder
        | readers.DataListReader
        | Sequence[
            _CapillaryRiseRateStructModule._DataStructModule.Reader
            | _CapillaryRiseRateStructModule._DataStructModule.Builder
            | dict[str, Any]
        ]
        | None = None,
        **kwargs: object,
    ) -> builders.CapillaryRiseRateBuilder: ...
    @override
    def __call__(
        self,
        num_first_segment_words: int | None = None,
        **kwargs: object,
    ) -> builders.CapillaryRiseRateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.CapillaryRiseRateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        builder: Literal[False] = False,
    ) -> AbstractContextManager[readers.CapillaryRiseRateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.CapillaryRiseRateBuilder]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None,
        nesting_limit: int | None,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.CapillaryRiseRateBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.CapillaryRiseRateReader: ...
    @override
    def from_segments(
        self,
        segments: Sequence[Any],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.CapillaryRiseRateReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.CapillaryRiseRateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.CapillaryRiseRateReader: ...
    @override
    async def read_async(
        self,
        stream: _AsyncIoStream,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.CapillaryRiseRateReader | None: ...
    @override
    def read_multiple(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.CapillaryRiseRateReader]: ...
    @override
    def read_multiple_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.CapillaryRiseRateReader]: ...
    @override
    def read_multiple_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.CapillaryRiseRateReader]: ...
    @override
    def read_multiple_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.CapillaryRiseRateReader]: ...
