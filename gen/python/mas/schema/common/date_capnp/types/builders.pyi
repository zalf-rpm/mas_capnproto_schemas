"""Builder helper types for `date.capnp`."""

from typing import override

from capnp.lib.capnp import (
    _DynamicStructBuilder,
)

from mas.schema.common.date_capnp.types import readers as readers

class DateBuilder(_DynamicStructBuilder):
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
    def as_reader(self) -> readers.DateReader: ...
