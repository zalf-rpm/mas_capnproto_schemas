"""Schema helper types for `modam.capnp`."""

from mas.schema.dakis.modam.modam_capnp.types import modules as modules

type _ModamWrapperServiceSchema = (
    modules._ModamWrapperServiceInterfaceModule._ModamWrapperServiceSchema
)
