"""This is an automatically generated stub for `cluster_admin_service.capnp`."""

from collections.abc import Awaitable, Callable, Iterator, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, NamedTuple, Protocol, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicListBuilder,
    _DynamicListReader,
    _DynamicObjectBuilder,
    _DynamicObjectReader,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
    _StructModule,
)

from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule

# Type alias for AnyPointer parameters (accepts all Cap'n Proto pointer types)
type AnyPointer = (
    str
    | bytes
    | _DynamicStructBuilder
    | _DynamicStructReader
    | _DynamicCapabilityClient
    | _DynamicCapabilityServer
    | _DynamicListBuilder
    | _DynamicListReader
    | _DynamicObjectReader
    | _DynamicObjectBuilder
)

class UnregisterRequest(Protocol):
    def send(self) -> UnregisterResult: ...

class UnregisterResult(Awaitable[UnregisterResult], Protocol):
    success: bool

class UnregisterServerResult(_DynamicStructBuilder):
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class UnregisterParams(Protocol): ...

class UnregisterCallContext(Protocol):
    params: UnregisterParams
    @property
    def results(self) -> UnregisterServerResult: ...

class UnregisterResultTuple(NamedTuple):
    success: bool

class UnregisterClient(_DynamicCapabilityClient):
    def unregister(self) -> UnregisterResult: ...
    def unregister_request(self) -> UnregisterRequest: ...

class NewinstanceRequest(Protocol):
    def send(self) -> NewinstanceResult: ...

class ValueRequest(Protocol):
    def send(self) -> ValueResult: ...

class ValueResult(Awaitable[ValueResult], Protocol):
    val: _DynamicObjectReader

class ValueServerResult(_DynamicStructBuilder):
    @property
    def val(self) -> AnyPointer: ...
    @val.setter
    def val(self, value: AnyPointer) -> None: ...

class ValueParams(Protocol): ...

class ValueCallContext(Protocol):
    params: ValueParams
    @property
    def results(self) -> ValueServerResult: ...

class ValueResultTuple(NamedTuple):
    val: AnyPointer

class ReleaseRequest(Protocol):
    def send(self) -> ReleaseResult: ...

class ReleaseResult(Awaitable[None], Protocol): ...
class ReleaseParams(Protocol): ...

class ReleaseCallContext(Protocol):
    params: ReleaseParams

class ValueHolderClient(_DynamicCapabilityClient):
    def value(self) -> ValueResult: ...
    def release(self) -> ReleaseResult: ...
    def value_request(self) -> ValueRequest: ...
    def release_request(self) -> ReleaseRequest: ...

class NewinstanceResult(Awaitable[NewinstanceResult], Protocol):
    instance: ValueHolderClient

class NewinstanceServerResult(_DynamicStructBuilder):
    @property
    def instance(
        self,
    ) -> (
        _ClusterStructModule._ValueHolderInterfaceModule.Server | ValueHolderClient
    ): ...
    @instance.setter
    def instance(
        self,
        value: _ClusterStructModule._ValueHolderInterfaceModule.Server
        | ValueHolderClient,
    ) -> None: ...

class NewinstanceParams(Protocol): ...

class NewinstanceCallContext(Protocol):
    params: NewinstanceParams
    @property
    def results(self) -> NewinstanceServerResult: ...

class NewinstanceResultTuple(NamedTuple):
    instance: (
        _ClusterStructModule._ValueHolderInterfaceModule.Server | ValueHolderClient
    )

class NewinstancesRequest(Protocol):
    numberOfInstances: int
    def send(self) -> NewinstancesResult: ...

class NewinstancesResult(Awaitable[NewinstancesResult], Protocol):
    instances: ValueHolderClient

class NewinstancesServerResult(_DynamicStructBuilder):
    @property
    def instances(
        self,
    ) -> (
        _ClusterStructModule._ValueHolderInterfaceModule.Server | ValueHolderClient
    ): ...
    @instances.setter
    def instances(
        self,
        value: _ClusterStructModule._ValueHolderInterfaceModule.Server
        | ValueHolderClient,
    ) -> None: ...

class NewinstancesParams(Protocol):
    numberOfInstances: int

