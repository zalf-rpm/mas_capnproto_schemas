"""This is an automatically generated stub for `model.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator, Sequence
from contextlib import contextmanager
from enum import Enum
from io import BufferedWriter
from typing import (
    Any,
    BinaryIO,
    Generic,
    Literal,
    NamedTuple,
    Protocol,
    Self,
    TypeAlias,
    TypeVar,
    overload,
)

from .climate_capnp import TimeSeries, TimeSeriesClient
from .common_capnp import Identifiable, IdentifiableClient
from .management_capnp import Event
from .persistence_capnp import Persistent, PersistentClient
from .service_capnp import Stoppable, StoppableClient
from .soil_capnp import Profile, ProfileClient

_RestInput = TypeVar("_RestInput")

XYResultBuilder: TypeAlias = XYResult.Builder
XYResultReader: TypeAlias = XYResult.Reader

class XYResult:
    class Reader:
        @property
        def xs(self) -> Sequence[float]: ...
        @property
        def ys(self) -> Sequence[float]: ...
        def as_builder(self) -> XYResult.Builder: ...

    class Builder:
        @property
        def xs(self) -> Sequence[float]: ...
        @xs.setter
        def xs(self, value: Sequence[float]) -> None: ...
        @property
        def ys(self) -> Sequence[float]: ...
        @ys.setter
        def ys(self, value: Sequence[float]) -> None: ...
        @staticmethod
        def from_dict(dictionary: dict[str, Any]) -> XYResult.Builder: ...
        @overload
        def init(
            self: Any, name: Literal["xs"], size: int = ...
        ) -> Sequence[float]: ...
        @overload
        def init(
            self: Any, name: Literal["ys"], size: int = ...
        ) -> Sequence[float]: ...
        def init(self: Any, name: str, size: int = ...) -> Any: ...
        def copy(self) -> XYResult.Builder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> XYResult.Reader: ...
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
    ) -> Iterator[XYResult.Reader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> XYResult.Reader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        xs: Sequence[float] | None = None,
        ys: Sequence[float] | None = None,
    ) -> XYResult.Builder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> XYResult.Reader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> XYResult.Reader: ...
    def to_dict(self) -> dict[str, Any]: ...

StatBuilder: TypeAlias = Stat.Builder
StatReader: TypeAlias = Stat.Reader

class Stat:
    class Type(Enum):
        min = "min"
        max = "max"
        sd = "sd"
        avg = "avg"
        median = "median"

    class Reader:
        @property
        def type(self) -> Stat.Type: ...
        @property
        def vs(self) -> Sequence[float]: ...
        def as_builder(self) -> Stat.Builder: ...

    class Builder:
        @property
        def type(self) -> Stat.Type: ...
        @type.setter
        def type(
            self, value: Stat.Type | Literal["min", "max", "sd", "avg", "median"]
        ) -> None: ...
        @property
        def vs(self) -> Sequence[float]: ...
        @vs.setter
        def vs(self, value: Sequence[float]) -> None: ...
        @staticmethod
        def from_dict(dictionary: dict[str, Any]) -> Stat.Builder: ...
        def init(self, name: Literal["vs"], size: int = ...) -> Sequence[float]: ...
        def copy(self) -> Stat.Builder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> Stat.Reader: ...
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
    ) -> Iterator[Stat.Reader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Stat.Reader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        type: Stat.Type | Literal["min", "max", "sd", "avg", "median"] | None = None,
        vs: Sequence[float] | None = None,
    ) -> Stat.Builder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Stat.Reader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Stat.Reader: ...
    def to_dict(self) -> dict[str, Any]: ...

XYPlusResultBuilder: TypeAlias = XYPlusResult.Builder
XYPlusResultReader: TypeAlias = XYPlusResult.Reader

class XYPlusResult:
    class Reader:
        @property
        def xy(self) -> XYResult.Reader: ...
        @property
        def stats(self) -> Sequence[Stat.Reader]: ...
        def as_builder(self) -> XYPlusResult.Builder: ...

    class Builder:
        @property
        def xy(self) -> XYResult.Builder: ...
        @xy.setter
        def xy(
            self, value: XYResult.Builder | XYResult.Reader | dict[str, Any]
        ) -> None: ...
        @property
        def stats(self) -> Sequence[Stat.Builder]: ...
        @stats.setter
        def stats(
            self, value: Sequence[Stat.Builder | Stat.Reader] | Sequence[dict[str, Any]]
        ) -> None: ...
        @staticmethod
        def from_dict(dictionary: dict[str, Any]) -> XYPlusResult.Builder: ...
        @overload
        def init(self: Any, name: Literal["xy"]) -> XYResult.Builder: ...
        @overload
        def init(
            self: Any, name: Literal["stats"], size: int = ...
        ) -> Sequence[Stat.Builder]: ...
        def init(self: Any, name: str, size: int = ...) -> Any: ...
        def copy(self) -> XYPlusResult.Builder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> XYPlusResult.Reader: ...
        @staticmethod
        def write(file: BufferedWriter) -> None: ...
        @staticmethod
        def write_packed(file: BufferedWriter) -> None: ...

    def init(self, name: Literal["xy"]) -> XYResult: ...
    @staticmethod
    @contextmanager
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[XYPlusResult.Reader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> XYPlusResult.Reader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        xy: XYResult.Builder | dict[str, Any] | None = None,
        stats: Sequence[Stat.Builder] | Sequence[dict[str, Any]] | None = None,
    ) -> XYPlusResult.Builder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> XYPlusResult.Reader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> XYPlusResult.Reader: ...
    def to_dict(self) -> dict[str, Any]: ...

class ClimateInstance:
    class RunRequest(Protocol):
        def send(self) -> ClimateInstance.RunResult: ...

    class RunResult(Awaitable[RunResult], Protocol):
        result: XYResult.Builder | XYResult.Reader

    class RunsetRequest(Protocol):
        def send(self) -> ClimateInstance.RunsetResult: ...

    class RunsetResult(Awaitable[RunsetResult], Protocol):
        result: XYPlusResult.Builder | XYPlusResult.Reader

    @classmethod
    def _new_client(
        cls, server: ClimateInstance.Server | Identifiable.Server
    ) -> "ClimateInstanceClient": ...
    class Server(Identifiable.Server):
        class RunResultTuple(NamedTuple):
            result: XYResult.Builder | XYResult.Reader

        class RunsetResultTuple(NamedTuple):
            result: XYPlusResult.Builder | XYPlusResult.Reader

        class RunCallContext(Protocol):
            results: ClimateInstance.RunResult

        class RunsetCallContext(Protocol):
            results: ClimateInstance.RunsetResult

        def run(
            self, _context: ClimateInstance.Server.RunCallContext, **kwargs: Any
        ) -> Awaitable[ClimateInstance.Server.RunResultTuple | None]: ...
        def runSet(
            self, _context: ClimateInstance.Server.RunsetCallContext, **kwargs: Any
        ) -> Awaitable[ClimateInstance.Server.RunsetResultTuple | None]: ...
        def __enter__(self) -> Self: ...
        def __exit__(self, *args: Any) -> None: ...

class ClimateInstanceClient(IdentifiableClient):
    def run(self) -> ClimateInstance.RunResult: ...
    def runSet(self) -> ClimateInstance.RunsetResult: ...
    def run_request(self) -> ClimateInstance.RunRequest: ...
    def runSet_request(self) -> ClimateInstance.RunsetRequest: ...

EnvBuilder: TypeAlias = Env.Builder
EnvReader: TypeAlias = Env.Reader

class Env(Generic[_RestInput]):
    class Reader:
        @property
        def rest(self) -> _RestInput: ...
        @property
        def timeSeries(self) -> TimeSeriesClient: ...
        @property
        def soilProfile(self) -> ProfileClient: ...
        @property
        def mgmtEvents(self) -> Sequence[Event.Reader]: ...
        def as_builder(self) -> Env.Builder: ...

    class Builder:
        @property
        def rest(self) -> _RestInput: ...
        @rest.setter
        def rest(self, value: _RestInput) -> None: ...
        @property
        def timeSeries(self) -> TimeSeriesClient: ...
        @timeSeries.setter
        def timeSeries(self, value: TimeSeriesClient | TimeSeries.Server) -> None: ...
        @property
        def soilProfile(self) -> ProfileClient: ...
        @soilProfile.setter
        def soilProfile(self, value: ProfileClient | Profile.Server) -> None: ...
        @property
        def mgmtEvents(self) -> Sequence[Event.Builder]: ...
        @mgmtEvents.setter
        def mgmtEvents(
            self,
            value: Sequence[Event.Builder | Event.Reader] | Sequence[dict[str, Any]],
        ) -> None: ...
        @staticmethod
        def from_dict(dictionary: dict[str, Any]) -> Env.Builder: ...
        def init(
            self, name: Literal["mgmtEvents"], size: int = ...
        ) -> Sequence[Event.Builder]: ...
        def copy(self) -> Env.Builder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> Env.Reader: ...
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
    ) -> Iterator[Env.Reader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Env.Reader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        rest: _RestInput | None = None,
        timeSeries: TimeSeriesClient | TimeSeries.Server | None = None,
        soilProfile: ProfileClient | Profile.Server | None = None,
        mgmtEvents: Sequence[Event.Builder] | Sequence[dict[str, Any]] | None = None,
    ) -> Env.Builder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Env.Reader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Env.Reader: ...
    def to_dict(self) -> dict[str, Any]: ...

class EnvInstance:
    class RunRequest(Protocol):
        env: Env[Any].Builder
        @overload
        def init(self, name: Literal["env"]) -> Env[Any].Builder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> EnvInstance.RunResult: ...

    class RunResult(Awaitable[RunResult], Protocol):
        result: Any

    @classmethod
    def _new_client(
        cls,
        server: EnvInstance.Server
        | Identifiable.Server
        | Persistent.Server
        | Stoppable.Server,
    ) -> "EnvInstanceClient": ...
    class Server(Identifiable.Server, Persistent.Server, Stoppable.Server):
        class RunResultTuple(NamedTuple):
            result: Any

        class RunCallContext(Protocol):
            results: EnvInstance.RunResult

        def run(
            self,
            env: Env[Any].Reader,
            _context: EnvInstance.Server.RunCallContext,
            **kwargs: Any,
        ) -> Awaitable[EnvInstance.Server.RunResultTuple | None]: ...
        def __enter__(self) -> Self: ...
        def __exit__(self, *args: Any) -> None: ...

class EnvInstanceClient(IdentifiableClient, PersistentClient, StoppableClient):
    def run(
        self, env: Env[Any] | dict[str, Any] | None = None
    ) -> EnvInstance.RunResult: ...
    def run_request(
        self, env: Env[Any].Builder | None = None
    ) -> EnvInstance.RunRequest: ...

class EnvInstanceProxy:
    class Unregister:
        class UnregisterRequest(Protocol):
            def send(self) -> EnvInstanceProxy.Unregister.UnregisterResult: ...

        class UnregisterResult(Awaitable[UnregisterResult], Protocol):
            success: bool

        @classmethod
        def _new_client(
            cls, server: EnvInstanceProxy.Unregister.Server
        ) -> "EnvInstanceProxy.UnregisterClient": ...
        class Server(Protocol):
            class UnregisterResultTuple(NamedTuple):
                success: bool

            class UnregisterCallContext(Protocol):
                results: EnvInstanceProxy.Unregister.UnregisterResult

            def unregister(
                self,
                _context: EnvInstanceProxy.Unregister.Server.UnregisterCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                bool | EnvInstanceProxy.Unregister.Server.UnregisterResultTuple | None
            ]: ...
            def __enter__(self) -> Self: ...
            def __exit__(self, *args: Any) -> None: ...

    class UnregisterClient(Protocol):
        def unregister(self) -> EnvInstanceProxy.Unregister.UnregisterResult: ...
        def unregister_request(
            self,
        ) -> EnvInstanceProxy.Unregister.UnregisterRequest: ...

    class RegisterenvinstanceRequest(Protocol):
        instance: EnvInstance | EnvInstance.Server
        def send(self) -> EnvInstanceProxy.RegisterenvinstanceResult: ...

    class RegisterenvinstanceResult(Awaitable[RegisterenvinstanceResult], Protocol):
        unregister: EnvInstanceProxy.UnregisterClient

    @classmethod
    def _new_client(
        cls,
        server: EnvInstanceProxy.Server
        | EnvInstance.Server
        | Identifiable.Server
        | Persistent.Server
        | Stoppable.Server,
    ) -> "EnvInstanceProxyClient": ...
    class Server(EnvInstance.Server):
        class RegisterenvinstanceResultTuple(NamedTuple):
            unregister: EnvInstanceProxy.Unregister.Server

        class RegisterenvinstanceCallContext(Protocol):
            results: EnvInstanceProxy.RegisterenvinstanceResult

        def registerEnvInstance(
            self,
            instance: EnvInstance,
            _context: EnvInstanceProxy.Server.RegisterenvinstanceCallContext,
            **kwargs: Any,
        ) -> Awaitable[
            EnvInstanceProxy.Unregister.Server
            | EnvInstanceProxy.Server.RegisterenvinstanceResultTuple
            | None
        ]: ...
        def __enter__(self) -> Self: ...
        def __exit__(self, *args: Any) -> None: ...

class EnvInstanceProxyClient(EnvInstanceClient):
    def registerEnvInstance(
        self, instance: EnvInstance | EnvInstance.Server | None = None
    ) -> EnvInstanceProxy.RegisterenvinstanceResult: ...
    def registerEnvInstance_request(
        self, instance: EnvInstance | EnvInstance.Server | None = None
    ) -> EnvInstanceProxy.RegisterenvinstanceRequest: ...

class InstanceFactory:
    class ModelinfoRequest(Protocol):
        def send(self) -> InstanceFactory.ModelinfoResult: ...

    class ModelinfoResult(Awaitable[ModelinfoResult], Protocol):
        id: str
        name: str
        description: str

    class NewinstanceRequest(Protocol):
        def send(self) -> InstanceFactory.NewinstanceResult: ...

    class NewinstanceResult(Awaitable[NewinstanceResult], Protocol):
        instance: IdentifiableClient

    class NewinstancesRequest(Protocol):
        numberOfInstances: int
        def send(self) -> InstanceFactory.NewinstancesResult: ...

    class NewinstancesResult(Awaitable[NewinstancesResult], Protocol):
        instances: Sequence[Identifiable]

    @classmethod
    def _new_client(
        cls, server: InstanceFactory.Server | Identifiable.Server
    ) -> "InstanceFactoryClient": ...
    class Server(Identifiable.Server):
        class ModelinfoResultTuple(NamedTuple):
            id: str
            name: str
            description: str

        class NewinstanceResultTuple(NamedTuple):
            instance: Identifiable.Server

        class NewinstancesResultTuple(NamedTuple):
            instances: Sequence[Identifiable]

        class ModelinfoCallContext(Protocol):
            results: InstanceFactory.ModelinfoResult

        class NewinstanceCallContext(Protocol):
            results: InstanceFactory.NewinstanceResult

        class NewinstancesCallContext(Protocol):
            results: InstanceFactory.NewinstancesResult

        def modelInfo(
            self, _context: InstanceFactory.Server.ModelinfoCallContext, **kwargs: Any
        ) -> Awaitable[InstanceFactory.Server.ModelinfoResultTuple | None]: ...
        def newInstance(
            self, _context: InstanceFactory.Server.NewinstanceCallContext, **kwargs: Any
        ) -> Awaitable[
            Identifiable.Server | InstanceFactory.Server.NewinstanceResultTuple | None
        ]: ...
        def newInstances(
            self,
            numberOfInstances: int,
            _context: InstanceFactory.Server.NewinstancesCallContext,
            **kwargs: Any,
        ) -> Awaitable[InstanceFactory.Server.NewinstancesResultTuple | None]: ...
        def __enter__(self) -> Self: ...
        def __exit__(self, *args: Any) -> None: ...

class InstanceFactoryClient(IdentifiableClient):
    def modelInfo(self) -> InstanceFactory.ModelinfoResult: ...
    def newInstance(self) -> InstanceFactory.NewinstanceResult: ...
    def newInstances(
        self, numberOfInstances: int | None = None
    ) -> InstanceFactory.NewinstancesResult: ...
    def modelInfo_request(self) -> InstanceFactory.ModelinfoRequest: ...
    def newInstance_request(self) -> InstanceFactory.NewinstanceRequest: ...
    def newInstances_request(
        self, numberOfInstances: int | None = None
    ) -> InstanceFactory.NewinstancesRequest: ...
