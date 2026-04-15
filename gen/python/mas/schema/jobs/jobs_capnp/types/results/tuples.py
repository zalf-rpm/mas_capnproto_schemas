"""Runtime placeholder module for result tuple helpers of `jobs.capnp`."""

from typing import NamedTuple


class NextjobResultTuple(NamedTuple):
    job: object


__all__ = ["NextjobResultTuple"]
