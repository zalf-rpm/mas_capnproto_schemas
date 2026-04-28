"""Module helper types for `crop.capnp`."""

from collections.abc import Awaitable
from typing import Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityServer,
    _InterfaceMethod,
    _InterfaceSchema,
    _ListSchema,
    _StructSchema,
    _StructSchemaField,
)

from mas.schema.common.common_capnp.types import (
    schemas as _mas_schema_common_common_capnp_schemas,
)
from mas.schema.common.common_capnp.types.builders import IdInformationBuilder
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.common.common_capnp.types.readers import IdInformationReader
from mas.schema.crop.crop_capnp.types import clients as clients
from mas.schema.crop.crop_capnp.types import common as common
from mas.schema.crop.crop_capnp.types import contexts as contexts
from mas.schema.crop.crop_capnp.types import schemas as schemas
from mas.schema.crop.crop_capnp.types.results import tuples as results_tuples
from mas.schema.persistence.persistence_capnp.types import (
    schemas as _mas_schema_persistence_persistence_capnp_schemas,
)
from mas.schema.persistence.persistence_capnp.types.modules import (
    _PersistentInterfaceModule,
)
from mas.schema.registry.registry_capnp.types import (
    schemas as _mas_schema_registry_registry_capnp_schemas,
)
from mas.schema.registry.registry_capnp.types.modules import _RegistryInterfaceModule

