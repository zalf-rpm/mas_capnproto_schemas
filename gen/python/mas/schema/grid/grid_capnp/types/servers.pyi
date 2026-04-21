"""Server helper types for `grid.capnp`."""

from mas.schema.grid.grid_capnp.types import modules as modules

CallbackServer = modules._GridInterfaceModule._CallbackInterfaceModule.Server

GridServer = modules._GridInterfaceModule.Server
