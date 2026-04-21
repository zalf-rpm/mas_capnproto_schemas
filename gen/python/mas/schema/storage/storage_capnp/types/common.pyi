"""Common typing aliases for `storage.capnp`."""

from capnp.lib.capnp import (
    _DynamicObjectBuilder,
    _DynamicObjectReader,
    _DynamicStructBuilder,
    _DynamicStructReader,
)

# Type alias for AnyStruct parameters
type AnyStruct = (
    _DynamicStructBuilder
    | _DynamicStructReader
    | _DynamicObjectReader
    | _DynamicObjectBuilder
)
