"""Runtime placeholder module for server helpers of `cluster_admin_service.capnp`."""

from .. import Cluster

AdminMasterServer = Cluster.AdminMaster.Server
ModelInstanceFactoryServer = Cluster.ModelInstanceFactory.Server
RuntimeServer = Cluster.Runtime.Server
UnregisterServer = Cluster.Unregister.Server
UserMasterServer = Cluster.UserMaster.Server
ValueHolderServer = Cluster.ValueHolder.Server