class NewinstancesCallContext(Protocol):
    params: NewinstancesParams
    @property
    def results(self) -> NewinstancesServerResult: ...

class NewinstancesResultTuple(NamedTuple):
    instances: (
        _ClusterStructModule._ValueHolderInterfaceModule.Server | ValueHolderClient
    )

class NewcloudviazmqpipelineproxiesRequest(Protocol):
    numberOfInstances: int
    def send(self) -> NewcloudviazmqpipelineproxiesResult: ...

class NewcloudviazmqpipelineproxiesResult(
    Awaitable[NewcloudviazmqpipelineproxiesResult],
    Protocol,
):
    proxyAddresses: ValueHolderClient

class NewcloudviazmqpipelineproxiesServerResult(_DynamicStructBuilder):
    @property
    def proxyAddresses(
        self,
    ) -> (
        _ClusterStructModule._ValueHolderInterfaceModule.Server | ValueHolderClient
    ): ...
    @proxyAddresses.setter
    def proxyAddresses(
        self,
        value: _ClusterStructModule._ValueHolderInterfaceModule.Server
        | ValueHolderClient,
    ) -> None: ...

class NewcloudviazmqpipelineproxiesParams(Protocol):
    numberOfInstances: int

class NewcloudviazmqpipelineproxiesCallContext(Protocol):
    params: NewcloudviazmqpipelineproxiesParams
    @property
    def results(self) -> NewcloudviazmqpipelineproxiesServerResult: ...

class NewcloudviazmqpipelineproxiesResultTuple(NamedTuple):
    proxyAddresses: (
        _ClusterStructModule._ValueHolderInterfaceModule.Server | ValueHolderClient
    )

class NewcloudviaproxyRequest(Protocol):
    numberOfInstances: int
    def send(self) -> NewcloudviaproxyResult: ...

class NewcloudviaproxyResult(Awaitable[NewcloudviaproxyResult], Protocol):
    proxy: ValueHolderClient

class NewcloudviaproxyServerResult(_DynamicStructBuilder):
    @property
    def proxy(
        self,
    ) -> (
        _ClusterStructModule._ValueHolderInterfaceModule.Server | ValueHolderClient
    ): ...
    @proxy.setter
    def proxy(
        self,
        value: _ClusterStructModule._ValueHolderInterfaceModule.Server
        | ValueHolderClient,
    ) -> None: ...

class NewcloudviaproxyParams(Protocol):
    numberOfInstances: int

class NewcloudviaproxyCallContext(Protocol):
    params: NewcloudviaproxyParams
    @property
    def results(self) -> NewcloudviaproxyServerResult: ...

class NewcloudviaproxyResultTuple(NamedTuple):
    proxy: _ClusterStructModule._ValueHolderInterfaceModule.Server | ValueHolderClient

class ModelidRequest(Protocol):
    def send(self) -> ModelidResult: ...

class ModelidResult(Awaitable[ModelidResult], Protocol):
    id: str

class ModelidServerResult(_DynamicStructBuilder):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str) -> None: ...

class ModelidParams(Protocol): ...

class ModelidCallContext(Protocol):
    params: ModelidParams
    @property
    def results(self) -> ModelidServerResult: ...

class ModelidResultTuple(NamedTuple):
    id: str

class RegistermodelinstanceRequest(Protocol):
    instance: AnyPointer
    registrationToken: str
    def send(self) -> RegistermodelinstanceResult: ...

class RegistermodelinstanceResult(Awaitable[RegistermodelinstanceResult], Protocol):
    unregister: UnregisterClient

class RegistermodelinstanceServerResult(_DynamicStructBuilder):
    @property
    def unregister(
        self,
    ) -> _ClusterStructModule._UnregisterInterfaceModule.Server | UnregisterClient: ...
    @unregister.setter
    def unregister(
        self,
        value: _ClusterStructModule._UnregisterInterfaceModule.Server
        | UnregisterClient,
    ) -> None: ...

class RegistermodelinstanceParams(Protocol):
    instance: AnyPointer
    registrationToken: str

class RegistermodelinstanceCallContext(Protocol):
    params: RegistermodelinstanceParams
    @property
    def results(self) -> RegistermodelinstanceServerResult: ...

