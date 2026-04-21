"""Server helper types for `crop.capnp`."""

from mas.schema.crop.crop_capnp.types import modules as modules

CropServer = modules._CropInterfaceModule.Server

ServiceServer = modules._ServiceInterfaceModule.Server
