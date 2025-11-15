"""This is an automatically generated stub for `model.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator, MutableSequence, Sequence
from enum import Enum
from typing import (
    Any,
    Generic,
    Literal,
    NamedTuple,
    Protocol,
    TypeAlias,
    TypeVar,
    overload,
    override,
)

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

from .climate_capnp import TimeSeries, TimeSeriesClient, _TimeSeriesModule
from .common_capnp import Identifiable, IdentifiableClient, _IdentifiableModule
from .management_capnp import _EventModule
from .persistence_capnp import Persistent, PersistentClient, _PersistentModule
from .service_capnp import Stoppable, StoppableClient, _StoppableModule
from .soil_capnp import Profile, ProfileClient, _ProfileModule

_RestInput = TypeVar("_RestInput")

class _XYResultModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def xs(self) -> Sequence[float]: ...
        @property
        def ys(self) -> Sequence[float]: ...
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _XYResultModule.Builder: ...

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
        def init(self, field: Literal["xs"], size: int | None = None) -> MutableSequence[float]: ...
        @overload
        def init(self, field: Literal["ys"], size: int | None = None) -> MutableSequence[float]: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> _XYResultModule.Reader: ...

    @override
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, xs: Sequence[float] | None = None, ys: Sequence[float] | None = None) -> _XYResultModule.Builder: ...

XYResultReader: TypeAlias = _XYResultModule.Reader
XYResultBuilder: TypeAlias = _XYResultModule.Builder
XYResult: _XYResultModule

class _StatModule(_StructModule):
    class _TypeModule(Enum):
        min = 0
        max = 1
        sd = 2
        avg = 3
        median = 4

    Type: TypeAlias = _TypeModule
    class Reader(_DynamicStructReader):
        @property
        def type(self) -> _StatModule._TypeModule: ...
        @property
        def vs(self) -> Sequence[float]: ...
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _StatModule.Builder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def type(self) -> _StatModule._TypeModule: ...
        @type.setter
        def type(self, value: _StatModule._TypeModule | Literal["min", "max", "sd", "avg", "median"]) -> None: ...
        @property
        def vs(self) -> MutableSequence[float]: ...
        @vs.setter
        def vs(self, value: Sequence[float]) -> None: ...
        def init(self, field: Literal["vs"], size: int | None = None) -> MutableSequence[float]: ...
        @override
        def as_reader(self) -> _StatModule.Reader: ...

    @override
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, type: _StatModule._TypeModule | Literal["min", "max", "sd", "avg", "median"] | None = None, vs: Sequence[float] | None = None) -> _StatModule.Builder: ...

StatReader: TypeAlias = _StatModule.Reader
StatBuilder: TypeAlias = _StatModule.Builder
Stat: _StatModule

class _XYPlusResultModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def xy(self) -> _XYResultModule.Reader: ...
        @property
        def stats(self) -> Sequence[_StatModule.Reader]: ...
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _XYPlusResultModule.Builder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def xy(self) -> _XYResultModule.Builder: ...
        @xy.setter
        def xy(self, value: _XYResultModule.Builder | _XYResultModule.Reader | dict[str, Any]) -> None: ...
        @property
        def stats(self) -> MutableSequence[_StatModule.Builder]: ...
        @stats.setter
        def stats(self, value: Sequence[_StatModule.Builder | _StatModule.Reader] | Sequence[dict[str, Any]]) -> None: ...
        @overload
        def init(self, field: Literal["xy"], size: int | None = None) -> _XYResultModule.Builder: ...
        @overload
        def init(self, field: Literal["stats"], size: int | None = None) -> MutableSequence[_StatModule.Builder]: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> _XYPlusResultModule.Reader: ...

    @override
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, xy: _XYResultModule.Builder | dict[str, Any] | None = None, stats: Sequence[_StatModule.Builder] | Sequence[dict[str, Any]] | None = None) -> _XYPlusResultModule.Builder: ...

XYPlusResultReader: TypeAlias = _XYPlusResultModule.Reader
XYPlusResultBuilder: TypeAlias = _XYPlusResultModule.Builder
XYPlusResult: _XYPlusResultModule

class _ClimateInstanceModule(_IdentifiableModule):
    class RunRequest(Protocol):
        def send(self) -> _ClimateInstanceModule.ClimateInstanceClient.RunResult: ...

    class RunsetRequest(Protocol):
        def send(self) -> _ClimateInstanceModule.ClimateInstanceClient.RunsetResult: ...

    @classmethod
    def _new_client(cls, server: _ClimateInstanceModule.Server | _IdentifiableModule.Server) -> _ClimateInstanceModule.ClimateInstanceClient: ...
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

        def run(self, _context: _ClimateInstanceModule.Server.RunCallContext, **kwargs: Any) -> Awaitable[_ClimateInstanceModule.Server.RunResultTuple | None]: ...
        def run_context(self, context: _ClimateInstanceModule.Server.RunCallContext) -> Awaitable[None]: ...
        def runSet(self, _context: _ClimateInstanceModule.Server.RunsetCallContext, **kwargs: Any) -> Awaitable[_ClimateInstanceModule.Server.RunsetResultTuple | None]: ...
        def runSet_context(self, context: _ClimateInstanceModule.Server.RunsetCallContext) -> Awaitable[None]: ...

    class ClimateInstanceClient(_IdentifiableModule.IdentifiableClient):
        class RunResult(Awaitable[RunResult], Protocol):
            result: _XYResultModule.Builder | _XYResultModule.Reader

        class RunsetResult(Awaitable[RunsetResult], Protocol):
            result: _XYPlusResultModule.Builder | _XYPlusResultModule.Reader

        def run(self) -> _ClimateInstanceModule.ClimateInstanceClient.RunResult: ...
        def runSet(self) -> _ClimateInstanceModule.ClimateInstanceClient.RunsetResult: ...
        def run_request(self) -> _ClimateInstanceModule.RunRequest: ...
        def runSet_request(self) -> _ClimateInstanceModule.RunsetRequest: ...

ClimateInstance: _ClimateInstanceModule
ClimateInstanceClient: TypeAlias = _ClimateInstanceModule.ClimateInstanceClient

class _EnvModule(Generic[_RestInput], _StructModule):
    class Reader(_DynamicStructReader):
        @property
        def rest(self) -> _RestInput: ...
        @property
        def timeSeries(self) -> _TimeSeriesModule.TimeSeriesClient: ...
        @property
        def soilProfile(self) -> _ProfileModule.ProfileClient: ...
        @property
        def mgmtEvents(self) -> Sequence[_EventModule.Reader]: ...
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _EnvModule.Builder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def rest(self) -> _RestInput: ...
        @rest.setter
        def rest(self, value: _RestInput) -> None: ...
        @property
        def timeSeries(self) -> _TimeSeriesModule.TimeSeriesClient: ...
        @timeSeries.setter
        def timeSeries(self, value: _TimeSeriesModule.TimeSeriesClient | _TimeSeriesModule.Server) -> None: ...
        @property
        def soilProfile(self) -> _ProfileModule.ProfileClient: ...
        @soilProfile.setter
        def soilProfile(self, value: _ProfileModule.ProfileClient | _ProfileModule.Server) -> None: ...
        @property
        def mgmtEvents(self) -> MutableSequence[_EventModule.Builder]: ...
        @mgmtEvents.setter
        def mgmtEvents(self, value: Sequence[_EventModule.Builder | _EventModule.Reader] | Sequence[dict[str, Any]]) -> None: ...
        def init(self, field: Literal["mgmtEvents"], size: int | None = None) -> MutableSequence[_EventModule.Builder]: ...
        @override
        def as_reader(self) -> _EnvModule.Reader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        rest: _RestInput | None = None,
        timeSeries: _TimeSeriesModule.TimeSeriesClient | _TimeSeriesModule.Server | None = None,
        soilProfile: _ProfileModule.ProfileClient | _ProfileModule.Server | None = None,
        mgmtEvents: Sequence[_EventModule.Builder] | Sequence[dict[str, Any]] | None = None,
    ) -> _EnvModule.Builder: ...

EnvReader: TypeAlias = _EnvModule.Reader
EnvBuilder: TypeAlias = _EnvModule.Builder
Env: _EnvModule

class _EnvInstanceModule(_IdentifiableModule, _PersistentModule, _StoppableModule):
    class RunRequest(Protocol):
        env: _EnvModule[_DynamicObjectReader].Builder
        @overload
        def init(self, name: Literal["env"]) -> _EnvModule[_DynamicObjectReader].Builder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> _EnvInstanceModule.EnvInstanceClient.RunResult: ...

    @classmethod
    def _new_client(cls, server: _EnvInstanceModule.Server | _IdentifiableModule.Server | _PersistentModule.Server | _StoppableModule.Server) -> _EnvInstanceModule.EnvInstanceClient: ...
    class Server(_IdentifiableModule.Server, _PersistentModule.Server, _StoppableModule.Server):
        class RunResult(Awaitable[RunResult], Protocol):
            result: str | bytes | _DynamicStructBuilder | _DynamicStructReader | _DynamicCapabilityClient | _DynamicCapabilityServer

        class RunResultTuple(NamedTuple):
            result: str | bytes | _DynamicStructBuilder | _DynamicStructReader | _DynamicCapabilityClient | _DynamicCapabilityServer

        class RunCallContext(Protocol):
            params: _EnvInstanceModule.RunRequest
            results: _EnvInstanceModule.Server.RunResult

        def run(self, env: _EnvModule[_DynamicObjectReader].Reader, _context: _EnvInstanceModule.Server.RunCallContext, **kwargs: Any) -> Awaitable[_EnvInstanceModule.Server.RunResultTuple | None]: ...
        def run_context(self, context: _EnvInstanceModule.Server.RunCallContext) -> Awaitable[None]: ...

    class EnvInstanceClient(_IdentifiableModule.IdentifiableClient, _PersistentModule.PersistentClient, _StoppableModule.StoppableClient):
        class RunResult(Awaitable[RunResult], Protocol):
            result: _DynamicObjectReader

        def run(self, env: _EnvModule[_DynamicObjectReader] | dict[str, Any] | None = None) -> _EnvInstanceModule.EnvInstanceClient.RunResult: ...
        def run_request(self, env: _EnvModule[_DynamicObjectReader].Builder | None = None) -> _EnvInstanceModule.RunRequest: ...

EnvInstance: _EnvInstanceModule
EnvInstanceClient: TypeAlias = _EnvInstanceModule.EnvInstanceClient

class _EnvInstanceProxyModule(_EnvInstanceModule):
    class _UnregisterModule(_InterfaceModule):
        class UnregisterRequest(Protocol):
            def send(self) -> _EnvInstanceProxyModule._UnregisterModule.UnregisterClient.UnregisterResult: ...

        @classmethod
        def _new_client(cls, server: _EnvInstanceProxyModule._UnregisterModule.Server) -> _EnvInstanceProxyModule._UnregisterModule.UnregisterClient: ...
        class Server(_DynamicCapabilityServer):
            class UnregisterResult(Awaitable[UnregisterResult], Protocol):
                success: bool

            class UnregisterResultTuple(NamedTuple):
                success: bool

            class UnregisterCallContext(Protocol):
                params: _EnvInstanceProxyModule._UnregisterModule.UnregisterRequest
                results: _EnvInstanceProxyModule._UnregisterModule.Server.UnregisterResult

            def unregister(self, _context: _EnvInstanceProxyModule._UnregisterModule.Server.UnregisterCallContext, **kwargs: Any) -> Awaitable[bool | _EnvInstanceProxyModule._UnregisterModule.Server.UnregisterResultTuple | None]: ...
            def unregister_context(self, context: _EnvInstanceProxyModule._UnregisterModule.Server.UnregisterCallContext) -> Awaitable[None]: ...

        class UnregisterClient(_DynamicCapabilityClient):
            class UnregisterResult(Awaitable[UnregisterResult], Protocol):
                success: bool

            def unregister(self) -> _EnvInstanceProxyModule._UnregisterModule.UnregisterClient.UnregisterResult: ...
            def unregister_request(self) -> _EnvInstanceProxyModule._UnregisterModule.UnregisterRequest: ...

    Unregister: _UnregisterModule
    UnregisterClient: TypeAlias = _EnvInstanceProxyModule._UnregisterModule.UnregisterClient
    class RegisterenvinstanceRequest(Protocol):
        instance: EnvInstanceClient | _EnvInstanceModule.Server
        def send(self) -> _EnvInstanceProxyModule.EnvInstanceProxyClient.RegisterenvinstanceResult: ...

    @classmethod
    def _new_client(cls, server: _EnvInstanceProxyModule.Server | _EnvInstanceModule.Server | _IdentifiableModule.Server | _PersistentModule.Server | _StoppableModule.Server) -> _EnvInstanceProxyModule.EnvInstanceProxyClient: ...
    class Server(_EnvInstanceModule.Server):
        class RegisterenvinstanceResult(Awaitable[RegisterenvinstanceResult], Protocol):
            unregister: _EnvInstanceProxyModule._UnregisterModule.UnregisterClient

        class RegisterenvinstanceResultTuple(NamedTuple):
            unregister: _EnvInstanceProxyModule._UnregisterModule.Server

        class RegisterenvinstanceCallContext(Protocol):
            params: _EnvInstanceProxyModule.RegisterenvinstanceRequest
            results: _EnvInstanceProxyModule.Server.RegisterenvinstanceResult

        def registerEnvInstance(self, instance: EnvInstanceClient, _context: _EnvInstanceProxyModule.Server.RegisterenvinstanceCallContext, **kwargs: Any) -> Awaitable[_EnvInstanceProxyModule._UnregisterModule.Server | _EnvInstanceProxyModule.Server.RegisterenvinstanceResultTuple | None]: ...
        def registerEnvInstance_context(self, context: _EnvInstanceProxyModule.Server.RegisterenvinstanceCallContext) -> Awaitable[None]: ...

    class EnvInstanceProxyClient(_EnvInstanceModule.EnvInstanceClient):
        class RegisterenvinstanceResult(Awaitable[RegisterenvinstanceResult], Protocol):
            unregister: _EnvInstanceProxyModule._UnregisterModule.UnregisterClient

        def registerEnvInstance(self, instance: EnvInstanceClient | _EnvInstanceModule.Server | None = None) -> _EnvInstanceProxyModule.EnvInstanceProxyClient.RegisterenvinstanceResult: ...
        def registerEnvInstance_request(self, instance: EnvInstanceClient | _EnvInstanceModule.Server | None = None) -> _EnvInstanceProxyModule.RegisterenvinstanceRequest: ...

EnvInstanceProxy: _EnvInstanceProxyModule
EnvInstanceProxyClient: TypeAlias = _EnvInstanceProxyModule.EnvInstanceProxyClient

class _InstanceFactoryModule(_IdentifiableModule):
    class ModelinfoRequest(Protocol):
        def send(self) -> _InstanceFactoryModule.InstanceFactoryClient.ModelinfoResult: ...

    class NewinstanceRequest(Protocol):
        def send(self) -> _InstanceFactoryModule.InstanceFactoryClient.NewinstanceResult: ...

    class NewinstancesRequest(Protocol):
        numberOfInstances: int
        def send(self) -> _InstanceFactoryModule.InstanceFactoryClient.NewinstancesResult: ...

    @classmethod
    def _new_client(cls, server: _InstanceFactoryModule.Server | _IdentifiableModule.Server) -> _InstanceFactoryModule.InstanceFactoryClient: ...
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

        def modelInfo(self, _context: _InstanceFactoryModule.Server.ModelinfoCallContext, **kwargs: Any) -> Awaitable[_InstanceFactoryModule.Server.ModelinfoResultTuple | None]: ...
        def modelInfo_context(self, context: _InstanceFactoryModule.Server.ModelinfoCallContext) -> Awaitable[None]: ...
        def newInstance(self, _context: _InstanceFactoryModule.Server.NewinstanceCallContext, **kwargs: Any) -> Awaitable[_IdentifiableModule.Server | _InstanceFactoryModule.Server.NewinstanceResultTuple | None]: ...
        def newInstance_context(self, context: _InstanceFactoryModule.Server.NewinstanceCallContext) -> Awaitable[None]: ...
        def newInstances(self, numberOfInstances: int, _context: _InstanceFactoryModule.Server.NewinstancesCallContext, **kwargs: Any) -> Awaitable[_InstanceFactoryModule.Server.NewinstancesResultTuple | None]: ...
        def newInstances_context(self, context: _InstanceFactoryModule.Server.NewinstancesCallContext) -> Awaitable[None]: ...

    class InstanceFactoryClient(_IdentifiableModule.IdentifiableClient):
        class ModelinfoResult(Awaitable[ModelinfoResult], Protocol):
            id: str
            name: str
            description: str

        class NewinstanceResult(Awaitable[NewinstanceResult], Protocol):
            instance: _IdentifiableModule.IdentifiableClient

        class NewinstancesResult(Awaitable[NewinstancesResult], Protocol):
            instances: Sequence[_IdentifiableModule]

        def modelInfo(self) -> _InstanceFactoryModule.InstanceFactoryClient.ModelinfoResult: ...
        def newInstance(self) -> _InstanceFactoryModule.InstanceFactoryClient.NewinstanceResult: ...
        def newInstances(self, numberOfInstances: int | None = None) -> _InstanceFactoryModule.InstanceFactoryClient.NewinstancesResult: ...
        def modelInfo_request(self) -> _InstanceFactoryModule.ModelinfoRequest: ...
        def newInstance_request(self) -> _InstanceFactoryModule.NewinstanceRequest: ...
        def newInstances_request(self, numberOfInstances: int | None = None) -> _InstanceFactoryModule.NewinstancesRequest: ...

InstanceFactory: _InstanceFactoryModule
InstanceFactoryClient: TypeAlias = _InstanceFactoryModule.InstanceFactoryClient

# Top-level type aliases for use in type annotations
UnregisterClient: TypeAlias = _EnvInstanceProxyModule._UnregisterModule.UnregisterClient
