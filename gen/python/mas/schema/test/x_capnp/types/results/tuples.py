"""Runtime placeholder module for result tuple helpers of `x.capnp`."""

from typing import NamedTuple


class XMResultTuple(NamedTuple):
    t: object


class ZMResultTuple(NamedTuple):
    r: object


__all__ = ["XMResultTuple", "ZMResultTuple"]