class RegistermodelinstanceResultTuple(NamedTuple):
    unregister: (
        _ClusterStructModule._UnregisterInterfaceModule.Server | UnregisterClient
    )

class RestoresturdyrefRequest(Protocol):
    sturdyRef: str
    def send(self) -> RestoresturdyrefResult: ...

class RestoresturdyrefResult(Awaitable[RestoresturdyrefResult], Protocol):
    cap: ValueHolderClient

class RestoresturdyrefServerResult(_DynamicStructBuilder):
    @property
    def cap(
        self,
    ) -> (
        _ClusterStructModule._ValueHolderInterfaceModule.Server | ValueHolderClient
    ): ...
    @cap.setter
    def cap(
        self,
        value: _ClusterStructModule._ValueHolderInterfaceModule.Server
        | ValueHolderClient,
    ) -> None: ...

class RestoresturdyrefParams(Protocol):
    sturdyRef: str

class RestoresturdyrefCallContext(Protocol):
    params: RestoresturdyrefParams
    @property
    def results(self) -> RestoresturdyrefServerResult: ...

class RestoresturdyrefResultTuple(NamedTuple):
    cap: _ClusterStructModule._ValueHolderInterfaceModule.Server | ValueHolderClient

class ModelInstanceFactoryClient(IdentifiableClient):
    def newInstance(self) -> NewinstanceResult: ...
    def newInstances(
        self,
        numberOfInstances: int | None = None,
    ) -> NewinstancesResult: ...
    def newCloudViaZmqPipelineProxies(
        self,
        numberOfInstances: int | None = None,
    ) -> NewcloudviazmqpipelineproxiesResult: ...
    def newCloudViaProxy(
        self,
        numberOfInstances: int | None = None,
    ) -> NewcloudviaproxyResult: ...
    def modelId(self) -> ModelidResult: ...
    def registerModelInstance(
        self,
        instance: AnyPointer | None = None,
        registrationToken: str | None = None,
    ) -> RegistermodelinstanceResult: ...
    def restoreSturdyRef(
        self,
        sturdyRef: str | None = None,
    ) -> RestoresturdyrefResult: ...
    def newInstance_request(self) -> NewinstanceRequest: ...
    def newInstances_request(
        self,
        numberOfInstances: int | None = None,
    ) -> NewinstancesRequest: ...
    def newCloudViaZmqPipelineProxies_request(
        self,
        numberOfInstances: int | None = None,
    ) -> NewcloudviazmqpipelineproxiesRequest: ...
    def newCloudViaProxy_request(
        self,
        numberOfInstances: int | None = None,
    ) -> NewcloudviaproxyRequest: ...
    def modelId_request(self) -> ModelidRequest: ...
    def registerModelInstance_request(
        self,
        instance: AnyPointer | None = None,
        registrationToken: str | None = None,
    ) -> RegistermodelinstanceRequest: ...
    def restoreSturdyRef_request(
        self,
        sturdyRef: str | None = None,
    ) -> RestoresturdyrefRequest: ...

class AdminMasterRegistermodelinstancefactoryRequest(Protocol):
    aModelId: str
    aFactory: (
        ModelInstanceFactoryClient
        | _ClusterStructModule._ModelInstanceFactoryInterfaceModule.Server
    )
    def send(self) -> AdminMasterRegistermodelinstancefactoryResult: ...

class AdminMasterRegistermodelinstancefactoryResult(
    Awaitable[AdminMasterRegistermodelinstancefactoryResult],
    Protocol,
):
    unregister: UnregisterClient

class AdminMasterRegistermodelinstancefactoryServerResult(_DynamicStructBuilder):
    @property
    def unregister(
        self,
    ) -> _ClusterStructModule._UnregisterInterfaceModule.Server | UnregisterClient: ...
    @unregister.setter
    def unregister(
        self,
        value: _ClusterStructModule._UnregisterInterfaceModule.Server
        | UnregisterClient,
    ) -> None: ...

class AdminMasterRegistermodelinstancefactoryParams(Protocol):
    aModelId: str
    aFactory: ModelInstanceFactoryClient

