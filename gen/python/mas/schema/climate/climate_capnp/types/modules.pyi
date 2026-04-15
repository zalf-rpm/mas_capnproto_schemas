"""Module helper types for `climate.capnp`."""

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

from mas.schema.common.common_capnp.types.builders import IdInformationBuilder
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.common.date_capnp.types.builders import DateBuilder
from mas.schema.common.date_capnp.types.readers import DateReader
from mas.schema.geo.geo_capnp.types.builders import LatLonCoordBuilder
from mas.schema.geo.geo_capnp.types.readers import LatLonCoordReader
from mas.schema.persistence.persistence_capnp.types.modules import (
    _PersistentInterfaceModule,
)

from . import _all as _all

class _EnsembleMemberStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        r: int | None = None,
        i: int | None = None,
        p: int | None = None,
        f: int | None = None,
        **kwargs: object,
    ) -> _all.EnsembleMemberBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.EnsembleMemberReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.EnsembleMemberReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.EnsembleMemberBuilder]: ...
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
    ) -> _all.EnsembleMemberReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.EnsembleMemberReader: ...

class _MetadataStructModule(_StructModule):
    class _SupportedInterfaceModule(_InterfaceModule):
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> _all.SupportedClient: ...
        class Server(_DynamicCapabilityServer):
            def categories(
                self,
                _context: _all.CategoriesCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _all.IdInformationListBuilder
                | _all.IdInformationListReader
                | Sequence[Any]
                | _all.CategoriesResultTuple
                | None
            ]: ...
            def categories_context(
                self,
                context: _all.CategoriesCallContext,
            ) -> Awaitable[None]: ...
            def supportedValues(
                self,
                typeId: str,
                _context: _all.SupportedvaluesCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _all.IdInformationListBuilder
                | _all.IdInformationListReader
                | Sequence[Any]
                | _all.SupportedvaluesResultTuple
                | None
            ]: ...
            def supportedValues_context(
                self,
                context: _all.SupportedvaluesCallContext,
            ) -> Awaitable[None]: ...

    Supported: _SupportedInterfaceModule
    type SupportedServer = _MetadataStructModule._SupportedInterfaceModule.Server
    class _ValueStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            text: str | None = None,
            float: float | None = None,
            int: int | None = None,
            bool: bool | None = None,
            date: DateBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> _all.ValueBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.ValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.ValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.ValueBuilder]: ...
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
        ) -> _all.ValueReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.ValueReader: ...

    Value: _ValueStructModule
    class _EntryStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            gcm: _all.GCMEnum | None = None,
            rcm: _all.RCMEnum | None = None,
            historical: None | None = None,
            rcp: _all.RCPEnum | None = None,
            ssp: _all.SSPEnum | None = None,
            ensMem: _all.EnsembleMemberBuilder | dict[str, Any] | None = None,
            version: str | None = None,
            start: DateBuilder | dict[str, Any] | None = None,
            end: DateBuilder | dict[str, Any] | None = None,
            co2: float | None = None,
            picontrol: None | None = None,
            description: str | None = None,
            **kwargs: object,
        ) -> _all.EntryBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.EntryReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.EntryReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.EntryBuilder]: ...
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
        ) -> _all.EntryReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.EntryReader: ...

    Entry: _EntryStructModule
    class _InformationInterfaceModule(_InterfaceModule):
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> _all.InformationClient: ...
        class Server(_DynamicCapabilityServer):
            def forOne(
                self,
                entry: _all.EntryReader,
                _context: _all.ForoneCallContext,
                **kwargs: object,
            ) -> Awaitable[_all.ForoneResultTuple | None]: ...
            def forOne_context(
                self,
                context: _all.ForoneCallContext,
            ) -> Awaitable[None]: ...
            def forAll(
                self,
                _context: _all.ForallCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _all.PairListBuilder
                | _all.PairListReader
                | Sequence[Any]
                | _all.ForallResultTuple
                | None
            ]: ...
            def forAll_context(
                self,
                context: _all.ForallCallContext,
            ) -> Awaitable[None]: ...

    Information: _InformationInterfaceModule
    type InformationServer = _MetadataStructModule._InformationInterfaceModule.Server
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        entries: _all.EntryListBuilder | dict[str, Any] | None = None,
        info: _all.InformationClient
        | _MetadataStructModule._InformationInterfaceModule.Server
        | None = None,
        **kwargs: object,
    ) -> _all.MetadataBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.MetadataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.MetadataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.MetadataBuilder]: ...
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
    ) -> _all.MetadataReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.MetadataReader: ...

