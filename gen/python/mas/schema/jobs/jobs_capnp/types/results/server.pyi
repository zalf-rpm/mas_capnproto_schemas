"""Server result helper types for `jobs.capnp`."""

from typing import Any, Literal, overload

from capnp.lib.capnp import (
    _DynamicStructBuilder,
)

from mas.schema.jobs.jobs_capnp.types import builders as builders
from mas.schema.jobs.jobs_capnp.types import readers as readers

class NextjobServerResult(_DynamicStructBuilder):
    @property
    def job(self) -> builders.JobBuilder: ...
    @job.setter
    def job(
        self,
        value: builders.JobBuilder | readers.JobReader | dict[str, Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["job"],
        size: int | None = None,
    ) -> builders.JobBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
