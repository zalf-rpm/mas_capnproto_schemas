"""Schema helper types for `grid.capnp`."""

from mas.schema.grid.grid_capnp.types import modules as modules

type _GridAggregationPartSchema = (
    modules._GridInterfaceModule._AggregationPartStructModule._AggregationPartSchema
)

type _GridCallbackSchema = (
    modules._GridInterfaceModule._CallbackInterfaceModule._CallbackSchema
)

type _GridLocationSchema = (
    modules._GridInterfaceModule._LocationStructModule._LocationSchema
)

type _GridResolutionSchema = (
    modules._GridInterfaceModule._ResolutionStructModule._ResolutionSchema
)

type _GridRowColSchema = modules._GridInterfaceModule._RowColStructModule._RowColSchema

type _GridSchema = modules._GridInterfaceModule._GridSchema

type _GridValueSchema = modules._GridInterfaceModule._ValueStructModule._ValueSchema
