"""Runtime placeholder module for result tuple helpers of `a.capnp`."""

from typing import NamedTuple


class MethodResultTuple(NamedTuple):
    res: object


__all__ = ["MethodResultTuple"]
