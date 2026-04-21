"""Runtime placeholder module for result tuple helpers of `crop.capnp`."""

# pyright: reportUnusedClass=none

from typing import NamedTuple


class CultivarResultTuple(NamedTuple):
    info: object


class ParametersResultTuple(NamedTuple):
    params: object


class SpeciesResultTuple(NamedTuple):
    info: object


__all__ = ["CultivarResultTuple", "ParametersResultTuple", "SpeciesResultTuple"]
