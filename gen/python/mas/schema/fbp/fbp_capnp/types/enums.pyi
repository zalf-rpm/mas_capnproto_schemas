"""Enum helper aliases for `fbp.capnp`."""

from typing import Literal

type ChannelCloseSemanticsEnum = int | Literal["fbp", "no"]

type ComponentComponentTypeEnum = (
    int | Literal["standard", "iip", "subflow", "view", "process"]
)

type ComponentPortPortTypeEnum = int | Literal["standard", "array"]

type IPTypeEnum = int | Literal["standard", "openBracket", "closeBracket"]

type ProcessStateEnum = (
    int | Literal["idle", "starting", "running", "stopping", "failed", "closed"]
)

type ProcessStopModeEnum = int | Literal["soft", "hard"]
