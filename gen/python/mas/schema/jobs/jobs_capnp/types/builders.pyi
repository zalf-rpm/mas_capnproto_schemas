"""Builder helper types for `jobs.capnp`."""

from typing import override

from capnp.lib.capnp import (
    _DynamicObjectReader,
    _DynamicStructBuilder,
)

from mas.schema.jobs.jobs_capnp.types import common as common
from mas.schema.jobs.jobs_capnp.types import readers as readers

class JobBuilder(_DynamicStructBuilder):
    @property
    def data(self) -> _DynamicObjectReader: ...
    @data.setter
    def data(self, value: common.AnyPointer) -> None: ...
    @property
    def noFurtherJobs(self) -> bool: ...
    @noFurtherJobs.setter
    def noFurtherJobs(self, value: bool) -> None: ...
    @override
    def as_reader(self) -> readers.JobReader: ...
