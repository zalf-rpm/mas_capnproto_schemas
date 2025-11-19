"""This is an automatically generated stub for `model.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, MutableSequence, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, NamedTuple, Protocol, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicObjectReader,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
    _StructModule,
)

from .climate_capnp import _TimeSeriesModule
from .common_capnp import _IdentifiableModule
from .management_capnp import _EventModule
from .persistence_capnp import _PersistentModule
from .service_capnp import _StoppableModule
from .soil_capnp import _ProfileModule

# Type alias for AnyPointer parameters (accepts all Cap'n Proto pointer types)
type AnyPointer = (
    str
    | bytes
    | _DynamicStructBuilder
    | _DynamicStructReader
    | _DynamicCapabilityClient
    | _DynamicCapabilityServer
)

class _XYResultModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def xs(self) -> Sequence[float]: ...
        @property
        def ys(self) -> Sequence[float]: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> XYResultBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def xs(self) -> MutableSequence[float]: ...
        @xs.setter
        def xs(self, value: Sequence[float]) -> None: ...
        @property
        def ys(self) -> MutableSequence[float]: ...
        @ys.setter
        def ys(self, value: Sequence[float]) -> None: ...
        @overload
        def init(
            self, field: Literal["xs"], size: int | None = None
        ) -> MutableSequence[float]: ...
        @overload
        def init(
            self, field: Literal["ys"], size: int | None = None
        ) -> MutableSequence[float]: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> XYResultReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        xs: Sequence[float] | None = None,
        ys: Sequence[float] | None = None,
        **kwargs: Any,
    ) -> XYResultBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[XYResultReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[XYResultReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[XYResultBuilder]: ...
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> XYResultReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> XYResultReader: ...

XYResult: _XYResultModule

class _StatModule(_StructModule):
    class _TypeModule:
        min: int
        max: int
        sd: int
        avg: int
        median: int

    Type: _TypeModule
    class Reader(_DynamicStructReader):
        @property
        def type(self) -> StatTypeEnum: ...
        @property
        def vs(self) -> Sequence[float]: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> StatBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def type(self) -> StatTypeEnum: ...
        @type.setter
        def type(self, value: StatTypeEnum) -> None: ...
        @property
        def vs(self) -> MutableSequence[float]: ...
        @vs.setter
        def vs(self, value: Sequence[float]) -> None: ...
        def init(
            self, field: Literal["vs"], size: int | None = None
        ) -> MutableSequence[float]: ...
        @override
        def as_reader(self) -> StatReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        type: StatTypeEnum | None = None,
        vs: Sequence[float] | None = None,
        **kwargs: Any,
    ) -> StatBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[StatReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[StatReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[StatBuilder]: ...
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> StatReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> StatReader: ...

Stat: _StatModule

class _XYPlusResultModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def xy(self) -> XYResultReader: ...
        @property
        def stats(self) -> Sequence[StatReader]: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> XYPlusResultBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def xy(self) -> XYResultBuilder: ...
        @xy.setter
        def xy(
            self, value: XYResultBuilder | XYResultReader | dict[str, Any]
        ) -> None: ...
        @property
        def stats(self) -> MutableSequence[StatBuilder]: ...
        @stats.setter
        def stats(
            self, value: Sequence[StatBuilder | StatReader] | Sequence[dict[str, Any]]
        ) -> None: ...
        @overload
        def init(
            self, field: Literal["xy"], size: int | None = None
        ) -> XYResultBuilder: ...
        @overload
        def init(
            self, field: Literal["stats"], size: int | None = None
        ) -> MutableSequence[StatBuilder]: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> XYPlusResultReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        xy: XYResultBuilder | dict[str, Any] | None = None,
        stats: Sequence[StatBuilder] | Sequence[dict[str, Any]] | None = None,
        **kwargs: Any,
    ) -> XYPlusResultBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[XYPlusResultReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[XYPlusResultReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[XYPlusResultBuilder]: ...
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> XYPlusResultReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> XYPlusResultReader: ...

XYPlusResult: _XYPlusResultModule

class _ClimateInstanceModule(_IdentifiableModule):
    class RunRequest(Protocol):
        def send(self) -> _ClimateInstanceModule.ClimateInstanceClient.RunResult: ...

    class RunsetRequest(Protocol):
        def send(self) -> _ClimateInstanceModule.ClimateInstanceClient.RunsetResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _ClimateInstanceModule.ClimateInstanceClient: ...
    class Server(_IdentifiableModule.Server):
        class RunResult(Awaitable[RunResult], Protocol):
            result: _XYResultModule.Builder | _XYResultModule.Reader

        class RunsetResult(Awaitable[RunsetResult], Protocol):
            result: _XYPlusResultModule.Builder | _XYPlusResultModule.Reader

        class RunResultTuple(NamedTuple):
            result: _XYResultModule.Builder | _XYResultModule.Reader

        class RunsetResultTuple(NamedTuple):
            result: _XYPlusResultModule.Builder | _XYPlusResultModule.Reader

        class RunCallContext(Protocol):
            params: _ClimateInstanceModule.RunRequest
            results: _ClimateInstanceModule.Server.RunResult

        class RunsetCallContext(Protocol):
            params: _ClimateInstanceModule.RunsetRequest
            results: _ClimateInstanceModule.Server.RunsetResult

        def run(
            self, _context: _ClimateInstanceModule.Server.RunCallContext, **kwargs: Any
        ) -> Awaitable[_ClimateInstanceModule.Server.RunResultTuple | None]: ...
        def run_context(
            self, context: _ClimateInstanceModule.Server.RunCallContext
        ) -> Awaitable[None]: ...
        def runSet(
            self,
            _context: _ClimateInstanceModule.Server.RunsetCallContext,
            **kwargs: Any,
        ) -> Awaitable[_ClimateInstanceModule.Server.RunsetResultTuple | None]: ...
        def runSet_context(
            self, context: _ClimateInstanceModule.Server.RunsetCallContext
        ) -> Awaitable[None]: ...

    class ClimateInstanceClient(_IdentifiableModule.IdentifiableClient):
        class RunResult(Awaitable[RunResult], Protocol):
            result: _XYResultModule.Builder | _XYResultModule.Reader

        class RunsetResult(Awaitable[RunsetResult], Protocol):
            result: _XYPlusResultModule.Builder | _XYPlusResultModule.Reader

        def run(self) -> _ClimateInstanceModule.ClimateInstanceClient.RunResult: ...
        def runSet(
            self,
        ) -> _ClimateInstanceModule.ClimateInstanceClient.RunsetResult: ...
        def run_request(self) -> _ClimateInstanceModule.RunRequest: ...
        def runSet_request(self) -> _ClimateInstanceModule.RunsetRequest: ...

ClimateInstance: _ClimateInstanceModule

class _EnvModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def rest(self) -> _DynamicObjectReader: ...
        @property
        def timeSeries(self) -> _TimeSeriesModule.TimeSeriesClient: ...
        @property
        def soilProfile(self) -> _ProfileModule.ProfileClient: ...
        @property
        def mgmtEvents(self) -> Sequence[_EventModule.Reader]: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> EnvBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def rest(self) -> _DynamicObjectReader: ...
        @rest.setter
        def rest(self, value: AnyPointer) -> None: ...
        @property
        def timeSeries(self) -> _TimeSeriesModule.TimeSeriesClient: ...
        @timeSeries.setter
        def timeSeries(
            self, value: _TimeSeriesModule.TimeSeriesClient | _TimeSeriesModule.Server
        ) -> None: ...
        @property
        def soilProfile(self) -> _ProfileModule.ProfileClient: ...
        @soilProfile.setter
        def soilProfile(
            self, value: _ProfileModule.ProfileClient | _ProfileModule.Server
        ) -> None: ...
        @property
        def mgmtEvents(self) -> MutableSequence[_EventModule.Builder]: ...
        @mgmtEvents.setter
        def mgmtEvents(
            self,
            value: Sequence[_EventModule.Builder | _EventModule.Reader]
            | Sequence[dict[str, Any]],
        ) -> None: ...
        def init(
            self, field: Literal["mgmtEvents"], size: int | None = None
        ) -> MutableSequence[_EventModule.Builder]: ...
        @override
        def as_reader(self) -> EnvReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        rest: AnyPointer | None = None,
        timeSeries: _TimeSeriesModule.TimeSeriesClient
        | _TimeSeriesModule.Server
        | None = None,
        soilProfile: _ProfileModule.ProfileClient | _ProfileModule.Server | None = None,
        mgmtEvents: Sequence[_EventModule.Builder]
        | Sequence[dict[str, Any]]
        | None = None,
        **kwargs: Any,
    ) -> EnvBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[EnvReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[EnvReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[EnvBuilder]: ...
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> EnvReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> EnvReader: ...

Env: _EnvModule

class _EnvInstanceModule(_IdentifiableModule, _PersistentModule, _StoppableModule):
    class RunRequest(Protocol):
        env: _EnvModule.Builder
        @overload
        def init(self, name: Literal["env"]) -> EnvBuilder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> _EnvInstanceModule.EnvInstanceClient.RunResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _EnvInstanceModule.EnvInstanceClient: ...
    class Server(
        _IdentifiableModule.Server, _PersistentModule.Server, _StoppableModule.Server
    ):
        class RunResult(Awaitable[RunResult], Protocol):
            result: AnyPointer

        class RunResultTuple(NamedTuple):
            result: AnyPointer

        class RunCallContext(Protocol):
            params: _EnvInstanceModule.RunRequest
            results: _EnvInstanceModule.Server.RunResult

        def run(
            self,
            env: _EnvModule.Reader,
            _context: _EnvInstanceModule.Server.RunCallContext,
            **kwargs: Any,
        ) -> Awaitable[_EnvInstanceModule.Server.RunResultTuple | None]: ...
        def run_context(
            self, context: _EnvInstanceModule.Server.RunCallContext
        ) -> Awaitable[None]: ...

    class EnvInstanceClient(
        _IdentifiableModule.IdentifiableClient,
        _PersistentModule.PersistentClient,
        _StoppableModule.StoppableClient,
    ):
        class RunResult(Awaitable[RunResult], Protocol):
            result: _DynamicObjectReader

        def run(
            self, env: EnvBuilder | EnvReader | dict[str, Any] | None = None
        ) -> _EnvInstanceModule.EnvInstanceClient.RunResult: ...
        def run_request(
            self, env: _EnvModule.Builder | None = None
        ) -> _EnvInstanceModule.RunRequest: ...

EnvInstance: _EnvInstanceModule

class _EnvInstanceProxyModule(_EnvInstanceModule):
    class _UnregisterModule(_InterfaceModule):
        class UnregisterRequest(Protocol):
            def send(
                self,
            ) -> _EnvInstanceProxyModule._UnregisterModule.UnregisterClient.UnregisterResult: ...

        def _new_client(
            self, server: _DynamicCapabilityServer
        ) -> _EnvInstanceProxyModule._UnregisterModule.UnregisterClient: ...
        class Server(_DynamicCapabilityServer):
            class UnregisterResult(Awaitable[UnregisterResult], Protocol):
                success: bool

            class UnregisterResultTuple(NamedTuple):
                success: bool

            class UnregisterCallContext(Protocol):
                params: _EnvInstanceProxyModule._UnregisterModule.UnregisterRequest
                results: (
                    _EnvInstanceProxyModule._UnregisterModule.Server.UnregisterResult
                )

            def unregister(
                self,
                _context: _EnvInstanceProxyModule._UnregisterModule.Server.UnregisterCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                bool
                | _EnvInstanceProxyModule._UnregisterModule.Server.UnregisterResultTuple
                | None
            ]: ...
            def unregister_context(
                self,
                context: _EnvInstanceProxyModule._UnregisterModule.Server.UnregisterCallContext,
            ) -> Awaitable[None]: ...

        class UnregisterClient(_DynamicCapabilityClient):
            class UnregisterResult(Awaitable[UnregisterResult], Protocol):
                success: bool

            def unregister(
                self,
            ) -> _EnvInstanceProxyModule._UnregisterModule.UnregisterClient.UnregisterResult: ...
            def unregister_request(
                self,
            ) -> _EnvInstanceProxyModule._UnregisterModule.UnregisterRequest: ...

    Unregister: _UnregisterModule
    type UnregisterClient = _EnvInstanceProxyModule._UnregisterModule.UnregisterClient
    class RegisterenvinstanceRequest(Protocol):
        instance: EnvInstanceClient | _EnvInstanceModule.Server
        def send(
            self,
        ) -> (
            _EnvInstanceProxyModule.EnvInstanceProxyClient.RegisterenvinstanceResult
        ): ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _EnvInstanceProxyModule.EnvInstanceProxyClient: ...
    class Server(_EnvInstanceModule.Server):
        class RegisterenvinstanceResult(Awaitable[RegisterenvinstanceResult], Protocol):
            unregister: _EnvInstanceProxyModule._UnregisterModule.UnregisterClient

        class RegisterenvinstanceResultTuple(NamedTuple):
            unregister: _EnvInstanceProxyModule._UnregisterModule.Server

        class RegisterenvinstanceCallContext(Protocol):
            params: _EnvInstanceProxyModule.RegisterenvinstanceRequest
            results: _EnvInstanceProxyModule.Server.RegisterenvinstanceResult

        def registerEnvInstance(
            self,
            instance: EnvInstanceClient,
            _context: _EnvInstanceProxyModule.Server.RegisterenvinstanceCallContext,
            **kwargs: Any,
        ) -> Awaitable[
            _EnvInstanceProxyModule._UnregisterModule.Server
            | _EnvInstanceProxyModule.Server.RegisterenvinstanceResultTuple
            | None
        ]: ...
        def registerEnvInstance_context(
            self, context: _EnvInstanceProxyModule.Server.RegisterenvinstanceCallContext
        ) -> Awaitable[None]: ...

    class EnvInstanceProxyClient(_EnvInstanceModule.EnvInstanceClient):
        class RegisterenvinstanceResult(Awaitable[RegisterenvinstanceResult], Protocol):
            unregister: _EnvInstanceProxyModule._UnregisterModule.UnregisterClient

        def registerEnvInstance(
            self, instance: EnvInstanceClient | _EnvInstanceModule.Server | None = None
        ) -> (
            _EnvInstanceProxyModule.EnvInstanceProxyClient.RegisterenvinstanceResult
        ): ...
        def registerEnvInstance_request(
            self, instance: EnvInstanceClient | _EnvInstanceModule.Server | None = None
        ) -> _EnvInstanceProxyModule.RegisterenvinstanceRequest: ...

EnvInstanceProxy: _EnvInstanceProxyModule

class _InstanceFactoryModule(_IdentifiableModule):
    class ModelinfoRequest(Protocol):
        def send(
            self,
        ) -> _InstanceFactoryModule.InstanceFactoryClient.ModelinfoResult: ...

    class NewinstanceRequest(Protocol):
        def send(
            self,
        ) -> _InstanceFactoryModule.InstanceFactoryClient.NewinstanceResult: ...

    class NewinstancesRequest(Protocol):
        numberOfInstances: int
        def send(
            self,
        ) -> _InstanceFactoryModule.InstanceFactoryClient.NewinstancesResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _InstanceFactoryModule.InstanceFactoryClient: ...
    class Server(_IdentifiableModule.Server):
        class ModelinfoResult(Awaitable[ModelinfoResult], Protocol):
            id: str
            name: str
            description: str

        class NewinstanceResult(Awaitable[NewinstanceResult], Protocol):
            instance: _IdentifiableModule.IdentifiableClient

        class NewinstancesResult(Awaitable[NewinstancesResult], Protocol):
            instances: Sequence[_IdentifiableModule]

        class ModelinfoResultTuple(NamedTuple):
            id: str
            name: str
            description: str

        class NewinstanceResultTuple(NamedTuple):
            instance: _IdentifiableModule.Server

        class NewinstancesResultTuple(NamedTuple):
            instances: Sequence[_IdentifiableModule]

        class ModelinfoCallContext(Protocol):
            params: _InstanceFactoryModule.ModelinfoRequest
            results: _InstanceFactoryModule.Server.ModelinfoResult

        class NewinstanceCallContext(Protocol):
            params: _InstanceFactoryModule.NewinstanceRequest
            results: _InstanceFactoryModule.Server.NewinstanceResult

        class NewinstancesCallContext(Protocol):
            params: _InstanceFactoryModule.NewinstancesRequest
            results: _InstanceFactoryModule.Server.NewinstancesResult

        def modelInfo(
            self,
            _context: _InstanceFactoryModule.Server.ModelinfoCallContext,
            **kwargs: Any,
        ) -> Awaitable[_InstanceFactoryModule.Server.ModelinfoResultTuple | None]: ...
        def modelInfo_context(
            self, context: _InstanceFactoryModule.Server.ModelinfoCallContext
        ) -> Awaitable[None]: ...
        def newInstance(
            self,
            _context: _InstanceFactoryModule.Server.NewinstanceCallContext,
            **kwargs: Any,
        ) -> Awaitable[
            _IdentifiableModule.Server
            | _InstanceFactoryModule.Server.NewinstanceResultTuple
            | None
        ]: ...
        def newInstance_context(
            self, context: _InstanceFactoryModule.Server.NewinstanceCallContext
        ) -> Awaitable[None]: ...
        def newInstances(
            self,
            numberOfInstances: int,
            _context: _InstanceFactoryModule.Server.NewinstancesCallContext,
            **kwargs: Any,
        ) -> Awaitable[
            _InstanceFactoryModule.Server.NewinstancesResultTuple | None
        ]: ...
        def newInstances_context(
            self, context: _InstanceFactoryModule.Server.NewinstancesCallContext
        ) -> Awaitable[None]: ...

    class InstanceFactoryClient(_IdentifiableModule.IdentifiableClient):
        class ModelinfoResult(Awaitable[ModelinfoResult], Protocol):
            id: str
            name: str
            description: str

        class NewinstanceResult(Awaitable[NewinstanceResult], Protocol):
            instance: _IdentifiableModule.IdentifiableClient

        class NewinstancesResult(Awaitable[NewinstancesResult], Protocol):
            instances: Sequence[_IdentifiableModule]

        def modelInfo(
            self,
        ) -> _InstanceFactoryModule.InstanceFactoryClient.ModelinfoResult: ...
        def newInstance(
            self,
        ) -> _InstanceFactoryModule.InstanceFactoryClient.NewinstanceResult: ...
        def newInstances(
            self, numberOfInstances: int | None = None
        ) -> _InstanceFactoryModule.InstanceFactoryClient.NewinstancesResult: ...
        def modelInfo_request(self) -> _InstanceFactoryModule.ModelinfoRequest: ...
        def newInstance_request(self) -> _InstanceFactoryModule.NewinstanceRequest: ...
        def newInstances_request(
            self, numberOfInstances: int | None = None
        ) -> _InstanceFactoryModule.NewinstancesRequest: ...

InstanceFactory: _InstanceFactoryModule

# Top-level type aliases for use in type annotations
type ClimateInstanceClient = _ClimateInstanceModule.ClimateInstanceClient
type EnvBuilder = _EnvModule.Builder
type EnvInstanceClient = _EnvInstanceModule.EnvInstanceClient
type EnvInstanceProxyClient = _EnvInstanceProxyModule.EnvInstanceProxyClient
type EnvReader = _EnvModule.Reader
type InstanceFactoryClient = _InstanceFactoryModule.InstanceFactoryClient
type ModelinfoResult = _InstanceFactoryModule.InstanceFactoryClient.ModelinfoResult
type NewinstanceResult = _InstanceFactoryModule.InstanceFactoryClient.NewinstanceResult
type NewinstancesResult = (
    _InstanceFactoryModule.InstanceFactoryClient.NewinstancesResult
)
type RegisterenvinstanceResult = (
    _EnvInstanceProxyModule.EnvInstanceProxyClient.RegisterenvinstanceResult
)
type RunResult = _EnvInstanceModule.EnvInstanceClient.RunResult
type RunsetResult = _ClimateInstanceModule.ClimateInstanceClient.RunsetResult
type StatBuilder = _StatModule.Builder
type StatReader = _StatModule.Reader
type StatTypeEnum = int | Literal["min", "max", "sd", "avg", "median"]
type UnregisterClient = _EnvInstanceProxyModule._UnregisterModule.UnregisterClient
type UnregisterResult = (
    _EnvInstanceProxyModule._UnregisterModule.UnregisterClient.UnregisterResult
)
type XYPlusResultBuilder = _XYPlusResultModule.Builder
type XYPlusResultReader = _XYPlusResultModule.Reader
type XYResultBuilder = _XYResultModule.Builder
type XYResultReader = _XYResultModule.Reader
