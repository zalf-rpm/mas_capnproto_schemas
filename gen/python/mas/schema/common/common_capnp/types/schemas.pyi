"""Schema helper types for `common.capnp`."""

from mas.schema.common.common_capnp.types import modules as modules

type _FactorySchema = modules._FactoryInterfaceModule._FactorySchema

type _IOFactorySchema = modules._IOFactoryInterfaceModule._IOFactorySchema

type _IdInformationSchema = modules._IdInformationStructModule._IdInformationSchema

type _IdentifiableHolderSchema = (
    modules._IdentifiableHolderInterfaceModule._IdentifiableHolderSchema
)

type _PairSchema = modules._PairStructModule._PairSchema

type _StructuredTextSchema = modules._StructuredTextStructModule._StructuredTextSchema

type _StructuredTextStructuredTextStructureSchema = modules._StructuredTextStructModule._StructuredTextStructureStructModule._StructuredTextStructureSchema

type _ValueSchema = modules._ValueStructModule._ValueSchema
