"""This is an automatically generated stub for `cluster_admin_service.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator
from contextlib import contextmanager
from io import BufferedWriter
from typing import Any, BinaryIO, NamedTuple, Protocol, TypeAlias

from .common_capnp import Identifiable, IdentifiableClient

ClusterBuilder: TypeAlias = Cluster.Builder
ClusterReader: TypeAlias = Cluster.Reader

class Cluster:
    class Unregister:
        class UnregisterRequest(Protocol):
            def send(self) -> Cluster.Unregister.UnregisterResult: ...

        class UnregisterResult(Awaitable[UnregisterResult], Protocol):
            success: bool

        @classmethod
        def _new_client(
            cls, server: Cluster.Unregister.Server
        ) -> Cluster.UnregisterClient: ...
        class Server(Protocol):
            class UnregisterResultTuple(NamedTuple):
                success: bool

            class UnregisterCallContext(Protocol):
                params: Cluster.Unregister.UnregisterRequest
                results: Cluster.Unregister.UnregisterResult

            def unregister(
                self,
                _context: Cluster.Unregister.Server.UnregisterCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                bool | Cluster.Unregister.Server.UnregisterResultTuple | None
            ]: ...
            def unregister_context(
                self, context: Cluster.Unregister.Server.UnregisterCallContext
            ) -> Awaitable[None]: ...

    class UnregisterClient(Protocol):
        def unregister(self) -> Cluster.Unregister.UnregisterResult: ...
        def unregister_request(self) -> Cluster.Unregister.UnregisterRequest: ...

    class AdminMaster:
        class RegistermodelinstancefactoryRequest(Protocol):
            aModelId: str
            def send(
                self,
            ) -> Cluster.AdminMaster.RegistermodelinstancefactoryResult: ...

        class RegistermodelinstancefactoryResult(
            Awaitable[RegistermodelinstancefactoryResult], Protocol
        ):
            unregister: Cluster.UnregisterClient

        class AvailablemodelsRequest(Protocol):
            def send(self) -> Cluster.AdminMaster.AvailablemodelsResult: ...

        class AvailablemodelsResult(Awaitable[AvailablemodelsResult], Protocol):
            factories: Any

        @classmethod
        def _new_client(
            cls, server: Cluster.AdminMaster.Server | Identifiable.Server
        ) -> Cluster.AdminMasterClient: ...
        class Server(Identifiable.Server):
            class RegistermodelinstancefactoryResultTuple(NamedTuple):
                unregister: Cluster.Unregister.Server

            class AvailablemodelsResultTuple(NamedTuple):
                pass

            class RegistermodelinstancefactoryCallContext(Protocol):
                params: Cluster.AdminMaster.RegistermodelinstancefactoryRequest
                results: Cluster.AdminMaster.RegistermodelinstancefactoryResult

            class AvailablemodelsCallContext(Protocol):
                params: Cluster.AdminMaster.AvailablemodelsRequest
                results: Cluster.AdminMaster.AvailablemodelsResult

            def registerModelInstanceFactory(
                self,
                aModelId: str,
                _context: Cluster.AdminMaster.Server.RegistermodelinstancefactoryCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                Cluster.Unregister.Server
                | Cluster.AdminMaster.Server.RegistermodelinstancefactoryResultTuple
                | None
            ]: ...
            def registerModelInstanceFactory_context(
                self,
                context: Cluster.AdminMaster.Server.RegistermodelinstancefactoryCallContext,
            ) -> Awaitable[None]: ...
            def availableModels(
                self,
                _context: Cluster.AdminMaster.Server.AvailablemodelsCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                Cluster.AdminMaster.Server.AvailablemodelsResultTuple | None
            ]: ...
            def availableModels_context(
                self, context: Cluster.AdminMaster.Server.AvailablemodelsCallContext
            ) -> Awaitable[None]: ...

    class AdminMasterClient(IdentifiableClient):
        def registerModelInstanceFactory(
            self, aModelId: str | None = None
        ) -> Cluster.AdminMaster.RegistermodelinstancefactoryResult: ...
        def availableModels(self) -> Cluster.AdminMaster.AvailablemodelsResult: ...
        def registerModelInstanceFactory_request(
            self, aModelId: str | None = None
        ) -> Cluster.AdminMaster.RegistermodelinstancefactoryRequest: ...
        def availableModels_request(
            self,
        ) -> Cluster.AdminMaster.AvailablemodelsRequest: ...

    class UserMaster:
        class AvailablemodelsRequest(Protocol):
            def send(self) -> Cluster.UserMaster.AvailablemodelsResult: ...

        class AvailablemodelsResult(Awaitable[AvailablemodelsResult], Protocol):
            factories: Any

        @classmethod
        def _new_client(
            cls, server: Cluster.UserMaster.Server | Identifiable.Server
        ) -> Cluster.UserMasterClient: ...
        class Server(Identifiable.Server):
            class AvailablemodelsResultTuple(NamedTuple):
                pass

            class AvailablemodelsCallContext(Protocol):
                params: Cluster.UserMaster.AvailablemodelsRequest
                results: Cluster.UserMaster.AvailablemodelsResult

            def availableModels(
                self,
                _context: Cluster.UserMaster.Server.AvailablemodelsCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                Cluster.UserMaster.Server.AvailablemodelsResultTuple | None
            ]: ...
            def availableModels_context(
                self, context: Cluster.UserMaster.Server.AvailablemodelsCallContext
            ) -> Awaitable[None]: ...

    class UserMasterClient(IdentifiableClient):
        def availableModels(self) -> Cluster.UserMaster.AvailablemodelsResult: ...
        def availableModels_request(
            self,
        ) -> Cluster.UserMaster.AvailablemodelsRequest: ...

    class Runtime:
        class RegistermodelinstancefactoryRequest(Protocol):
            aModelId: str
            def send(self) -> Cluster.Runtime.RegistermodelinstancefactoryResult: ...

        class RegistermodelinstancefactoryResult(
            Awaitable[RegistermodelinstancefactoryResult], Protocol
        ):
            unregister: Cluster.UnregisterClient

        class AvailablemodelsRequest(Protocol):
            def send(self) -> Cluster.Runtime.AvailablemodelsResult: ...

        class AvailablemodelsResult(Awaitable[AvailablemodelsResult], Protocol):
            factories: Any

        class NumberofcoresRequest(Protocol):
            def send(self) -> Cluster.Runtime.NumberofcoresResult: ...

        class NumberofcoresResult(Awaitable[NumberofcoresResult], Protocol):
            cores: int

        class FreenumberofcoresRequest(Protocol):
            def send(self) -> Cluster.Runtime.FreenumberofcoresResult: ...

        class FreenumberofcoresResult(Awaitable[FreenumberofcoresResult], Protocol):
            cores: int

        class ReservenumberofcoresRequest(Protocol):
            reserveCores: int
            aModelId: str
            def send(self) -> Cluster.Runtime.ReservenumberofcoresResult: ...

        class ReservenumberofcoresResult(
            Awaitable[ReservenumberofcoresResult], Protocol
        ):
            reservedCores: int

        @classmethod
        def _new_client(
            cls, server: Cluster.Runtime.Server | Identifiable.Server
        ) -> Cluster.RuntimeClient: ...
        class Server(Identifiable.Server):
            class RegistermodelinstancefactoryResultTuple(NamedTuple):
                unregister: Cluster.Unregister.Server

            class AvailablemodelsResultTuple(NamedTuple):
                pass

            class NumberofcoresResultTuple(NamedTuple):
                cores: int

            class FreenumberofcoresResultTuple(NamedTuple):
                cores: int

            class ReservenumberofcoresResultTuple(NamedTuple):
                reservedCores: int

            class RegistermodelinstancefactoryCallContext(Protocol):
                params: Cluster.Runtime.RegistermodelinstancefactoryRequest
                results: Cluster.Runtime.RegistermodelinstancefactoryResult

            class AvailablemodelsCallContext(Protocol):
                params: Cluster.Runtime.AvailablemodelsRequest
                results: Cluster.Runtime.AvailablemodelsResult

            class NumberofcoresCallContext(Protocol):
                params: Cluster.Runtime.NumberofcoresRequest
                results: Cluster.Runtime.NumberofcoresResult

            class FreenumberofcoresCallContext(Protocol):
                params: Cluster.Runtime.FreenumberofcoresRequest
                results: Cluster.Runtime.FreenumberofcoresResult

            class ReservenumberofcoresCallContext(Protocol):
                params: Cluster.Runtime.ReservenumberofcoresRequest
                results: Cluster.Runtime.ReservenumberofcoresResult

            def registerModelInstanceFactory(
                self,
                aModelId: str,
                _context: Cluster.Runtime.Server.RegistermodelinstancefactoryCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                Cluster.Unregister.Server
                | Cluster.Runtime.Server.RegistermodelinstancefactoryResultTuple
                | None
            ]: ...
            def registerModelInstanceFactory_context(
                self,
                context: Cluster.Runtime.Server.RegistermodelinstancefactoryCallContext,
            ) -> Awaitable[None]: ...
            def availableModels(
                self,
                _context: Cluster.Runtime.Server.AvailablemodelsCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                Cluster.Runtime.Server.AvailablemodelsResultTuple | None
            ]: ...
            def availableModels_context(
                self, context: Cluster.Runtime.Server.AvailablemodelsCallContext
            ) -> Awaitable[None]: ...
            def numberOfCores(
                self,
                _context: Cluster.Runtime.Server.NumberofcoresCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                int | Cluster.Runtime.Server.NumberofcoresResultTuple | None
            ]: ...
            def numberOfCores_context(
                self, context: Cluster.Runtime.Server.NumberofcoresCallContext
            ) -> Awaitable[None]: ...
            def freeNumberOfCores(
                self,
                _context: Cluster.Runtime.Server.FreenumberofcoresCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                int | Cluster.Runtime.Server.FreenumberofcoresResultTuple | None
            ]: ...
            def freeNumberOfCores_context(
                self, context: Cluster.Runtime.Server.FreenumberofcoresCallContext
            ) -> Awaitable[None]: ...
            def reserveNumberOfCores(
                self,
                reserveCores: int,
                aModelId: str,
                _context: Cluster.Runtime.Server.ReservenumberofcoresCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                int | Cluster.Runtime.Server.ReservenumberofcoresResultTuple | None
            ]: ...
            def reserveNumberOfCores_context(
                self, context: Cluster.Runtime.Server.ReservenumberofcoresCallContext
            ) -> Awaitable[None]: ...

    class RuntimeClient(IdentifiableClient):
        def registerModelInstanceFactory(
            self, aModelId: str | None = None
        ) -> Cluster.Runtime.RegistermodelinstancefactoryResult: ...
        def availableModels(self) -> Cluster.Runtime.AvailablemodelsResult: ...
        def numberOfCores(self) -> Cluster.Runtime.NumberofcoresResult: ...
        def freeNumberOfCores(self) -> Cluster.Runtime.FreenumberofcoresResult: ...
        def reserveNumberOfCores(
            self, reserveCores: int | None = None, aModelId: str | None = None
        ) -> Cluster.Runtime.ReservenumberofcoresResult: ...
        def registerModelInstanceFactory_request(
            self, aModelId: str | None = None
        ) -> Cluster.Runtime.RegistermodelinstancefactoryRequest: ...
        def availableModels_request(self) -> Cluster.Runtime.AvailablemodelsRequest: ...
        def numberOfCores_request(self) -> Cluster.Runtime.NumberofcoresRequest: ...
        def freeNumberOfCores_request(
            self,
        ) -> Cluster.Runtime.FreenumberofcoresRequest: ...
        def reserveNumberOfCores_request(
            self, reserveCores: int | None = None, aModelId: str | None = None
        ) -> Cluster.Runtime.ReservenumberofcoresRequest: ...

    ZmqPipelineAddressesBuilder: TypeAlias = ZmqPipelineAddresses.Builder
    ZmqPipelineAddressesReader: TypeAlias = ZmqPipelineAddresses.Reader
    class ZmqPipelineAddresses:
        class Reader:
            @property
            def input(self) -> str: ...
            @property
            def output(self) -> str: ...
            def as_builder(self) -> Cluster.ZmqPipelineAddresses.Builder: ...

        class Builder:
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
            ) -> Cluster.ZmqPipelineAddresses.Builder: ...
            def copy(self) -> Cluster.ZmqPipelineAddresses.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Cluster.ZmqPipelineAddresses.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Cluster.ZmqPipelineAddresses.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Cluster.ZmqPipelineAddresses.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            input: str | None = None,
            output: str | None = None,
        ) -> Cluster.ZmqPipelineAddresses.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Cluster.ZmqPipelineAddresses.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Cluster.ZmqPipelineAddresses.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    class ValueHolder:
        class ValueRequest(Protocol):
            def send(self) -> Cluster.ValueHolder.ValueResult: ...

        class ValueResult(Awaitable[ValueResult], Protocol):
            val: Any

        class ReleaseRequest(Protocol):
            def send(self) -> None: ...

        @classmethod
        def _new_client(
            cls, server: Cluster.ValueHolder.Server
        ) -> Cluster.ValueHolderClient: ...
        class Server(Protocol):
            class ValueResultTuple(NamedTuple):
                val: Any

            class ValueCallContext(Protocol):
                params: Cluster.ValueHolder.ValueRequest
                results: Cluster.ValueHolder.ValueResult

            class ReleaseCallContext(Protocol):
                params: Cluster.ValueHolder.ReleaseRequest

            def value(
                self,
                _context: Cluster.ValueHolder.Server.ValueCallContext,
                **kwargs: Any,
            ) -> Awaitable[Cluster.ValueHolder.Server.ValueResultTuple | None]: ...
            def value_context(
                self, context: Cluster.ValueHolder.Server.ValueCallContext
            ) -> Awaitable[None]: ...
            def release(
                self,
                _context: Cluster.ValueHolder.Server.ReleaseCallContext,
                **kwargs: Any,
            ) -> Awaitable[None]: ...
            def release_context(
                self, context: Cluster.ValueHolder.Server.ReleaseCallContext
            ) -> Awaitable[None]: ...

    class ValueHolderClient(Protocol):
        def value(self) -> Cluster.ValueHolder.ValueResult: ...
        def release(self) -> None: ...
        def value_request(self) -> Cluster.ValueHolder.ValueRequest: ...
        def release_request(self) -> Cluster.ValueHolder.ReleaseRequest: ...

    class ModelInstanceFactory:
        class NewinstanceRequest(Protocol):
            def send(self) -> Cluster.ModelInstanceFactory.NewinstanceResult: ...

        class NewinstanceResult(Awaitable[NewinstanceResult], Protocol):
            instance: Cluster.ValueHolderClient

        class NewinstancesRequest(Protocol):
            numberOfInstances: int
            def send(self) -> Cluster.ModelInstanceFactory.NewinstancesResult: ...

        class NewinstancesResult(Awaitable[NewinstancesResult], Protocol):
            instances: Cluster.ValueHolderClient

        class NewcloudviazmqpipelineproxiesRequest(Protocol):
            numberOfInstances: int
            def send(
                self,
            ) -> Cluster.ModelInstanceFactory.NewcloudviazmqpipelineproxiesResult: ...

        class NewcloudviazmqpipelineproxiesResult(
            Awaitable[NewcloudviazmqpipelineproxiesResult], Protocol
        ):
            proxyAddresses: Cluster.ValueHolderClient

        class NewcloudviaproxyRequest(Protocol):
            numberOfInstances: int
            def send(self) -> Cluster.ModelInstanceFactory.NewcloudviaproxyResult: ...

        class NewcloudviaproxyResult(Awaitable[NewcloudviaproxyResult], Protocol):
            proxy: Cluster.ValueHolderClient

        class ModelidRequest(Protocol):
            def send(self) -> Cluster.ModelInstanceFactory.ModelidResult: ...

        class ModelidResult(Awaitable[ModelidResult], Protocol):
            id: str

        class RegistermodelinstanceRequest(Protocol):
            instance: Any
            registrationToken: str
            def send(
                self,
            ) -> Cluster.ModelInstanceFactory.RegistermodelinstanceResult: ...

        class RegistermodelinstanceResult(
            Awaitable[RegistermodelinstanceResult], Protocol
        ):
            unregister: Cluster.UnregisterClient

        class RestoresturdyrefRequest(Protocol):
            sturdyRef: str
            def send(self) -> Cluster.ModelInstanceFactory.RestoresturdyrefResult: ...

        class RestoresturdyrefResult(Awaitable[RestoresturdyrefResult], Protocol):
            cap: Cluster.ValueHolderClient

        @classmethod
        def _new_client(
            cls, server: Cluster.ModelInstanceFactory.Server | Identifiable.Server
        ) -> Cluster.ModelInstanceFactoryClient: ...
        class Server(Identifiable.Server):
            class NewinstanceResultTuple(NamedTuple):
                instance: Cluster.ValueHolder.Server

            class NewinstancesResultTuple(NamedTuple):
                instances: Cluster.ValueHolder.Server

            class NewcloudviazmqpipelineproxiesResultTuple(NamedTuple):
                proxyAddresses: Cluster.ValueHolder.Server

            class NewcloudviaproxyResultTuple(NamedTuple):
                proxy: Cluster.ValueHolder.Server

            class ModelidResultTuple(NamedTuple):
                id: str

            class RegistermodelinstanceResultTuple(NamedTuple):
                unregister: Cluster.Unregister.Server

            class RestoresturdyrefResultTuple(NamedTuple):
                cap: Cluster.ValueHolder.Server

            class NewinstanceCallContext(Protocol):
                params: Cluster.ModelInstanceFactory.NewinstanceRequest
                results: Cluster.ModelInstanceFactory.NewinstanceResult

            class NewinstancesCallContext(Protocol):
                params: Cluster.ModelInstanceFactory.NewinstancesRequest
                results: Cluster.ModelInstanceFactory.NewinstancesResult

            class NewcloudviazmqpipelineproxiesCallContext(Protocol):
                params: (
                    Cluster.ModelInstanceFactory.NewcloudviazmqpipelineproxiesRequest
                )
                results: (
                    Cluster.ModelInstanceFactory.NewcloudviazmqpipelineproxiesResult
                )

            class NewcloudviaproxyCallContext(Protocol):
                params: Cluster.ModelInstanceFactory.NewcloudviaproxyRequest
                results: Cluster.ModelInstanceFactory.NewcloudviaproxyResult

            class ModelidCallContext(Protocol):
                params: Cluster.ModelInstanceFactory.ModelidRequest
                results: Cluster.ModelInstanceFactory.ModelidResult

            class RegistermodelinstanceCallContext(Protocol):
                params: Cluster.ModelInstanceFactory.RegistermodelinstanceRequest
                results: Cluster.ModelInstanceFactory.RegistermodelinstanceResult

            class RestoresturdyrefCallContext(Protocol):
                params: Cluster.ModelInstanceFactory.RestoresturdyrefRequest
                results: Cluster.ModelInstanceFactory.RestoresturdyrefResult

            def newInstance(
                self,
                _context: Cluster.ModelInstanceFactory.Server.NewinstanceCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                Cluster.ValueHolder.Server
                | Cluster.ModelInstanceFactory.Server.NewinstanceResultTuple
                | None
            ]: ...
            def newInstance_context(
                self,
                context: Cluster.ModelInstanceFactory.Server.NewinstanceCallContext,
            ) -> Awaitable[None]: ...
            def newInstances(
                self,
                numberOfInstances: int,
                _context: Cluster.ModelInstanceFactory.Server.NewinstancesCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                Cluster.ValueHolder.Server
                | Cluster.ModelInstanceFactory.Server.NewinstancesResultTuple
                | None
            ]: ...
            def newInstances_context(
                self,
                context: Cluster.ModelInstanceFactory.Server.NewinstancesCallContext,
            ) -> Awaitable[None]: ...
            def newCloudViaZmqPipelineProxies(
                self,
                numberOfInstances: int,
                _context: Cluster.ModelInstanceFactory.Server.NewcloudviazmqpipelineproxiesCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                Cluster.ValueHolder.Server
                | Cluster.ModelInstanceFactory.Server.NewcloudviazmqpipelineproxiesResultTuple
                | None
            ]: ...
            def newCloudViaZmqPipelineProxies_context(
                self,
                context: Cluster.ModelInstanceFactory.Server.NewcloudviazmqpipelineproxiesCallContext,
            ) -> Awaitable[None]: ...
            def newCloudViaProxy(
                self,
                numberOfInstances: int,
                _context: Cluster.ModelInstanceFactory.Server.NewcloudviaproxyCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                Cluster.ValueHolder.Server
                | Cluster.ModelInstanceFactory.Server.NewcloudviaproxyResultTuple
                | None
            ]: ...
            def newCloudViaProxy_context(
                self,
                context: Cluster.ModelInstanceFactory.Server.NewcloudviaproxyCallContext,
            ) -> Awaitable[None]: ...
            def modelId(
                self,
                _context: Cluster.ModelInstanceFactory.Server.ModelidCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                str | Cluster.ModelInstanceFactory.Server.ModelidResultTuple | None
            ]: ...
            def modelId_context(
                self, context: Cluster.ModelInstanceFactory.Server.ModelidCallContext
            ) -> Awaitable[None]: ...
            def registerModelInstance(
                self,
                instance: Any,
                registrationToken: str,
                _context: Cluster.ModelInstanceFactory.Server.RegistermodelinstanceCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                Cluster.Unregister.Server
                | Cluster.ModelInstanceFactory.Server.RegistermodelinstanceResultTuple
                | None
            ]: ...
            def registerModelInstance_context(
                self,
                context: Cluster.ModelInstanceFactory.Server.RegistermodelinstanceCallContext,
            ) -> Awaitable[None]: ...
            def restoreSturdyRef(
                self,
                sturdyRef: str,
                _context: Cluster.ModelInstanceFactory.Server.RestoresturdyrefCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                Cluster.ValueHolder.Server
                | Cluster.ModelInstanceFactory.Server.RestoresturdyrefResultTuple
                | None
            ]: ...
            def restoreSturdyRef_context(
                self,
                context: Cluster.ModelInstanceFactory.Server.RestoresturdyrefCallContext,
            ) -> Awaitable[None]: ...

    class ModelInstanceFactoryClient(IdentifiableClient):
        def newInstance(self) -> Cluster.ModelInstanceFactory.NewinstanceResult: ...
        def newInstances(
            self, numberOfInstances: int | None = None
        ) -> Cluster.ModelInstanceFactory.NewinstancesResult: ...
        def newCloudViaZmqPipelineProxies(
            self, numberOfInstances: int | None = None
        ) -> Cluster.ModelInstanceFactory.NewcloudviazmqpipelineproxiesResult: ...
        def newCloudViaProxy(
            self, numberOfInstances: int | None = None
        ) -> Cluster.ModelInstanceFactory.NewcloudviaproxyResult: ...
        def modelId(self) -> Cluster.ModelInstanceFactory.ModelidResult: ...
        def registerModelInstance(
            self, instance: Any | None = None, registrationToken: str | None = None
        ) -> Cluster.ModelInstanceFactory.RegistermodelinstanceResult: ...
        def restoreSturdyRef(
            self, sturdyRef: str | None = None
        ) -> Cluster.ModelInstanceFactory.RestoresturdyrefResult: ...
        def newInstance_request(
            self,
        ) -> Cluster.ModelInstanceFactory.NewinstanceRequest: ...
        def newInstances_request(
            self, numberOfInstances: int | None = None
        ) -> Cluster.ModelInstanceFactory.NewinstancesRequest: ...
        def newCloudViaZmqPipelineProxies_request(
            self, numberOfInstances: int | None = None
        ) -> Cluster.ModelInstanceFactory.NewcloudviazmqpipelineproxiesRequest: ...
        def newCloudViaProxy_request(
            self, numberOfInstances: int | None = None
        ) -> Cluster.ModelInstanceFactory.NewcloudviaproxyRequest: ...
        def modelId_request(self) -> Cluster.ModelInstanceFactory.ModelidRequest: ...
        def registerModelInstance_request(
            self, instance: Any | None = None, registrationToken: str | None = None
        ) -> Cluster.ModelInstanceFactory.RegistermodelinstanceRequest: ...
        def restoreSturdyRef_request(
            self, sturdyRef: str | None = None
        ) -> Cluster.ModelInstanceFactory.RestoresturdyrefRequest: ...

    class Reader:
        def as_builder(self) -> Cluster.Builder: ...

    class Builder:
        @staticmethod
        def from_dict(dictionary: dict[str, Any]) -> Cluster.Builder: ...
        def copy(self) -> Cluster.Builder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> Cluster.Reader: ...
        @staticmethod
        def write(file: BufferedWriter) -> None: ...
        @staticmethod
        def write_packed(file: BufferedWriter) -> None: ...

    @staticmethod
    @contextmanager
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[Cluster.Reader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Cluster.Reader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None, allocate_seg_callable: Any = None
    ) -> Cluster.Builder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Cluster.Reader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Cluster.Reader: ...
    def to_dict(self) -> dict[str, Any]: ...
