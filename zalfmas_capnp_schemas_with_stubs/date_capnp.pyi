"""This is an automatically generated stub for `date.capnp`."""

from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager
from io import BufferedWriter
from typing import Any, BinaryIO, TypeAlias

DateBuilder: TypeAlias = Date.Builder
DateReader: TypeAlias = Date.Reader

class Date:
    class Reader:
        @property
        def year(self) -> int: ...
        @property
        def month(self) -> int: ...
        @property
        def day(self) -> int: ...
        def as_builder(self) -> Date.Builder: ...

    class Builder:
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
        @staticmethod
        def from_dict(dictionary: dict[str, Any]) -> Date.Builder: ...
        def copy(self) -> Date.Builder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> Date.Reader: ...
        @staticmethod
        def write(file: BufferedWriter) -> None: ...
        @staticmethod
        def write_packed(file: BufferedWriter) -> None: ...

    @contextmanager
    @staticmethod
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[Date.Reader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Date.Reader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        year: int | None = None,
        month: int | None = None,
        day: int | None = None,
    ) -> Date.Builder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Date.Reader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Date.Reader: ...
    def to_dict(self) -> dict[str, Any]: ...
