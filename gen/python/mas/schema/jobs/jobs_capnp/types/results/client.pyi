"""Client result helper types for `jobs.capnp`."""

from collections.abc import Awaitable
from typing import Protocol

from mas.schema.jobs.jobs_capnp.types import readers as readers

class NextjobResult(Awaitable[NextjobResult], Protocol):
    job: readers.JobReader
