"""Runtime placeholder module for result tuple helpers of `persistence.capnp`."""

# pyright: reportUnusedClass=none

from typing import NamedTuple


class GatewayRegisterResultTuple(NamedTuple):
    sturdyRef: object
    heartbeat: object
    secsHeartbeatInterval: object


class SturdyrefatgatewayResultTuple(NamedTuple):
    selfAtGatewaySR: object


class ResolveResultTuple(NamedTuple):
    host: object
    port: object


class RegistrarRegisterResultTuple(NamedTuple):
    heartbeat: object
    secsHeartbeatInterval: object


class SaveResultTuple(NamedTuple):
    sturdyRef: object
    unsaveSR: object


class ReleaseResultTuple(NamedTuple):
    success: object


class RestoreResultTuple(NamedTuple):
    cap: object


__all__ = [
    "GatewayRegisterResultTuple",
    "RegistrarRegisterResultTuple",
    "ReleaseResultTuple",
    "ResolveResultTuple",
    "RestoreResultTuple",
    "SaveResultTuple",
    "SturdyrefatgatewayResultTuple",
]
