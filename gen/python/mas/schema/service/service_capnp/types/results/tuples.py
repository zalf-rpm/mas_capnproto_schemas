"""Runtime placeholder module for result tuple helpers of `service.capnp`."""

from typing import NamedTuple


class IdentitiesResultTuple(NamedTuple):
    infos: object


class FactoryCreateResultTuple(NamedTuple):
    adminCap: object
    serviceCaps: object
    error: object


class ServiceinterfacenamesResultTuple(NamedTuple):
    names: object


class SimpleFactoryCreateResultTuple(NamedTuple):
    caps: object


class StoppableStopResultTuple(NamedTuple):
    success: object


__all__ = [
    "FactoryCreateResultTuple",
    "IdentitiesResultTuple",
    "ServiceinterfacenamesResultTuple",
    "SimpleFactoryCreateResultTuple",
    "StoppableStopResultTuple",
]