class AdminMasterRegistermodelinstancefactoryCallContext(Protocol):
    params: AdminMasterRegistermodelinstancefactoryParams
    @property
    def results(self) -> AdminMasterRegistermodelinstancefactoryServerResult: ...

class AdminMasterRegistermodelinstancefactoryResultTuple(NamedTuple):
    unregister: (
        _ClusterStructModule._UnregisterInterfaceModule.Server | UnregisterClient
    )

class AdminMasterAvailablemodelsRequest(Protocol):
    def send(self) -> AdminMasterAvailablemodelsResult: ...

class _ModelInstanceFactoryClientList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> ModelInstanceFactoryClient: ...
        @override
        def __iter__(self) -> Iterator[ModelInstanceFactoryClient]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> ModelInstanceFactoryClient: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: ModelInstanceFactoryClient
            | _ClusterStructModule._ModelInstanceFactoryInterfaceModule.Server,
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[ModelInstanceFactoryClient]: ...

class AdminMasterAvailablemodelsResult(
    Awaitable[AdminMasterAvailablemodelsResult],
    Protocol,
):
    factories: ModelInstanceFactoryClientListReader

class AdminMasterAvailablemodelsServerResult(_DynamicStructBuilder):
    @property
    def factories(self) -> ModelInstanceFactoryClientListBuilder: ...
    @factories.setter
    def factories(
        self,
        value: ModelInstanceFactoryClientListBuilder
        | ModelInstanceFactoryClientListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["factories"],
        size: int | None = None,
    ) -> ModelInstanceFactoryClientListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class AdminMasterAvailablemodelsParams(Protocol): ...

class AdminMasterAvailablemodelsCallContext(Protocol):
    params: AdminMasterAvailablemodelsParams
    @property
    def results(self) -> AdminMasterAvailablemodelsServerResult: ...

class AdminMasterAvailablemodelsResultTuple(NamedTuple):
    factories: (
        ModelInstanceFactoryClientListBuilder
        | ModelInstanceFactoryClientListReader
        | Sequence[Any]
    )

class AdminMasterClient(IdentifiableClient):
    def registerModelInstanceFactory(
        self,
        aModelId: str | None = None,
        aFactory: ModelInstanceFactoryClient
        | _ClusterStructModule._ModelInstanceFactoryInterfaceModule.Server
        | None = None,
    ) -> AdminMasterRegistermodelinstancefactoryResult: ...
    def availableModels(self) -> AdminMasterAvailablemodelsResult: ...
    def registerModelInstanceFactory_request(
        self,
        aModelId: str | None = None,
        aFactory: ModelInstanceFactoryClient
        | _ClusterStructModule._ModelInstanceFactoryInterfaceModule.Server
        | None = None,
    ) -> AdminMasterRegistermodelinstancefactoryRequest: ...
    def availableModels_request(self) -> AdminMasterAvailablemodelsRequest: ...

class UserMasterAvailablemodelsRequest(Protocol):
    def send(self) -> UserMasterAvailablemodelsResult: ...

class UserMasterAvailablemodelsResult(
    Awaitable[UserMasterAvailablemodelsResult],
    Protocol,
):
    factories: ModelInstanceFactoryClientListReader

class UserMasterAvailablemodelsServerResult(_DynamicStructBuilder):
    @property
    def factories(self) -> ModelInstanceFactoryClientListBuilder: ...
    @factories.setter
    def factories(
        self,
        value: ModelInstanceFactoryClientListBuilder
        | ModelInstanceFactoryClientListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["factories"],
        size: int | None = None,
    ) -> ModelInstanceFactoryClientListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class UserMasterAvailablemodelsParams(Protocol): ...

class UserMasterAvailablemodelsCallContext(Protocol):
    params: UserMasterAvailablemodelsParams
    @property
    def results(self) -> UserMasterAvailablemodelsServerResult: ...

class UserMasterAvailablemodelsResultTuple(NamedTuple):
    factories: (
        ModelInstanceFactoryClientListBuilder
        | ModelInstanceFactoryClientListReader
        | Sequence[Any]
    )

class UserMasterClient(IdentifiableClient):
    def availableModels(self) -> UserMasterAvailablemodelsResult: ...
    def availableModels_request(self) -> UserMasterAvailablemodelsRequest: ...

