"""Runtime placeholder module for result tuple helpers of `management.capnp`."""

# pyright: reportUnusedClass=none

from typing import NamedTuple


class NutrientsResultTuple(NamedTuple):
    nutrients: object


class ParametersResultTuple(NamedTuple):
    params: object


class ManagementatResultTuple(NamedTuple):
    mgmt: object


__all__ = ["ManagementatResultTuple", "NutrientsResultTuple", "ParametersResultTuple"]
