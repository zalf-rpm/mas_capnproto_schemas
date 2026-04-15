"""This is an automatically generated stub for `model.capnp`."""

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

from mas.schema.climate.climate_capnp.types.clients import TimeSeriesClient
from mas.schema.climate.climate_capnp.types.modules import _TimeSeriesInterfaceModule
from mas.schema.common.common_capnp.types.builders import IdInformationBuilder
from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.management.management_capnp.types.builders import EventBuilder
from mas.schema.management.management_capnp.types.readers import EventReader
from mas.schema.persistence.persistence_capnp.types.clients import PersistentClient
from mas.schema.persistence.persistence_capnp.types.modules import (
    _PersistentInterfaceModule,
)
from mas.schema.service.service_capnp.types.clients import StoppableClient
from mas.schema.service.service_capnp.types.modules import _StoppableInterfaceModule
from mas.schema.soil.soil_capnp.types.clients import ProfileClient
from mas.schema.soil.soil_capnp.types.modules import _ProfileInterfaceModule

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

class _Float64List:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> float: ...
        @override
        def __iter__(self) -> Iterator[float]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> float: ...
        @override
        def __setitem__(self, key: int, value: float) -> None: ...
        @override
        def __iter__(self) -> Iterator[float]: ...

class _XYResultStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        xs: Float64ListBuilder | dict[str, Any] | None = None,
        ys: Float64ListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> XYResultBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[XYResultReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[XYResultReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[XYResultBuilder]: ...
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
    ) -> XYResultReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> XYResultReader: ...

class XYResultReader(_DynamicStructReader):
    @property
    def xs(self) -> Float64ListReader: ...
    @property
    def ys(self) -> Float64ListReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> XYResultBuilder: ...

class XYResultBuilder(_DynamicStructBuilder):
    @property
    def xs(self) -> Float64ListBuilder: ...
    @xs.setter
    def xs(
        self,
        value: Float64ListBuilder | Float64ListReader | dict[str, Any],
    ) -> None: ...
    @property
    def ys(self) -> Float64ListBuilder: ...
    @ys.setter
    def ys(
        self,
        value: Float64ListBuilder | Float64ListReader | dict[str, Any],
    ) -> None: ...
    @override
    @overload
    def init(
        self,
        field: Literal["xs"],
        size: int | None = None,
    ) -> Float64ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["ys"],
        size: int | None = None,
    ) -> Float64ListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> XYResultReader: ...

XYResult: _XYResultStructModule