class RuntimeRegistermodelinstancefactoryRequest(Protocol):
    aModelId: str
    aFactory: (
        ModelInstanceFactoryClient
        | _ClusterStructModule._ModelInstanceFactoryInterfaceModule.Server
    )
    def send(self) -> RuntimeRegistermodelinstancefactoryResult: ...

class RuntimeRegistermodelinstancefactoryResult(
    Awaitable[RuntimeRegistermodelinstancefactoryResult],
    Protocol,
):
    unregister: UnregisterClient

class RuntimeRegistermodelinstancefactoryServerResult(_DynamicStructBuilder):
    @property
    def unregister(
        self,
    ) -> _ClusterStructModule._UnregisterInterfaceModule.Server | UnregisterClient: ...
    @unregister.setter
    def unregister(
        self,
        value: _ClusterStructModule._UnregisterInterfaceModule.Server
        | UnregisterClient,
    ) -> None: ...

class RuntimeRegistermodelinstancefactoryParams(Protocol):
    aModelId: str
    aFactory: ModelInstanceFactoryClient

class RuntimeRegistermodelinstancefactoryCallContext(Protocol):
    params: RuntimeRegistermodelinstancefactoryParams
    @property
    def results(self) -> RuntimeRegistermodelinstancefactoryServerResult: ...

class RuntimeRegistermodelinstancefactoryResultTuple(NamedTuple):
    unregister: (
        _ClusterStructModule._UnregisterInterfaceModule.Server | UnregisterClient
    )

class RuntimeAvailablemodelsRequest(Protocol):
    def send(self) -> RuntimeAvailablemodelsResult: ...

class RuntimeAvailablemodelsResult(Awaitable[RuntimeAvailablemodelsResult], Protocol):
    factories: ModelInstanceFactoryClientListReader

class RuntimeAvailablemodelsServerResult(_DynamicStructBuilder):
    @property
    def factories(self) -> ModelInstanceFactoryClientListBuilder: ...
    @factories.setter
    def factories(
        self,
        value: ModelInstanceFactoryClientListBuilder
        | ModelInstanceFactoryClientListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["factories"],
        size: int | None = None,
    ) -> ModelInstanceFactoryClientListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class RuntimeAvailablemodelsParams(Protocol): ...

class RuntimeAvailablemodelsCallContext(Protocol):
    params: RuntimeAvailablemodelsParams
    @property
    def results(self) -> RuntimeAvailablemodelsServerResult: ...

class RuntimeAvailablemodelsResultTuple(NamedTuple):
    factories: (
        ModelInstanceFactoryClientListBuilder
        | ModelInstanceFactoryClientListReader
        | Sequence[Any]
    )

class NumberofcoresRequest(Protocol):
    def send(self) -> NumberofcoresResult: ...

class NumberofcoresResult(Awaitable[NumberofcoresResult], Protocol):
    cores: int

class NumberofcoresServerResult(_DynamicStructBuilder):
    @property
    def cores(self) -> int: ...
    @cores.setter
    def cores(self, value: int) -> None: ...

class NumberofcoresParams(Protocol): ...

class NumberofcoresCallContext(Protocol):
    params: NumberofcoresParams
    @property
    def results(self) -> NumberofcoresServerResult: ...

class NumberofcoresResultTuple(NamedTuple):
    cores: int

class FreenumberofcoresRequest(Protocol):
    def send(self) -> FreenumberofcoresResult: ...

class FreenumberofcoresResult(Awaitable[FreenumberofcoresResult], Protocol):
    cores: int

class FreenumberofcoresServerResult(_DynamicStructBuilder):
    @property
    def cores(self) -> int: ...
    @cores.setter
    def cores(self, value: int) -> None: ...

class FreenumberofcoresParams(Protocol): ...

class FreenumberofcoresCallContext(Protocol):
    params: FreenumberofcoresParams
    @property
    def results(self) -> FreenumberofcoresServerResult: ...

class FreenumberofcoresResultTuple(NamedTuple):
    cores: int

class ReservenumberofcoresRequest(Protocol):
    reserveCores: int
    aModelId: str
    def send(self) -> ReservenumberofcoresResult: ...

