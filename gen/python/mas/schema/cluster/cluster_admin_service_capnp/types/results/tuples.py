"""Runtime placeholder module for result tuple helpers of `cluster_admin_service.capnp`."""

from typing import NamedTuple


class AdminMasterAvailablemodelsResultTuple(NamedTuple):
    factories: object


class AdminMasterRegistermodelinstancefactoryResultTuple(NamedTuple):
    unregister: object


class ModelidResultTuple(NamedTuple):
    id: object


class NewcloudviaproxyResultTuple(NamedTuple):
    proxy: object


class NewcloudviazmqpipelineproxiesResultTuple(NamedTuple):
    proxyAddresses: object


class NewinstanceResultTuple(NamedTuple):
    instance: object


class NewinstancesResultTuple(NamedTuple):
    instances: object


class RegistermodelinstanceResultTuple(NamedTuple):
    unregister: object


class RestoresturdyrefResultTuple(NamedTuple):
    cap: object


class FreenumberofcoresResultTuple(NamedTuple):
    cores: object


class NumberofcoresResultTuple(NamedTuple):
    cores: object


class ReservenumberofcoresResultTuple(NamedTuple):
    reservedCores: object


class RuntimeAvailablemodelsResultTuple(NamedTuple):
    factories: object


class RuntimeRegistermodelinstancefactoryResultTuple(NamedTuple):
    unregister: object


class UnregisterResultTuple(NamedTuple):
    success: object


class UserMasterAvailablemodelsResultTuple(NamedTuple):
    factories: object


class ValueResultTuple(NamedTuple):
    val: object


__all__ = [
    "AdminMasterAvailablemodelsResultTuple",
    "AdminMasterRegistermodelinstancefactoryResultTuple",
    "FreenumberofcoresResultTuple",
    "ModelidResultTuple",
    "NewcloudviaproxyResultTuple",
    "NewcloudviazmqpipelineproxiesResultTuple",
    "NewinstanceResultTuple",
    "NewinstancesResultTuple",
    "NumberofcoresResultTuple",
    "RegistermodelinstanceResultTuple",
    "ReservenumberofcoresResultTuple",
    "RestoresturdyrefResultTuple",
    "RuntimeAvailablemodelsResultTuple",
    "RuntimeRegistermodelinstancefactoryResultTuple",
    "UnregisterResultTuple",
    "UserMasterAvailablemodelsResultTuple",
    "ValueResultTuple",
]
