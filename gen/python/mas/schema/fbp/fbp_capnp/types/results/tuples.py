"""Runtime placeholder module for result tuple helpers of `fbp.capnp`."""

# pyright: reportUnusedClass=none

from typing import NamedTuple


class EndpointsResultTuple(NamedTuple):
    r: object
    w: object


class ReaderResultTuple(NamedTuple):
    r: object


class RegisterstatscallbackResultTuple(NamedTuple):
    unregisterCallback: object


class WriterResultTuple(NamedTuple):
    w: object


class ReadResultTuple(NamedTuple):
    value: object
    done: object
    noMsg: object


class ReadifmsgResultTuple(NamedTuple):
    value: object
    done: object
    noMsg: object


class UnregResultTuple(NamedTuple):
    success: object


class WriteifspaceResultTuple(NamedTuple):
    success: object


class ConfigentriesResultTuple(NamedTuple):
    config: object


class ConnectinportResultTuple(NamedTuple):
    connected: object


class ConnectoutportResultTuple(NamedTuple):
    connected: object


class InportsResultTuple(NamedTuple):
    ports: object


class OutportsResultTuple(NamedTuple):
    ports: object


class StateResultTuple(NamedTuple):
    currentState: object


class ProcessFactoryCreateResultTuple(NamedTuple):
    out: object


class RunnableStartResultTuple(NamedTuple):
    success: object


class RunnableStopResultTuple(NamedTuple):
    success: object


class RunnableFactoryCreateResultTuple(NamedTuple):
    out: object


class StartChannelsServiceStartResultTuple(NamedTuple):
    startupInfos: object
    stop: object


__all__ = [
    "ConfigentriesResultTuple",
    "ConnectinportResultTuple",
    "ConnectoutportResultTuple",
    "EndpointsResultTuple",
    "InportsResultTuple",
    "OutportsResultTuple",
    "ProcessFactoryCreateResultTuple",
    "ReadResultTuple",
    "ReaderResultTuple",
    "ReadifmsgResultTuple",
    "RegisterstatscallbackResultTuple",
    "RunnableFactoryCreateResultTuple",
    "RunnableStartResultTuple",
    "RunnableStopResultTuple",
    "StartChannelsServiceStartResultTuple",
    "StateResultTuple",
    "UnregResultTuple",
    "WriteifspaceResultTuple",
    "WriterResultTuple",
]
