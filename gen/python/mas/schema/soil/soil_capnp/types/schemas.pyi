"""Schema helper types for `soil.capnp`."""

from mas.schema.soil.soil_capnp.types import modules as modules

type _LayerPropertySchema = (
    modules._LayerStructModule._PropertyStructModule._PropertySchema
)

type _LayerSchema = modules._LayerStructModule._LayerSchema

type _ProfileDataSchema = modules._ProfileDataStructModule._ProfileDataSchema

type _ProfileSchema = modules._ProfileInterfaceModule._ProfileSchema

type _QueryResultSchema = modules._QueryStructModule._ResultStructModule._ResultSchema

type _QuerySchema = modules._QueryStructModule._QuerySchema

type _ServiceSchema = modules._ServiceInterfaceModule._ServiceSchema

type _ServiceStreamSchema = (
    modules._ServiceInterfaceModule._StreamInterfaceModule._StreamSchema
)
