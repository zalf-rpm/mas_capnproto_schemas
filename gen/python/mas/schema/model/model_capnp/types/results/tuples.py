"""Runtime placeholder module for result tuple helpers of `model.capnp`."""

# pyright: reportUnusedClass=none

from typing import NamedTuple


class ClimateInstanceRunResultTuple(NamedTuple):
    result: object


class RunsetResultTuple(NamedTuple):
    result: object


class EnvInstanceRunResultTuple(NamedTuple):
    result: object


class RegisterenvinstanceResultTuple(NamedTuple):
    unregister: object


class UnregisterResultTuple(NamedTuple):
    success: object


class ModelinfoResultTuple(NamedTuple):
    id: object
    name: object
    description: object


class NewinstanceResultTuple(NamedTuple):
    instance: object


class NewinstancesResultTuple(NamedTuple):
    instances: object


__all__ = [
    "ClimateInstanceRunResultTuple",
    "EnvInstanceRunResultTuple",
    "ModelinfoResultTuple",
    "NewinstanceResultTuple",
    "NewinstancesResultTuple",
    "RegisterenvinstanceResultTuple",
    "RunsetResultTuple",
    "UnregisterResultTuple",
]
