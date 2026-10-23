"""Module helper types for `date.capnp`."""

from collections.abc import Callable, Iterator, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _AsyncIoStream,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _StructModule,
    _StructSchema,
    _StructSchemaField,
)

from mas.schema.common.date_capnp.types import builders as builders
from mas.schema.common.date_capnp.types import readers as readers
from mas.schema.common.date_capnp.types import schemas as schemas

class _DateStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _DateSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["year"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["month"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["day"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _DateStructModule._DateSchema._Fields: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], Any] | None = None,
        year: int | None = None,
        month: int | None = None,
        day: int | None = None,
        **kwargs: object,
    ) -> builders.DateBuilder: ...
    @override
    def __call__(
        self,
        num_first_segment_words: int | None = None,
        **kwargs: object,
    ) -> builders.DateBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.DateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        builder: Literal[False] = False,
    ) -> AbstractContextManager[readers.DateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.DateBuilder]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None,
        nesting_limit: int | None,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.DateBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.DateReader: ...
    @override
    def from_segments(
        self,
        segments: Sequence[Any],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.DateReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.DateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.DateReader: ...
    @override
    async def read_async(
        self,
        stream: _AsyncIoStream,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.DateReader | None: ...
    @override
    def read_multiple(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.DateReader]: ...
    @override
    def read_multiple_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.DateReader]: ...
    @override
    def read_multiple_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.DateReader]: ...
    @override
    def read_multiple_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.DateReader]: ...
