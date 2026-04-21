"""Runtime placeholder module for result tuple helpers of `config.capnp`."""

# pyright: reportUnusedClass=none

from typing import NamedTuple


class NextconfigResultTuple(NamedTuple):
    config: object
    noFurtherConfigs: object


__all__ = ["NextconfigResultTuple"]
