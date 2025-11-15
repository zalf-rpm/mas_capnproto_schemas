"""This is an automatically generated stub for `date.capnp`."""

from __future__ import annotations

from typing import Any, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
    _Request,
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
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> DateBuilder: ...

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
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, year: int | None = None, month: int | None = None, day: int | None = None) -> DateBuilder: ...

Date: _DateModule

# Top-level type aliases for use in type annotations
type DateBuilder = _DateModule.Builder
type DateReader = _DateModule.Reader
