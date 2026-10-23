"""Common typing aliases for `fbp.capnp`."""

from typing import Literal, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicEnumField,
    _DynamicListBuilder,
    _DynamicListReader,
    _DynamicObjectBuilder,
    _DynamicObjectReader,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _StructModuleWhich,
)

# Type alias for AnyPointer parameters (accepts all Cap'n Proto pointer types)
type AnyPointer = (
    str
    | bytes
    | _DynamicStructBuilder
    | _DynamicStructReader
    | _DynamicCapabilityClient
    | _DynamicCapabilityServer
    | _DynamicListBuilder
    | _DynamicListReader
    | _DynamicObjectReader
    | _DynamicObjectBuilder
)

class _ComponentFactoryModuleWhich(_StructModuleWhich):
    none: _ComponentFactoryModuleWhich
    runnable: _ComponentFactoryModuleWhich
    process: _ComponentFactoryModuleWhich

class _ComponentFactoryWhich(_DynamicEnumField):
    @override
    def __call__(self) -> Literal["none", "runnable", "process"]: ...

class _MsgModuleWhich(_StructModuleWhich):
    Value: _MsgModuleWhich
    Done: _MsgModuleWhich
    NoMsg: _MsgModuleWhich

class _MsgWhich(_DynamicEnumField):
    @override
    def __call__(self) -> Literal["value", "done", "noMsg"]: ...

class _NameAndSRWhich(_DynamicEnumField):
    @override
    def __call__(self) -> Literal["sr", "srs"]: ...

class _SysAttributesBracketTypeModuleWhich(_StructModuleWhich):
    standard: _SysAttributesBracketTypeModuleWhich
    chunkedContent: _SysAttributesBracketTypeModuleWhich
    chunkedIp: _SysAttributesBracketTypeModuleWhich

class _SysAttributesBracketTypeWhich(_DynamicEnumField):
    @override
    def __call__(self) -> Literal["standard", "chunkedContent", "chunkedIp"]: ...
