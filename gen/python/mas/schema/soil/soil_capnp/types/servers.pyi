"""Server helper types for `soil.capnp`."""

from mas.schema.soil.soil_capnp.types import modules as modules

ProfileServer = modules._ProfileInterfaceModule.Server

ServiceServer = modules._ServiceInterfaceModule.Server

StreamServer = modules._ServiceInterfaceModule._StreamInterfaceModule.Server
