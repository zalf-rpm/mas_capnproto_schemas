"""Schema helper types for `crop.capnp`."""

from mas.schema.crop.crop_capnp.types import modules as modules

type _CropSchema = modules._CropInterfaceModule._CropSchema

type _ServiceSchema = modules._ServiceInterfaceModule._ServiceSchema
