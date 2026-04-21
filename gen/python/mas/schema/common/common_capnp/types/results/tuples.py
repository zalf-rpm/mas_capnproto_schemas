"""Runtime placeholder module for result tuple helpers of `common.capnp`."""

# pyright: reportUnusedClass=none

from typing import NamedTuple


class CreateResultTuple(NamedTuple):
    out: object


class ValueResultTuple(NamedTuple):
    value: object


class ProduceResultTuple(NamedTuple):
    out: object


class InfoResultTuple(NamedTuple):
    id: object
    name: object
    description: object


__all__ = [
    "CreateResultTuple",
    "InfoResultTuple",
    "ProduceResultTuple",
    "ValueResultTuple",
]
