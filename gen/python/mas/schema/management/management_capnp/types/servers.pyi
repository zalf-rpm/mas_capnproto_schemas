"""Server helper types for `management.capnp`."""

from mas.schema.management.management_capnp.types import modules as modules

FertilizerServer = modules._FertilizerInterfaceModule.Server

FertilizerServiceServer = modules._FertilizerServiceInterfaceModule.Server

ServiceServer = modules._ServiceInterfaceModule.Server
