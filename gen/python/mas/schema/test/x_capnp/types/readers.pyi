"""Reader helper types for `x.capnp`."""

from collections.abc import Callable
from typing import override

from capnp.lib.capnp import (
    _DynamicStructReader,
)

from mas.schema.test.x_capnp.types import builders as builders
from mas.schema.test.x_capnp.types import clients as clients

class SReader(_DynamicStructReader):
    @property
    def c(self) -> clients.XClient: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.SBuilder: ...
