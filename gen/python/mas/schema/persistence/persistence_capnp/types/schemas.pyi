"""Schema helper types for `persistence.capnp`."""

from mas.schema.persistence.persistence_capnp.types import modules as modules

type _AddressAddressIp6Schema = (
    modules._AddressStructModule._AddressIp6StructModule._AddressIp6Schema
)

type _AddressSchema = modules._AddressStructModule._AddressSchema

type _GatewayRegResultsSchema = (
    modules._GatewayInterfaceModule._RegResultsStructModule._RegResultsSchema
)

type _GatewaySchema = modules._GatewayInterfaceModule._GatewaySchema

type _HeartbeatSchema = modules._HeartbeatInterfaceModule._HeartbeatSchema

type _HostPortResolverRegistrarRegisterParamsSchema = modules._HostPortResolverInterfaceModule._RegistrarInterfaceModule._RegisterParamsStructModule._RegisterParamsSchema

type _HostPortResolverRegistrarSchema = (
    modules._HostPortResolverInterfaceModule._RegistrarInterfaceModule._RegistrarSchema
)

type _HostPortResolverSchema = (
    modules._HostPortResolverInterfaceModule._HostPortResolverSchema
)

type _PersistentReleaseSturdyRefSchema = modules._PersistentInterfaceModule._ReleaseSturdyRefInterfaceModule._ReleaseSturdyRefSchema

type _PersistentSaveParamsSchema = (
    modules._PersistentInterfaceModule._SaveParamsStructModule._SaveParamsSchema
)

type _PersistentSaveResultsSchema = (
    modules._PersistentInterfaceModule._SaveResultsStructModule._SaveResultsSchema
)

type _RestorerRestoreParamsSchema = (
    modules._RestorerInterfaceModule._RestoreParamsStructModule._RestoreParamsSchema
)

type _SturdyRefOwnerSchema = (
    modules._SturdyRefStructModule._OwnerStructModule._OwnerSchema
)

type _SturdyRefSchema = modules._SturdyRefStructModule._SturdyRefSchema

type _SturdyRefTokenSchema = (
    modules._SturdyRefStructModule._TokenStructModule._TokenSchema
)

type _VatIdSchema = modules._VatIdStructModule._VatIdSchema

type _VatPathSchema = modules._VatPathStructModule._VatPathSchema
