"""Module helper types for `model.capnp`."""

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

from mas.schema.climate.climate_capnp.types.clients import TimeSeriesClient
from mas.schema.climate.climate_capnp.types.modules import _TimeSeriesInterfaceModule
from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.persistence.persistence_capnp.types.modules import (
    _PersistentInterfaceModule,
)
from mas.schema.service.service_capnp.types.modules import _StoppableInterfaceModule
from mas.schema.soil.soil_capnp.types.clients import ProfileClient
from mas.schema.soil.soil_capnp.types.modules import _ProfileInterfaceModule

from . import _all as _all

class _XYResultStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        xs: _all.Float64ListBuilder | dict[str, Any] | None = None,
        ys: _all.Float64ListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> _all.XYResultBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.XYResultReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.XYResultReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.XYResultBuilder]: ...
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
    ) -> _all.XYResultReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.XYResultReader: ...

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
        type: _all.StatTypeEnum | None = None,
        vs: _all.Float64ListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> _all.StatBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.StatReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.StatReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.StatBuilder]: ...
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
    ) -> _all.StatReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.StatReader: ...

class _XYPlusResultStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        xy: _all.XYResultBuilder | dict[str, Any] | None = None,
        stats: _all.StatListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> _all.XYPlusResultBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.XYPlusResultReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.XYPlusResultReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.XYPlusResultBuilder]: ...
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
    ) -> _all.XYPlusResultReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.XYPlusResultReader: ...

class _ClimateInstanceInterfaceModule(_IdentifiableInterfaceModule):
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> _all.ClimateInstanceClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def run(
            self,
            timeSeries: TimeSeriesClient,
            _context: _all.ClimateInstanceRunCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _all.XYResultBuilder
            | _all.XYResultReader
            | dict[str, Any]
            | _all.ClimateInstanceRunResultTuple
            | None
        ]: ...
        def run_context(
            self,
            context: _all.ClimateInstanceRunCallContext,
        ) -> Awaitable[None]: ...
        def runSet(
            self,
            dataset: _all.TimeSeriesClientListReader,
            _context: _all.RunsetCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _all.XYPlusResultBuilder
            | _all.XYPlusResultReader
            | dict[str, Any]
            | _all.RunsetResultTuple
            | None
        ]: ...
        def runSet_context(
            self,
            context: _all.RunsetCallContext,
        ) -> Awaitable[None]: ...

class _EnvStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        rest: _all.AnyPointer | None = None,
        timeSeries: TimeSeriesClient | _TimeSeriesInterfaceModule.Server | None = None,
        soilProfile: ProfileClient | _ProfileInterfaceModule.Server | None = None,
        mgmtEvents: _all.EventListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> _all.EnvBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.EnvReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.EnvReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.EnvBuilder]: ...
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
    ) -> _all.EnvReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.EnvReader: ...

class _EnvInstanceInterfaceModule(
    _IdentifiableInterfaceModule,
    _PersistentInterfaceModule,
    _StoppableInterfaceModule,
):
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> _all.EnvInstanceClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
        _StoppableInterfaceModule.Server,
    ):
        def run(
            self,
            env: _all.EnvReader,
            _context: _all.EnvInstanceRunCallContext,
            **kwargs: object,
        ) -> Awaitable[_all.AnyPointer | _all.EnvInstanceRunResultTuple | None]: ...
        def run_context(
            self,
            context: _all.EnvInstanceRunCallContext,
        ) -> Awaitable[None]: ...

class _EnvInstanceProxyInterfaceModule(_EnvInstanceInterfaceModule):
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
    type UnregisterServer = (
        _EnvInstanceProxyInterfaceModule._UnregisterInterfaceModule.Server
    )
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> _all.EnvInstanceProxyClient: ...
    class Server(_EnvInstanceInterfaceModule.Server):
        def registerEnvInstance(
            self,
            instance: _all.EnvInstanceClient,
            _context: _all.RegisterenvinstanceCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _EnvInstanceProxyInterfaceModule._UnregisterInterfaceModule.Server
            | _all.UnregisterClient
            | _all.RegisterenvinstanceResultTuple
            | None
        ]: ...
        def registerEnvInstance_context(
            self,
            context: _all.RegisterenvinstanceCallContext,
        ) -> Awaitable[None]: ...

class _InstanceFactoryInterfaceModule(_IdentifiableInterfaceModule):
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> _all.InstanceFactoryClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def modelInfo(
            self,
            _context: _all.ModelinfoCallContext,
            **kwargs: object,
        ) -> Awaitable[_all.ModelinfoResultTuple | None]: ...
        def modelInfo_context(
            self,
            context: _all.ModelinfoCallContext,
        ) -> Awaitable[None]: ...
        def newInstance(
            self,
            _context: _all.NewinstanceCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _IdentifiableInterfaceModule.Server
            | IdentifiableClient
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
            _all.IdentifiableClientListBuilder
            | _all.IdentifiableClientListReader
            | Sequence[Any]
            | _all.NewinstancesResultTuple
            | None
        ]: ...
        def newInstances_context(
            self,
            context: _all.NewinstancesCallContext,
        ) -> Awaitable[None]: ...
