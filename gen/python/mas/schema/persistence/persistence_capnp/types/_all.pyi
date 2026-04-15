"""This is an automatically generated stub for `persistence.capnp`."""

from collections.abc import Awaitable, Callable
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

from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule

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

# Type alias for Capability parameters
type Capability = (
    _DynamicCapabilityClient
    | _DynamicCapabilityServer
    | _DynamicObjectReader
    | _DynamicObjectBuilder
)

class _VatIdStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        publicKey0: int | None = None,
        publicKey1: int | None = None,
        publicKey2: int | None = None,
        publicKey3: int | None = None,
        **kwargs: object,
    ) -> VatIdBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[VatIdReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[VatIdReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[VatIdBuilder]: ...
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
    ) -> VatIdReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> VatIdReader: ...

class VatIdReader(_DynamicStructReader):
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> VatIdBuilder: ...

class VatIdBuilder(_DynamicStructBuilder):
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

VatId: _VatIdStructModule

class AddressIp6Reader(_DynamicStructReader):
    @property
    def lower64(self) -> int: ...
    @property
    def upper64(self) -> int: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> AddressIp6Builder: ...

class AddressIp6Builder(_DynamicStructBuilder):
    @property
    def lower64(self) -> int: ...
    @lower64.setter
    def lower64(self, value: int) -> None: ...
    @property
    def upper64(self) -> int: ...
    @upper64.setter
    def upper64(self, value: int) -> None: ...
    @override
    def as_reader(self) -> AddressIp6Reader: ...

class _AddressStructModule(_StructModule):
    class _AddressIp6StructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            lower64: int | None = None,
            upper64: int | None = None,
            **kwargs: object,
        ) -> AddressIp6Builder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[AddressIp6Reader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[AddressIp6Reader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[AddressIp6Builder]: ...
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
        ) -> AddressIp6Reader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AddressIp6Reader: ...

    AddressIp6: _AddressIp6StructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        ip6: AddressIp6Builder | dict[str, Any] | None = None,
        port: int | None = None,
        host: str | None = None,
        **kwargs: object,
    ) -> AddressBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[AddressReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[AddressReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[AddressBuilder]: ...
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
    ) -> AddressReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AddressReader: ...

class AddressReader(_DynamicStructReader):
    @property
    def ip6(self) -> AddressIp6Reader: ...
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> AddressBuilder: ...

class AddressBuilder(_DynamicStructBuilder):
    @property
    def ip6(self) -> AddressIp6Builder: ...
    @ip6.setter
    def ip6(
        self,
        value: AddressIp6Builder | AddressIp6Reader | dict[str, Any],
    ) -> None: ...
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
    @override
    def init(
        self,
        field: Literal["ip6"],
        size: int | None = None,
    ) -> AddressIp6Builder: ...
    @override
    def as_reader(self) -> AddressReader: ...

Address: _AddressStructModule

class _VatPathStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        id: VatIdBuilder | dict[str, Any] | None = None,
        address: AddressBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> VatPathBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[VatPathReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[VatPathReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[VatPathBuilder]: ...
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
    ) -> VatPathReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> VatPathReader: ...

class VatPathReader(_DynamicStructReader):
    @property
    def id(self) -> VatIdReader: ...
    @property
    def address(self) -> AddressReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> VatPathBuilder: ...

class VatPathBuilder(_DynamicStructBuilder):
    @property
    def id(self) -> VatIdBuilder: ...
    @id.setter
    def id(self, value: VatIdBuilder | VatIdReader | dict[str, Any]) -> None: ...
    @property
    def address(self) -> AddressBuilder: ...
    @address.setter
    def address(
        self,
        value: AddressBuilder | AddressReader | dict[str, Any],
    ) -> None: ...
    @override
    @overload
    def init(self, field: Literal["id"], size: int | None = None) -> VatIdBuilder: ...
    @overload
    def init(
        self,
        field: Literal["address"],
        size: int | None = None,
    ) -> AddressBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> VatPathReader: ...

VatPath: _VatPathStructModule

class OwnerReader(_DynamicStructReader):
    @property
    def guid(self) -> str: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> OwnerBuilder: ...

class OwnerBuilder(_DynamicStructBuilder):
    @property
    def guid(self) -> str: ...
    @guid.setter
    def guid(self, value: str) -> None: ...
    @override
    def as_reader(self) -> OwnerReader: ...

class TokenReader(_DynamicStructReader):
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> TokenBuilder: ...

class TokenBuilder(_DynamicStructBuilder):
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

class _SturdyRefStructModule(_StructModule):
    class _OwnerStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            guid: str | None = None,
            **kwargs: object,
        ) -> OwnerBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[OwnerReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[OwnerReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[OwnerBuilder]: ...
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
        ) -> OwnerReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> OwnerReader: ...

    Owner: _OwnerStructModule
    class _TokenStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            text: str | None = None,
            data: bytes | None = None,
            **kwargs: object,
        ) -> TokenBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[TokenReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[TokenReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[TokenBuilder]: ...
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
        ) -> TokenReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> TokenReader: ...

    Token: _TokenStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        vat: VatPathBuilder | dict[str, Any] | None = None,
        localRef: TokenBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> SturdyRefBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[SturdyRefReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[SturdyRefReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[SturdyRefBuilder]: ...
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
    ) -> SturdyRefReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> SturdyRefReader: ...

class SturdyRefReader(_DynamicStructReader):
    @property
    def vat(self) -> VatPathReader: ...
    @property
    def localRef(self) -> TokenReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> SturdyRefBuilder: ...

class SturdyRefBuilder(_DynamicStructBuilder):
    @property
    def vat(self) -> VatPathBuilder: ...
    @vat.setter
    def vat(self, value: VatPathBuilder | VatPathReader | dict[str, Any]) -> None: ...
    @property
    def localRef(self) -> TokenBuilder: ...
    @localRef.setter
    def localRef(self, value: TokenBuilder | TokenReader | dict[str, Any]) -> None: ...
    @override
    @overload
    def init(
        self,
        field: Literal["vat"],
        size: int | None = None,
    ) -> VatPathBuilder: ...
    @overload
    def init(
        self,
        field: Literal["localRef"],
        size: int | None = None,
    ) -> TokenBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> SturdyRefReader: ...

SturdyRef: _SturdyRefStructModule

class _HeartbeatInterfaceModule(_InterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> HeartbeatClient: ...
    class Server(_DynamicCapabilityServer):
        def beat(
            self,
            _context: BeatCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def beat_context(self, context: BeatCallContext) -> Awaitable[None]: ...

class BeatRequest(Protocol):
    def send(self) -> BeatResult: ...

class BeatResult(Awaitable[None], Protocol): ...
class BeatParams(Protocol): ...

class BeatCallContext(Protocol):
    params: BeatParams

class HeartbeatClient(_DynamicCapabilityClient):
    def beat(self) -> BeatResult: ...
    def beat_request(self) -> BeatRequest: ...

Heartbeat: _HeartbeatInterfaceModule

class _PersistentInterfaceModule(_InterfaceModule):
    class _SaveParamsStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            sealFor: OwnerBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> SaveParamsBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[SaveParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[SaveParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[SaveParamsBuilder]: ...
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
        ) -> SaveParamsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> SaveParamsReader: ...

    SaveParams: _SaveParamsStructModule
    class _SaveResultsStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            sturdyRef: SturdyRefBuilder | dict[str, Any] | None = None,
            unsaveSR: SturdyRefBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> SaveResultsBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[SaveResultsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[SaveResultsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[SaveResultsBuilder]: ...
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
        ) -> SaveResultsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> SaveResultsReader: ...

    SaveResults: _SaveResultsStructModule
    class _ReleaseSturdyRefInterfaceModule(_InterfaceModule):
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> ReleaseSturdyRefClient: ...
        class Server(_DynamicCapabilityServer):
            def release(
                self,
                _context: ReleaseCallContext,
                **kwargs: object,
            ) -> Awaitable[bool | ReleaseResultTuple | None]: ...
            def release_context(
                self,
                context: ReleaseCallContext,
            ) -> Awaitable[None]: ...

    ReleaseSturdyRef: _ReleaseSturdyRefInterfaceModule
    type ReleaseSturdyRefServer = (
        _PersistentInterfaceModule._ReleaseSturdyRefInterfaceModule.Server
    )
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> PersistentClient: ...
    class Server(_DynamicCapabilityServer):
        def save(
            self,
            sealFor: OwnerReader,
            _context: SaveCallContext,
            **kwargs: object,
        ) -> Awaitable[SaveResultTuple | None]: ...
        def save_context(self, context: SaveCallContext) -> Awaitable[None]: ...

class SaveParamsReader(_DynamicStructReader):
    @property
    def sealFor(self) -> OwnerReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> SaveParamsBuilder: ...

class SaveParamsBuilder(_DynamicStructBuilder):
    @property
    def sealFor(self) -> OwnerBuilder: ...
    @sealFor.setter
    def sealFor(self, value: OwnerBuilder | OwnerReader | dict[str, Any]) -> None: ...
    @override
    def init(
        self,
        field: Literal["sealFor"],
        size: int | None = None,
    ) -> OwnerBuilder: ...
    @override
    def as_reader(self) -> SaveParamsReader: ...

class SaveResultsReader(_DynamicStructReader):
    @property
    def sturdyRef(self) -> SturdyRefReader: ...
    @property
    def unsaveSR(self) -> SturdyRefReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> SaveResultsBuilder: ...

class SaveResultsBuilder(_DynamicStructBuilder):
    @property
    def sturdyRef(self) -> SturdyRefBuilder: ...
    @sturdyRef.setter
    def sturdyRef(
        self,
        value: SturdyRefBuilder | SturdyRefReader | dict[str, Any],
    ) -> None: ...
    @property
    def unsaveSR(self) -> SturdyRefBuilder: ...
    @unsaveSR.setter
    def unsaveSR(
        self,
        value: SturdyRefBuilder | SturdyRefReader | dict[str, Any],
    ) -> None: ...
    @override
    @overload
    def init(
        self,
        field: Literal["sturdyRef"],
        size: int | None = None,
    ) -> SturdyRefBuilder: ...
    @overload
    def init(
        self,
        field: Literal["unsaveSR"],
        size: int | None = None,
    ) -> SturdyRefBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> SaveResultsReader: ...

class ReleaseRequest(Protocol):
    def send(self) -> ReleaseResult: ...

class ReleaseResult(Awaitable[ReleaseResult], Protocol):
    success: bool

class ReleaseServerResult(_DynamicStructBuilder):
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class ReleaseParams(Protocol): ...

class ReleaseCallContext(Protocol):
    params: ReleaseParams
    @property
    def results(self) -> ReleaseServerResult: ...

class ReleaseResultTuple(NamedTuple):
    success: bool

class ReleaseSturdyRefClient(_DynamicCapabilityClient):
    def release(self) -> ReleaseResult: ...
    def release_request(self) -> ReleaseRequest: ...

class SaveRequest(Protocol):
    sealFor: OwnerBuilder
    @overload
    def init(self, name: Literal["sealFor"]) -> OwnerBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> SaveResult: ...

class SaveResult(Awaitable[SaveResult], Protocol):
    sturdyRef: SturdyRefReader
    unsaveSR: SturdyRefReader

class SaveCallContext(Protocol):
    params: SaveParamsReader
    @property
    def results(self) -> SaveResultsBuilder: ...

class SaveResultTuple(NamedTuple):
    sturdyRef: SturdyRefBuilder | SturdyRefReader | dict[str, Any]
    unsaveSR: SturdyRefBuilder | SturdyRefReader | dict[str, Any]

class PersistentClient(_DynamicCapabilityClient):
    def save(
        self,
        sealFor: OwnerBuilder | OwnerReader | dict[str, Any] | None = None,
    ) -> SaveResult: ...
    def save_request(self, sealFor: OwnerBuilder | None = None) -> SaveRequest: ...

Persistent: _PersistentInterfaceModule

class _RestorerInterfaceModule(_InterfaceModule):
    class _RestoreParamsStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            localRef: TokenBuilder | dict[str, Any] | None = None,
            sealedBy: OwnerBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> RestoreParamsBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[RestoreParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[RestoreParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[RestoreParamsBuilder]: ...
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
        ) -> RestoreParamsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> RestoreParamsReader: ...

    RestoreParams: _RestoreParamsStructModule
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> RestorerClient: ...
    class Server(_DynamicCapabilityServer):
        def restore(
            self,
            localRef: TokenReader,
            sealedBy: OwnerReader,
            _context: RestoreCallContext,
            **kwargs: object,
        ) -> Awaitable[Capability | RestoreResultTuple | None]: ...
        def restore_context(self, context: RestoreCallContext) -> Awaitable[None]: ...

class RestoreParamsReader(_DynamicStructReader):
    @property
    def localRef(self) -> TokenReader: ...
    @property
    def sealedBy(self) -> OwnerReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> RestoreParamsBuilder: ...

class RestoreParamsBuilder(_DynamicStructBuilder):
    @property
    def localRef(self) -> TokenBuilder: ...
    @localRef.setter
    def localRef(self, value: TokenBuilder | TokenReader | dict[str, Any]) -> None: ...
    @property
    def sealedBy(self) -> OwnerBuilder: ...
    @sealedBy.setter
    def sealedBy(self, value: OwnerBuilder | OwnerReader | dict[str, Any]) -> None: ...
    @override
    @overload
    def init(
        self,
        field: Literal["localRef"],
        size: int | None = None,
    ) -> TokenBuilder: ...
    @overload
    def init(
        self,
        field: Literal["sealedBy"],
        size: int | None = None,
    ) -> OwnerBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> RestoreParamsReader: ...

class RestoreRequest(Protocol):
    localRef: TokenBuilder
    sealedBy: OwnerBuilder
    @overload
    def init(self, name: Literal["localRef"]) -> TokenBuilder: ...
    @overload
    def init(self, name: Literal["sealedBy"]) -> OwnerBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> RestoreResult: ...

class RestoreResult(Awaitable[RestoreResult], Protocol):
    cap: _DynamicObjectReader

class RestoreServerResult(_DynamicStructBuilder):
    @property
    def cap(self) -> Capability: ...
    @cap.setter
    def cap(self, value: Capability) -> None: ...

class RestoreCallContext(Protocol):
    params: RestoreParamsReader
    @property
    def results(self) -> RestoreServerResult: ...

class RestoreResultTuple(NamedTuple):
    cap: Capability

class RestorerClient(_DynamicCapabilityClient):
    def restore(
        self,
        localRef: TokenBuilder | TokenReader | dict[str, Any] | None = None,
        sealedBy: OwnerBuilder | OwnerReader | dict[str, Any] | None = None,
    ) -> RestoreResult: ...
    def restore_request(
        self,
        localRef: TokenBuilder | None = None,
        sealedBy: OwnerBuilder | None = None,
    ) -> RestoreRequest: ...

Restorer: _RestorerInterfaceModule

class _HostPortResolverInterfaceModule(
    _IdentifiableInterfaceModule,
    _RestorerInterfaceModule,
):
    class _RegistrarInterfaceModule(_InterfaceModule):
        class _RegisterParamsStructModule(_StructModule):
            class Reader(_DynamicStructReader): ...
            class Builder(_DynamicStructBuilder): ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
                base64VatId: str | None = None,
                host: str | None = None,
                port: int | None = None,
                alias: str | None = None,
                identityProof: bytes | None = None,
                **kwargs: object,
            ) -> RegisterParamsBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[RegisterParamsReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[RegisterParamsReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[RegisterParamsBuilder]: ...
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
            ) -> RegisterParamsReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> RegisterParamsReader: ...

        RegisterParams: _RegisterParamsStructModule
        @override
        def _new_client(self, server: _DynamicCapabilityServer) -> RegistrarClient: ...
        class Server(_DynamicCapabilityServer):
            def register(
                self,
                base64VatId: str,
                host: str,
                port: int,
                alias: str,
                identityProof: bytes,
                _context: RegistrarRegisterCallContext,
                **kwargs: object,
            ) -> Awaitable[RegistrarRegisterResultTuple | None]: ...
            def register_context(
                self,
                context: RegistrarRegisterCallContext,
            ) -> Awaitable[None]: ...

    Registrar: _RegistrarInterfaceModule
    type RegistrarServer = (
        _HostPortResolverInterfaceModule._RegistrarInterfaceModule.Server
    )
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> HostPortResolverClient: ...
    class Server(_IdentifiableInterfaceModule.Server, _RestorerInterfaceModule.Server):
        def resolve(
            self,
            id: str,
            _context: ResolveCallContext,
            **kwargs: object,
        ) -> Awaitable[ResolveResultTuple | None]: ...
        def resolve_context(self, context: ResolveCallContext) -> Awaitable[None]: ...

class RegisterParamsReader(_DynamicStructReader):
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> RegisterParamsBuilder: ...

class RegisterParamsBuilder(_DynamicStructBuilder):
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

class RegistrarRegisterRequest(Protocol):
    base64VatId: str
    host: str
    port: int
    alias: str
    identityProof: bytes
    def send(self) -> RegistrarRegisterResult: ...

class RegistrarRegisterResult(Awaitable[RegistrarRegisterResult], Protocol):
    heartbeat: HeartbeatClient
    secsHeartbeatInterval: int

class RegistrarRegisterServerResult(_DynamicStructBuilder):
    @property
    def heartbeat(self) -> _HeartbeatInterfaceModule.Server | HeartbeatClient: ...
    @heartbeat.setter
    def heartbeat(
        self,
        value: _HeartbeatInterfaceModule.Server | HeartbeatClient,
    ) -> None: ...
    @property
    def secsHeartbeatInterval(self) -> int: ...
    @secsHeartbeatInterval.setter
    def secsHeartbeatInterval(self, value: int) -> None: ...

class RegistrarRegisterCallContext(Protocol):
    params: RegisterParamsReader
    @property
    def results(self) -> RegistrarRegisterServerResult: ...

class RegistrarRegisterResultTuple(NamedTuple):
    heartbeat: _HeartbeatInterfaceModule.Server | HeartbeatClient
    secsHeartbeatInterval: int

class RegistrarClient(_DynamicCapabilityClient):
    def register(
        self,
        base64VatId: str | None = None,
        host: str | None = None,
        port: int | None = None,
        alias: str | None = None,
        identityProof: bytes | None = None,
    ) -> RegistrarRegisterResult: ...
    def register_request(
        self,
        base64VatId: str | None = None,
        host: str | None = None,
        port: int | None = None,
        alias: str | None = None,
        identityProof: bytes | None = None,
    ) -> RegistrarRegisterRequest: ...

class ResolveRequest(Protocol):
    id: str
    def send(self) -> ResolveResult: ...

class ResolveResult(Awaitable[ResolveResult], Protocol):
    host: str
    port: int

class ResolveServerResult(_DynamicStructBuilder):
    @property
    def host(self) -> str: ...
    @host.setter
    def host(self, value: str) -> None: ...
    @property
    def port(self) -> int: ...
    @port.setter
    def port(self, value: int) -> None: ...

class ResolveParams(Protocol):
    id: str

class ResolveCallContext(Protocol):
    params: ResolveParams
    @property
    def results(self) -> ResolveServerResult: ...

class ResolveResultTuple(NamedTuple):
    host: str
    port: int

class HostPortResolverClient(IdentifiableClient, RestorerClient):
    def resolve(self, id: str | None = None) -> ResolveResult: ...
    def resolve_request(self, id: str | None = None) -> ResolveRequest: ...

HostPortResolver: _HostPortResolverInterfaceModule

class _GatewayInterfaceModule(_IdentifiableInterfaceModule, _RestorerInterfaceModule):
    class _RegResultsStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            sturdyRef: SturdyRefBuilder | dict[str, Any] | None = None,
            heartbeat: HeartbeatClient | _HeartbeatInterfaceModule.Server | None = None,
            secsHeartbeatInterval: int | None = None,
            **kwargs: object,
        ) -> RegResultsBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[RegResultsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[RegResultsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[RegResultsBuilder]: ...
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
        ) -> RegResultsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> RegResultsReader: ...

    RegResults: _RegResultsStructModule
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> GatewayClient: ...
    class Server(_IdentifiableInterfaceModule.Server, _RestorerInterfaceModule.Server):
        def register(
            self,
            cap: AnyPointer,
            secretSeed: str,
            _context: GatewayRegisterCallContext,
            **kwargs: object,
        ) -> Awaitable[GatewayRegisterResultTuple | None]: ...
        def register_context(
            self,
            context: GatewayRegisterCallContext,
        ) -> Awaitable[None]: ...

class RegResultsReader(_DynamicStructReader):
    @property
    def sturdyRef(self) -> SturdyRefReader: ...
    @property
    def heartbeat(self) -> HeartbeatClient: ...
    @property
    def secsHeartbeatInterval(self) -> int: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> RegResultsBuilder: ...

class RegResultsBuilder(_DynamicStructBuilder):
    @property
    def sturdyRef(self) -> SturdyRefBuilder: ...
    @sturdyRef.setter
    def sturdyRef(
        self,
        value: SturdyRefBuilder | SturdyRefReader | dict[str, Any],
    ) -> None: ...
    @property
    def heartbeat(self) -> HeartbeatClient: ...
    @heartbeat.setter
    def heartbeat(
        self,
        value: HeartbeatClient | _HeartbeatInterfaceModule.Server,
    ) -> None: ...
    @property
    def secsHeartbeatInterval(self) -> int: ...
    @secsHeartbeatInterval.setter
    def secsHeartbeatInterval(self, value: int) -> None: ...
    @override
    def init(
        self,
        field: Literal["sturdyRef"],
        size: int | None = None,
    ) -> SturdyRefBuilder: ...
    @override
    def as_reader(self) -> RegResultsReader: ...

class GatewayRegisterRequest(Protocol):
    cap: AnyPointer
    secretSeed: str
    def send(self) -> GatewayRegisterResult: ...

class GatewayRegisterResult(Awaitable[GatewayRegisterResult], Protocol):
    sturdyRef: SturdyRefReader
    heartbeat: HeartbeatClient
    secsHeartbeatInterval: int

class GatewayRegisterParams(Protocol):
    cap: AnyPointer
    secretSeed: str

class GatewayRegisterCallContext(Protocol):
    params: GatewayRegisterParams
    @property
    def results(self) -> RegResultsBuilder: ...

class GatewayRegisterResultTuple(NamedTuple):
    sturdyRef: SturdyRefBuilder | SturdyRefReader | dict[str, Any]
    heartbeat: _HeartbeatInterfaceModule.Server | HeartbeatClient
    secsHeartbeatInterval: int

class GatewayClient(IdentifiableClient, RestorerClient):
    def register(
        self,
        cap: AnyPointer | None = None,
        secretSeed: str | None = None,
    ) -> GatewayRegisterResult: ...
    def register_request(
        self,
        cap: AnyPointer | None = None,
        secretSeed: str | None = None,
    ) -> GatewayRegisterRequest: ...

Gateway: _GatewayInterfaceModule

class _GatewayRegistrableInterfaceModule(_InterfaceModule):
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> GatewayRegistrableClient: ...
    class Server(_DynamicCapabilityServer):
        def sturdyRefAtGateway(
            self,
            gatewaySR: SturdyRefReader,
            gatewayId: str,
            _context: SturdyrefatgatewayCallContext,
            **kwargs: object,
        ) -> Awaitable[
            SturdyRefBuilder
            | SturdyRefReader
            | dict[str, Any]
            | SturdyrefatgatewayResultTuple
            | None
        ]: ...
        def sturdyRefAtGateway_context(
            self,
            context: SturdyrefatgatewayCallContext,
        ) -> Awaitable[None]: ...

class SturdyrefatgatewayRequest(Protocol):
    gatewaySR: SturdyRefBuilder
    gatewayId: str
    @overload
    def init(self, name: Literal["gatewaySR"]) -> SturdyRefBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> SturdyrefatgatewayResult: ...

class SturdyrefatgatewayResult(Awaitable[SturdyrefatgatewayResult], Protocol):
    selfAtGatewaySR: SturdyRefReader

class SturdyrefatgatewayServerResult(_DynamicStructBuilder):
    @property
    def selfAtGatewaySR(self) -> SturdyRefBuilder: ...
    @selfAtGatewaySR.setter
    def selfAtGatewaySR(
        self,
        value: SturdyRefBuilder | SturdyRefReader | dict[str, Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["selfAtGatewaySR"],
        size: int | None = None,
    ) -> SturdyRefBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class SturdyrefatgatewayParams(Protocol):
    gatewaySR: SturdyRefReader
    gatewayId: str

class SturdyrefatgatewayCallContext(Protocol):
    params: SturdyrefatgatewayParams
    @property
    def results(self) -> SturdyrefatgatewayServerResult: ...

class SturdyrefatgatewayResultTuple(NamedTuple):
    selfAtGatewaySR: SturdyRefBuilder | SturdyRefReader | dict[str, Any]

class GatewayRegistrableClient(_DynamicCapabilityClient):
    def sturdyRefAtGateway(
        self,
        gatewaySR: SturdyRefBuilder | SturdyRefReader | dict[str, Any] | None = None,
        gatewayId: str | None = None,
    ) -> SturdyrefatgatewayResult: ...
    def sturdyRefAtGateway_request(
        self,
        gatewaySR: SturdyRefBuilder | None = None,
        gatewayId: str | None = None,
    ) -> SturdyrefatgatewayRequest: ...

GatewayRegistrable: _GatewayRegistrableInterfaceModule

# Top-level type aliases for use in type annotations
GatewayRegistrableServer = _GatewayRegistrableInterfaceModule.Server
GatewayServer = _GatewayInterfaceModule.Server
HeartbeatServer = _HeartbeatInterfaceModule.Server
HostPortResolverServer = _HostPortResolverInterfaceModule.Server
PersistentServer = _PersistentInterfaceModule.Server
RegistrarServer = _HostPortResolverInterfaceModule._RegistrarInterfaceModule.Server
ReleaseSturdyRefServer = (
    _PersistentInterfaceModule._ReleaseSturdyRefInterfaceModule.Server
)
RestorerServer = _RestorerInterfaceModule.Server
