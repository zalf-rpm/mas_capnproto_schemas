"""Module helper types for `cluster_admin_service.capnp`."""

from collections.abc import Awaitable, Callable, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
    _StructModule,
)

from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule

from . import _all as _all

class _ClusterStructModule(_StructModule):
    class _UnregisterInterfaceModule(_InterfaceModule):
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> _all.UnregisterClient: ...
        class Server(_DynamicCapabilityServer):
            def unregister(
                self,
                _context: _all.UnregisterCallContext,
                **kwargs: object,
            ) -> Awaitable[bool | _all.UnregisterResultTuple | None]: ...
            def unregister_context(
                self,
                context: _all.UnregisterCallContext,
            ) -> Awaitable[None]: ...

    Unregister: _UnregisterInterfaceModule
    type UnregisterServer = _ClusterStructModule._UnregisterInterfaceModule.Server
    class _AdminMasterInterfaceModule(_IdentifiableInterfaceModule):
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> _all.AdminMasterClient: ...
        class Server(_IdentifiableInterfaceModule.Server):
            def registerModelInstanceFactory(
                self,
                aModelId: str,
                aFactory: _all.ModelInstanceFactoryClient,
                _context: _all.AdminMasterRegistermodelinstancefactoryCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _ClusterStructModule._UnregisterInterfaceModule.Server
                | _all.UnregisterClient
                | _all.AdminMasterRegistermodelinstancefactoryResultTuple
                | None
            ]: ...
            def registerModelInstanceFactory_context(
                self,
                context: _all.AdminMasterRegistermodelinstancefactoryCallContext,
            ) -> Awaitable[None]: ...
            def availableModels(
                self,
                _context: _all.AdminMasterAvailablemodelsCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _all.ModelInstanceFactoryClientListBuilder
                | _all.ModelInstanceFactoryClientListReader
                | Sequence[Any]
                | _all.AdminMasterAvailablemodelsResultTuple
                | None
            ]: ...
            def availableModels_context(
                self,
                context: _all.AdminMasterAvailablemodelsCallContext,
            ) -> Awaitable[None]: ...

    class _ModelInstanceFactoryInterfaceModule(_IdentifiableInterfaceModule):
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> _all.ModelInstanceFactoryClient: ...
        class Server(_IdentifiableInterfaceModule.Server):
            def newInstance(
                self,
                _context: _all.NewinstanceCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _ClusterStructModule._ValueHolderInterfaceModule.Server
                | _all.ValueHolderClient
                | _all.NewinstanceResultTuple
                | None
            ]: ...
            def newInstance_context(
                self,
                context: _all.NewinstanceCallContext,
            ) -> Awaitable[None]: ...
            def newInstances(
                self,
                numberOfInstances: int,
                _context: _all.NewinstancesCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _ClusterStructModule._ValueHolderInterfaceModule.Server
                | _all.ValueHolderClient
                | _all.NewinstancesResultTuple
                | None
            ]: ...
            def newInstances_context(
                self,
                context: _all.NewinstancesCallContext,
            ) -> Awaitable[None]: ...
            def newCloudViaZmqPipelineProxies(
                self,
                numberOfInstances: int,
                _context: _all.NewcloudviazmqpipelineproxiesCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _ClusterStructModule._ValueHolderInterfaceModule.Server
                | _all.ValueHolderClient
                | _all.NewcloudviazmqpipelineproxiesResultTuple
                | None
            ]: ...
            def newCloudViaZmqPipelineProxies_context(
                self,
                context: _all.NewcloudviazmqpipelineproxiesCallContext,
            ) -> Awaitable[None]: ...
            def newCloudViaProxy(
                self,
                numberOfInstances: int,
                _context: _all.NewcloudviaproxyCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _ClusterStructModule._ValueHolderInterfaceModule.Server
                | _all.ValueHolderClient
                | _all.NewcloudviaproxyResultTuple
                | None
            ]: ...
            def newCloudViaProxy_context(
                self,
                context: _all.NewcloudviaproxyCallContext,
            ) -> Awaitable[None]: ...
            def modelId(
                self,
                _context: _all.ModelidCallContext,
                **kwargs: object,
            ) -> Awaitable[str | _all.ModelidResultTuple | None]: ...
            def modelId_context(
                self,
                context: _all.ModelidCallContext,
            ) -> Awaitable[None]: ...
            def registerModelInstance(
                self,
                instance: _all.AnyPointer,
                registrationToken: str,
                _context: _all.RegistermodelinstanceCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _ClusterStructModule._UnregisterInterfaceModule.Server
                | _all.UnregisterClient
                | _all.RegistermodelinstanceResultTuple
                | None
            ]: ...
            def registerModelInstance_context(
                self,
                context: _all.RegistermodelinstanceCallContext,
            ) -> Awaitable[None]: ...
            def restoreSturdyRef(
                self,
                sturdyRef: str,
                _context: _all.RestoresturdyrefCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _ClusterStructModule._ValueHolderInterfaceModule.Server
                | _all.ValueHolderClient
                | _all.RestoresturdyrefResultTuple
                | None
            ]: ...
            def restoreSturdyRef_context(
                self,
                context: _all.RestoresturdyrefCallContext,
            ) -> Awaitable[None]: ...

    class _ValueHolderInterfaceModule(_InterfaceModule):
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> _all.ValueHolderClient: ...
        class Server(_DynamicCapabilityServer):
            def value(
                self,
                _context: _all.ValueCallContext,
                **kwargs: object,
            ) -> Awaitable[_all.AnyPointer | _all.ValueResultTuple | None]: ...
            def value_context(
                self,
                context: _all.ValueCallContext,
            ) -> Awaitable[None]: ...
            def release(
                self,
                _context: _all.ReleaseCallContext,
                **kwargs: object,
            ) -> Awaitable[None]: ...
            def release_context(
                self,
                context: _all.ReleaseCallContext,
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
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> _all.UserMasterClient: ...
        class Server(_IdentifiableInterfaceModule.Server):
            def availableModels(
                self,
                _context: _all.UserMasterAvailablemodelsCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _all.ModelInstanceFactoryClientListBuilder
                | _all.ModelInstanceFactoryClientListReader
                | Sequence[Any]
                | _all.UserMasterAvailablemodelsResultTuple
                | None
            ]: ...
            def availableModels_context(
                self,
                context: _all.UserMasterAvailablemodelsCallContext,
            ) -> Awaitable[None]: ...

    UserMaster: _UserMasterInterfaceModule
    type UserMasterServer = _ClusterStructModule._UserMasterInterfaceModule.Server
    class _RuntimeInterfaceModule(_IdentifiableInterfaceModule):
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> _all.RuntimeClient: ...
        class Server(_IdentifiableInterfaceModule.Server):
            def registerModelInstanceFactory(
                self,
                aModelId: str,
                aFactory: _all.ModelInstanceFactoryClient,
                _context: _all.RuntimeRegistermodelinstancefactoryCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _ClusterStructModule._UnregisterInterfaceModule.Server
                | _all.UnregisterClient
                | _all.RuntimeRegistermodelinstancefactoryResultTuple
                | None
            ]: ...
            def registerModelInstanceFactory_context(
                self,
                context: _all.RuntimeRegistermodelinstancefactoryCallContext,
            ) -> Awaitable[None]: ...
            def availableModels(
                self,
                _context: _all.RuntimeAvailablemodelsCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _all.ModelInstanceFactoryClientListBuilder
                | _all.ModelInstanceFactoryClientListReader
                | Sequence[Any]
                | _all.RuntimeAvailablemodelsResultTuple
                | None
            ]: ...
            def availableModels_context(
                self,
                context: _all.RuntimeAvailablemodelsCallContext,
            ) -> Awaitable[None]: ...
            def numberOfCores(
                self,
                _context: _all.NumberofcoresCallContext,
                **kwargs: object,
            ) -> Awaitable[int | _all.NumberofcoresResultTuple | None]: ...
            def numberOfCores_context(
                self,
                context: _all.NumberofcoresCallContext,
            ) -> Awaitable[None]: ...
            def freeNumberOfCores(
                self,
                _context: _all.FreenumberofcoresCallContext,
                **kwargs: object,
            ) -> Awaitable[int | _all.FreenumberofcoresResultTuple | None]: ...
            def freeNumberOfCores_context(
                self,
                context: _all.FreenumberofcoresCallContext,
            ) -> Awaitable[None]: ...
            def reserveNumberOfCores(
                self,
                reserveCores: int,
                aModelId: str,
                _context: _all.ReservenumberofcoresCallContext,
                **kwargs: object,
            ) -> Awaitable[int | _all.ReservenumberofcoresResultTuple | None]: ...
            def reserveNumberOfCores_context(
                self,
                context: _all.ReservenumberofcoresCallContext,
            ) -> Awaitable[None]: ...

    Runtime: _RuntimeInterfaceModule
    type RuntimeServer = _ClusterStructModule._RuntimeInterfaceModule.Server
    class _ZmqPipelineAddressesStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            input: str | None = None,
            output: str | None = None,
            **kwargs: object,
        ) -> _all.ZmqPipelineAddressesBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.ZmqPipelineAddressesReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.ZmqPipelineAddressesReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.ZmqPipelineAddressesBuilder]: ...
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
        ) -> _all.ZmqPipelineAddressesReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.ZmqPipelineAddressesReader: ...

    ZmqPipelineAddresses: _ZmqPipelineAddressesStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        **kwargs: object,
    ) -> _all.ClusterBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.ClusterReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.ClusterReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.ClusterBuilder]: ...
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
    ) -> _all.ClusterReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.ClusterReader: ...
