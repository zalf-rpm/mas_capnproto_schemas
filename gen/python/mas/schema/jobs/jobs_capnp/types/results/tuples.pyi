"""Result tuple helper types for `jobs.capnp`."""

from typing import Any, NamedTuple

from mas.schema.jobs.jobs_capnp.types import builders as builders
from mas.schema.jobs.jobs_capnp.types import readers as readers

class NextjobResultTuple(NamedTuple):
    job: builders.JobBuilder | readers.JobReader | dict[str, Any]
