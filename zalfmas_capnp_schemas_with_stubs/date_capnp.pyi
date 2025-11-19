"""This is an automatically generated stub for `date.capnp`."""

from __future__ import annotations

from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicStructBuilder,
    _DynamicStructReader,
    _StructModule,
)

class _DateModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def year(self) -> int: ...
        @property
        def month(self) -> int: ...
        @property
        def day(self) -> int: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> DateBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def year(self) -> int: ...
        @year.setter
        def year(self, value: int) -> None: ...
        @property
        def month(self) -> int: ...
        @month.setter
        def month(self, value: int) -> None: ...
        @property
        def day(self) -> int: ...
        @day.setter
        def day(self, value: int) -> None: ...
        @override
        def as_reader(self) -> DateReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        year: int | None = None,
        month: int | None = None,
        day: int | None = None,
        **kwargs: Any,
    ) -> DateBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[DateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[DateReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[DateBuilder]: ...
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
    ) -> DateReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> DateReader: ...

Date: _DateModule

# Top-level type aliases for use in type annotations
type DateBuilder = _DateModule.Builder
type DateReader = _DateModule.Reader
