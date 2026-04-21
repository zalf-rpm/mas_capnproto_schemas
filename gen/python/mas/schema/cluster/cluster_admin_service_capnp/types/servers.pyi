"""Server helper types for `cluster_admin_service.capnp`."""

from mas.schema.cluster.cluster_admin_service_capnp.types import modules as modules

AdminMasterServer = modules._ClusterStructModule._AdminMasterInterfaceModule.Server

ModelInstanceFactoryServer = (
    modules._ClusterStructModule._ModelInstanceFactoryInterfaceModule.Server
)

RuntimeServer = modules._ClusterStructModule._RuntimeInterfaceModule.Server

UnregisterServer = modules._ClusterStructModule._UnregisterInterfaceModule.Server

UserMasterServer = modules._ClusterStructModule._UserMasterInterfaceModule.Server

ValueHolderServer = modules._ClusterStructModule._ValueHolderInterfaceModule.Server
