"""Schema helper types for `cluster_admin_service.capnp`."""

from mas.schema.cluster.cluster_admin_service_capnp.types import modules as modules

type _ClusterAdminMasterSchema = (
    modules._ClusterStructModule._AdminMasterInterfaceModule._AdminMasterSchema
)

type _ClusterModelInstanceFactorySchema = modules._ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema

type _ClusterRuntimeSchema = (
    modules._ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema
)

type _ClusterSchema = modules._ClusterStructModule._ClusterSchema

type _ClusterUnregisterSchema = (
    modules._ClusterStructModule._UnregisterInterfaceModule._UnregisterSchema
)

type _ClusterUserMasterSchema = (
    modules._ClusterStructModule._UserMasterInterfaceModule._UserMasterSchema
)

type _ClusterValueHolderSchema = (
    modules._ClusterStructModule._ValueHolderInterfaceModule._ValueHolderSchema
)

type _ClusterZmqPipelineAddressesSchema = modules._ClusterStructModule._ZmqPipelineAddressesStructModule._ZmqPipelineAddressesSchema
