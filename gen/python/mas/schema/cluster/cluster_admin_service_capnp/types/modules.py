"""Runtime placeholder module for module helper types of `cluster_admin_service.capnp`."""

# pyright: reportUnusedClass=none

from __future__ import annotations

from capnp.lib.capnp import _InterfaceModule, _StructModule


class _ClusterStructModule(_StructModule):
    class _UnregisterInterfaceModule(_InterfaceModule):
        pass

    class _AdminMasterInterfaceModule(_InterfaceModule):
        pass

    class _UserMasterInterfaceModule(_InterfaceModule):
        pass

    class _RuntimeInterfaceModule(_InterfaceModule):
        pass

    class _ZmqPipelineAddressesStructModule(_StructModule):
        pass

    class _ValueHolderInterfaceModule(_InterfaceModule):
        pass

    class _ModelInstanceFactoryInterfaceModule(_InterfaceModule):
        pass
