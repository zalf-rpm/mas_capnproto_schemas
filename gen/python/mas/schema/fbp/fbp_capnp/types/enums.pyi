"""Enum helper aliases for `fbp.capnp`."""

from typing import Literal

type ChannelCloseSemanticsEnum = int | Literal["fbp", "no"]

type ComponentComponentTypeEnum = (
    int | Literal["standard", "iip", "subflow", "view", "process"]
)

type ComponentPortPortTypeEnum = int | Literal["standard", "array"]

type IPTypeEnum = int | Literal["standard", "openBracket", "closeBracket"]

type ProcessErrorInfoPhaseEnum = (
    int | Literal["unknown", "config", "read", "run", "write", "close"]
)

type ProcessStateEnum = (
    int | Literal["idle", "starting", "running", "stopping", "failed", "closed"]
)
