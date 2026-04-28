"""Common typing aliases for `persistence.capnp`."""

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicObjectBuilder,
    _DynamicObjectReader,
)

# Type alias for Capability parameters
type Capability = (
    _DynamicCapabilityClient
    | _DynamicCapabilityServer
    | _DynamicObjectReader
    | _DynamicObjectBuilder
)
