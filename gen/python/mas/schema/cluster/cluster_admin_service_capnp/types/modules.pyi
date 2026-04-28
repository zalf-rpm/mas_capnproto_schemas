"""Module helper types for `cluster_admin_service.capnp`."""

from collections.abc import Awaitable, Callable, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityServer,
    _DynamicObjectReader,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceMethod,
    _InterfaceModule,
    _InterfaceSchema,
    _ListSchema,
    _StructModule,
    _StructSchema,
    _StructSchemaField,
)

from mas.schema.cluster.cluster_admin_service_capnp.types import builders as builders
from mas.schema.cluster.cluster_admin_service_capnp.types import clients as clients
from mas.schema.cluster.cluster_admin_service_capnp.types import common as common
from mas.schema.cluster.cluster_admin_service_capnp.types import contexts as contexts
from mas.schema.cluster.cluster_admin_service_capnp.types import readers as readers
from mas.schema.cluster.cluster_admin_service_capnp.types import schemas as schemas
from mas.schema.cluster.cluster_admin_service_capnp.types import servers as servers
from mas.schema.cluster.cluster_admin_service_capnp.types.results import (
    tuples as results_tuples,
)
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule

class _ClusterStructModule(_StructModule):
    class _UnregisterInterfaceModule(_InterfaceModule):
        class _UnregisterSchema(_InterfaceSchema):
            class _UnregisterInterfaceModuleUnregisterParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._UnregisterInterfaceModule._UnregisterSchema._UnregisterInterfaceModuleUnregisterParamSchema._Fields: ...

            class _UnregisterInterfaceModuleUnregisterResultSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["success"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._UnregisterInterfaceModule._UnregisterSchema._UnregisterInterfaceModuleUnregisterResultSchema._Fields: ...

            class _UnregisterInterfaceModuleUnregisterMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ClusterStructModule._UnregisterInterfaceModule._UnregisterSchema._UnregisterInterfaceModuleUnregisterParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ClusterStructModule._UnregisterInterfaceModule._UnregisterSchema._UnregisterInterfaceModuleUnregisterResultSchema: ...

            class _Methods(dict[str, _InterfaceMethod]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["unregister"],
                ) -> _ClusterStructModule._UnregisterInterfaceModule._UnregisterSchema._UnregisterInterfaceModuleUnregisterMethod: ...
                @overload
                def __getitem__(self, key: str) -> _InterfaceMethod: ...

            @property
            @override
            def methods(
                self,
            ) -> _ClusterStructModule._UnregisterInterfaceModule._UnregisterSchema._Methods: ...

        @property
        @override
        def schema(self) -> schemas._ClusterUnregisterSchema: ...
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> clients.UnregisterClient: ...
        class Server(_DynamicCapabilityServer):
            def unregister(
                self,
                _context: contexts.UnregisterCallContext,
                **kwargs: object,
            ) -> Awaitable[bool | results_tuples.UnregisterResultTuple | None]: ...
            def unregister_context(
                self,
                context: contexts.UnregisterCallContext,
            ) -> Awaitable[None]: ...

    Unregister: _UnregisterInterfaceModule
    type UnregisterServer = _ClusterStructModule._UnregisterInterfaceModule.Server
    class _AdminMasterInterfaceModule(_IdentifiableInterfaceModule):
        class _AdminMasterSchema(_InterfaceSchema):
            class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._AdminMasterInterfaceModule._AdminMasterSchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

            class _IdentifiableInterfaceModuleInfoResultSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["name"],
                    ) -> _StructSchemaField: ...
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
                ) -> _ClusterStructModule._AdminMasterInterfaceModule._AdminMasterSchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

            class _IdentifiableInterfaceModuleInfoMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ClusterStructModule._AdminMasterInterfaceModule._AdminMasterSchema._IdentifiableInterfaceModuleInfoParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ClusterStructModule._AdminMasterInterfaceModule._AdminMasterSchema._IdentifiableInterfaceModuleInfoResultSchema: ...

            class _AdminMasterInterfaceModuleRegisterModelInstanceFactoryParamSchema(
                _StructSchema,
            ):
                class _AFactoryField(_StructSchemaField):
                    @property
                    @override
                    def schema(self) -> schemas._ClusterModelInstanceFactorySchema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["aModelId"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["aFactory"],
                    ) -> _ClusterStructModule._AdminMasterInterfaceModule._AdminMasterSchema._AdminMasterInterfaceModuleRegisterModelInstanceFactoryParamSchema._AFactoryField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._AdminMasterInterfaceModule._AdminMasterSchema._AdminMasterInterfaceModuleRegisterModelInstanceFactoryParamSchema._Fields: ...

            class _AdminMasterInterfaceModuleRegisterModelInstanceFactoryResultSchema(
                _StructSchema,
            ):
                class _UnregisterField(_StructSchemaField):
                    @property
                    @override
                    def schema(self) -> schemas._ClusterUnregisterSchema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["unregister"],
                    ) -> _ClusterStructModule._AdminMasterInterfaceModule._AdminMasterSchema._AdminMasterInterfaceModuleRegisterModelInstanceFactoryResultSchema._UnregisterField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._AdminMasterInterfaceModule._AdminMasterSchema._AdminMasterInterfaceModuleRegisterModelInstanceFactoryResultSchema._Fields: ...

            class _AdminMasterInterfaceModuleRegisterModelInstanceFactoryMethod(
                _InterfaceMethod,
            ):
                @property
                @override
                def param_type(
                    self,
                ) -> _ClusterStructModule._AdminMasterInterfaceModule._AdminMasterSchema._AdminMasterInterfaceModuleRegisterModelInstanceFactoryParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ClusterStructModule._AdminMasterInterfaceModule._AdminMasterSchema._AdminMasterInterfaceModuleRegisterModelInstanceFactoryResultSchema: ...

            class _AdminMasterInterfaceModuleAvailableModelsParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._AdminMasterInterfaceModule._AdminMasterSchema._AdminMasterInterfaceModuleAvailableModelsParamSchema._Fields: ...

            class _AdminMasterInterfaceModuleAvailableModelsResultSchema(_StructSchema):
                class _FactoriesField(_StructSchemaField):
                    class _Schema(_ListSchema):
                        @property
                        @override
                        def elementType(
                            self,
                        ) -> schemas._ClusterModelInstanceFactorySchema: ...

                    @property
                    @override
                    def schema(
                        self,
                    ) -> _ClusterStructModule._AdminMasterInterfaceModule._AdminMasterSchema._AdminMasterInterfaceModuleAvailableModelsResultSchema._FactoriesField._Schema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["factories"],
                    ) -> _ClusterStructModule._AdminMasterInterfaceModule._AdminMasterSchema._AdminMasterInterfaceModuleAvailableModelsResultSchema._FactoriesField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._AdminMasterInterfaceModule._AdminMasterSchema._AdminMasterInterfaceModuleAvailableModelsResultSchema._Fields: ...

            class _AdminMasterInterfaceModuleAvailableModelsMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ClusterStructModule._AdminMasterInterfaceModule._AdminMasterSchema._AdminMasterInterfaceModuleAvailableModelsParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ClusterStructModule._AdminMasterInterfaceModule._AdminMasterSchema._AdminMasterInterfaceModuleAvailableModelsResultSchema: ...

            class _Methods(dict[str, _InterfaceMethod]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["info"],
                ) -> _ClusterStructModule._AdminMasterInterfaceModule._AdminMasterSchema._IdentifiableInterfaceModuleInfoMethod: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["registerModelInstanceFactory"],
                ) -> _ClusterStructModule._AdminMasterInterfaceModule._AdminMasterSchema._AdminMasterInterfaceModuleRegisterModelInstanceFactoryMethod: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["availableModels"],
                ) -> _ClusterStructModule._AdminMasterInterfaceModule._AdminMasterSchema._AdminMasterInterfaceModuleAvailableModelsMethod: ...
                @overload
                def __getitem__(self, key: str) -> _InterfaceMethod: ...

            @property
            @override
            def methods(
                self,
            ) -> _ClusterStructModule._AdminMasterInterfaceModule._AdminMasterSchema._Methods: ...

        @property
        @override
        def schema(self) -> schemas._ClusterAdminMasterSchema: ...
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> clients.AdminMasterClient: ...
        class Server(_IdentifiableInterfaceModule.Server):
            def registerModelInstanceFactory(
                self,
                aModelId: str,
                aFactory: clients.ModelInstanceFactoryClient,
                _context: contexts.AdminMasterRegistermodelinstancefactoryCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _ClusterStructModule._UnregisterInterfaceModule.Server
                | clients.UnregisterClient
                | results_tuples.AdminMasterRegistermodelinstancefactoryResultTuple
                | None
            ]: ...
            def registerModelInstanceFactory_context(
                self,
                context: contexts.AdminMasterRegistermodelinstancefactoryCallContext,
            ) -> Awaitable[None]: ...
            def availableModels(
                self,
                _context: contexts.AdminMasterAvailablemodelsCallContext,
                **kwargs: object,
            ) -> Awaitable[
                builders.ModelInstanceFactoryClientListBuilder
                | readers.ModelInstanceFactoryClientListReader
                | Sequence[Any]
                | results_tuples.AdminMasterAvailablemodelsResultTuple
                | None
            ]: ...
            def availableModels_context(
                self,
                context: contexts.AdminMasterAvailablemodelsCallContext,
            ) -> Awaitable[None]: ...

    class _ModelInstanceFactoryInterfaceModule(_IdentifiableInterfaceModule):
        class _ModelInstanceFactorySchema(_InterfaceSchema):
            class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

            class _IdentifiableInterfaceModuleInfoResultSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["name"],
                    ) -> _StructSchemaField: ...
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
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

            class _IdentifiableInterfaceModuleInfoMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._IdentifiableInterfaceModuleInfoParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._IdentifiableInterfaceModuleInfoResultSchema: ...

            class _ModelInstanceFactoryInterfaceModuleNewInstanceParamSchema(
                _StructSchema,
            ):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleNewInstanceParamSchema._Fields: ...

            class _ModelInstanceFactoryInterfaceModuleNewInstanceResultSchema(
                _StructSchema,
            ):
                class _InstanceField(_StructSchemaField):
                    @property
                    @override
                    def schema(self) -> schemas._ClusterValueHolderSchema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["instance"],
                    ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleNewInstanceResultSchema._InstanceField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleNewInstanceResultSchema._Fields: ...

            class _ModelInstanceFactoryInterfaceModuleNewInstanceMethod(
                _InterfaceMethod,
            ):
                @property
                @override
                def param_type(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleNewInstanceParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleNewInstanceResultSchema: ...

            class _ModelInstanceFactoryInterfaceModuleNewInstancesParamSchema(
                _StructSchema,
            ):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["numberOfInstances"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleNewInstancesParamSchema._Fields: ...

            class _ModelInstanceFactoryInterfaceModuleNewInstancesResultSchema(
                _StructSchema,
            ):
                class _InstancesField(_StructSchemaField):
                    @property
                    @override
                    def schema(self) -> schemas._ClusterValueHolderSchema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["instances"],
                    ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleNewInstancesResultSchema._InstancesField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleNewInstancesResultSchema._Fields: ...

            class _ModelInstanceFactoryInterfaceModuleNewInstancesMethod(
                _InterfaceMethod,
            ):
                @property
                @override
                def param_type(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleNewInstancesParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleNewInstancesResultSchema: ...

            class _ModelInstanceFactoryInterfaceModuleNewCloudViaZmqPipelineProxiesParamSchema(
                _StructSchema,
            ):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["numberOfInstances"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleNewCloudViaZmqPipelineProxiesParamSchema._Fields: ...

            class _ModelInstanceFactoryInterfaceModuleNewCloudViaZmqPipelineProxiesResultSchema(
                _StructSchema,
            ):
                class _ProxyAddressesField(_StructSchemaField):
                    @property
                    @override
                    def schema(self) -> schemas._ClusterValueHolderSchema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["proxyAddresses"],
                    ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleNewCloudViaZmqPipelineProxiesResultSchema._ProxyAddressesField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleNewCloudViaZmqPipelineProxiesResultSchema._Fields: ...

            class _ModelInstanceFactoryInterfaceModuleNewCloudViaZmqPipelineProxiesMethod(
                _InterfaceMethod,
            ):
                @property
                @override
                def param_type(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleNewCloudViaZmqPipelineProxiesParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleNewCloudViaZmqPipelineProxiesResultSchema: ...

            class _ModelInstanceFactoryInterfaceModuleNewCloudViaProxyParamSchema(
                _StructSchema,
            ):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["numberOfInstances"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleNewCloudViaProxyParamSchema._Fields: ...

            class _ModelInstanceFactoryInterfaceModuleNewCloudViaProxyResultSchema(
                _StructSchema,
            ):
                class _ProxyField(_StructSchemaField):
                    @property
                    @override
                    def schema(self) -> schemas._ClusterValueHolderSchema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["proxy"],
                    ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleNewCloudViaProxyResultSchema._ProxyField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleNewCloudViaProxyResultSchema._Fields: ...

            class _ModelInstanceFactoryInterfaceModuleNewCloudViaProxyMethod(
                _InterfaceMethod,
            ):
                @property
                @override
                def param_type(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleNewCloudViaProxyParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleNewCloudViaProxyResultSchema: ...

            class _ModelInstanceFactoryInterfaceModuleModelIdParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleModelIdParamSchema._Fields: ...

            class _ModelInstanceFactoryInterfaceModuleModelIdResultSchema(
                _StructSchema,
            ):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleModelIdResultSchema._Fields: ...

            class _ModelInstanceFactoryInterfaceModuleModelIdMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleModelIdParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleModelIdResultSchema: ...

            class _ModelInstanceFactoryInterfaceModuleRegisterModelInstanceParamSchema(
                _StructSchema,
            ):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["instance"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["registrationToken"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleRegisterModelInstanceParamSchema._Fields: ...

            class _ModelInstanceFactoryInterfaceModuleRegisterModelInstanceResultSchema(
                _StructSchema,
            ):
                class _UnregisterField(_StructSchemaField):
                    @property
                    @override
                    def schema(self) -> schemas._ClusterUnregisterSchema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["unregister"],
                    ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleRegisterModelInstanceResultSchema._UnregisterField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleRegisterModelInstanceResultSchema._Fields: ...

            class _ModelInstanceFactoryInterfaceModuleRegisterModelInstanceMethod(
                _InterfaceMethod,
            ):
                @property
                @override
                def param_type(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleRegisterModelInstanceParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleRegisterModelInstanceResultSchema: ...

            class _ModelInstanceFactoryInterfaceModuleRestoreSturdyRefParamSchema(
                _StructSchema,
            ):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["sturdyRef"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleRestoreSturdyRefParamSchema._Fields: ...

            class _ModelInstanceFactoryInterfaceModuleRestoreSturdyRefResultSchema(
                _StructSchema,
            ):
                class _CapField(_StructSchemaField):
                    @property
                    @override
                    def schema(self) -> schemas._ClusterValueHolderSchema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["cap"],
                    ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleRestoreSturdyRefResultSchema._CapField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleRestoreSturdyRefResultSchema._Fields: ...

            class _ModelInstanceFactoryInterfaceModuleRestoreSturdyRefMethod(
                _InterfaceMethod,
            ):
                @property
                @override
                def param_type(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleRestoreSturdyRefParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleRestoreSturdyRefResultSchema: ...

            class _Methods(dict[str, _InterfaceMethod]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["info"],
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._IdentifiableInterfaceModuleInfoMethod: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["newInstance"],
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleNewInstanceMethod: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["newInstances"],
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleNewInstancesMethod: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["newCloudViaZmqPipelineProxies"],
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleNewCloudViaZmqPipelineProxiesMethod: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["newCloudViaProxy"],
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleNewCloudViaProxyMethod: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["modelId"],
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleModelIdMethod: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["registerModelInstance"],
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleRegisterModelInstanceMethod: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["restoreSturdyRef"],
                ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._ModelInstanceFactoryInterfaceModuleRestoreSturdyRefMethod: ...
                @overload
                def __getitem__(self, key: str) -> _InterfaceMethod: ...

            @property
            @override
            def methods(
                self,
            ) -> _ClusterStructModule._ModelInstanceFactoryInterfaceModule._ModelInstanceFactorySchema._Methods: ...

        @property
        @override
        def schema(self) -> schemas._ClusterModelInstanceFactorySchema: ...
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> clients.ModelInstanceFactoryClient: ...
        class Server(_IdentifiableInterfaceModule.Server):
            def newInstance(
                self,
                _context: contexts.NewinstanceCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _ClusterStructModule._ValueHolderInterfaceModule.Server
                | clients.ValueHolderClient
                | results_tuples.NewinstanceResultTuple
                | None
            ]: ...
            def newInstance_context(
                self,
                context: contexts.NewinstanceCallContext,
            ) -> Awaitable[None]: ...
            def newInstances(
                self,
                numberOfInstances: int,
                _context: contexts.NewinstancesCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _ClusterStructModule._ValueHolderInterfaceModule.Server
                | clients.ValueHolderClient
                | results_tuples.NewinstancesResultTuple
                | None
            ]: ...
            def newInstances_context(
                self,
                context: contexts.NewinstancesCallContext,
            ) -> Awaitable[None]: ...
            def newCloudViaZmqPipelineProxies(
                self,
                numberOfInstances: int,
                _context: contexts.NewcloudviazmqpipelineproxiesCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _ClusterStructModule._ValueHolderInterfaceModule.Server
                | clients.ValueHolderClient
                | results_tuples.NewcloudviazmqpipelineproxiesResultTuple
                | None
            ]: ...
            def newCloudViaZmqPipelineProxies_context(
                self,
                context: contexts.NewcloudviazmqpipelineproxiesCallContext,
            ) -> Awaitable[None]: ...
            def newCloudViaProxy(
                self,
                numberOfInstances: int,
                _context: contexts.NewcloudviaproxyCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _ClusterStructModule._ValueHolderInterfaceModule.Server
                | clients.ValueHolderClient
                | results_tuples.NewcloudviaproxyResultTuple
                | None
            ]: ...
            def newCloudViaProxy_context(
                self,
                context: contexts.NewcloudviaproxyCallContext,
            ) -> Awaitable[None]: ...
            def modelId(
                self,
                _context: contexts.ModelidCallContext,
                **kwargs: object,
            ) -> Awaitable[str | results_tuples.ModelidResultTuple | None]: ...
            def modelId_context(
                self,
                context: contexts.ModelidCallContext,
            ) -> Awaitable[None]: ...
            def registerModelInstance(
                self,
                instance: _DynamicObjectReader,
                registrationToken: str,
                _context: contexts.RegistermodelinstanceCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _ClusterStructModule._UnregisterInterfaceModule.Server
                | clients.UnregisterClient
                | results_tuples.RegistermodelinstanceResultTuple
                | None
            ]: ...
            def registerModelInstance_context(
                self,
                context: contexts.RegistermodelinstanceCallContext,
            ) -> Awaitable[None]: ...
            def restoreSturdyRef(
                self,
                sturdyRef: str,
                _context: contexts.RestoresturdyrefCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _ClusterStructModule._ValueHolderInterfaceModule.Server
                | clients.ValueHolderClient
                | results_tuples.RestoresturdyrefResultTuple
                | None
            ]: ...
            def restoreSturdyRef_context(
                self,
                context: contexts.RestoresturdyrefCallContext,
            ) -> Awaitable[None]: ...

    class _ValueHolderInterfaceModule(_InterfaceModule):
        class _ValueHolderSchema(_InterfaceSchema):
            class _ValueHolderInterfaceModuleValueParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._ValueHolderInterfaceModule._ValueHolderSchema._ValueHolderInterfaceModuleValueParamSchema._Fields: ...

            class _ValueHolderInterfaceModuleValueResultSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["val"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._ValueHolderInterfaceModule._ValueHolderSchema._ValueHolderInterfaceModuleValueResultSchema._Fields: ...

            class _ValueHolderInterfaceModuleValueMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ClusterStructModule._ValueHolderInterfaceModule._ValueHolderSchema._ValueHolderInterfaceModuleValueParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ClusterStructModule._ValueHolderInterfaceModule._ValueHolderSchema._ValueHolderInterfaceModuleValueResultSchema: ...

            class _ValueHolderInterfaceModuleReleaseParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._ValueHolderInterfaceModule._ValueHolderSchema._ValueHolderInterfaceModuleReleaseParamSchema._Fields: ...

            class _ValueHolderInterfaceModuleReleaseResultSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._ValueHolderInterfaceModule._ValueHolderSchema._ValueHolderInterfaceModuleReleaseResultSchema._Fields: ...

            class _ValueHolderInterfaceModuleReleaseMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ClusterStructModule._ValueHolderInterfaceModule._ValueHolderSchema._ValueHolderInterfaceModuleReleaseParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ClusterStructModule._ValueHolderInterfaceModule._ValueHolderSchema._ValueHolderInterfaceModuleReleaseResultSchema: ...

            class _Methods(dict[str, _InterfaceMethod]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["value"],
                ) -> _ClusterStructModule._ValueHolderInterfaceModule._ValueHolderSchema._ValueHolderInterfaceModuleValueMethod: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["release"],
                ) -> _ClusterStructModule._ValueHolderInterfaceModule._ValueHolderSchema._ValueHolderInterfaceModuleReleaseMethod: ...
                @overload
                def __getitem__(self, key: str) -> _InterfaceMethod: ...

            @property
            @override
            def methods(
                self,
            ) -> _ClusterStructModule._ValueHolderInterfaceModule._ValueHolderSchema._Methods: ...

        @property
        @override
        def schema(self) -> schemas._ClusterValueHolderSchema: ...
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> clients.ValueHolderClient: ...
        class Server(_DynamicCapabilityServer):
            def value(
                self,
                _context: contexts.ValueCallContext,
                **kwargs: object,
            ) -> Awaitable[
                common.AnyPointer | results_tuples.ValueResultTuple | None
            ]: ...
            def value_context(
                self,
                context: contexts.ValueCallContext,
            ) -> Awaitable[None]: ...
            def release(
                self,
                _context: contexts.ReleaseCallContext,
                **kwargs: object,
            ) -> Awaitable[None]: ...
            def release_context(
                self,
                context: contexts.ReleaseCallContext,
            ) -> Awaitable[None]: ...

    ValueHolder: _ValueHolderInterfaceModule
    type ValueHolderServer = _ClusterStructModule._ValueHolderInterfaceModule.Server
    ModelInstanceFactory: _ModelInstanceFactoryInterfaceModule
    type ModelInstanceFactoryServer = (
        _ClusterStructModule._ModelInstanceFactoryInterfaceModule.Server
    )
    AdminMaster: _AdminMasterInterfaceModule
    type AdminMasterServer = _ClusterStructModule._AdminMasterInterfaceModule.Server
    class _UserMasterInterfaceModule(_IdentifiableInterfaceModule):
        class _UserMasterSchema(_InterfaceSchema):
            class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._UserMasterInterfaceModule._UserMasterSchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

            class _IdentifiableInterfaceModuleInfoResultSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["name"],
                    ) -> _StructSchemaField: ...
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
                ) -> _ClusterStructModule._UserMasterInterfaceModule._UserMasterSchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

            class _IdentifiableInterfaceModuleInfoMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ClusterStructModule._UserMasterInterfaceModule._UserMasterSchema._IdentifiableInterfaceModuleInfoParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ClusterStructModule._UserMasterInterfaceModule._UserMasterSchema._IdentifiableInterfaceModuleInfoResultSchema: ...

            class _UserMasterInterfaceModuleAvailableModelsParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._UserMasterInterfaceModule._UserMasterSchema._UserMasterInterfaceModuleAvailableModelsParamSchema._Fields: ...

            class _UserMasterInterfaceModuleAvailableModelsResultSchema(_StructSchema):
                class _FactoriesField(_StructSchemaField):
                    class _Schema(_ListSchema):
                        @property
                        @override
                        def elementType(
                            self,
                        ) -> schemas._ClusterModelInstanceFactorySchema: ...

                    @property
                    @override
                    def schema(
                        self,
                    ) -> _ClusterStructModule._UserMasterInterfaceModule._UserMasterSchema._UserMasterInterfaceModuleAvailableModelsResultSchema._FactoriesField._Schema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["factories"],
                    ) -> _ClusterStructModule._UserMasterInterfaceModule._UserMasterSchema._UserMasterInterfaceModuleAvailableModelsResultSchema._FactoriesField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._UserMasterInterfaceModule._UserMasterSchema._UserMasterInterfaceModuleAvailableModelsResultSchema._Fields: ...

            class _UserMasterInterfaceModuleAvailableModelsMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ClusterStructModule._UserMasterInterfaceModule._UserMasterSchema._UserMasterInterfaceModuleAvailableModelsParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ClusterStructModule._UserMasterInterfaceModule._UserMasterSchema._UserMasterInterfaceModuleAvailableModelsResultSchema: ...

            class _Methods(dict[str, _InterfaceMethod]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["info"],
                ) -> _ClusterStructModule._UserMasterInterfaceModule._UserMasterSchema._IdentifiableInterfaceModuleInfoMethod: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["availableModels"],
                ) -> _ClusterStructModule._UserMasterInterfaceModule._UserMasterSchema._UserMasterInterfaceModuleAvailableModelsMethod: ...
                @overload
                def __getitem__(self, key: str) -> _InterfaceMethod: ...

            @property
            @override
            def methods(
                self,
            ) -> _ClusterStructModule._UserMasterInterfaceModule._UserMasterSchema._Methods: ...

        @property
        @override
        def schema(self) -> schemas._ClusterUserMasterSchema: ...
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> clients.UserMasterClient: ...
        class Server(_IdentifiableInterfaceModule.Server):
            def availableModels(
                self,
                _context: contexts.UserMasterAvailablemodelsCallContext,
                **kwargs: object,
            ) -> Awaitable[
                builders.ModelInstanceFactoryClientListBuilder
                | readers.ModelInstanceFactoryClientListReader
                | Sequence[Any]
                | results_tuples.UserMasterAvailablemodelsResultTuple
                | None
            ]: ...
            def availableModels_context(
                self,
                context: contexts.UserMasterAvailablemodelsCallContext,
            ) -> Awaitable[None]: ...

    UserMaster: _UserMasterInterfaceModule
    type UserMasterServer = _ClusterStructModule._UserMasterInterfaceModule.Server
    class _RuntimeInterfaceModule(_IdentifiableInterfaceModule):
        class _RuntimeSchema(_InterfaceSchema):
            class _IdentifiableInterfaceModuleInfoParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._IdentifiableInterfaceModuleInfoParamSchema._Fields: ...

            class _IdentifiableInterfaceModuleInfoResultSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(self, key: Literal["id"]) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["name"],
                    ) -> _StructSchemaField: ...
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
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._IdentifiableInterfaceModuleInfoResultSchema._Fields: ...

            class _IdentifiableInterfaceModuleInfoMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._IdentifiableInterfaceModuleInfoParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._IdentifiableInterfaceModuleInfoResultSchema: ...

            class _RuntimeInterfaceModuleRegisterModelInstanceFactoryParamSchema(
                _StructSchema,
            ):
                class _AFactoryField(_StructSchemaField):
                    @property
                    @override
                    def schema(self) -> schemas._ClusterModelInstanceFactorySchema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["aModelId"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["aFactory"],
                    ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleRegisterModelInstanceFactoryParamSchema._AFactoryField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleRegisterModelInstanceFactoryParamSchema._Fields: ...

            class _RuntimeInterfaceModuleRegisterModelInstanceFactoryResultSchema(
                _StructSchema,
            ):
                class _UnregisterField(_StructSchemaField):
                    @property
                    @override
                    def schema(self) -> schemas._ClusterUnregisterSchema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["unregister"],
                    ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleRegisterModelInstanceFactoryResultSchema._UnregisterField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleRegisterModelInstanceFactoryResultSchema._Fields: ...

            class _RuntimeInterfaceModuleRegisterModelInstanceFactoryMethod(
                _InterfaceMethod,
            ):
                @property
                @override
                def param_type(
                    self,
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleRegisterModelInstanceFactoryParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleRegisterModelInstanceFactoryResultSchema: ...

            class _RuntimeInterfaceModuleAvailableModelsParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleAvailableModelsParamSchema._Fields: ...

            class _RuntimeInterfaceModuleAvailableModelsResultSchema(_StructSchema):
                class _FactoriesField(_StructSchemaField):
                    class _Schema(_ListSchema):
                        @property
                        @override
                        def elementType(
                            self,
                        ) -> schemas._ClusterModelInstanceFactorySchema: ...

                    @property
                    @override
                    def schema(
                        self,
                    ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleAvailableModelsResultSchema._FactoriesField._Schema: ...

                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["factories"],
                    ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleAvailableModelsResultSchema._FactoriesField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleAvailableModelsResultSchema._Fields: ...

            class _RuntimeInterfaceModuleAvailableModelsMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleAvailableModelsParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleAvailableModelsResultSchema: ...

            class _RuntimeInterfaceModuleNumberOfCoresParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleNumberOfCoresParamSchema._Fields: ...

            class _RuntimeInterfaceModuleNumberOfCoresResultSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["cores"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleNumberOfCoresResultSchema._Fields: ...

            class _RuntimeInterfaceModuleNumberOfCoresMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleNumberOfCoresParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleNumberOfCoresResultSchema: ...

            class _RuntimeInterfaceModuleFreeNumberOfCoresParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]): ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleFreeNumberOfCoresParamSchema._Fields: ...

            class _RuntimeInterfaceModuleFreeNumberOfCoresResultSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["cores"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleFreeNumberOfCoresResultSchema._Fields: ...

            class _RuntimeInterfaceModuleFreeNumberOfCoresMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleFreeNumberOfCoresParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleFreeNumberOfCoresResultSchema: ...

            class _RuntimeInterfaceModuleReserveNumberOfCoresParamSchema(_StructSchema):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["reserveCores"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["aModelId"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleReserveNumberOfCoresParamSchema._Fields: ...

            class _RuntimeInterfaceModuleReserveNumberOfCoresResultSchema(
                _StructSchema,
            ):
                class _Fields(dict[str, _StructSchemaField]):
                    @overload
                    def __getitem__(
                        self,
                        key: Literal["reservedCores"],
                    ) -> _StructSchemaField: ...
                    @overload
                    def __getitem__(self, key: str) -> _StructSchemaField: ...

                @property
                @override
                def fields(
                    self,
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleReserveNumberOfCoresResultSchema._Fields: ...

            class _RuntimeInterfaceModuleReserveNumberOfCoresMethod(_InterfaceMethod):
                @property
                @override
                def param_type(
                    self,
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleReserveNumberOfCoresParamSchema: ...
                @property
                @override
                def result_type(
                    self,
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleReserveNumberOfCoresResultSchema: ...

            class _Methods(dict[str, _InterfaceMethod]):
                @overload
                def __getitem__(
                    self,
                    key: Literal["info"],
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._IdentifiableInterfaceModuleInfoMethod: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["registerModelInstanceFactory"],
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleRegisterModelInstanceFactoryMethod: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["availableModels"],
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleAvailableModelsMethod: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["numberOfCores"],
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleNumberOfCoresMethod: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["freeNumberOfCores"],
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleFreeNumberOfCoresMethod: ...
                @overload
                def __getitem__(
                    self,
                    key: Literal["reserveNumberOfCores"],
                ) -> _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._RuntimeInterfaceModuleReserveNumberOfCoresMethod: ...
                @overload
                def __getitem__(self, key: str) -> _InterfaceMethod: ...

            @property
            @override
            def methods(
                self,
            ) -> (
                _ClusterStructModule._RuntimeInterfaceModule._RuntimeSchema._Methods
            ): ...

        @property
        @override
        def schema(self) -> schemas._ClusterRuntimeSchema: ...
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> clients.RuntimeClient: ...
        class Server(_IdentifiableInterfaceModule.Server):
            def registerModelInstanceFactory(
                self,
                aModelId: str,
                aFactory: clients.ModelInstanceFactoryClient,
                _context: contexts.RuntimeRegistermodelinstancefactoryCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _ClusterStructModule._UnregisterInterfaceModule.Server
                | clients.UnregisterClient
                | results_tuples.RuntimeRegistermodelinstancefactoryResultTuple
                | None
            ]: ...
            def registerModelInstanceFactory_context(
                self,
                context: contexts.RuntimeRegistermodelinstancefactoryCallContext,
            ) -> Awaitable[None]: ...
            def availableModels(
                self,
                _context: contexts.RuntimeAvailablemodelsCallContext,
                **kwargs: object,
            ) -> Awaitable[
                builders.ModelInstanceFactoryClientListBuilder
                | readers.ModelInstanceFactoryClientListReader
                | Sequence[Any]
                | results_tuples.RuntimeAvailablemodelsResultTuple
                | None
            ]: ...
            def availableModels_context(
                self,
                context: contexts.RuntimeAvailablemodelsCallContext,
            ) -> Awaitable[None]: ...
            def numberOfCores(
                self,
                _context: contexts.NumberofcoresCallContext,
                **kwargs: object,
            ) -> Awaitable[int | results_tuples.NumberofcoresResultTuple | None]: ...
            def numberOfCores_context(
                self,
                context: contexts.NumberofcoresCallContext,
            ) -> Awaitable[None]: ...
            def freeNumberOfCores(
                self,
                _context: contexts.FreenumberofcoresCallContext,
                **kwargs: object,
            ) -> Awaitable[
                int | results_tuples.FreenumberofcoresResultTuple | None
            ]: ...
            def freeNumberOfCores_context(
                self,
                context: contexts.FreenumberofcoresCallContext,
            ) -> Awaitable[None]: ...
            def reserveNumberOfCores(
                self,
                reserveCores: int,
                aModelId: str,
                _context: contexts.ReservenumberofcoresCallContext,
                **kwargs: object,
            ) -> Awaitable[
                int | results_tuples.ReservenumberofcoresResultTuple | None
            ]: ...
            def reserveNumberOfCores_context(
                self,
                context: contexts.ReservenumberofcoresCallContext,
            ) -> Awaitable[None]: ...

    Runtime: _RuntimeInterfaceModule
    type RuntimeServer = _ClusterStructModule._RuntimeInterfaceModule.Server
    class _ZmqPipelineAddressesStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        class _ZmqPipelineAddressesSchema(_StructSchema):
            class _Fields(dict[str, _StructSchemaField]):
                @overload
                def __getitem__(self, key: Literal["input"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: Literal["output"]) -> _StructSchemaField: ...
                @overload
                def __getitem__(self, key: str) -> _StructSchemaField: ...

            @property
            @override
            def fields(
                self,
            ) -> _ClusterStructModule._ZmqPipelineAddressesStructModule._ZmqPipelineAddressesSchema._Fields: ...

        @property
        @override
        def schema(self) -> schemas._ClusterZmqPipelineAddressesSchema: ...
        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            input: str | None = None,
            output: str | None = None,
            **kwargs: object,
        ) -> builders.ZmqPipelineAddressesBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[readers.ZmqPipelineAddressesReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[readers.ZmqPipelineAddressesReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[builders.ZmqPipelineAddressesBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.ZmqPipelineAddressesReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> readers.ZmqPipelineAddressesReader: ...

    ZmqPipelineAddresses: _ZmqPipelineAddressesStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _ClusterSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]): ...

        @property
        @override
        def fields(self) -> _ClusterStructModule._ClusterSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._ClusterSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        **kwargs: object,
    ) -> builders.ClusterBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.ClusterReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.ClusterReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.ClusterBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.ClusterReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.ClusterReader: ...