class ReservenumberofcoresResult(Awaitable[ReservenumberofcoresResult], Protocol):
    reservedCores: int

class ReservenumberofcoresServerResult(_DynamicStructBuilder):
    @property
    def reservedCores(self) -> int: ...
    @reservedCores.setter
    def reservedCores(self, value: int) -> None: ...

class ReservenumberofcoresParams(Protocol):
    reserveCores: int
    aModelId: str

class ReservenumberofcoresCallContext(Protocol):
    params: ReservenumberofcoresParams
    @property
    def results(self) -> ReservenumberofcoresServerResult: ...

class ReservenumberofcoresResultTuple(NamedTuple):
    reservedCores: int

class RuntimeClient(IdentifiableClient):
    def registerModelInstanceFactory(
        self,
        aModelId: str | None = None,
        aFactory: ModelInstanceFactoryClient
        | _ClusterStructModule._ModelInstanceFactoryInterfaceModule.Server
        | None = None,
    ) -> RuntimeRegistermodelinstancefactoryResult: ...
    def availableModels(self) -> RuntimeAvailablemodelsResult: ...
    def numberOfCores(self) -> NumberofcoresResult: ...
    def freeNumberOfCores(self) -> FreenumberofcoresResult: ...
    def reserveNumberOfCores(
        self,
        reserveCores: int | None = None,
        aModelId: str | None = None,
    ) -> ReservenumberofcoresResult: ...
    def registerModelInstanceFactory_request(
        self,
        aModelId: str | None = None,
        aFactory: ModelInstanceFactoryClient
        | _ClusterStructModule._ModelInstanceFactoryInterfaceModule.Server
        | None = None,
    ) -> RuntimeRegistermodelinstancefactoryRequest: ...
    def availableModels_request(self) -> RuntimeAvailablemodelsRequest: ...
    def numberOfCores_request(self) -> NumberofcoresRequest: ...
    def freeNumberOfCores_request(self) -> FreenumberofcoresRequest: ...
    def reserveNumberOfCores_request(
        self,
        reserveCores: int | None = None,
        aModelId: str | None = None,
    ) -> ReservenumberofcoresRequest: ...

class ZmqPipelineAddressesReader(_DynamicStructReader):
    @property
    def input(self) -> str: ...
    @property
    def output(self) -> str: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> ZmqPipelineAddressesBuilder: ...

class ZmqPipelineAddressesBuilder(_DynamicStructBuilder):
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