class _CropInterfaceModule(_IdentifiableInterfaceModule, _PersistentInterfaceModule):
    class _CropSchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _CropInterfaceModule._CropSchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

        class _IdentifiableInterfaceModuleInfoResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["name"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["description"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _CropInterfaceModule._CropSchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

        class _IdentifiableInterfaceModuleInfoMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _CropInterfaceModule._CropSchema._IdentifiableInterfaceModuleInfoParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _CropInterfaceModule._CropSchema._IdentifiableInterfaceModuleInfoResultSchema: ...

        class _PersistentInterfaceModuleSaveParamSchema(_StructSchema):
            class _SealForField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_persistence_persistence_capnp_schemas._SturdyRefOwnerSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["sealFor"],
                ) -> _CropInterfaceModule._CropSchema._PersistentInterfaceModuleSaveParamSchema._SealForField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _CropInterfaceModule._CropSchema._PersistentInterfaceModuleSaveParamSchema._Fields: ...

        class _PersistentInterfaceModuleSaveResultSchema(_StructSchema):
            class _SturdyRefField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> (
                    _mas_schema_persistence_persistence_capnp_schemas._SturdyRefSchema
                ): ...

            class _UnsaveSRField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> (
                    _mas_schema_persistence_persistence_capnp_schemas._SturdyRefSchema
                ): ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["sturdyRef"],
                ) -> _CropInterfaceModule._CropSchema._PersistentInterfaceModuleSaveResultSchema._SturdyRefField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["unsaveSR"],
                ) -> _CropInterfaceModule._CropSchema._PersistentInterfaceModuleSaveResultSchema._UnsaveSRField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _CropInterfaceModule._CropSchema._PersistentInterfaceModuleSaveResultSchema._Fields: ...

        class _PersistentInterfaceModuleSaveMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _CropInterfaceModule._CropSchema._PersistentInterfaceModuleSaveParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _CropInterfaceModule._CropSchema._PersistentInterfaceModuleSaveResultSchema: ...

        class _CropInterfaceModuleParametersParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _CropInterfaceModule._CropSchema._CropInterfaceModuleParametersParamSchema._Fields: ...

        class _CropInterfaceModuleParametersResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["params"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _CropInterfaceModule._CropSchema._CropInterfaceModuleParametersResultSchema._Fields: ...

        class _CropInterfaceModuleParametersMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _CropInterfaceModule._CropSchema._CropInterfaceModuleParametersParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _CropInterfaceModule._CropSchema._CropInterfaceModuleParametersResultSchema: ...

        class _CropInterfaceModuleCultivarParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _CropInterfaceModule._CropSchema._CropInterfaceModuleCultivarParamSchema._Fields: ...

        class _CropInterfaceModuleCultivarResultSchema(_StructSchema):
            class _InfoField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_common_common_capnp_schemas._IdInformationSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["info"],
                ) -> _CropInterfaceModule._CropSchema._CropInterfaceModuleCultivarResultSchema._InfoField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _CropInterfaceModule._CropSchema._CropInterfaceModuleCultivarResultSchema._Fields: ...

        class _CropInterfaceModuleCultivarMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> (
                _CropInterfaceModule._CropSchema._CropInterfaceModuleCultivarParamSchema
            ): ...
            @property
            @override
            def result_type(
                self,
            ) -> _CropInterfaceModule._CropSchema._CropInterfaceModuleCultivarResultSchema: ...

        class _CropInterfaceModuleSpeciesParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _CropInterfaceModule._CropSchema._CropInterfaceModuleSpeciesParamSchema._Fields: ...

        class _CropInterfaceModuleSpeciesResultSchema(_StructSchema):
            class _InfoField(_StructSchemaField):
                @property
                @override
                def schema(
                    self,
                ) -> _mas_schema_common_common_capnp_schemas._IdInformationSchema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["info"],
                ) -> _CropInterfaceModule._CropSchema._CropInterfaceModuleSpeciesResultSchema._InfoField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _CropInterfaceModule._CropSchema._CropInterfaceModuleSpeciesResultSchema._Fields: ...

        class _CropInterfaceModuleSpeciesMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> (
                _CropInterfaceModule._CropSchema._CropInterfaceModuleSpeciesParamSchema
            ): ...
            @property
            @override
            def result_type(
                self,
            ) -> (
                _CropInterfaceModule._CropSchema._CropInterfaceModuleSpeciesResultSchema
            ): ...

        class _Methods(dict[str, _InterfaceMethod]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> (
                _CropInterfaceModule._CropSchema._IdentifiableInterfaceModuleInfoMethod
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["save"],
            ) -> (
                _CropInterfaceModule._CropSchema._PersistentInterfaceModuleSaveMethod
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["parameters"],
            ) -> (
                _CropInterfaceModule._CropSchema._CropInterfaceModuleParametersMethod
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["cultivar"],
            ) -> (
                _CropInterfaceModule._CropSchema._CropInterfaceModuleCultivarMethod
            ): ...
            @overload
            def __getitem__(
                self,
                key: Literal["species"],
            ) -> _CropInterfaceModule._CropSchema._CropInterfaceModuleSpeciesMethod: ...
            @overload
            def __getitem__(self, key: str) -> _InterfaceMethod: ...

        @property
        @override
        def methods(self) -> _CropInterfaceModule._CropSchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._CropSchema: ...
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> clients.CropClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def parameters(
            self,
            _context: contexts.ParametersCallContext,
            **kwargs: object,
        ) -> Awaitable[
            common.AnyPointer | results_tuples.ParametersResultTuple | None
        ]: ...
        def parameters_context(
            self,
            context: contexts.ParametersCallContext,
        ) -> Awaitable[None]: ...
        def cultivar(
            self,
            _context: contexts.CultivarCallContext,
            **kwargs: object,
        ) -> Awaitable[
            IdInformationBuilder
            | IdInformationReader
            | dict[str, Any]
            | results_tuples.CultivarResultTuple
            | None
        ]: ...
        def cultivar_context(
            self,
            context: contexts.CultivarCallContext,
        ) -> Awaitable[None]: ...
        def species(
            self,
            _context: contexts.SpeciesCallContext,
            **kwargs: object,
        ) -> Awaitable[
            IdInformationBuilder
            | IdInformationReader
            | dict[str, Any]
            | results_tuples.SpeciesResultTuple
            | None
        ]: ...
        def species_context(
            self,
            context: contexts.SpeciesCallContext,
        ) -> Awaitable[None]: ...

class _ServiceInterfaceModule(_RegistryInterfaceModule):
    class _ServiceSchema(_InterfaceSchema):
        class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

        class _IdentifiableInterfaceModuleInfoResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["name"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["description"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

        class _IdentifiableInterfaceModuleInfoMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._IdentifiableInterfaceModuleInfoParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._IdentifiableInterfaceModuleInfoResultSchema: ...

        class _RegistryInterfaceModuleSupportedCategoriesParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]): ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._RegistryInterfaceModuleSupportedCategoriesParamSchema._Fields: ...

        class _RegistryInterfaceModuleSupportedCategoriesResultSchema(_StructSchema):
            class _CatsField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(
                        self,
                    ) -> (
                        _mas_schema_common_common_capnp_schemas._IdInformationSchema
                    ): ...

                @property
                @override
                def schema(
                    self,
                ) -> _ServiceInterfaceModule._ServiceSchema._RegistryInterfaceModuleSupportedCategoriesResultSchema._CatsField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["cats"],
                ) -> _ServiceInterfaceModule._ServiceSchema._RegistryInterfaceModuleSupportedCategoriesResultSchema._CatsField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._RegistryInterfaceModuleSupportedCategoriesResultSchema._Fields: ...

        class _RegistryInterfaceModuleSupportedCategoriesMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._RegistryInterfaceModuleSupportedCategoriesParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._RegistryInterfaceModuleSupportedCategoriesResultSchema: ...

        class _RegistryInterfaceModuleCategoryInfoParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["categoryId"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._RegistryInterfaceModuleCategoryInfoParamSchema._Fields: ...

        class _RegistryInterfaceModuleCategoryInfoResultSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["name"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["description"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._RegistryInterfaceModuleCategoryInfoResultSchema._Fields: ...

        class _RegistryInterfaceModuleCategoryInfoMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._RegistryInterfaceModuleCategoryInfoParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._RegistryInterfaceModuleCategoryInfoResultSchema: ...

        class _RegistryInterfaceModuleEntriesParamSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["categoryId"],
                ) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._RegistryInterfaceModuleEntriesParamSchema._Fields: ...

        class _RegistryInterfaceModuleEntriesResultSchema(_StructSchema):
            class _EntriesField(_StructSchemaField):
                class _Schema(_ListSchema):
                    @property
                    @override
                    def elementType(
                        self,
                    ) -> (
                        _mas_schema_registry_registry_capnp_schemas._RegistryEntrySchema
                    ): ...

                @property
                @override
                def schema(
                    self,
                ) -> _ServiceInterfaceModule._ServiceSchema._RegistryInterfaceModuleEntriesResultSchema._EntriesField._Schema: ...

            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["entries"],
                ) -> _ServiceInterfaceModule._ServiceSchema._RegistryInterfaceModuleEntriesResultSchema._EntriesField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._RegistryInterfaceModuleEntriesResultSchema._Fields: ...

        class _RegistryInterfaceModuleEntriesMethod(_InterfaceMethod):
            @property
            @override
            def param_type(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._RegistryInterfaceModuleEntriesParamSchema: ...
            @property
            @override
            def result_type(
                self,
            ) -> _ServiceInterfaceModule._ServiceSchema._RegistryInterfaceModuleEntriesResultSchema: ...

        class _Methods(dict[str, _InterfaceMethod]):
            @overload
            def __getitem__(
                self,
                key: Literal["info"],
            ) -> _ServiceInterfaceModule._ServiceSchema._IdentifiableInterfaceModuleInfoMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["supportedCategories"],
            ) -> _ServiceInterfaceModule._ServiceSchema._RegistryInterfaceModuleSupportedCategoriesMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["categoryInfo"],
            ) -> _ServiceInterfaceModule._ServiceSchema._RegistryInterfaceModuleCategoryInfoMethod: ...
            @overload
            def __getitem__(
                self,
                key: Literal["entries"],
            ) -> _ServiceInterfaceModule._ServiceSchema._RegistryInterfaceModuleEntriesMethod: ...
            @overload
            def __getitem__(self, key: str) -> _InterfaceMethod: ...

        @property
        @override
        def methods(self) -> _ServiceInterfaceModule._ServiceSchema._Methods: ...

    @property
    @override
    def schema(self) -> schemas._ServiceSchema: ...
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> clients.ServiceClient: ...
    class Server(_RegistryInterfaceModule.Server): ...
