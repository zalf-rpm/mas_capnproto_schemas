"""Runtime placeholder module for module helper types of `persistence.capnp`."""

# pyright: reportUnusedClass=none

from __future__ import annotations

from capnp.lib.capnp import _InterfaceModule, _StructModule


class _VatIdStructModule(_StructModule):
    pass


class _AddressStructModule(_StructModule):
    pass


class _VatPathStructModule(_StructModule):
    pass


class _SturdyRefStructModule(_StructModule):
    class _OwnerStructModule(_StructModule):
        pass

    class _TokenStructModule(_StructModule):
        pass


class _HeartbeatInterfaceModule(_InterfaceModule):
    pass


class _PersistentInterfaceModule(_InterfaceModule):
    class _SaveParamsStructModule(_StructModule):
        pass

    class _SaveResultsStructModule(_StructModule):
        pass

    class _ReleaseSturdyRefInterfaceModule(_InterfaceModule):
        pass


class _RestorerInterfaceModule(_InterfaceModule):
    class _RestoreParamsStructModule(_StructModule):
        pass


class _HostPortResolverInterfaceModule(_InterfaceModule):
    class _RegistrarInterfaceModule(_InterfaceModule):
        class _RegisterParamsStructModule(_StructModule):
            pass


class _GatewayInterfaceModule(_InterfaceModule):
    class _RegResultsStructModule(_StructModule):
        pass


class _GatewayRegistrableInterfaceModule(_InterfaceModule):
    pass