class _ClusterStructModule(_StructModule):
    class _UnregisterInterfaceModule(_InterfaceModule):
        @override
        def _new_client(self, server: _DynamicCapabilityServer) -> UnregisterClient: ...
        class Server(_DynamicCapabilityServer):
            def unregister(
                self,
                _context: UnregisterCallContext,
                **kwargs: object,
            ) -> Awaitable[bool | UnregisterResultTuple | None]: ...
            def unregister_context(
                self,
                context: UnregisterCallContext,
            ) -> Awaitable[None]: ...

    Unregister: _UnregisterInterfaceModule
    type UnregisterServer = _ClusterStructModule._UnregisterInterfaceModule.Server
    class _AdminMasterInterfaceModule(_IdentifiableInterfaceModule):
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> AdminMasterClient: ...
        class Server(_IdentifiableInterfaceModule.Server):
            def registerModelInstanceFactory(
                self,
                aModelId: str,
                aFactory: ModelInstanceFactoryClient,
                _context: AdminMasterRegistermodelinstancefactoryCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _ClusterStructModule._UnregisterInterfaceModule.Server
                | UnregisterClient
                | AdminMasterRegistermodelinstancefactoryResultTuple
                | None
            ]: ...
            def registerModelInstanceFactory_context(
                self,
                context: AdminMasterRegistermodelinstancefactoryCallContext,
            ) -> Awaitable[None]: ...
            def availableModels(
                self,
                _context: AdminMasterAvailablemodelsCallContext,
                **kwargs: object,
            ) -> Awaitable[
                ModelInstanceFactoryClientListBuilder
                | ModelInstanceFactoryClientListReader
                | Sequence[Any]
                | AdminMasterAvailablemodelsResultTuple
                | None
            ]: ...
            def availableModels_context(
                self,
                context: AdminMasterAvailablemodelsCallContext,
            ) -> Awaitable[None]: ...

    class _ModelInstanceFactoryInterfaceModule(_IdentifiableInterfaceModule):
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> ModelInstanceFactoryClient: ...
        class Server(_IdentifiableInterfaceModule.Server):
            def newInstance(
                self,
                _context: NewinstanceCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _ClusterStructModule._ValueHolderInterfaceModule.Server
                | ValueHolderClient
                | NewinstanceResultTuple
                | None
            ]: ...
            def newInstance_context(
                self,
                context: NewinstanceCallContext,
            ) -> Awaitable[None]: ...
            def newInstances(
                self,
                numberOfInstances: int,
                _context: NewinstancesCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _ClusterStructModule._ValueHolderInterfaceModule.Server
                | ValueHolderClient
                | NewinstancesResultTuple
                | None
            ]: ...
            def newInstances_context(
                self,
                context: NewinstancesCallContext,
            ) -> Awaitable[None]: ...
            def newCloudViaZmqPipelineProxies(
                self,
                numberOfInstances: int,
                _context: NewcloudviazmqpipelineproxiesCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _ClusterStructModule._ValueHolderInterfaceModule.Server
                | ValueHolderClient
                | NewcloudviazmqpipelineproxiesResultTuple
                | None
            ]: ...
            def newCloudViaZmqPipelineProxies_context(
                self,
                context: NewcloudviazmqpipelineproxiesCallContext,
            ) -> Awaitable[None]: ...
            def newCloudViaProxy(
                self,
                numberOfInstances: int,
                _context: NewcloudviaproxyCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _ClusterStructModule._ValueHolderInterfaceModule.Server
                | ValueHolderClient
                | NewcloudviaproxyResultTuple
                | None
            ]: ...
            def newCloudViaProxy_context(
                self,
                context: NewcloudviaproxyCallContext,
            ) -> Awaitable[None]: ...
            def modelId(
                self,
                _context: ModelidCallContext,
                **kwargs: object,
            ) -> Awaitable[str | ModelidResultTuple | None]: ...
            def modelId_context(
                self,
                context: ModelidCallContext,
            ) -> Awaitable[None]: ...
            def registerModelInstance(
                self,
                instance: AnyPointer,
                registrationToken: str,
                _context: RegistermodelinstanceCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _ClusterStructModule._UnregisterInterfaceModule.Server
                | UnregisterClient
                | RegistermodelinstanceResultTuple
                | None
            ]: ...
            def registerModelInstance_context(
                self,
                context: RegistermodelinstanceCallContext,
            ) -> Awaitable[None]: ...
            def restoreSturdyRef(
                self,
                sturdyRef: str,
                _context: RestoresturdyrefCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _ClusterStructModule._ValueHolderInterfaceModule.Server
                | ValueHolderClient
                | RestoresturdyrefResultTuple
                | None
            ]: ...
            def restoreSturdyRef_context(
                self,
                context: RestoresturdyrefCallContext,
            ) -> Awaitable[None]: ...

    class _ValueHolderInterfaceModule(_InterfaceModule):
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> ValueHolderClient: ...
        class Server(_DynamicCapabilityServer):
            def value(
                self,
                _context: ValueCallContext,
                **kwargs: object,
            ) -> Awaitable[AnyPointer | ValueResultTuple | None]: ...
            def value_context(self, context: ValueCallContext) -> Awaitable[None]: ...
            def release(
                self,
                _context: ReleaseCallContext,
                **kwargs: object,
            ) -> Awaitable[None]: ...
            def release_context(
                self,
                context: ReleaseCallContext,
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
        def _new_client(self, server: _DynamicCapabilityServer) -> UserMasterClient: ...
        class Server(_IdentifiableInterfaceModule.Server):
            def availableModels(
                self,
                _context: UserMasterAvailablemodelsCallContext,
                **kwargs: object,
            ) -> Awaitable[
                ModelInstanceFactoryClientListBuilder
                | ModelInstanceFactoryClientListReader
                | Sequence[Any]
                | UserMasterAvailablemodelsResultTuple
                | None
            ]: ...
            def availableModels_context(
                self,
                context: UserMasterAvailablemodelsCallContext,
            ) -> Awaitable[None]: ...

    UserMaster: _UserMasterInterfaceModule
    type UserMasterServer = _ClusterStructModule._UserMasterInterfaceModule.Server
    class _RuntimeInterfaceModule(_IdentifiableInterfaceModule):
        @override
        def _new_client(self, server: _DynamicCapabilityServer) -> RuntimeClient: ...
        class Server(_IdentifiableInterfaceModule.Server):
            def registerModelInstanceFactory(
                self,
                aModelId: str,
                aFactory: ModelInstanceFactoryClient,
                _context: RuntimeRegistermodelinstancefactoryCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _ClusterStructModule._UnregisterInterfaceModule.Server
                | UnregisterClient
                | RuntimeRegistermodelinstancefactoryResultTuple
                | None
            ]: ...
            def registerModelInstanceFactory_context(
                self,
                context: RuntimeRegistermodelinstancefactoryCallContext,
            ) -> Awaitable[None]: ...
            def availableModels(
                self,
                _context: RuntimeAvailablemodelsCallContext,
                **kwargs: object,
            ) -> Awaitable[
                ModelInstanceFactoryClientListBuilder
                | ModelInstanceFactoryClientListReader
                | Sequence[Any]
                | RuntimeAvailablemodelsResultTuple
                | None
            ]: ...
            def availableModels_context(
                self,
                context: RuntimeAvailablemodelsCallContext,
            ) -> Awaitable[None]: ...
            def numberOfCores(
                self,
                _context: NumberofcoresCallContext,
                **kwargs: object,
            ) -> Awaitable[int | NumberofcoresResultTuple | None]: ...
            def numberOfCores_context(
                self,
                context: NumberofcoresCallContext,
            ) -> Awaitable[None]: ...
            def freeNumberOfCores(
                self,
                _context: FreenumberofcoresCallContext,
                **kwargs: object,
            ) -> Awaitable[int | FreenumberofcoresResultTuple | None]: ...
            def freeNumberOfCores_context(
                self,
                context: FreenumberofcoresCallContext,
            ) -> Awaitable[None]: ...
            def reserveNumberOfCores(
                self,
                reserveCores: int,
                aModelId: str,
                _context: ReservenumberofcoresCallContext,
                **kwargs: object,
            ) -> Awaitable[int | ReservenumberofcoresResultTuple | None]: ...
            def reserveNumberOfCores_context(
                self,
                context: ReservenumberofcoresCallContext,
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
        ) -> ZmqPipelineAddressesBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[ZmqPipelineAddressesReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[ZmqPipelineAddressesReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[ZmqPipelineAddressesBuilder]: ...
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
        ) -> ZmqPipelineAddressesReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> ZmqPipelineAddressesReader: ...

    ZmqPipelineAddresses: _ZmqPipelineAddressesStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        **kwargs: object,
    ) -> ClusterBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[ClusterReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[ClusterReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[ClusterBuilder]: ...
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
    ) -> ClusterReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> ClusterReader: ...

class ClusterReader(_DynamicStructReader):
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> ClusterBuilder: ...

class ClusterBuilder(_DynamicStructBuilder):
    @override
    def as_reader(self) -> ClusterReader: ...

Cluster: _ClusterStructModule

# Top-level type aliases for use in type annotations
AdminMasterServer = _ClusterStructModule._AdminMasterInterfaceModule.Server
type ModelInstanceFactoryClientListBuilder = _ModelInstanceFactoryClientList.Builder
type ModelInstanceFactoryClientListReader = _ModelInstanceFactoryClientList.Reader
ModelInstanceFactoryServer = (
    _ClusterStructModule._ModelInstanceFactoryInterfaceModule.Server
)
RuntimeServer = _ClusterStructModule._RuntimeInterfaceModule.Server
UnregisterServer = _ClusterStructModule._UnregisterInterfaceModule.Server
UserMasterServer = _ClusterStructModule._UserMasterInterfaceModule.Server
ValueHolderServer = _ClusterStructModule._ValueHolderInterfaceModule.Server