class _StatStructModule(_StructModule):
    class _TypeEnumModule:
        min: int
        max: int
        sd: int
        avg: int
        median: int

    Type: _TypeEnumModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        type: StatTypeEnum | None = None,
        vs: Float64ListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> StatBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[StatReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[StatReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[StatBuilder]: ...
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
    ) -> StatReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> StatReader: ...

class StatReader(_DynamicStructReader):
    @property
    def type(self) -> StatTypeEnum: ...
    @property
    def vs(self) -> Float64ListReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> StatBuilder: ...

class StatBuilder(_DynamicStructBuilder):
    @property
    def type(self) -> StatTypeEnum: ...
    @type.setter
    def type(self, value: StatTypeEnum) -> None: ...
    @property
    def vs(self) -> Float64ListBuilder: ...
    @vs.setter
    def vs(
        self,
        value: Float64ListBuilder | Float64ListReader | dict[str, Any],
    ) -> None: ...
    @override
    def init(
        self,
        field: Literal["vs"],
        size: int | None = None,
    ) -> Float64ListBuilder: ...
    @override
    def as_reader(self) -> StatReader: ...

Stat: _StatStructModule

class _StatList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> StatReader: ...
        @override
        def __iter__(self) -> Iterator[StatReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> StatBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: StatReader | StatBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[StatBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> StatBuilder: ...

class _XYPlusResultStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        xy: XYResultBuilder | dict[str, Any] | None = None,
        stats: StatListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> XYPlusResultBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[XYPlusResultReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[XYPlusResultReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[XYPlusResultBuilder]: ...
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
    ) -> XYPlusResultReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> XYPlusResultReader: ...

class XYPlusResultReader(_DynamicStructReader):
    @property
    def xy(self) -> XYResultReader: ...
    @property
    def stats(self) -> StatListReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> XYPlusResultBuilder: ...

class XYPlusResultBuilder(_DynamicStructBuilder):
    @property
    def xy(self) -> XYResultBuilder: ...
    @xy.setter
    def xy(self, value: XYResultBuilder | XYResultReader | dict[str, Any]) -> None: ...
    @property
    def stats(self) -> StatListBuilder: ...
    @stats.setter
    def stats(
        self,
        value: StatListBuilder | StatListReader | dict[str, Any],
    ) -> None: ...
    @override
    @overload
    def init(
        self,
        field: Literal["xy"],
        size: int | None = None,
    ) -> XYResultBuilder: ...
    @overload
    def init(
        self,
        field: Literal["stats"],
        size: int | None = None,
    ) -> StatListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> XYPlusResultReader: ...

XYPlusResult: _XYPlusResultStructModule

class _ClimateInstanceInterfaceModule(_IdentifiableInterfaceModule):
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> ClimateInstanceClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def run(
            self,
            timeSeries: TimeSeriesClient,
            _context: ClimateInstanceRunCallContext,
            **kwargs: object,
        ) -> Awaitable[
            XYResultBuilder
            | XYResultReader
            | dict[str, Any]
            | ClimateInstanceRunResultTuple
            | None
        ]: ...
        def run_context(
            self,
            context: ClimateInstanceRunCallContext,
        ) -> Awaitable[None]: ...
        def runSet(
            self,
            dataset: TimeSeriesClientListReader,
            _context: RunsetCallContext,
            **kwargs: object,
        ) -> Awaitable[
            XYPlusResultBuilder
            | XYPlusResultReader
            | dict[str, Any]
            | RunsetResultTuple
            | None
        ]: ...
        def runSet_context(self, context: RunsetCallContext) -> Awaitable[None]: ...

class ClimateInstanceRunRequest(Protocol):
    timeSeries: TimeSeriesClient | _TimeSeriesInterfaceModule.Server
    def send(self) -> ClimateInstanceRunResult: ...

class ClimateInstanceRunResult(Awaitable[ClimateInstanceRunResult], Protocol):
    result: XYResultReader

class ClimateInstanceRunServerResult(_DynamicStructBuilder):
    @property
    def result(self) -> XYResultBuilder: ...
    @result.setter
    def result(
        self,
        value: XYResultBuilder | XYResultReader | dict[str, Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["result"],
        size: int | None = None,
    ) -> XYResultBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class ClimateInstanceRunParams(Protocol):
    timeSeries: TimeSeriesClient

class ClimateInstanceRunCallContext(Protocol):
    params: ClimateInstanceRunParams
    @property
    def results(self) -> ClimateInstanceRunServerResult: ...

class ClimateInstanceRunResultTuple(NamedTuple):
    result: XYResultBuilder | XYResultReader | dict[str, Any]

class _TimeSeriesClientList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> TimeSeriesClient: ...
        @override
        def __iter__(self) -> Iterator[TimeSeriesClient]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> TimeSeriesClient: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: TimeSeriesClient | _TimeSeriesInterfaceModule.Server,
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[TimeSeriesClient]: ...

class RunsetRequest(Protocol):
    dataset: TimeSeriesClientListBuilder | TimeSeriesClientListReader | Sequence[Any]
    @overload
    def init(
        self,
        name: Literal["dataset"],
        size: int = ...,
    ) -> TimeSeriesClientListBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> RunsetResult: ...

class RunsetResult(Awaitable[RunsetResult], Protocol):
    result: XYPlusResultReader

class RunsetServerResult(_DynamicStructBuilder):
    @property
    def result(self) -> XYPlusResultBuilder: ...
    @result.setter
    def result(
        self,
        value: XYPlusResultBuilder | XYPlusResultReader | dict[str, Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["result"],
        size: int | None = None,
    ) -> XYPlusResultBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class RunsetParams(Protocol):
    dataset: TimeSeriesClientListReader

class RunsetCallContext(Protocol):
    params: RunsetParams
    @property
    def results(self) -> RunsetServerResult: ...

class RunsetResultTuple(NamedTuple):
    result: XYPlusResultBuilder | XYPlusResultReader | dict[str, Any]

class ClimateInstanceClient(IdentifiableClient):
    def run(
        self,
        timeSeries: TimeSeriesClient | _TimeSeriesInterfaceModule.Server | None = None,
    ) -> ClimateInstanceRunResult: ...
    def runSet(
        self,
        dataset: TimeSeriesClientListBuilder
        | TimeSeriesClientListReader
        | Sequence[Any]
        | None = None,
    ) -> RunsetResult: ...
    def run_request(
        self,
        timeSeries: TimeSeriesClient | _TimeSeriesInterfaceModule.Server | None = None,
    ) -> ClimateInstanceRunRequest: ...
    def runSet_request(
        self,
        dataset: TimeSeriesClientListBuilder
        | TimeSeriesClientListReader
        | Sequence[Any]
        | None = None,
    ) -> RunsetRequest: ...

ClimateInstance: _ClimateInstanceInterfaceModule

class _EventList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> EventReader: ...
        @override
        def __iter__(self) -> Iterator[EventReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> EventBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: EventReader | EventBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[EventBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> EventBuilder: ...

class _EnvStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        rest: AnyPointer | None = None,
        timeSeries: TimeSeriesClient | _TimeSeriesInterfaceModule.Server | None = None,
        soilProfile: ProfileClient | _ProfileInterfaceModule.Server | None = None,
        mgmtEvents: EventListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> EnvBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[EnvReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[EnvReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[EnvBuilder]: ...
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
    ) -> EnvReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> EnvReader: ...

class EnvReader(_DynamicStructReader):
    @property
    def rest(self) -> _DynamicObjectReader: ...
    @property
    def timeSeries(self) -> TimeSeriesClient: ...
    @property
    def soilProfile(self) -> ProfileClient: ...
    @property
    def mgmtEvents(self) -> EventListReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> EnvBuilder: ...

class EnvBuilder(_DynamicStructBuilder):
    @property
    def rest(self) -> _DynamicObjectReader: ...
    @rest.setter
    def rest(self, value: AnyPointer) -> None: ...
    @property
    def timeSeries(self) -> TimeSeriesClient: ...
    @timeSeries.setter
    def timeSeries(
        self,
        value: TimeSeriesClient | _TimeSeriesInterfaceModule.Server,
    ) -> None: ...
    @property
    def soilProfile(self) -> ProfileClient: ...
    @soilProfile.setter
    def soilProfile(
        self,
        value: ProfileClient | _ProfileInterfaceModule.Server,
    ) -> None: ...
    @property
    def mgmtEvents(self) -> EventListBuilder: ...
    @mgmtEvents.setter
    def mgmtEvents(
        self,
        value: EventListBuilder | EventListReader | dict[str, Any],
    ) -> None: ...
    @override
    def init(
        self,
        field: Literal["mgmtEvents"],
        size: int | None = None,
    ) -> EventListBuilder: ...
    @override
    def as_reader(self) -> EnvReader: ...

Env: _EnvStructModule

class _EnvInstanceInterfaceModule(
    _IdentifiableInterfaceModule,
    _PersistentInterfaceModule,
    _StoppableInterfaceModule,
):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> EnvInstanceClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
        _StoppableInterfaceModule.Server,
    ):
        def run(
            self,
            env: EnvReader,
            _context: EnvInstanceRunCallContext,
            **kwargs: object,
        ) -> Awaitable[AnyPointer | EnvInstanceRunResultTuple | None]: ...
        def run_context(
            self,
            context: EnvInstanceRunCallContext,
        ) -> Awaitable[None]: ...

class EnvInstanceRunRequest(Protocol):
    env: EnvBuilder
    @overload
    def init(self, name: Literal["env"]) -> EnvBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> EnvInstanceRunResult: ...

class EnvInstanceRunResult(Awaitable[EnvInstanceRunResult], Protocol):
    result: _DynamicObjectReader

class EnvInstanceRunServerResult(_DynamicStructBuilder):
    @property
    def result(self) -> AnyPointer: ...
    @result.setter
    def result(self, value: AnyPointer) -> None: ...

class EnvInstanceRunParams(Protocol):
    env: EnvReader

class EnvInstanceRunCallContext(Protocol):
    params: EnvInstanceRunParams
    @property
    def results(self) -> EnvInstanceRunServerResult: ...

class EnvInstanceRunResultTuple(NamedTuple):
    result: AnyPointer

class EnvInstanceClient(IdentifiableClient, PersistentClient, StoppableClient):
    def run(
        self,
        env: EnvBuilder | EnvReader | dict[str, Any] | None = None,
    ) -> EnvInstanceRunResult: ...
    def run_request(self, env: EnvBuilder | None = None) -> EnvInstanceRunRequest: ...

EnvInstance: _EnvInstanceInterfaceModule

class _EnvInstanceProxyInterfaceModule(_EnvInstanceInterfaceModule):
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
    type UnregisterServer = (
        _EnvInstanceProxyInterfaceModule._UnregisterInterfaceModule.Server
    )
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> EnvInstanceProxyClient: ...
    class Server(_EnvInstanceInterfaceModule.Server):
        def registerEnvInstance(
            self,
            instance: EnvInstanceClient,
            _context: RegisterenvinstanceCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _EnvInstanceProxyInterfaceModule._UnregisterInterfaceModule.Server
            | UnregisterClient
            | RegisterenvinstanceResultTuple
            | None
        ]: ...
        def registerEnvInstance_context(
            self,
            context: RegisterenvinstanceCallContext,
        ) -> Awaitable[None]: ...

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

class RegisterenvinstanceRequest(Protocol):
    instance: EnvInstanceClient | _EnvInstanceInterfaceModule.Server
    def send(self) -> RegisterenvinstanceResult: ...

class RegisterenvinstanceResult(Awaitable[RegisterenvinstanceResult], Protocol):
    unregister: UnregisterClient

class RegisterenvinstanceServerResult(_DynamicStructBuilder):
    @property
    def unregister(
        self,
    ) -> (
        _EnvInstanceProxyInterfaceModule._UnregisterInterfaceModule.Server
        | UnregisterClient
    ): ...
    @unregister.setter
    def unregister(
        self,
        value: _EnvInstanceProxyInterfaceModule._UnregisterInterfaceModule.Server
        | UnregisterClient,
    ) -> None: ...

class RegisterenvinstanceParams(Protocol):
    instance: EnvInstanceClient

class RegisterenvinstanceCallContext(Protocol):
    params: RegisterenvinstanceParams
    @property
    def results(self) -> RegisterenvinstanceServerResult: ...

class RegisterenvinstanceResultTuple(NamedTuple):
    unregister: (
        _EnvInstanceProxyInterfaceModule._UnregisterInterfaceModule.Server
        | UnregisterClient
    )

class EnvInstanceProxyClient(EnvInstanceClient):
    def registerEnvInstance(
        self,
        instance: EnvInstanceClient | _EnvInstanceInterfaceModule.Server | None = None,
    ) -> RegisterenvinstanceResult: ...
    def registerEnvInstance_request(
        self,
        instance: EnvInstanceClient | _EnvInstanceInterfaceModule.Server | None = None,
    ) -> RegisterenvinstanceRequest: ...

EnvInstanceProxy: _EnvInstanceProxyInterfaceModule

class _InstanceFactoryInterfaceModule(_IdentifiableInterfaceModule):
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> InstanceFactoryClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def modelInfo(
            self,
            _context: ModelinfoCallContext,
            **kwargs: object,
        ) -> Awaitable[ModelinfoResultTuple | None]: ...
        def modelInfo_context(
            self,
            context: ModelinfoCallContext,
        ) -> Awaitable[None]: ...
        def newInstance(
            self,
            _context: NewinstanceCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _IdentifiableInterfaceModule.Server
            | IdentifiableClient
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
            IdentifiableClientListBuilder
            | IdentifiableClientListReader
            | Sequence[Any]
            | NewinstancesResultTuple
            | None
        ]: ...
        def newInstances_context(
            self,
            context: NewinstancesCallContext,
        ) -> Awaitable[None]: ...

class ModelinfoRequest(Protocol):
    def send(self) -> ModelinfoResult: ...

class ModelinfoResult(Awaitable[ModelinfoResult], Protocol):
    id: str
    name: str
    description: str

class ModelinfoParams(Protocol): ...

class ModelinfoCallContext(Protocol):
    params: ModelinfoParams
    @property
    def results(self) -> IdInformationBuilder: ...

class ModelinfoResultTuple(NamedTuple):
    id: str
    name: str
    description: str

class NewinstanceRequest(Protocol):
    def send(self) -> NewinstanceResult: ...

class NewinstanceResult(Awaitable[NewinstanceResult], Protocol):
    instance: IdentifiableClient

class NewinstanceServerResult(_DynamicStructBuilder):
    @property
    def instance(self) -> _IdentifiableInterfaceModule.Server | IdentifiableClient: ...
    @instance.setter
    def instance(
        self,
        value: _IdentifiableInterfaceModule.Server | IdentifiableClient,
    ) -> None: ...

class NewinstanceParams(Protocol): ...

class NewinstanceCallContext(Protocol):
    params: NewinstanceParams
    @property
    def results(self) -> NewinstanceServerResult: ...

class NewinstanceResultTuple(NamedTuple):
    instance: _IdentifiableInterfaceModule.Server | IdentifiableClient

class NewinstancesRequest(Protocol):
    numberOfInstances: int
    def send(self) -> NewinstancesResult: ...

class _IdentifiableClientList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> IdentifiableClient: ...
        @override
        def __iter__(self) -> Iterator[IdentifiableClient]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> IdentifiableClient: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: IdentifiableClient | _IdentifiableInterfaceModule.Server,
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[IdentifiableClient]: ...

class NewinstancesResult(Awaitable[NewinstancesResult], Protocol):
    instances: IdentifiableClientListReader

class NewinstancesServerResult(_DynamicStructBuilder):
    @property
    def instances(self) -> IdentifiableClientListBuilder: ...
    @instances.setter
    def instances(
        self,
        value: IdentifiableClientListBuilder
        | IdentifiableClientListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["instances"],
        size: int | None = None,
    ) -> IdentifiableClientListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class NewinstancesParams(Protocol):
    numberOfInstances: int

class NewinstancesCallContext(Protocol):
    params: NewinstancesParams
    @property
    def results(self) -> NewinstancesServerResult: ...

class NewinstancesResultTuple(NamedTuple):
    instances: (
        IdentifiableClientListBuilder | IdentifiableClientListReader | Sequence[Any]
    )

class InstanceFactoryClient(IdentifiableClient):
    def modelInfo(self) -> ModelinfoResult: ...
    def newInstance(self) -> NewinstanceResult: ...
    def newInstances(
        self,
        numberOfInstances: int | None = None,
    ) -> NewinstancesResult: ...
    def modelInfo_request(self) -> ModelinfoRequest: ...
    def newInstance_request(self) -> NewinstanceRequest: ...
    def newInstances_request(
        self,
        numberOfInstances: int | None = None,
    ) -> NewinstancesRequest: ...

InstanceFactory: _InstanceFactoryInterfaceModule

# Top-level type aliases for use in type annotations
ClimateInstanceServer = _ClimateInstanceInterfaceModule.Server
EnvInstanceProxyServer = _EnvInstanceProxyInterfaceModule.Server
EnvInstanceServer = _EnvInstanceInterfaceModule.Server
type EventListBuilder = _EventList.Builder
type EventListReader = _EventList.Reader
type Float64ListBuilder = _Float64List.Builder
type Float64ListReader = _Float64List.Reader
type IdentifiableClientListBuilder = _IdentifiableClientList.Builder
type IdentifiableClientListReader = _IdentifiableClientList.Reader
InstanceFactoryServer = _InstanceFactoryInterfaceModule.Server
type StatListBuilder = _StatList.Builder
type StatListReader = _StatList.Reader
type StatTypeEnum = int | Literal["min", "max", "sd", "avg", "median"]
type TimeSeriesClientListBuilder = _TimeSeriesClientList.Builder
type TimeSeriesClientListReader = _TimeSeriesClientList.Reader
UnregisterServer = _EnvInstanceProxyInterfaceModule._UnregisterInterfaceModule.Server