class _DatasetInterfaceModule(_IdentifiableInterfaceModule, _PersistentInterfaceModule):
    class _GetLocationsCallbackInterfaceModule(_InterfaceModule):
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> _all.GetLocationsCallbackClient: ...
        class Server(_DynamicCapabilityServer):
            def nextLocations(
                self,
                maxCount: int,
                _context: _all.NextlocationsCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _all.LocationListBuilder
                | _all.LocationListReader
                | Sequence[Any]
                | _all.NextlocationsResultTuple
                | None
            ]: ...
            def nextLocations_context(
                self,
                context: _all.NextlocationsCallContext,
            ) -> Awaitable[None]: ...

    GetLocationsCallback: _GetLocationsCallbackInterfaceModule
    type GetLocationsCallbackServer = (
        _DatasetInterfaceModule._GetLocationsCallbackInterfaceModule.Server
    )
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> _all.DatasetClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def metadata(
            self,
            _context: _all.DatasetMetadataCallContext,
            **kwargs: object,
        ) -> Awaitable[_all.DatasetMetadataResultTuple | None]: ...
        def metadata_context(
            self,
            context: _all.DatasetMetadataCallContext,
        ) -> Awaitable[None]: ...
        def closestTimeSeriesAt(
            self,
            latlon: LatLonCoordReader,
            _context: _all.ClosesttimeseriesatCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _TimeSeriesInterfaceModule.Server
            | _all.TimeSeriesClient
            | _all.ClosesttimeseriesatResultTuple
            | None
        ]: ...
        def closestTimeSeriesAt_context(
            self,
            context: _all.ClosesttimeseriesatCallContext,
        ) -> Awaitable[None]: ...
        def timeSeriesAt(
            self,
            locationId: str,
            _context: _all.TimeseriesatCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _TimeSeriesInterfaceModule.Server
            | _all.TimeSeriesClient
            | _all.TimeseriesatResultTuple
            | None
        ]: ...
        def timeSeriesAt_context(
            self,
            context: _all.TimeseriesatCallContext,
        ) -> Awaitable[None]: ...
        def locations(
            self,
            _context: _all.LocationsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _all.LocationListBuilder
            | _all.LocationListReader
            | Sequence[Any]
            | _all.LocationsResultTuple
            | None
        ]: ...
        def locations_context(
            self,
            context: _all.LocationsCallContext,
        ) -> Awaitable[None]: ...
        def streamLocations(
            self,
            startAfterLocationId: str,
            _context: _all.StreamlocationsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _DatasetInterfaceModule._GetLocationsCallbackInterfaceModule.Server
            | _all.GetLocationsCallbackClient
            | _all.StreamlocationsResultTuple
            | None
        ]: ...
        def streamLocations_context(
            self,
            context: _all.StreamlocationsCallContext,
        ) -> Awaitable[None]: ...

