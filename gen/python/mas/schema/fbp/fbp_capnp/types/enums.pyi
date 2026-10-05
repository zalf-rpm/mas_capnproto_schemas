"""Enum helper aliases for `fbp.capnp`."""

from typing import Literal

type ChannelCloseSemanticsEnum = int | Literal["fbp", "no"]

type ComponentComponentTypeEnum = (
    int | Literal["standard", "iip", "subflow", "view", "process"]
)

type ComponentPortPortRoleEnum = (
    int | Literal["data", "config", "log", "error", "reject", "control"]
)

type ComponentPortPortTypeEnum = int | Literal["standard", "array"]

type IPTypeEnum = int | Literal["standard", "openBracket", "closeBracket"]

type LogMessageLevelEnum = (
    int | Literal["debug", "info", "warning", "error", "critical"]
)

type ProcessActivityStateEnum = (
    int | Literal["none", "waitingInput", "processing", "waitingOutput", "closing"]
)

type ProcessRunInfoOutcomeEnum = int | Literal["none", "completed", "stopped", "failed"]

type ProcessRunInfoPhaseEnum = (
    int | Literal["unknown", "config", "read", "run", "write", "close"]
)

type ProcessStateEnum = (
    int | Literal["idle", "starting", "running", "stopping", "failed"]
)
