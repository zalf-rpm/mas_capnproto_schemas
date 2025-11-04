"""This is an automatically generated stub for `cluster_admin_service.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator
from contextlib import contextmanager
from io import BufferedWriter
from typing import Any, BinaryIO, Protocol

from .common_capnp import Identifiable

class Cluster:
    class Unregister(Protocol):
        class UnregisterResult(Awaitable[UnregisterResult], Protocol):
            success: bool

        def unregister(self) -> UnregisterResult: ...
        class UnregisterRequest(Protocol):
            def send(self) -> Cluster.Unregister.UnregisterResult: ...

        def unregister_request(self) -> UnregisterRequest: ...
        class Server:
            def unregister(self, **kwargs) -> Awaitable[bool]: ...

    class AdminMaster(Identifiable, Protocol):
        class RegistermodelinstancefactoryResult(
            Awaitable[RegistermodelinstancefactoryResult], Protocol
        ):
            unregister: Cluster.Unregister

        def registerModelInstanceFactory(
            self, aModelId: str, aFactory: Any
        ) -> RegistermodelinstancefactoryResult: ...
        class RegistermodelinstancefactoryRequest(Protocol):
            aModelId: str
            aFactory: Any
            def send(
                self,
            ) -> Cluster.AdminMaster.RegistermodelinstancefactoryResult: ...

        def registerModelInstanceFactory_request(
            self,
        ) -> RegistermodelinstancefactoryRequest: ...
        class AvailablemodelsResult(Awaitable[AvailablemodelsResult], Protocol):
            factories: Any

        def availableModels(self) -> AvailablemodelsResult: ...
        class AvailablemodelsRequest(Protocol):
            def send(self) -> Cluster.AdminMaster.AvailablemodelsResult: ...

        def availableModels_request(self) -> AvailablemodelsRequest: ...
        class Server(Identifiable.Server):
            def registerModelInstanceFactory(
                self, aModelId: str, aFactory: Any, **kwargs
            ) -> Awaitable[Cluster.Unregister | Cluster.Unregister.Server]: ...
            def availableModels(self, **kwargs) -> Awaitable[Any]: ...

    class UserMaster(Identifiable, Protocol):
        class AvailablemodelsResult(Awaitable[AvailablemodelsResult], Protocol):
            factories: Any

        def availableModels(self) -> AvailablemodelsResult: ...
        class AvailablemodelsRequest(Protocol):
            def send(self) -> Cluster.UserMaster.AvailablemodelsResult: ...

        def availableModels_request(self) -> AvailablemodelsRequest: ...
        class Server(Identifiable.Server):
            def availableModels(self, **kwargs) -> Awaitable[Any]: ...

    class Runtime(Identifiable, Protocol):
        class RegistermodelinstancefactoryResult(
            Awaitable[RegistermodelinstancefactoryResult], Protocol
        ):
            unregister: Cluster.Unregister

        def registerModelInstanceFactory(
            self, aModelId: str, aFactory: Any
        ) -> RegistermodelinstancefactoryResult: ...
        class RegistermodelinstancefactoryRequest(Protocol):
            aModelId: str
            aFactory: Any
            def send(self) -> Cluster.Runtime.RegistermodelinstancefactoryResult: ...

        def registerModelInstanceFactory_request(
            self,
        ) -> RegistermodelinstancefactoryRequest: ...
        class AvailablemodelsResult(Awaitable[AvailablemodelsResult], Protocol):
            factories: Any

        def availableModels(self) -> AvailablemodelsResult: ...
        class AvailablemodelsRequest(Protocol):
            def send(self) -> Cluster.Runtime.AvailablemodelsResult: ...

        def availableModels_request(self) -> AvailablemodelsRequest: ...
        class NumberofcoresResult(Awaitable[NumberofcoresResult], Protocol):
            cores: int

        def numberOfCores(self) -> NumberofcoresResult: ...
        class NumberofcoresRequest(Protocol):
            def send(self) -> Cluster.Runtime.NumberofcoresResult: ...

        def numberOfCores_request(self) -> NumberofcoresRequest: ...
        class FreenumberofcoresResult(Awaitable[FreenumberofcoresResult], Protocol):
            cores: int

        def freeNumberOfCores(self) -> FreenumberofcoresResult: ...
        class FreenumberofcoresRequest(Protocol):
            def send(self) -> Cluster.Runtime.FreenumberofcoresResult: ...

        def freeNumberOfCores_request(self) -> FreenumberofcoresRequest: ...
        class ReservenumberofcoresResult(
            Awaitable[ReservenumberofcoresResult], Protocol
        ):
            reservedCores: int

        def reserveNumberOfCores(
            self, reserveCores: int, aModelId: str
        ) -> ReservenumberofcoresResult: ...
        class ReservenumberofcoresRequest(Protocol):
            reserveCores: int
            aModelId: str
            def send(self) -> Cluster.Runtime.ReservenumberofcoresResult: ...

        def reserveNumberOfCores_request(self) -> ReservenumberofcoresRequest: ...
        class Server(Identifiable.Server):
            def registerModelInstanceFactory(
                self, aModelId: str, aFactory: Any, **kwargs
            ) -> Awaitable[Cluster.Unregister | Cluster.Unregister.Server]: ...
            def availableModels(self, **kwargs) -> Awaitable[Any]: ...
            def numberOfCores(self, **kwargs) -> Awaitable[int]: ...
            def freeNumberOfCores(self, **kwargs) -> Awaitable[int]: ...
            def reserveNumberOfCores(
                self, reserveCores: int, aModelId: str, **kwargs
            ) -> Awaitable[int]: ...

    class ZmqPipelineAddresses:
        @property
        def input(self) -> str: ...
        @property
        def output(self) -> str: ...
        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Cluster.ZmqPipelineAddressesReader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Cluster.ZmqPipelineAddressesReader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            input: str | None = None,
            output: str | None = None,
        ) -> Cluster.ZmqPipelineAddressesBuilder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Cluster.ZmqPipelineAddressesReader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Cluster.ZmqPipelineAddressesReader: ...
        def to_dict(self) -> dict[str, Any]: ...

    class ZmqPipelineAddressesReader(Cluster.ZmqPipelineAddresses):
        def as_builder(self) -> Cluster.ZmqPipelineAddressesBuilder: ...

    class ZmqPipelineAddressesBuilder(Cluster.ZmqPipelineAddresses):
        @property
        def input(self) -> str: ...
        @input.setter
        def input(self, value: str) -> None: ...
        @property
        def output(self) -> str: ...
        @output.setter
        def output(self, value: str) -> None: ...
        @staticmethod
        def from_dict(
            dictionary: dict[str, Any],
        ) -> Cluster.ZmqPipelineAddressesBuilder: ...
        def copy(self) -> Cluster.ZmqPipelineAddressesBuilder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> Cluster.ZmqPipelineAddressesReader: ...
        @staticmethod
        def write(file: BufferedWriter) -> None: ...
        @staticmethod
        def write_packed(file: BufferedWriter) -> None: ...

    class ValueHolder(Protocol):
        class ValueResult(Awaitable[ValueResult], Protocol):
            val: Any

        def value(self) -> ValueResult: ...
        class ValueRequest(Protocol):
            def send(self) -> Cluster.ValueHolder.ValueResult: ...

        def value_request(self) -> ValueRequest: ...
        def release(self) -> None: ...
        class ReleaseRequest(Protocol):
            def send(self) -> Any: ...

        def release_request(self) -> ReleaseRequest: ...
        class Server:
            def value(self, **kwargs) -> Awaitable[Any]: ...
            def release(self, **kwargs) -> None: ...

    class ModelInstanceFactory(Identifiable, Protocol):
        class NewinstanceResult(Awaitable[NewinstanceResult], Protocol):
            instance: Cluster.ValueHolder

        def newInstance(self) -> NewinstanceResult: ...
        class NewinstanceRequest(Protocol):
            def send(self) -> Cluster.ModelInstanceFactory.NewinstanceResult: ...

        def newInstance_request(self) -> NewinstanceRequest: ...
        class NewinstancesResult(Awaitable[NewinstancesResult], Protocol):
            instances: Cluster.ValueHolder

        def newInstances(self, numberOfInstances: int) -> NewinstancesResult: ...
        class NewinstancesRequest(Protocol):
            numberOfInstances: int
            def send(self) -> Cluster.ModelInstanceFactory.NewinstancesResult: ...

        def newInstances_request(self) -> NewinstancesRequest: ...
        class NewcloudviazmqpipelineproxiesResult(
            Awaitable[NewcloudviazmqpipelineproxiesResult], Protocol
        ):
            proxyAddresses: Cluster.ValueHolder

        def newCloudViaZmqPipelineProxies(
            self, numberOfInstances: int
        ) -> NewcloudviazmqpipelineproxiesResult: ...
        class NewcloudviazmqpipelineproxiesRequest(Protocol):
            numberOfInstances: int
            def send(
                self,
            ) -> Cluster.ModelInstanceFactory.NewcloudviazmqpipelineproxiesResult: ...

        def newCloudViaZmqPipelineProxies_request(
            self,
        ) -> NewcloudviazmqpipelineproxiesRequest: ...
        class NewcloudviaproxyResult(Awaitable[NewcloudviaproxyResult], Protocol):
            proxy: Cluster.ValueHolder

        def newCloudViaProxy(
            self, numberOfInstances: int
        ) -> NewcloudviaproxyResult: ...
        class NewcloudviaproxyRequest(Protocol):
            numberOfInstances: int
            def send(self) -> Cluster.ModelInstanceFactory.NewcloudviaproxyResult: ...

        def newCloudViaProxy_request(self) -> NewcloudviaproxyRequest: ...
        class ModelidResult(Awaitable[ModelidResult], Protocol):
            id: str

        def modelId(self) -> ModelidResult: ...
        class ModelidRequest(Protocol):
            def send(self) -> Cluster.ModelInstanceFactory.ModelidResult: ...

        def modelId_request(self) -> ModelidRequest: ...
        class RegistermodelinstanceResult(
            Awaitable[RegistermodelinstanceResult], Protocol
        ):
            unregister: Cluster.Unregister

        def registerModelInstance(
            self, instance: Any, registrationToken: str
        ) -> RegistermodelinstanceResult: ...
        class RegistermodelinstanceRequest(Protocol):
            instance: Any
            registrationToken: str
            def send(
                self,
            ) -> Cluster.ModelInstanceFactory.RegistermodelinstanceResult: ...

        def registerModelInstance_request(self) -> RegistermodelinstanceRequest: ...
        class RestoresturdyrefResult(Awaitable[RestoresturdyrefResult], Protocol):
            cap: Cluster.ValueHolder

        def restoreSturdyRef(self, sturdyRef: str) -> RestoresturdyrefResult: ...
        class RestoresturdyrefRequest(Protocol):
            sturdyRef: str
            def send(self) -> Cluster.ModelInstanceFactory.RestoresturdyrefResult: ...

        def restoreSturdyRef_request(self) -> RestoresturdyrefRequest: ...
        class Server(Identifiable.Server):
            def newInstance(
                self, **kwargs
            ) -> Awaitable[Cluster.ValueHolder | Cluster.ValueHolder.Server]: ...
            def newInstances(
                self, numberOfInstances: int, **kwargs
            ) -> Awaitable[Cluster.ValueHolder | Cluster.ValueHolder.Server]: ...
            def newCloudViaZmqPipelineProxies(
                self, numberOfInstances: int, **kwargs
            ) -> Awaitable[Cluster.ValueHolder | Cluster.ValueHolder.Server]: ...
            def newCloudViaProxy(
                self, numberOfInstances: int, **kwargs
            ) -> Awaitable[Cluster.ValueHolder | Cluster.ValueHolder.Server]: ...
            def modelId(self, **kwargs) -> Awaitable[str]: ...
            def registerModelInstance(
                self, instance: Any, registrationToken: str, **kwargs
            ) -> Awaitable[Cluster.Unregister | Cluster.Unregister.Server]: ...
            def restoreSturdyRef(
                self, sturdyRef: str, **kwargs
            ) -> Awaitable[Cluster.ValueHolder | Cluster.ValueHolder.Server]: ...

    @staticmethod
    @contextmanager
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[ClusterReader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> ClusterReader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None, allocate_seg_callable: Any = None
    ) -> ClusterBuilder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> ClusterReader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> ClusterReader: ...
    def to_dict(self) -> dict[str, Any]: ...

class ClusterReader(Cluster):
    def as_builder(self) -> ClusterBuilder: ...

class ClusterBuilder(Cluster):
    @staticmethod
    def from_dict(dictionary: dict[str, Any]) -> ClusterBuilder: ...
    def copy(self) -> ClusterBuilder: ...
    def to_bytes(self) -> bytes: ...
    def to_bytes_packed(self) -> bytes: ...
    def to_segments(self) -> list[bytes]: ...
    def as_reader(self) -> ClusterReader: ...
    @staticmethod
    def write(file: BufferedWriter) -> None: ...
    @staticmethod
    def write_packed(file: BufferedWriter) -> None: ...
