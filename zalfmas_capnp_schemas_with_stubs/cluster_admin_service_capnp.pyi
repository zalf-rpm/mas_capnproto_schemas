"""This is an automatically generated stub for `cluster_admin_service.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator
from typing import Any, NamedTuple, Protocol, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicObjectReader,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
    _Request,
    _StructModule,
)

from .common_capnp import Identifiable, IdentifiableClient, _IdentifiableModule

# Type alias for AnyPointer parameters (accepts all Cap'n Proto pointer types)
type AnyPointer = str | bytes | _DynamicStructBuilder | _DynamicStructReader | _DynamicCapabilityClient | _DynamicCapabilityServer

class _ClusterModule(_StructModule):
    class _UnregisterModule(_InterfaceModule):
        class UnregisterRequest(Protocol):
            def send(self) -> _ClusterModule._UnregisterModule.UnregisterClient.UnregisterResult: ...

        @classmethod
        def _new_client(cls, server: _ClusterModule._UnregisterModule.Server) -> _ClusterModule._UnregisterModule.UnregisterClient: ...
        class Server(_DynamicCapabilityServer):
            class UnregisterResult(Awaitable[UnregisterResult], Protocol):
                success: bool

            class UnregisterResultTuple(NamedTuple):
                success: bool

            class UnregisterCallContext(Protocol):
                params: _ClusterModule._UnregisterModule.UnregisterRequest
                results: _ClusterModule._UnregisterModule.Server.UnregisterResult

            def unregister(self, _context: _ClusterModule._UnregisterModule.Server.UnregisterCallContext, **kwargs: Any) -> Awaitable[bool | _ClusterModule._UnregisterModule.Server.UnregisterResultTuple | None]: ...
            def unregister_context(self, context: _ClusterModule._UnregisterModule.Server.UnregisterCallContext) -> Awaitable[None]: ...

        class UnregisterClient(_DynamicCapabilityClient):
            class UnregisterResult(Awaitable[UnregisterResult], Protocol):
                success: bool

            def unregister(self) -> _ClusterModule._UnregisterModule.UnregisterClient.UnregisterResult: ...
            def unregister_request(self) -> _ClusterModule._UnregisterModule.UnregisterRequest: ...

    Unregister: _UnregisterModule
    type UnregisterClient = _ClusterModule._UnregisterModule.UnregisterClient
    class _AdminMasterModule(_IdentifiableModule):
        class RegistermodelinstancefactoryRequest(Protocol):
            aModelId: str
            def send(self) -> _ClusterModule._AdminMasterModule.AdminMasterClient.RegistermodelinstancefactoryResult: ...

        class AvailablemodelsRequest(Protocol):
            def send(self) -> _ClusterModule._AdminMasterModule.AdminMasterClient.AvailablemodelsResult: ...

        @classmethod
        def _new_client(cls, server: _ClusterModule._AdminMasterModule.Server | _IdentifiableModule.Server) -> _ClusterModule._AdminMasterModule.AdminMasterClient: ...
        class Server(_IdentifiableModule.Server):
            class RegistermodelinstancefactoryResult(Awaitable[RegistermodelinstancefactoryResult], Protocol):
                unregister: _ClusterModule._UnregisterModule.UnregisterClient

            class AvailablemodelsResult(Awaitable[AvailablemodelsResult], Protocol):
                factories: Any

            class RegistermodelinstancefactoryResultTuple(NamedTuple):
                unregister: _ClusterModule._UnregisterModule.Server

            class AvailablemodelsResultTuple(NamedTuple):
                pass

            class RegistermodelinstancefactoryCallContext(Protocol):
                params: _ClusterModule._AdminMasterModule.RegistermodelinstancefactoryRequest
                results: _ClusterModule._AdminMasterModule.Server.RegistermodelinstancefactoryResult

            class AvailablemodelsCallContext(Protocol):
                params: _ClusterModule._AdminMasterModule.AvailablemodelsRequest
                results: _ClusterModule._AdminMasterModule.Server.AvailablemodelsResult

            def registerModelInstanceFactory(
                self, aModelId: str, _context: _ClusterModule._AdminMasterModule.Server.RegistermodelinstancefactoryCallContext, **kwargs: Any
            ) -> Awaitable[_ClusterModule._UnregisterModule.Server | _ClusterModule._AdminMasterModule.Server.RegistermodelinstancefactoryResultTuple | None]: ...
            def registerModelInstanceFactory_context(self, context: _ClusterModule._AdminMasterModule.Server.RegistermodelinstancefactoryCallContext) -> Awaitable[None]: ...
            def availableModels(self, _context: _ClusterModule._AdminMasterModule.Server.AvailablemodelsCallContext, **kwargs: Any) -> Awaitable[_ClusterModule._AdminMasterModule.Server.AvailablemodelsResultTuple | None]: ...
            def availableModels_context(self, context: _ClusterModule._AdminMasterModule.Server.AvailablemodelsCallContext) -> Awaitable[None]: ...

        class AdminMasterClient(_IdentifiableModule.IdentifiableClient):
            class RegistermodelinstancefactoryResult(Awaitable[RegistermodelinstancefactoryResult], Protocol):
                unregister: _ClusterModule._UnregisterModule.UnregisterClient

            class AvailablemodelsResult(Awaitable[AvailablemodelsResult], Protocol):
                factories: Any

            def registerModelInstanceFactory(self, aModelId: str | None = None) -> _ClusterModule._AdminMasterModule.AdminMasterClient.RegistermodelinstancefactoryResult: ...
            def availableModels(self) -> _ClusterModule._AdminMasterModule.AdminMasterClient.AvailablemodelsResult: ...
            def registerModelInstanceFactory_request(self, aModelId: str | None = None) -> _ClusterModule._AdminMasterModule.RegistermodelinstancefactoryRequest: ...
            def availableModels_request(self) -> _ClusterModule._AdminMasterModule.AvailablemodelsRequest: ...

    AdminMaster: _AdminMasterModule
    type AdminMasterClient = _ClusterModule._AdminMasterModule.AdminMasterClient
    class _UserMasterModule(_IdentifiableModule):
        class AvailablemodelsRequest(Protocol):
            def send(self) -> _ClusterModule._UserMasterModule.UserMasterClient.AvailablemodelsResult: ...

        @classmethod
        def _new_client(cls, server: _ClusterModule._UserMasterModule.Server | _IdentifiableModule.Server) -> _ClusterModule._UserMasterModule.UserMasterClient: ...
        class Server(_IdentifiableModule.Server):
            class AvailablemodelsResult(Awaitable[AvailablemodelsResult], Protocol):
                factories: Any

            class AvailablemodelsResultTuple(NamedTuple):
                pass

            class AvailablemodelsCallContext(Protocol):
                params: _ClusterModule._UserMasterModule.AvailablemodelsRequest
                results: _ClusterModule._UserMasterModule.Server.AvailablemodelsResult

            def availableModels(self, _context: _ClusterModule._UserMasterModule.Server.AvailablemodelsCallContext, **kwargs: Any) -> Awaitable[_ClusterModule._UserMasterModule.Server.AvailablemodelsResultTuple | None]: ...
            def availableModels_context(self, context: _ClusterModule._UserMasterModule.Server.AvailablemodelsCallContext) -> Awaitable[None]: ...

        class UserMasterClient(_IdentifiableModule.IdentifiableClient):
            class AvailablemodelsResult(Awaitable[AvailablemodelsResult], Protocol):
                factories: Any

            def availableModels(self) -> _ClusterModule._UserMasterModule.UserMasterClient.AvailablemodelsResult: ...
            def availableModels_request(self) -> _ClusterModule._UserMasterModule.AvailablemodelsRequest: ...

    UserMaster: _UserMasterModule
    type UserMasterClient = _ClusterModule._UserMasterModule.UserMasterClient
    class _RuntimeModule(_IdentifiableModule):
        class RegistermodelinstancefactoryRequest(Protocol):
            aModelId: str
            def send(self) -> _ClusterModule._RuntimeModule.RuntimeClient.RegistermodelinstancefactoryResult: ...

        class AvailablemodelsRequest(Protocol):
            def send(self) -> _ClusterModule._RuntimeModule.RuntimeClient.AvailablemodelsResult: ...

        class NumberofcoresRequest(Protocol):
            def send(self) -> _ClusterModule._RuntimeModule.RuntimeClient.NumberofcoresResult: ...

        class FreenumberofcoresRequest(Protocol):
            def send(self) -> _ClusterModule._RuntimeModule.RuntimeClient.FreenumberofcoresResult: ...

        class ReservenumberofcoresRequest(Protocol):
            reserveCores: int
            aModelId: str
            def send(self) -> _ClusterModule._RuntimeModule.RuntimeClient.ReservenumberofcoresResult: ...

        @classmethod
        def _new_client(cls, server: _ClusterModule._RuntimeModule.Server | _IdentifiableModule.Server) -> _ClusterModule._RuntimeModule.RuntimeClient: ...
        class Server(_IdentifiableModule.Server):
            class RegistermodelinstancefactoryResult(Awaitable[RegistermodelinstancefactoryResult], Protocol):
                unregister: _ClusterModule._UnregisterModule.UnregisterClient

            class AvailablemodelsResult(Awaitable[AvailablemodelsResult], Protocol):
                factories: Any

            class NumberofcoresResult(Awaitable[NumberofcoresResult], Protocol):
                cores: int

            class FreenumberofcoresResult(Awaitable[FreenumberofcoresResult], Protocol):
                cores: int

            class ReservenumberofcoresResult(Awaitable[ReservenumberofcoresResult], Protocol):
                reservedCores: int

            class RegistermodelinstancefactoryResultTuple(NamedTuple):
                unregister: _ClusterModule._UnregisterModule.Server

            class AvailablemodelsResultTuple(NamedTuple):
                pass

            class NumberofcoresResultTuple(NamedTuple):
                cores: int

            class FreenumberofcoresResultTuple(NamedTuple):
                cores: int

            class ReservenumberofcoresResultTuple(NamedTuple):
                reservedCores: int

            class RegistermodelinstancefactoryCallContext(Protocol):
                params: _ClusterModule._RuntimeModule.RegistermodelinstancefactoryRequest
                results: _ClusterModule._RuntimeModule.Server.RegistermodelinstancefactoryResult

            class AvailablemodelsCallContext(Protocol):
                params: _ClusterModule._RuntimeModule.AvailablemodelsRequest
                results: _ClusterModule._RuntimeModule.Server.AvailablemodelsResult

            class NumberofcoresCallContext(Protocol):
                params: _ClusterModule._RuntimeModule.NumberofcoresRequest
                results: _ClusterModule._RuntimeModule.Server.NumberofcoresResult

            class FreenumberofcoresCallContext(Protocol):
                params: _ClusterModule._RuntimeModule.FreenumberofcoresRequest
                results: _ClusterModule._RuntimeModule.Server.FreenumberofcoresResult

            class ReservenumberofcoresCallContext(Protocol):
                params: _ClusterModule._RuntimeModule.ReservenumberofcoresRequest
                results: _ClusterModule._RuntimeModule.Server.ReservenumberofcoresResult

            def registerModelInstanceFactory(self, aModelId: str, _context: _ClusterModule._RuntimeModule.Server.RegistermodelinstancefactoryCallContext, **kwargs: Any) -> Awaitable[_ClusterModule._UnregisterModule.Server | _ClusterModule._RuntimeModule.Server.RegistermodelinstancefactoryResultTuple | None]: ...
            def registerModelInstanceFactory_context(self, context: _ClusterModule._RuntimeModule.Server.RegistermodelinstancefactoryCallContext) -> Awaitable[None]: ...
            def availableModels(self, _context: _ClusterModule._RuntimeModule.Server.AvailablemodelsCallContext, **kwargs: Any) -> Awaitable[_ClusterModule._RuntimeModule.Server.AvailablemodelsResultTuple | None]: ...
            def availableModels_context(self, context: _ClusterModule._RuntimeModule.Server.AvailablemodelsCallContext) -> Awaitable[None]: ...
            def numberOfCores(self, _context: _ClusterModule._RuntimeModule.Server.NumberofcoresCallContext, **kwargs: Any) -> Awaitable[int | _ClusterModule._RuntimeModule.Server.NumberofcoresResultTuple | None]: ...
            def numberOfCores_context(self, context: _ClusterModule._RuntimeModule.Server.NumberofcoresCallContext) -> Awaitable[None]: ...
            def freeNumberOfCores(self, _context: _ClusterModule._RuntimeModule.Server.FreenumberofcoresCallContext, **kwargs: Any) -> Awaitable[int | _ClusterModule._RuntimeModule.Server.FreenumberofcoresResultTuple | None]: ...
            def freeNumberOfCores_context(self, context: _ClusterModule._RuntimeModule.Server.FreenumberofcoresCallContext) -> Awaitable[None]: ...
            def reserveNumberOfCores(self, reserveCores: int, aModelId: str, _context: _ClusterModule._RuntimeModule.Server.ReservenumberofcoresCallContext, **kwargs: Any) -> Awaitable[int | _ClusterModule._RuntimeModule.Server.ReservenumberofcoresResultTuple | None]: ...
            def reserveNumberOfCores_context(self, context: _ClusterModule._RuntimeModule.Server.ReservenumberofcoresCallContext) -> Awaitable[None]: ...

        class RuntimeClient(_IdentifiableModule.IdentifiableClient):
            class RegistermodelinstancefactoryResult(Awaitable[RegistermodelinstancefactoryResult], Protocol):
                unregister: _ClusterModule._UnregisterModule.UnregisterClient

            class AvailablemodelsResult(Awaitable[AvailablemodelsResult], Protocol):
                factories: Any

            class NumberofcoresResult(Awaitable[NumberofcoresResult], Protocol):
                cores: int

            class FreenumberofcoresResult(Awaitable[FreenumberofcoresResult], Protocol):
                cores: int

            class ReservenumberofcoresResult(Awaitable[ReservenumberofcoresResult], Protocol):
                reservedCores: int

            def registerModelInstanceFactory(self, aModelId: str | None = None) -> _ClusterModule._RuntimeModule.RuntimeClient.RegistermodelinstancefactoryResult: ...
            def availableModels(self) -> _ClusterModule._RuntimeModule.RuntimeClient.AvailablemodelsResult: ...
            def numberOfCores(self) -> _ClusterModule._RuntimeModule.RuntimeClient.NumberofcoresResult: ...
            def freeNumberOfCores(self) -> _ClusterModule._RuntimeModule.RuntimeClient.FreenumberofcoresResult: ...
            def reserveNumberOfCores(self, reserveCores: int | None = None, aModelId: str | None = None) -> _ClusterModule._RuntimeModule.RuntimeClient.ReservenumberofcoresResult: ...
            def registerModelInstanceFactory_request(self, aModelId: str | None = None) -> _ClusterModule._RuntimeModule.RegistermodelinstancefactoryRequest: ...
            def availableModels_request(self) -> _ClusterModule._RuntimeModule.AvailablemodelsRequest: ...
            def numberOfCores_request(self) -> _ClusterModule._RuntimeModule.NumberofcoresRequest: ...
            def freeNumberOfCores_request(self) -> _ClusterModule._RuntimeModule.FreenumberofcoresRequest: ...
            def reserveNumberOfCores_request(self, reserveCores: int | None = None, aModelId: str | None = None) -> _ClusterModule._RuntimeModule.ReservenumberofcoresRequest: ...

    Runtime: _RuntimeModule
    type RuntimeClient = _ClusterModule._RuntimeModule.RuntimeClient
    class _ZmqPipelineAddressesModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def input(self) -> str: ...
            @property
            def output(self) -> str: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> ZmqPipelineAddressesBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def input(self) -> str: ...
            @input.setter
            def input(self, value: str) -> None: ...
            @property
            def output(self) -> str: ...
            @output.setter
            def output(self, value: str) -> None: ...
            @override
            def as_reader(self) -> ZmqPipelineAddressesReader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, input: str | None = None, output: str | None = None) -> ZmqPipelineAddressesBuilder: ...

    type ZmqPipelineAddressesReader = _ZmqPipelineAddressesModule.Reader
    type ZmqPipelineAddressesBuilder = _ZmqPipelineAddressesModule.Builder
    ZmqPipelineAddresses: _ZmqPipelineAddressesModule
    class _ValueHolderModule(_InterfaceModule):
        class ValueRequest(Protocol):
            def send(self) -> _ClusterModule._ValueHolderModule.ValueHolderClient.ValueResult: ...

        class ReleaseRequest(Protocol):
            def send(self) -> _ClusterModule._ValueHolderModule.ValueHolderClient.ReleaseResult: ...

        @classmethod
        def _new_client(cls, server: _ClusterModule._ValueHolderModule.Server) -> _ClusterModule._ValueHolderModule.ValueHolderClient: ...
        class Server(_DynamicCapabilityServer):
            class ValueResult(Awaitable[ValueResult], Protocol):
                val: AnyPointer

            class ReleaseResult(Awaitable[None], Protocol): ...

            class ValueResultTuple(NamedTuple):
                val: AnyPointer

            class ValueCallContext(Protocol):
                params: _ClusterModule._ValueHolderModule.ValueRequest
                results: _ClusterModule._ValueHolderModule.Server.ValueResult

            class ReleaseCallContext(Protocol):
                params: _ClusterModule._ValueHolderModule.ReleaseRequest

            def value(self, _context: _ClusterModule._ValueHolderModule.Server.ValueCallContext, **kwargs: Any) -> Awaitable[_ClusterModule._ValueHolderModule.Server.ValueResultTuple | None]: ...
            def value_context(self, context: _ClusterModule._ValueHolderModule.Server.ValueCallContext) -> Awaitable[None]: ...
            def release(self, _context: _ClusterModule._ValueHolderModule.Server.ReleaseCallContext, **kwargs: Any) -> Awaitable[None]: ...
            def release_context(self, context: _ClusterModule._ValueHolderModule.Server.ReleaseCallContext) -> Awaitable[None]: ...

        class ValueHolderClient(_DynamicCapabilityClient):
            class ValueResult(Awaitable[ValueResult], Protocol):
                val: _DynamicObjectReader

            class ReleaseResult(Awaitable[None], Protocol): ...

            def value(self) -> _ClusterModule._ValueHolderModule.ValueHolderClient.ValueResult: ...
            def release(self) -> _ClusterModule._ValueHolderModule.ValueHolderClient.ReleaseResult: ...
            def value_request(self) -> _ClusterModule._ValueHolderModule.ValueRequest: ...
            def release_request(self) -> _ClusterModule._ValueHolderModule.ReleaseRequest: ...

    ValueHolder: _ValueHolderModule
    type ValueHolderClient = _ClusterModule._ValueHolderModule.ValueHolderClient
    class _ModelInstanceFactoryModule(_IdentifiableModule):
        class NewinstanceRequest(Protocol):
            def send(self) -> _ClusterModule._ModelInstanceFactoryModule.ModelInstanceFactoryClient.NewinstanceResult: ...

        class NewinstancesRequest(Protocol):
            numberOfInstances: int
            def send(self) -> _ClusterModule._ModelInstanceFactoryModule.ModelInstanceFactoryClient.NewinstancesResult: ...

        class NewcloudviazmqpipelineproxiesRequest(Protocol):
            numberOfInstances: int
            def send(self) -> _ClusterModule._ModelInstanceFactoryModule.ModelInstanceFactoryClient.NewcloudviazmqpipelineproxiesResult: ...

        class NewcloudviaproxyRequest(Protocol):
            numberOfInstances: int
            def send(self) -> _ClusterModule._ModelInstanceFactoryModule.ModelInstanceFactoryClient.NewcloudviaproxyResult: ...

        class ModelidRequest(Protocol):
            def send(self) -> _ClusterModule._ModelInstanceFactoryModule.ModelInstanceFactoryClient.ModelidResult: ...

        class RegistermodelinstanceRequest(Protocol):
            instance: AnyPointer
            registrationToken: str
            def send(self) -> _ClusterModule._ModelInstanceFactoryModule.ModelInstanceFactoryClient.RegistermodelinstanceResult: ...

        class RestoresturdyrefRequest(Protocol):
            sturdyRef: str
            def send(self) -> _ClusterModule._ModelInstanceFactoryModule.ModelInstanceFactoryClient.RestoresturdyrefResult: ...

        @classmethod
        def _new_client(cls, server: _ClusterModule._ModelInstanceFactoryModule.Server | _IdentifiableModule.Server) -> _ClusterModule._ModelInstanceFactoryModule.ModelInstanceFactoryClient: ...
        class Server(_IdentifiableModule.Server):
            class NewinstanceResult(Awaitable[NewinstanceResult], Protocol):
                instance: _ClusterModule._ValueHolderModule.ValueHolderClient

            class NewinstancesResult(Awaitable[NewinstancesResult], Protocol):
                instances: _ClusterModule._ValueHolderModule.ValueHolderClient

            class NewcloudviazmqpipelineproxiesResult(Awaitable[NewcloudviazmqpipelineproxiesResult], Protocol):
                proxyAddresses: _ClusterModule._ValueHolderModule.ValueHolderClient

            class NewcloudviaproxyResult(Awaitable[NewcloudviaproxyResult], Protocol):
                proxy: _ClusterModule._ValueHolderModule.ValueHolderClient

            class ModelidResult(Awaitable[ModelidResult], Protocol):
                id: str

            class RegistermodelinstanceResult(Awaitable[RegistermodelinstanceResult], Protocol):
                unregister: _ClusterModule._UnregisterModule.UnregisterClient

            class RestoresturdyrefResult(Awaitable[RestoresturdyrefResult], Protocol):
                cap: _ClusterModule._ValueHolderModule.ValueHolderClient

            class NewinstanceResultTuple(NamedTuple):
                instance: _ClusterModule._ValueHolderModule.Server

            class NewinstancesResultTuple(NamedTuple):
                instances: _ClusterModule._ValueHolderModule.Server

            class NewcloudviazmqpipelineproxiesResultTuple(NamedTuple):
                proxyAddresses: _ClusterModule._ValueHolderModule.Server

            class NewcloudviaproxyResultTuple(NamedTuple):
                proxy: _ClusterModule._ValueHolderModule.Server

            class ModelidResultTuple(NamedTuple):
                id: str

            class RegistermodelinstanceResultTuple(NamedTuple):
                unregister: _ClusterModule._UnregisterModule.Server

            class RestoresturdyrefResultTuple(NamedTuple):
                cap: _ClusterModule._ValueHolderModule.Server

            class NewinstanceCallContext(Protocol):
                params: _ClusterModule._ModelInstanceFactoryModule.NewinstanceRequest
                results: _ClusterModule._ModelInstanceFactoryModule.Server.NewinstanceResult

            class NewinstancesCallContext(Protocol):
                params: _ClusterModule._ModelInstanceFactoryModule.NewinstancesRequest
                results: _ClusterModule._ModelInstanceFactoryModule.Server.NewinstancesResult

            class NewcloudviazmqpipelineproxiesCallContext(Protocol):
                params: _ClusterModule._ModelInstanceFactoryModule.NewcloudviazmqpipelineproxiesRequest
                results: _ClusterModule._ModelInstanceFactoryModule.Server.NewcloudviazmqpipelineproxiesResult

            class NewcloudviaproxyCallContext(Protocol):
                params: _ClusterModule._ModelInstanceFactoryModule.NewcloudviaproxyRequest
                results: _ClusterModule._ModelInstanceFactoryModule.Server.NewcloudviaproxyResult

            class ModelidCallContext(Protocol):
                params: _ClusterModule._ModelInstanceFactoryModule.ModelidRequest
                results: _ClusterModule._ModelInstanceFactoryModule.Server.ModelidResult

            class RegistermodelinstanceCallContext(Protocol):
                params: _ClusterModule._ModelInstanceFactoryModule.RegistermodelinstanceRequest
                results: _ClusterModule._ModelInstanceFactoryModule.Server.RegistermodelinstanceResult

            class RestoresturdyrefCallContext(Protocol):
                params: _ClusterModule._ModelInstanceFactoryModule.RestoresturdyrefRequest
                results: _ClusterModule._ModelInstanceFactoryModule.Server.RestoresturdyrefResult

            def newInstance(self, _context: _ClusterModule._ModelInstanceFactoryModule.Server.NewinstanceCallContext, **kwargs: Any) -> Awaitable[_ClusterModule._ValueHolderModule.Server | _ClusterModule._ModelInstanceFactoryModule.Server.NewinstanceResultTuple | None]: ...
            def newInstance_context(self, context: _ClusterModule._ModelInstanceFactoryModule.Server.NewinstanceCallContext) -> Awaitable[None]: ...
            def newInstances(self, numberOfInstances: int, _context: _ClusterModule._ModelInstanceFactoryModule.Server.NewinstancesCallContext, **kwargs: Any) -> Awaitable[_ClusterModule._ValueHolderModule.Server | _ClusterModule._ModelInstanceFactoryModule.Server.NewinstancesResultTuple | None]: ...
            def newInstances_context(self, context: _ClusterModule._ModelInstanceFactoryModule.Server.NewinstancesCallContext) -> Awaitable[None]: ...
            def newCloudViaZmqPipelineProxies(
                self, numberOfInstances: int, _context: _ClusterModule._ModelInstanceFactoryModule.Server.NewcloudviazmqpipelineproxiesCallContext, **kwargs: Any
            ) -> Awaitable[_ClusterModule._ValueHolderModule.Server | _ClusterModule._ModelInstanceFactoryModule.Server.NewcloudviazmqpipelineproxiesResultTuple | None]: ...
            def newCloudViaZmqPipelineProxies_context(self, context: _ClusterModule._ModelInstanceFactoryModule.Server.NewcloudviazmqpipelineproxiesCallContext) -> Awaitable[None]: ...
            def newCloudViaProxy(self, numberOfInstances: int, _context: _ClusterModule._ModelInstanceFactoryModule.Server.NewcloudviaproxyCallContext, **kwargs: Any) -> Awaitable[_ClusterModule._ValueHolderModule.Server | _ClusterModule._ModelInstanceFactoryModule.Server.NewcloudviaproxyResultTuple | None]: ...
            def newCloudViaProxy_context(self, context: _ClusterModule._ModelInstanceFactoryModule.Server.NewcloudviaproxyCallContext) -> Awaitable[None]: ...
            def modelId(self, _context: _ClusterModule._ModelInstanceFactoryModule.Server.ModelidCallContext, **kwargs: Any) -> Awaitable[str | _ClusterModule._ModelInstanceFactoryModule.Server.ModelidResultTuple | None]: ...
            def modelId_context(self, context: _ClusterModule._ModelInstanceFactoryModule.Server.ModelidCallContext) -> Awaitable[None]: ...
            def registerModelInstance(
                self, instance: AnyPointer, registrationToken: str, _context: _ClusterModule._ModelInstanceFactoryModule.Server.RegistermodelinstanceCallContext, **kwargs: Any
            ) -> Awaitable[_ClusterModule._UnregisterModule.Server | _ClusterModule._ModelInstanceFactoryModule.Server.RegistermodelinstanceResultTuple | None]: ...
            def registerModelInstance_context(self, context: _ClusterModule._ModelInstanceFactoryModule.Server.RegistermodelinstanceCallContext) -> Awaitable[None]: ...
            def restoreSturdyRef(self, sturdyRef: str, _context: _ClusterModule._ModelInstanceFactoryModule.Server.RestoresturdyrefCallContext, **kwargs: Any) -> Awaitable[_ClusterModule._ValueHolderModule.Server | _ClusterModule._ModelInstanceFactoryModule.Server.RestoresturdyrefResultTuple | None]: ...
            def restoreSturdyRef_context(self, context: _ClusterModule._ModelInstanceFactoryModule.Server.RestoresturdyrefCallContext) -> Awaitable[None]: ...

        class ModelInstanceFactoryClient(_IdentifiableModule.IdentifiableClient):
            class NewinstanceResult(Awaitable[NewinstanceResult], Protocol):
                instance: _ClusterModule._ValueHolderModule.ValueHolderClient

            class NewinstancesResult(Awaitable[NewinstancesResult], Protocol):
                instances: _ClusterModule._ValueHolderModule.ValueHolderClient

            class NewcloudviazmqpipelineproxiesResult(Awaitable[NewcloudviazmqpipelineproxiesResult], Protocol):
                proxyAddresses: _ClusterModule._ValueHolderModule.ValueHolderClient

            class NewcloudviaproxyResult(Awaitable[NewcloudviaproxyResult], Protocol):
                proxy: _ClusterModule._ValueHolderModule.ValueHolderClient

            class ModelidResult(Awaitable[ModelidResult], Protocol):
                id: str

            class RegistermodelinstanceResult(Awaitable[RegistermodelinstanceResult], Protocol):
                unregister: _ClusterModule._UnregisterModule.UnregisterClient

            class RestoresturdyrefResult(Awaitable[RestoresturdyrefResult], Protocol):
                cap: _ClusterModule._ValueHolderModule.ValueHolderClient

            def newInstance(self) -> _ClusterModule._ModelInstanceFactoryModule.ModelInstanceFactoryClient.NewinstanceResult: ...
            def newInstances(self, numberOfInstances: int | None = None) -> _ClusterModule._ModelInstanceFactoryModule.ModelInstanceFactoryClient.NewinstancesResult: ...
            def newCloudViaZmqPipelineProxies(self, numberOfInstances: int | None = None) -> _ClusterModule._ModelInstanceFactoryModule.ModelInstanceFactoryClient.NewcloudviazmqpipelineproxiesResult: ...
            def newCloudViaProxy(self, numberOfInstances: int | None = None) -> _ClusterModule._ModelInstanceFactoryModule.ModelInstanceFactoryClient.NewcloudviaproxyResult: ...
            def modelId(self) -> _ClusterModule._ModelInstanceFactoryModule.ModelInstanceFactoryClient.ModelidResult: ...
            def registerModelInstance(self, instance: _DynamicObjectReader | None = None, registrationToken: str | None = None) -> _ClusterModule._ModelInstanceFactoryModule.ModelInstanceFactoryClient.RegistermodelinstanceResult: ...
            def restoreSturdyRef(self, sturdyRef: str | None = None) -> _ClusterModule._ModelInstanceFactoryModule.ModelInstanceFactoryClient.RestoresturdyrefResult: ...
            def newInstance_request(self) -> _ClusterModule._ModelInstanceFactoryModule.NewinstanceRequest: ...
            def newInstances_request(self, numberOfInstances: int | None = None) -> _ClusterModule._ModelInstanceFactoryModule.NewinstancesRequest: ...
            def newCloudViaZmqPipelineProxies_request(self, numberOfInstances: int | None = None) -> _ClusterModule._ModelInstanceFactoryModule.NewcloudviazmqpipelineproxiesRequest: ...
            def newCloudViaProxy_request(self, numberOfInstances: int | None = None) -> _ClusterModule._ModelInstanceFactoryModule.NewcloudviaproxyRequest: ...
            def modelId_request(self) -> _ClusterModule._ModelInstanceFactoryModule.ModelidRequest: ...
            def registerModelInstance_request(self, instance: AnyPointer | None = None, registrationToken: str | None = None) -> _ClusterModule._ModelInstanceFactoryModule.RegistermodelinstanceRequest: ...
            def restoreSturdyRef_request(self, sturdyRef: str | None = None) -> _ClusterModule._ModelInstanceFactoryModule.RestoresturdyrefRequest: ...

    ModelInstanceFactory: _ModelInstanceFactoryModule
    type ModelInstanceFactoryClient = _ClusterModule._ModelInstanceFactoryModule.ModelInstanceFactoryClient
    class Reader(_DynamicStructReader):
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> ClusterBuilder: ...

    class Builder(_DynamicStructBuilder):
        @override
        def as_reader(self) -> ClusterReader: ...

    @override
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> ClusterBuilder: ...

Cluster: _ClusterModule

# Top-level type aliases for use in type annotations
type AdminMasterClient = _ClusterModule._AdminMasterModule.AdminMasterClient
type ClusterBuilder = _ClusterModule.Builder
type ClusterReader = _ClusterModule.Reader
type ModelInstanceFactoryClient = _ClusterModule._ModelInstanceFactoryModule.ModelInstanceFactoryClient
type RuntimeClient = _ClusterModule._RuntimeModule.RuntimeClient
type UnregisterClient = _ClusterModule._UnregisterModule.UnregisterClient
type UserMasterClient = _ClusterModule._UserMasterModule.UserMasterClient
type ValueHolderClient = _ClusterModule._ValueHolderModule.ValueHolderClient
type ZmqPipelineAddressesBuilder = _ClusterModule._ZmqPipelineAddressesModule.Builder
type ZmqPipelineAddressesReader = _ClusterModule._ZmqPipelineAddressesModule.Reader
