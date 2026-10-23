"""Common typing aliases for `persistence.capnp`."""

from typing import Literal, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicEnumField,
    _DynamicObjectBuilder,
    _DynamicObjectReader,
    _StructModuleWhich,
)

# Type alias for Capability parameters
type Capability = (
    _DynamicCapabilityClient
    | _DynamicCapabilityServer
    | _DynamicObjectReader
    | _DynamicObjectBuilder
)

class _AddressWhich(_DynamicEnumField):
    @override
    def __call__(self) -> Literal["ip6", "host"]: ...

class _TokenModuleWhich(_StructModuleWhich):
    Text: _TokenModuleWhich
    Data: _TokenModuleWhich

class _TokenWhich(_DynamicEnumField):
    @override
    def __call__(self) -> Literal["text", "data"]: ...