class _TimeSeriesInterfaceModule(
    _IdentifiableInterfaceModule,
    _PersistentInterfaceModule,
):
    class _ResolutionEnumModule:
        daily: int
        hourly: int

    Resolution: _ResolutionEnumModule
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> _all.TimeSeriesClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def resolution(
            self,
            _context: _all.ResolutionCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _all.TimeSeriesResolutionEnum | _all.ResolutionResultTuple | None
        ]: ...
        def resolution_context(
            self,
            context: _all.ResolutionCallContext,
        ) -> Awaitable[None]: ...
        def range(
            self,
            _context: _all.RangeCallContext,
            **kwargs: object,
        ) -> Awaitable[_all.RangeResultTuple | None]: ...
        def range_context(self, context: _all.RangeCallContext) -> Awaitable[None]: ...
        def header(
            self,
            _context: _all.HeaderCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _all.ElementEnumListBuilder
            | _all.ElementEnumListReader
            | Sequence[Any]
            | _all.HeaderResultTuple
            | None
        ]: ...
        def header_context(
            self,
            context: _all.HeaderCallContext,
        ) -> Awaitable[None]: ...
        def data(
            self,
            _context: _all.DataCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _all.Float32ListListBuilder
            | _all.Float32ListListReader
            | Sequence[Any]
            | _all.DataResultTuple
            | None
        ]: ...
        def data_context(self, context: _all.DataCallContext) -> Awaitable[None]: ...
        def dataT(
            self,
            _context: _all.DatatCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _all.Float32ListListBuilder
            | _all.Float32ListListReader
            | Sequence[Any]
            | _all.DatatResultTuple
            | None
        ]: ...
        def dataT_context(self, context: _all.DatatCallContext) -> Awaitable[None]: ...
        def subrange(
            self,
            start: DateReader,
            end: DateReader,
            _context: _all.SubrangeCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _TimeSeriesInterfaceModule.Server
            | _all.TimeSeriesClient
            | _all.SubrangeResultTuple
            | None
        ]: ...
        def subrange_context(
            self,
            context: _all.SubrangeCallContext,
        ) -> Awaitable[None]: ...
        def subheader(
            self,
            elements: _all.ElementEnumListReader,
            _context: _all.SubheaderCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _TimeSeriesInterfaceModule.Server
            | _all.TimeSeriesClient
            | _all.SubheaderResultTuple
            | None
        ]: ...
        def subheader_context(
            self,
            context: _all.SubheaderCallContext,
        ) -> Awaitable[None]: ...
        def metadata(
            self,
            _context: _all.TimeSeriesMetadataCallContext,
            **kwargs: object,
        ) -> Awaitable[_all.TimeSeriesMetadataResultTuple | None]: ...
        def metadata_context(
            self,
            context: _all.TimeSeriesMetadataCallContext,
        ) -> Awaitable[None]: ...
        def location(
            self,
            _context: _all.LocationCallContext,
            **kwargs: object,
        ) -> Awaitable[_all.LocationResultTuple | None]: ...
        def location_context(
            self,
            context: _all.LocationCallContext,
        ) -> Awaitable[None]: ...

class _LocationStructModule(_StructModule):
    class _KVStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            key: str | None = None,
            value: _all.AnyPointer | None = None,
            **kwargs: object,
        ) -> _all.KVBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.KVReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.KVReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.KVBuilder]: ...
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
        ) -> _all.KVReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.KVReader: ...

    KV: _KVStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        id: IdInformationBuilder | dict[str, Any] | None = None,
        heightNN: float | None = None,
        latlon: LatLonCoordBuilder | dict[str, Any] | None = None,
        timeSeries: _all.TimeSeriesClient
        | _TimeSeriesInterfaceModule.Server
        | None = None,
        customData: _all.KVListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> _all.LocationBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.LocationReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.LocationReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.LocationBuilder]: ...
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
    ) -> _all.LocationReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.LocationReader: ...

class _MetaPlusDataStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        meta: _all.MetadataBuilder | dict[str, Any] | None = None,
        data: _all.DatasetClient | _DatasetInterfaceModule.Server | None = None,
        **kwargs: object,
    ) -> _all.MetaPlusDataBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.MetaPlusDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.MetaPlusDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.MetaPlusDataBuilder]: ...
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
    ) -> _all.MetaPlusDataReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.MetaPlusDataReader: ...

class _TimeSeriesDataStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        data: _all.Float32ListListBuilder | dict[str, Any] | None = None,
        isTransposed: bool | None = None,
        header: _all.ElementEnumListBuilder | dict[str, Any] | None = None,
        startDate: DateBuilder | dict[str, Any] | None = None,
        endDate: DateBuilder | dict[str, Any] | None = None,
        resolution: _all.TimeSeriesResolutionEnum | None = None,
        **kwargs: object,
    ) -> _all.TimeSeriesDataBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.TimeSeriesDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.TimeSeriesDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.TimeSeriesDataBuilder]: ...
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
    ) -> _all.TimeSeriesDataReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.TimeSeriesDataReader: ...

