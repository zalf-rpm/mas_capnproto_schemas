"""This is an automatically generated stub for `persistence.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable
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

from .common_capnp import _IdentifiableModule

# Type alias for AnyPointer parameters (accepts all Cap'n Proto pointer types)
type AnyPointer = (
    str
    | bytes
    | _DynamicStructBuilder
    | _DynamicStructReader
    | _DynamicCapabilityClient
    | _DynamicCapabilityServer
)

class _VatIdModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def publicKey0(self) -> int: ...
        @property
        def publicKey1(self) -> int: ...
        @property
        def publicKey2(self) -> int: ...
        @property
        def publicKey3(self) -> int: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> VatIdBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def publicKey0(self) -> int: ...
        @publicKey0.setter
        def publicKey0(self, value: int) -> None: ...
        @property
        def publicKey1(self) -> int: ...
        @publicKey1.setter
        def publicKey1(self, value: int) -> None: ...
        @property
        def publicKey2(self) -> int: ...
        @publicKey2.setter
        def publicKey2(self, value: int) -> None: ...
        @property
        def publicKey3(self) -> int: ...
        @publicKey3.setter
        def publicKey3(self, value: int) -> None: ...
        @override
        def as_reader(self) -> VatIdReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        publicKey0: int | None = None,
        publicKey1: int | None = None,
        publicKey2: int | None = None,
        publicKey3: int | None = None,
        **kwargs: Any,
    ) -> VatIdBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[VatIdReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[VatIdReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[VatIdBuilder]: ...
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
    ) -> VatIdReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> VatIdReader: ...

VatId: _VatIdModule

class _AddressModule(_StructModule):
    class _Ip6Module(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def lower64(self) -> int: ...
            @property
            def upper64(self) -> int: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> Ip6Builder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def lower64(self) -> int: ...
            @lower64.setter
            def lower64(self, value: int) -> None: ...
            @property
            def upper64(self) -> int: ...
            @upper64.setter
            def upper64(self, value: int) -> None: ...
            @override
            def as_reader(self) -> Ip6Reader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            lower64: int | None = None,
            upper64: int | None = None,
            **kwargs: Any,
        ) -> Ip6Builder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[Ip6Reader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[Ip6Reader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[Ip6Builder]: ...
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
        ) -> Ip6Reader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Ip6Reader: ...

    type Ip6Reader = _Ip6Module.Reader
    type Ip6Builder = _Ip6Module.Builder
    Ip6: _Ip6Module
    class Reader(_DynamicStructReader):
        @property
        def ip6(self) -> Ip6Reader: ...
        @property
        def port(self) -> int: ...
        @property
        def host(self) -> str: ...
        @override
        def which(self) -> Literal["ip6", "host"]: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> AddressBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def ip6(self) -> Ip6Builder: ...
        @ip6.setter
        def ip6(self, value: Ip6Builder | Ip6Reader | dict[str, Any]) -> None: ...
        @property
        def port(self) -> int: ...
        @port.setter
        def port(self, value: int) -> None: ...
        @property
        def host(self) -> str: ...
        @host.setter
        def host(self, value: str) -> None: ...
        @override
        def which(self) -> Literal["ip6", "host"]: ...
        def init(
            self, field: Literal["ip6"], size: int | None = None
        ) -> Ip6Builder: ...
        @override
        def as_reader(self) -> AddressReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        ip6: Ip6Builder | dict[str, Any] | None = None,
        port: int | None = None,
        host: str | None = None,
        **kwargs: Any,
    ) -> AddressBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[AddressReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[AddressReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[AddressBuilder]: ...
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
    ) -> AddressReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AddressReader: ...

Address: _AddressModule

class _VatPathModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def id(self) -> VatIdReader: ...
        @property
        def address(self) -> AddressReader: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> VatPathBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def id(self) -> VatIdBuilder: ...
        @id.setter
        def id(self, value: VatIdBuilder | VatIdReader | dict[str, Any]) -> None: ...
        @property
        def address(self) -> AddressBuilder: ...
        @address.setter
        def address(
            self, value: AddressBuilder | AddressReader | dict[str, Any]
        ) -> None: ...
        @overload
        def init(
            self, field: Literal["id"], size: int | None = None
        ) -> VatIdBuilder: ...
        @overload
        def init(
            self, field: Literal["address"], size: int | None = None
        ) -> AddressBuilder: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> VatPathReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        id: VatIdBuilder | dict[str, Any] | None = None,
        address: AddressBuilder | dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> VatPathBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[VatPathReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[VatPathReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[VatPathBuilder]: ...
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
    ) -> VatPathReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> VatPathReader: ...

VatPath: _VatPathModule

class _SturdyRefModule(_StructModule):
    class _OwnerModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def guid(self) -> str: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> OwnerBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def guid(self) -> str: ...
            @guid.setter
            def guid(self, value: str) -> None: ...
            @override
            def as_reader(self) -> OwnerReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            guid: str | None = None,
            **kwargs: Any,
        ) -> OwnerBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[OwnerReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[OwnerReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[OwnerBuilder]: ...
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
        ) -> OwnerReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> OwnerReader: ...

    type OwnerReader = _OwnerModule.Reader
    type OwnerBuilder = _OwnerModule.Builder
    Owner: _OwnerModule
    class _TokenModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def text(self) -> str: ...
            @property
            def data(self) -> bytes: ...
            @override
            def which(self) -> Literal["text", "data"]: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> TokenBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def text(self) -> str: ...
            @text.setter
            def text(self, value: str) -> None: ...
            @property
            def data(self) -> bytes: ...
            @data.setter
            def data(self, value: bytes) -> None: ...
            @override
            def which(self) -> Literal["text", "data"]: ...
            @override
            def as_reader(self) -> TokenReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            text: str | None = None,
            data: bytes | None = None,
            **kwargs: Any,
        ) -> TokenBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[TokenReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[TokenReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[TokenBuilder]: ...
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
        ) -> TokenReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> TokenReader: ...

    type TokenReader = _TokenModule.Reader
    type TokenBuilder = _TokenModule.Builder
    Token: _TokenModule
    class Reader(_DynamicStructReader):
        @property
        def vat(self) -> VatPathReader: ...
        @property
        def localRef(self) -> TokenReader: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> SturdyRefBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def vat(self) -> VatPathBuilder: ...
        @vat.setter
        def vat(
            self, value: VatPathBuilder | VatPathReader | dict[str, Any]
        ) -> None: ...
        @property
        def localRef(self) -> TokenBuilder: ...
        @localRef.setter
        def localRef(
            self, value: TokenBuilder | TokenReader | dict[str, Any]
        ) -> None: ...
        @overload
        def init(
            self, field: Literal["vat"], size: int | None = None
        ) -> VatPathBuilder: ...
        @overload
        def init(
            self, field: Literal["localRef"], size: int | None = None
        ) -> TokenBuilder: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> SturdyRefReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        vat: VatPathBuilder | dict[str, Any] | None = None,
        localRef: TokenBuilder | dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> SturdyRefBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[SturdyRefReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[SturdyRefReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[SturdyRefBuilder]: ...
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
    ) -> SturdyRefReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> SturdyRefReader: ...

SturdyRef: _SturdyRefModule

class _HeartbeatModule(_InterfaceModule):
    class BeatRequest(Protocol):
        def send(self) -> _HeartbeatModule.HeartbeatClient.BeatResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _HeartbeatModule.HeartbeatClient: ...
    class Server(_DynamicCapabilityServer):
        class BeatResult(Awaitable[None], Protocol): ...
        class BeatParams(Protocol): ...

        class BeatCallContext(Protocol):
            params: _HeartbeatModule.Server.BeatParams

        def beat(
            self,
            _context: _HeartbeatModule.Server.BeatCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[None]: ...
        def beat_context(
            self, context: _HeartbeatModule.Server.BeatCallContext
        ) -> Awaitable[None]: ...

    class HeartbeatClient(_DynamicCapabilityClient):
        class BeatResult(Awaitable[None], Protocol): ...

        def beat(self) -> _HeartbeatModule.HeartbeatClient.BeatResult: ...
        def beat_request(self) -> _HeartbeatModule.BeatRequest: ...

Heartbeat: _HeartbeatModule

class _PersistentModule(_InterfaceModule):
    class _SaveParamsModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def sealFor(self) -> OwnerReader: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> SaveParamsBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def sealFor(self) -> OwnerBuilder: ...
            @sealFor.setter
            def sealFor(
                self, value: OwnerBuilder | OwnerReader | dict[str, Any]
            ) -> None: ...
            def init(
                self, field: Literal["sealFor"], size: int | None = None
            ) -> OwnerBuilder: ...
            @override
            def as_reader(self) -> SaveParamsReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            sealFor: OwnerBuilder | dict[str, Any] | None = None,
            **kwargs: Any,
        ) -> SaveParamsBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[SaveParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[SaveParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[SaveParamsBuilder]: ...
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
        ) -> SaveParamsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> SaveParamsReader: ...

    type SaveParamsReader = _SaveParamsModule.Reader
    type SaveParamsBuilder = _SaveParamsModule.Builder
    SaveParams: _SaveParamsModule
    class _SaveResultsModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def sturdyRef(self) -> SturdyRefReader: ...
            @property
            def unsaveSR(self) -> SturdyRefReader: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> SaveResultsBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def sturdyRef(self) -> SturdyRefBuilder: ...
            @sturdyRef.setter
            def sturdyRef(
                self, value: SturdyRefBuilder | SturdyRefReader | dict[str, Any]
            ) -> None: ...
            @property
            def unsaveSR(self) -> SturdyRefBuilder: ...
            @unsaveSR.setter
            def unsaveSR(
                self, value: SturdyRefBuilder | SturdyRefReader | dict[str, Any]
            ) -> None: ...
            @overload
            def init(
                self, field: Literal["sturdyRef"], size: int | None = None
            ) -> SturdyRefBuilder: ...
            @overload
            def init(
                self, field: Literal["unsaveSR"], size: int | None = None
            ) -> SturdyRefBuilder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...
            @override
            def as_reader(self) -> SaveResultsReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            sturdyRef: SturdyRefBuilder | dict[str, Any] | None = None,
            unsaveSR: SturdyRefBuilder | dict[str, Any] | None = None,
            **kwargs: Any,
        ) -> SaveResultsBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[SaveResultsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[SaveResultsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[SaveResultsBuilder]: ...
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
        ) -> SaveResultsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> SaveResultsReader: ...

    type SaveResultsReader = _SaveResultsModule.Reader
    type SaveResultsBuilder = _SaveResultsModule.Builder
    SaveResults: _SaveResultsModule
    class _ReleaseSturdyRefModule(_InterfaceModule):
        class ReleaseRequest(Protocol):
            def send(
                self,
            ) -> _PersistentModule._ReleaseSturdyRefModule.ReleaseSturdyRefClient.ReleaseResult: ...

        def _new_client(
            self, server: _DynamicCapabilityServer
        ) -> _PersistentModule._ReleaseSturdyRefModule.ReleaseSturdyRefClient: ...
        class Server(_DynamicCapabilityServer):
            class ReleaseResult(Awaitable[ReleaseResult], Protocol):
                success: bool

            class ReleaseResultTuple(NamedTuple):
                success: bool

            class ReleaseParams(Protocol): ...

            class ReleaseCallContext(Protocol):
                params: _PersistentModule._ReleaseSturdyRefModule.Server.ReleaseParams
                results: _PersistentModule._ReleaseSturdyRefModule.Server.ReleaseResult

            def release(
                self,
                _context: _PersistentModule._ReleaseSturdyRefModule.Server.ReleaseCallContext,
                **kwargs: dict[str, Any],
            ) -> Awaitable[
                bool
                | _PersistentModule._ReleaseSturdyRefModule.Server.ReleaseResultTuple
                | None
            ]: ...
            def release_context(
                self,
                context: _PersistentModule._ReleaseSturdyRefModule.Server.ReleaseCallContext,
            ) -> Awaitable[None]: ...

        class ReleaseSturdyRefClient(_DynamicCapabilityClient):
            class ReleaseResult(Awaitable[ReleaseResult], Protocol):
                success: bool

            def release(
                self,
            ) -> _PersistentModule._ReleaseSturdyRefModule.ReleaseSturdyRefClient.ReleaseResult: ...
            def release_request(
                self,
            ) -> _PersistentModule._ReleaseSturdyRefModule.ReleaseRequest: ...

    ReleaseSturdyRef: _ReleaseSturdyRefModule
    type ReleaseSturdyRefClient = (
        _PersistentModule._ReleaseSturdyRefModule.ReleaseSturdyRefClient
    )
    class SaveRequest(Protocol):
        sealFor: OwnerBuilder
        @overload
        def init(self, name: Literal["sealFor"]) -> OwnerBuilder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> _PersistentModule.PersistentClient.SaveResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _PersistentModule.PersistentClient: ...
    class Server(_DynamicCapabilityServer):
        class SaveResult(Awaitable[SaveResult], Protocol):
            sturdyRef: SturdyRefBuilder | SturdyRefReader
            unsaveSR: SturdyRefBuilder | SturdyRefReader

        class SaveResultTuple(NamedTuple):
            sturdyRef: SturdyRefBuilder | SturdyRefReader
            unsaveSR: SturdyRefBuilder | SturdyRefReader

        class SaveParams(Protocol):
            sealFor: OwnerReader

        class SaveCallContext(Protocol):
            params: _PersistentModule.Server.SaveParams
            results: _PersistentModule.Server.SaveResult

        def save(
            self,
            sealFor: OwnerReader,
            _context: _PersistentModule.Server.SaveCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_PersistentModule.Server.SaveResultTuple | None]: ...
        def save_context(
            self, context: _PersistentModule.Server.SaveCallContext
        ) -> Awaitable[None]: ...

    class PersistentClient(_DynamicCapabilityClient):
        class SaveResult(Awaitable[SaveResult], Protocol):
            sturdyRef: SturdyRefReader
            unsaveSR: SturdyRefReader

        def save(
            self, sealFor: OwnerBuilder | OwnerReader | dict[str, Any] | None = None
        ) -> _PersistentModule.PersistentClient.SaveResult: ...
        def save_request(
            self, sealFor: OwnerBuilder | None = None
        ) -> _PersistentModule.SaveRequest: ...

Persistent: _PersistentModule

class _RestorerModule(_InterfaceModule):
    class _RestoreParamsModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def localRef(self) -> TokenReader: ...
            @property
            def sealedBy(self) -> OwnerReader: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> RestoreParamsBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def localRef(self) -> TokenBuilder: ...
            @localRef.setter
            def localRef(
                self, value: TokenBuilder | TokenReader | dict[str, Any]
            ) -> None: ...
            @property
            def sealedBy(self) -> OwnerBuilder: ...
            @sealedBy.setter
            def sealedBy(
                self, value: OwnerBuilder | OwnerReader | dict[str, Any]
            ) -> None: ...
            @overload
            def init(
                self, field: Literal["localRef"], size: int | None = None
            ) -> TokenBuilder: ...
            @overload
            def init(
                self, field: Literal["sealedBy"], size: int | None = None
            ) -> OwnerBuilder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...
            @override
            def as_reader(self) -> RestoreParamsReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            localRef: TokenBuilder | dict[str, Any] | None = None,
            sealedBy: OwnerBuilder | dict[str, Any] | None = None,
            **kwargs: Any,
        ) -> RestoreParamsBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[RestoreParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[RestoreParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[RestoreParamsBuilder]: ...
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
        ) -> RestoreParamsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> RestoreParamsReader: ...

    type RestoreParamsReader = _RestoreParamsModule.Reader
    type RestoreParamsBuilder = _RestoreParamsModule.Builder
    RestoreParams: _RestoreParamsModule
    class RestoreRequest(Protocol):
        localRef: TokenBuilder
        sealedBy: OwnerBuilder
        @overload
        def init(self, name: Literal["localRef"]) -> TokenBuilder: ...
        @overload
        def init(self, name: Literal["sealedBy"]) -> OwnerBuilder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> _RestorerModule.RestorerClient.RestoreResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _RestorerModule.RestorerClient: ...
    class Server(_DynamicCapabilityServer):
        class RestoreResult(Awaitable[RestoreResult], Protocol):
            cap: AnyPointer

        class RestoreResultTuple(NamedTuple):
            cap: AnyPointer

        class RestoreParams(Protocol):
            localRef: TokenReader
            sealedBy: OwnerReader

        class RestoreCallContext(Protocol):
            params: _RestorerModule.Server.RestoreParams
            results: _RestorerModule.Server.RestoreResult

        def restore(
            self,
            localRef: TokenReader,
            sealedBy: OwnerReader,
            _context: _RestorerModule.Server.RestoreCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_RestorerModule.Server.RestoreResultTuple | None]: ...
        def restore_context(
            self, context: _RestorerModule.Server.RestoreCallContext
        ) -> Awaitable[None]: ...

    class RestorerClient(_DynamicCapabilityClient):
        class RestoreResult(Awaitable[RestoreResult], Protocol):
            cap: _DynamicObjectReader

        def restore(
            self,
            localRef: TokenBuilder | TokenReader | dict[str, Any] | None = None,
            sealedBy: OwnerBuilder | OwnerReader | dict[str, Any] | None = None,
        ) -> _RestorerModule.RestorerClient.RestoreResult: ...
        def restore_request(
            self,
            localRef: TokenBuilder | None = None,
            sealedBy: OwnerBuilder | None = None,
        ) -> _RestorerModule.RestoreRequest: ...

Restorer: _RestorerModule

class _HostPortResolverModule(_IdentifiableModule, _RestorerModule):
    class _RegistrarModule(_InterfaceModule):
        class _RegisterParamsModule(_StructModule):
            class Reader(_DynamicStructReader):
                @property
                def base64VatId(self) -> str: ...
                @property
                def host(self) -> str: ...
                @property
                def port(self) -> int: ...
                @property
                def alias(self) -> str: ...
                @property
                def identityProof(self) -> bytes: ...
                @override
                def as_builder(
                    self,
                    num_first_segment_words: int | None = None,
                    allocate_seg_callable: Any = None,
                ) -> RegisterParamsBuilder: ...

            class Builder(_DynamicStructBuilder):
                @property
                def base64VatId(self) -> str: ...
                @base64VatId.setter
                def base64VatId(self, value: str) -> None: ...
                @property
                def host(self) -> str: ...
                @host.setter
                def host(self, value: str) -> None: ...
                @property
                def port(self) -> int: ...
                @port.setter
                def port(self, value: int) -> None: ...
                @property
                def alias(self) -> str: ...
                @alias.setter
                def alias(self, value: str) -> None: ...
                @property
                def identityProof(self) -> bytes: ...
                @identityProof.setter
                def identityProof(self, value: bytes) -> None: ...
                @override
                def as_reader(self) -> RegisterParamsReader: ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
                base64VatId: str | None = None,
                host: str | None = None,
                port: int | None = None,
                alias: str | None = None,
                identityProof: bytes | None = None,
                **kwargs: Any,
            ) -> RegisterParamsBuilder: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> AbstractContextManager[RegisterParamsReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[RegisterParamsReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[RegisterParamsBuilder]: ...
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
            ) -> RegisterParamsReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = ...,
                nesting_limit: int | None = ...,
            ) -> RegisterParamsReader: ...

        type RegisterParamsReader = _RegisterParamsModule.Reader
        type RegisterParamsBuilder = _RegisterParamsModule.Builder
        RegisterParams: _RegisterParamsModule
        class RegisterRequest(Protocol):
            base64VatId: str
            host: str
            port: int
            alias: str
            identityProof: bytes
            def send(
                self,
            ) -> (
                _HostPortResolverModule._RegistrarModule.RegistrarClient.RegisterResult
            ): ...

        def _new_client(
            self, server: _DynamicCapabilityServer
        ) -> _HostPortResolverModule._RegistrarModule.RegistrarClient: ...
        class Server(_DynamicCapabilityServer):
            class RegisterResult(Awaitable[RegisterResult], Protocol):
                heartbeat: _HeartbeatModule.HeartbeatClient
                secsHeartbeatInterval: int

            class RegisterResultTuple(NamedTuple):
                heartbeat: _HeartbeatModule.Server
                secsHeartbeatInterval: int

            class RegisterParams(Protocol):
                base64VatId: str
                host: str
                port: int
                alias: str
                identityProof: bytes

            class RegisterCallContext(Protocol):
                params: _HostPortResolverModule._RegistrarModule.Server.RegisterParams
                results: _HostPortResolverModule._RegistrarModule.Server.RegisterResult

            def register(
                self,
                base64VatId: str,
                host: str,
                port: int,
                alias: str,
                identityProof: bytes,
                _context: _HostPortResolverModule._RegistrarModule.Server.RegisterCallContext,
                **kwargs: dict[str, Any],
            ) -> Awaitable[
                _HostPortResolverModule._RegistrarModule.Server.RegisterResultTuple
                | None
            ]: ...
            def register_context(
                self,
                context: _HostPortResolverModule._RegistrarModule.Server.RegisterCallContext,
            ) -> Awaitable[None]: ...

        class RegistrarClient(_DynamicCapabilityClient):
            class RegisterResult(Awaitable[RegisterResult], Protocol):
                heartbeat: _HeartbeatModule.HeartbeatClient
                secsHeartbeatInterval: int

            def register(
                self,
                base64VatId: str | None = None,
                host: str | None = None,
                port: int | None = None,
                alias: str | None = None,
                identityProof: bytes | None = None,
            ) -> (
                _HostPortResolverModule._RegistrarModule.RegistrarClient.RegisterResult
            ): ...
            def register_request(
                self,
                base64VatId: str | None = None,
                host: str | None = None,
                port: int | None = None,
                alias: str | None = None,
                identityProof: bytes | None = None,
            ) -> _HostPortResolverModule._RegistrarModule.RegisterRequest: ...

    Registrar: _RegistrarModule
    type RegistrarClient = _HostPortResolverModule._RegistrarModule.RegistrarClient
    class ResolveRequest(Protocol):
        id: str
        def send(
            self,
        ) -> _HostPortResolverModule.HostPortResolverClient.ResolveResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _HostPortResolverModule.HostPortResolverClient: ...
    class Server(_IdentifiableModule.Server, _RestorerModule.Server):
        class ResolveResult(Awaitable[ResolveResult], Protocol):
            host: str
            port: int

        class ResolveResultTuple(NamedTuple):
            host: str
            port: int

        class ResolveParams(Protocol):
            id: str

        class ResolveCallContext(Protocol):
            params: _HostPortResolverModule.Server.ResolveParams
            results: _HostPortResolverModule.Server.ResolveResult

        def resolve(
            self,
            id: str,
            _context: _HostPortResolverModule.Server.ResolveCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_HostPortResolverModule.Server.ResolveResultTuple | None]: ...
        def resolve_context(
            self, context: _HostPortResolverModule.Server.ResolveCallContext
        ) -> Awaitable[None]: ...

    class HostPortResolverClient(
        _IdentifiableModule.IdentifiableClient, _RestorerModule.RestorerClient
    ):
        class ResolveResult(Awaitable[ResolveResult], Protocol):
            host: str
            port: int

        def resolve(
            self, id: str | None = None
        ) -> _HostPortResolverModule.HostPortResolverClient.ResolveResult: ...
        def resolve_request(
            self, id: str | None = None
        ) -> _HostPortResolverModule.ResolveRequest: ...

HostPortResolver: _HostPortResolverModule

class _GatewayModule(_IdentifiableModule, _RestorerModule):
    class _RegResultsModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def sturdyRef(self) -> SturdyRefReader: ...
            @property
            def heartbeat(self) -> _HeartbeatModule.HeartbeatClient: ...
            @property
            def secsHeartbeatInterval(self) -> int: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> RegResultsBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def sturdyRef(self) -> SturdyRefBuilder: ...
            @sturdyRef.setter
            def sturdyRef(
                self, value: SturdyRefBuilder | SturdyRefReader | dict[str, Any]
            ) -> None: ...
            @property
            def heartbeat(self) -> _HeartbeatModule.HeartbeatClient: ...
            @heartbeat.setter
            def heartbeat(
                self, value: _HeartbeatModule.HeartbeatClient | _HeartbeatModule.Server
            ) -> None: ...
            @property
            def secsHeartbeatInterval(self) -> int: ...
            @secsHeartbeatInterval.setter
            def secsHeartbeatInterval(self, value: int) -> None: ...
            def init(
                self, field: Literal["sturdyRef"], size: int | None = None
            ) -> SturdyRefBuilder: ...
            @override
            def as_reader(self) -> RegResultsReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            sturdyRef: SturdyRefBuilder | dict[str, Any] | None = None,
            heartbeat: _HeartbeatModule.HeartbeatClient
            | _HeartbeatModule.Server
            | None = None,
            secsHeartbeatInterval: int | None = None,
            **kwargs: Any,
        ) -> RegResultsBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[RegResultsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[RegResultsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[RegResultsBuilder]: ...
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
        ) -> RegResultsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> RegResultsReader: ...

    type RegResultsReader = _RegResultsModule.Reader
    type RegResultsBuilder = _RegResultsModule.Builder
    RegResults: _RegResultsModule
    class RegisterRequest(Protocol):
        cap: AnyPointer
        def send(self) -> _GatewayModule.GatewayClient.RegisterResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _GatewayModule.GatewayClient: ...
    class Server(_IdentifiableModule.Server, _RestorerModule.Server):
        class RegisterResult(Awaitable[RegisterResult], Protocol):
            sturdyRef: SturdyRefBuilder | SturdyRefReader
            heartbeat: _HeartbeatModule.HeartbeatClient
            secsHeartbeatInterval: int

        class RegisterResultTuple(NamedTuple):
            sturdyRef: SturdyRefBuilder | SturdyRefReader
            heartbeat: _HeartbeatModule.Server
            secsHeartbeatInterval: int

        class RegisterParams(Protocol):
            cap: AnyPointer

        class RegisterCallContext(Protocol):
            params: _GatewayModule.Server.RegisterParams
            results: _GatewayModule.Server.RegisterResult

        def register(
            self,
            cap: AnyPointer,
            _context: _GatewayModule.Server.RegisterCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_GatewayModule.Server.RegisterResultTuple | None]: ...
        def register_context(
            self, context: _GatewayModule.Server.RegisterCallContext
        ) -> Awaitable[None]: ...

    class GatewayClient(
        _IdentifiableModule.IdentifiableClient, _RestorerModule.RestorerClient
    ):
        class RegisterResult(Awaitable[RegisterResult], Protocol):
            sturdyRef: SturdyRefReader
            heartbeat: _HeartbeatModule.HeartbeatClient
            secsHeartbeatInterval: int

        def register(
            self, cap: _DynamicObjectReader | None = None
        ) -> _GatewayModule.GatewayClient.RegisterResult: ...
        def register_request(
            self, cap: AnyPointer | None = None
        ) -> _GatewayModule.RegisterRequest: ...

Gateway: _GatewayModule

# Top-level type aliases for use in type annotations
type AddressBuilder = _AddressModule.Builder
type AddressReader = _AddressModule.Reader
type BeatResult = _HeartbeatModule.HeartbeatClient.BeatResult
type GatewayClient = _GatewayModule.GatewayClient
type HeartbeatClient = _HeartbeatModule.HeartbeatClient
type HostPortResolverClient = _HostPortResolverModule.HostPortResolverClient
type Ip6Builder = _AddressModule._Ip6Module.Builder
type Ip6Reader = _AddressModule._Ip6Module.Reader
type OwnerBuilder = _SturdyRefModule._OwnerModule.Builder
type OwnerReader = _SturdyRefModule._OwnerModule.Reader
type PersistentClient = _PersistentModule.PersistentClient
type RegResultsBuilder = _GatewayModule._RegResultsModule.Builder
type RegResultsReader = _GatewayModule._RegResultsModule.Reader
type RegisterParamsBuilder = (
    _HostPortResolverModule._RegistrarModule._RegisterParamsModule.Builder
)
type RegisterParamsReader = (
    _HostPortResolverModule._RegistrarModule._RegisterParamsModule.Reader
)
type RegisterResult = _GatewayModule.GatewayClient.RegisterResult
type RegistrarClient = _HostPortResolverModule._RegistrarModule.RegistrarClient
type ReleaseResult = (
    _PersistentModule._ReleaseSturdyRefModule.ReleaseSturdyRefClient.ReleaseResult
)
type ReleaseSturdyRefClient = (
    _PersistentModule._ReleaseSturdyRefModule.ReleaseSturdyRefClient
)
type ResolveResult = _HostPortResolverModule.HostPortResolverClient.ResolveResult
type RestoreParamsBuilder = _RestorerModule._RestoreParamsModule.Builder
type RestoreParamsReader = _RestorerModule._RestoreParamsModule.Reader
type RestoreResult = _RestorerModule.RestorerClient.RestoreResult
type RestorerClient = _RestorerModule.RestorerClient
type SaveParamsBuilder = _PersistentModule._SaveParamsModule.Builder
type SaveParamsReader = _PersistentModule._SaveParamsModule.Reader
type SaveResult = _PersistentModule.PersistentClient.SaveResult
type SaveResultsBuilder = _PersistentModule._SaveResultsModule.Builder
type SaveResultsReader = _PersistentModule._SaveResultsModule.Reader
type SturdyRefBuilder = _SturdyRefModule.Builder
type SturdyRefReader = _SturdyRefModule.Reader
type TokenBuilder = _SturdyRefModule._TokenModule.Builder
type TokenReader = _SturdyRefModule._TokenModule.Reader
type VatIdBuilder = _VatIdModule.Builder
type VatIdReader = _VatIdModule.Reader
type VatPathBuilder = _VatPathModule.Builder
type VatPathReader = _VatPathModule.Reader
