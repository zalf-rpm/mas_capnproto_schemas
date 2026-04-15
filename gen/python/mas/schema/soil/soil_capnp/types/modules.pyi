"""Module helper types for `soil.capnp`."""

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
from mas.schema.geo.geo_capnp.types.readers import LatLonCoordReader
from mas.schema.persistence.persistence_capnp.types.modules import (
    _PersistentInterfaceModule,
)

from . import _all as _all

class _LayerStructModule(_StructModule):
    class _PropertyStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            name: _all.PropertyNameEnum | None = None,
            f32Value: float | None = None,
            bValue: bool | None = None,
            type: str | None = None,
            unset: None | None = None,
            **kwargs: object,
        ) -> _all.PropertyBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.PropertyReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.PropertyReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.PropertyBuilder]: ...
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
        ) -> _all.PropertyReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.PropertyReader: ...

    Property: _PropertyStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        properties: _all.PropertyListBuilder | dict[str, Any] | None = None,
        size: float | None = None,
        description: str | None = None,
        **kwargs: object,
    ) -> _all.LayerBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.LayerReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.LayerReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.LayerBuilder]: ...
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
    ) -> _all.LayerReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.LayerReader: ...

class _QueryStructModule(_StructModule):
    class _ResultStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            failed: bool | None = None,
            mandatory: _all.PropertyNameEnumListBuilder | dict[str, Any] | None = None,
            optional: _all.PropertyNameEnumListBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> _all.ResultBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.ResultReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.ResultReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.ResultBuilder]: ...
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
        ) -> _all.ResultReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.ResultReader: ...

    Result: _ResultStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        mandatory: _all.PropertyNameEnumListBuilder | dict[str, Any] | None = None,
        optional: _all.PropertyNameEnumListBuilder | dict[str, Any] | None = None,
        onlyRawData: bool | None = None,
        **kwargs: object,
    ) -> _all.QueryBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.QueryReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.QueryReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.QueryBuilder]: ...
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
    ) -> _all.QueryReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.QueryReader: ...

class _ProfileDataStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        layers: _all.LayerListBuilder | dict[str, Any] | None = None,
        percentageOfArea: float | None = None,
        **kwargs: object,
    ) -> _all.ProfileDataBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.ProfileDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.ProfileDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.ProfileDataBuilder]: ...
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
    ) -> _all.ProfileDataReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.ProfileDataReader: ...

class _ProfileInterfaceModule(_IdentifiableInterfaceModule, _PersistentInterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> _all.ProfileClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def data(
            self,
            _context: _all.DataCallContext,
            **kwargs: object,
        ) -> Awaitable[_all.DataResultTuple | None]: ...
        def data_context(self, context: _all.DataCallContext) -> Awaitable[None]: ...
        def geoLocation(
            self,
            _context: _all.GeolocationCallContext,
            **kwargs: object,
        ) -> Awaitable[_all.GeolocationResultTuple | None]: ...
        def geoLocation_context(
            self,
            context: _all.GeolocationCallContext,
        ) -> Awaitable[None]: ...

class _ServiceInterfaceModule(_IdentifiableInterfaceModule, _PersistentInterfaceModule):
    class _StreamInterfaceModule(_InterfaceModule):
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> _all.StreamClient: ...
        class Server(_DynamicCapabilityServer):
            def nextProfiles(
                self,
                maxCount: int,
                _context: _all.NextprofilesCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _all.ProfileClientListBuilder
                | _all.ProfileClientListReader
                | Sequence[Any]
                | _all.NextprofilesResultTuple
                | None
            ]: ...
            def nextProfiles_context(
                self,
                context: _all.NextprofilesCallContext,
            ) -> Awaitable[None]: ...

    Stream: _StreamInterfaceModule
    type StreamServer = _ServiceInterfaceModule._StreamInterfaceModule.Server
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> _all.ServiceClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def checkAvailableParameters(
            self,
            mandatory: _all.PropertyNameEnumListReader,
            optional: _all.PropertyNameEnumListReader,
            onlyRawData: bool,
            _context: _all.CheckavailableparametersCallContext,
            **kwargs: object,
        ) -> Awaitable[_all.CheckavailableparametersResultTuple | None]: ...
        def checkAvailableParameters_context(
            self,
            context: _all.CheckavailableparametersCallContext,
        ) -> Awaitable[None]: ...
        def getAllAvailableParameters(
            self,
            onlyRawData: bool,
            _context: _all.GetallavailableparametersCallContext,
            **kwargs: object,
        ) -> Awaitable[_all.GetallavailableparametersResultTuple | None]: ...
        def getAllAvailableParameters_context(
            self,
            context: _all.GetallavailableparametersCallContext,
        ) -> Awaitable[None]: ...
        def closestProfilesAt(
            self,
            coord: LatLonCoordReader,
            query: _all.QueryReader,
            _context: _all.ClosestprofilesatCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _all.ProfileClientListBuilder
            | _all.ProfileClientListReader
            | Sequence[Any]
            | _all.ClosestprofilesatResultTuple
            | None
        ]: ...
        def closestProfilesAt_context(
            self,
            context: _all.ClosestprofilesatCallContext,
        ) -> Awaitable[None]: ...
        def streamAllProfiles(
            self,
            mandatory: _all.PropertyNameEnumListReader,
            optional: _all.PropertyNameEnumListReader,
            onlyRawData: bool,
            _context: _all.StreamallprofilesCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _ServiceInterfaceModule._StreamInterfaceModule.Server
            | _all.StreamClient
            | _all.StreamallprofilesResultTuple
            | None
        ]: ...
        def streamAllProfiles_context(
            self,
            context: _all.StreamallprofilesCallContext,
        ) -> Awaitable[None]: ...