class _ServiceInterfaceModule(_IdentifiableInterfaceModule, _PersistentInterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> _all.ServiceClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def getAvailableDatasets(
            self,
            _context: _all.GetavailabledatasetsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _all.MetaPlusDataListBuilder
            | _all.MetaPlusDataListReader
            | Sequence[Any]
            | _all.GetavailabledatasetsResultTuple
            | None
        ]: ...
        def getAvailableDatasets_context(
            self,
            context: _all.GetavailabledatasetsCallContext,
        ) -> Awaitable[None]: ...
        def getDatasetsFor(
            self,
            template: _all.MetadataReader,
            _context: _all.GetdatasetsforCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _all.DatasetClientListBuilder
            | _all.DatasetClientListReader
            | Sequence[Any]
            | _all.GetdatasetsforResultTuple
            | None
        ]: ...
        def getDatasetsFor_context(
            self,
            context: _all.GetdatasetsforCallContext,
        ) -> Awaitable[None]: ...

class _CSVTimeSeriesFactoryInterfaceModule(_IdentifiableInterfaceModule):
    class _CSVConfigStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            sep: str | None = None,
            headerMap: _all.PairListBuilder | dict[str, Any] | None = None,
            skipLinesToHeader: int | None = None,
            skipLinesFromHeaderToData: int | None = None,
            **kwargs: object,
        ) -> _all.CSVConfigBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.CSVConfigReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.CSVConfigReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.CSVConfigBuilder]: ...
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
        ) -> _all.CSVConfigReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.CSVConfigReader: ...

    CSVConfig: _CSVConfigStructModule
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> _all.CSVTimeSeriesFactoryClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def create(
            self,
            csvData: str,
            config: _all.CSVConfigReader,
            _context: _all.CreateCallContext,
            **kwargs: object,
        ) -> Awaitable[_all.CreateResultTuple | None]: ...
        def create_context(
            self,
            context: _all.CreateCallContext,
        ) -> Awaitable[None]: ...

class _AlterTimeSeriesWrapperInterfaceModule(_TimeSeriesInterfaceModule):
    class _AlterTypeEnumModule:
        add: int
        mul: int

    AlterType: _AlterTypeEnumModule
    class _AlteredStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            element: _all.ElementEnum | None = None,
            value: float | None = None,
            type: _all.AlterTimeSeriesWrapperAlterTypeEnum | None = None,
            **kwargs: object,
        ) -> _all.AlteredBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.AlteredReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.AlteredReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.AlteredBuilder]: ...
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
        ) -> _all.AlteredReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.AlteredReader: ...

    Altered: _AlteredStructModule
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> _all.AlterTimeSeriesWrapperClient: ...
    class Server(_TimeSeriesInterfaceModule.Server):
        def wrappedTimeSeries(
            self,
            _context: _all.WrappedtimeseriesCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _TimeSeriesInterfaceModule.Server
            | _all.TimeSeriesClient
            | _all.WrappedtimeseriesResultTuple
            | None
        ]: ...
        def wrappedTimeSeries_context(
            self,
            context: _all.WrappedtimeseriesCallContext,
        ) -> Awaitable[None]: ...
        def alteredElements(
            self,
            _context: _all.AlteredelementsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _all.AlteredListBuilder
            | _all.AlteredListReader
            | Sequence[Any]
            | _all.AlteredelementsResultTuple
            | None
        ]: ...
        def alteredElements_context(
            self,
            context: _all.AlteredelementsCallContext,
        ) -> Awaitable[None]: ...
        def alter(
            self,
            desc: _all.AlteredReader,
            asNewTimeSeries: bool,
            _context: _all.AlterCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _TimeSeriesInterfaceModule.Server
            | _all.TimeSeriesClient
            | _all.AlterResultTuple
            | None
        ]: ...
        def alter_context(self, context: _all.AlterCallContext) -> Awaitable[None]: ...
        def remove(
            self,
            alteredElement: _all.ElementEnum,
            _context: _all.RemoveCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def remove_context(
            self,
            context: _all.RemoveCallContext,
        ) -> Awaitable[None]: ...
        def replaceWrappedTimeSeries(
            self,
            timeSeries: _all.TimeSeriesClient,
            _context: _all.ReplacewrappedtimeseriesCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def replaceWrappedTimeSeries_context(
            self,
            context: _all.ReplacewrappedtimeseriesCallContext,
        ) -> Awaitable[None]: ...

class _AlterTimeSeriesWrapperFactoryInterfaceModule(_IdentifiableInterfaceModule):
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> _all.AlterTimeSeriesWrapperFactoryClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def wrap(
            self,
            timeSeries: _all.TimeSeriesClient,
            _context: _all.WrapCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _AlterTimeSeriesWrapperInterfaceModule.Server
            | _all.AlterTimeSeriesWrapperClient
            | _all.WrapResultTuple
            | None
        ]: ...
        def wrap_context(self, context: _all.WrapCallContext) -> Awaitable[None]: ...
