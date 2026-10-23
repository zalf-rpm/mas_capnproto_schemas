"""Enum helper aliases for `fbp.capnp`."""

from typing import Literal, override

from capnp.lib.capnp import _DynamicEnum

class IPTypeValue(_DynamicEnum):
    @override
    def __str__(self) -> Literal["standard", "openBracket", "closeBracket"]: ...

class LogMessageLevelValue(_DynamicEnum):
    @override
    def __str__(self) -> Literal["debug", "info", "warning", "error", "critical"]: ...

class ChannelCloseSemanticsValue(_DynamicEnum):
    @override
    def __str__(self) -> Literal["fbp", "no"]: ...

class ComponentComponentTypeValue(_DynamicEnum):
    @override
    def __str__(self) -> Literal["standard", "iip", "subflow", "view", "process"]: ...

class ComponentPortPortTypeValue(_DynamicEnum):
    @override
    def __str__(self) -> Literal["standard", "array"]: ...

class ComponentPortPortRoleValue(_DynamicEnum):
    @override
    def __str__(
        self,
    ) -> Literal["data", "config", "log", "error", "reject", "control"]: ...

class ProcessStateValue(_DynamicEnum):
    @override
    def __str__(
        self,
    ) -> Literal["idle", "starting", "running", "stopping", "failed"]: ...

class ProcessActivityStateValue(_DynamicEnum):
    @override
    def __str__(
        self,
    ) -> Literal["none", "waitingInput", "processing", "waitingOutput", "closing"]: ...

class ProcessRunInfoOutcomeValue(_DynamicEnum):
    @override
    def __str__(self) -> Literal["none", "completed", "stopped", "failed"]: ...

class ProcessRunInfoPhaseValue(_DynamicEnum):
    @override
    def __str__(
        self,
    ) -> Literal["unknown", "config", "read", "run", "write", "close"]: ...

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
