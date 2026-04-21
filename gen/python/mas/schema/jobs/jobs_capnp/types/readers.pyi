"""Reader helper types for `jobs.capnp`."""

from collections.abc import Callable
from typing import override

from capnp.lib.capnp import (
    _DynamicObjectReader,
    _DynamicStructReader,
)

from mas.schema.jobs.jobs_capnp.types import builders as builders

class JobReader(_DynamicStructReader):
    @property
    def data(self) -> _DynamicObjectReader: ...
    @property
    def noFurtherJobs(self) -> bool: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.JobBuilder: ...
