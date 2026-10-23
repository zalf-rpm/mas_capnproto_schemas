"""Common typing aliases for `geo.capnp`."""

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

class _CoordModuleWhich(_StructModuleWhich):
    Gk: _CoordModuleWhich
    Latlon: _CoordModuleWhich
    Utm: _CoordModuleWhich
    P2D: _CoordModuleWhich
    Rowcol: _CoordModuleWhich

class _CoordWhich(_DynamicEnumField):
    @override
    def __call__(self) -> Literal["gk", "latlon", "utm", "p2D", "rowcol"]: ...
