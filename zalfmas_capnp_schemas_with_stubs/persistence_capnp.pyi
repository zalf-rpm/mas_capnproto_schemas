"""This is an automatically generated stub for `persistence.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator
from typing import Any, Literal, NamedTuple, Protocol, TypeAlias, overload, override

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

from .common_capnp import Identifiable, IdentifiableClient, _IdentifiableModule

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
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _VatIdModule.Builder: ...

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
        def as_reader(self) -> _VatIdModule.Reader: ...

    @override
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, publicKey0: int | None = None, publicKey1: int | None = None, publicKey2: int | None = None, publicKey3: int | None = None) -> _VatIdModule.Builder: ...

VatIdReader: TypeAlias = _VatIdModule.Reader
VatIdBuilder: TypeAlias = _VatIdModule.Builder
VatId: _VatIdModule

class _AddressModule(_StructModule):
    class _Ip6Module(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def lower64(self) -> int: ...
            @property
            def upper64(self) -> int: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _AddressModule._Ip6Module.Builder: ...

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
            def as_reader(self) -> _AddressModule._Ip6Module.Reader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, lower64: int | None = None, upper64: int | None = None) -> _AddressModule._Ip6Module.Builder: ...

    Ip6Reader: TypeAlias = _Ip6Module.Reader
    Ip6Builder: TypeAlias = _Ip6Module.Builder
    Ip6: _Ip6Module
    class Reader(_DynamicStructReader):
        @property
        def ip6(self) -> _AddressModule._Ip6Module.Reader: ...
        @property
        def port(self) -> int: ...
        @property
        def host(self) -> str: ...
        @override
        def which(self) -> Literal["ip6", "host"]: ...
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _AddressModule.Builder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def ip6(self) -> _AddressModule._Ip6Module.Builder: ...
        @ip6.setter
        def ip6(self, value: _AddressModule._Ip6Module.Builder | _AddressModule._Ip6Module.Reader | dict[str, Any]) -> None: ...
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
        def init(self, field: Literal["ip6"], size: int | None = None) -> _AddressModule._Ip6Module.Builder: ...
        @override
        def as_reader(self) -> _AddressModule.Reader: ...

    @override
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, ip6: _AddressModule._Ip6Module.Builder | dict[str, Any] | None = None, port: int | None = None, host: str | None = None) -> _AddressModule.Builder: ...

AddressReader: TypeAlias = _AddressModule.Reader
AddressBuilder: TypeAlias = _AddressModule.Builder
Address: _AddressModule

class _VatPathModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def id(self) -> _VatIdModule.Reader: ...
        @property
        def address(self) -> _AddressModule.Reader: ...
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _VatPathModule.Builder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def id(self) -> _VatIdModule.Builder: ...
        @id.setter
        def id(self, value: _VatIdModule.Builder | _VatIdModule.Reader | dict[str, Any]) -> None: ...
        @property
        def address(self) -> _AddressModule.Builder: ...
        @address.setter
        def address(self, value: _AddressModule.Builder | _AddressModule.Reader | dict[str, Any]) -> None: ...
        @overload
        def init(self, field: Literal["id"], size: int | None = None) -> _VatIdModule.Builder: ...
        @overload
        def init(self, field: Literal["address"], size: int | None = None) -> _AddressModule.Builder: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> _VatPathModule.Reader: ...

    @override
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, id: _VatIdModule.Builder | dict[str, Any] | None = None, address: _AddressModule.Builder | dict[str, Any] | None = None) -> _VatPathModule.Builder: ...

VatPathReader: TypeAlias = _VatPathModule.Reader
VatPathBuilder: TypeAlias = _VatPathModule.Builder
VatPath: _VatPathModule

class _SturdyRefModule(_StructModule):
    class _OwnerModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def guid(self) -> str: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _SturdyRefModule._OwnerModule.Builder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def guid(self) -> str: ...
            @guid.setter
            def guid(self, value: str) -> None: ...
            @override
            def as_reader(self) -> _SturdyRefModule._OwnerModule.Reader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, guid: str | None = None) -> _SturdyRefModule._OwnerModule.Builder: ...

    OwnerReader: TypeAlias = _OwnerModule.Reader
    OwnerBuilder: TypeAlias = _OwnerModule.Builder
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
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _SturdyRefModule._TokenModule.Builder: ...

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
            def as_reader(self) -> _SturdyRefModule._TokenModule.Reader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, text: str | None = None, data: bytes | None = None) -> _SturdyRefModule._TokenModule.Builder: ...

    TokenReader: TypeAlias = _TokenModule.Reader
    TokenBuilder: TypeAlias = _TokenModule.Builder
    Token: _TokenModule
    class Reader(_DynamicStructReader):
        @property
        def vat(self) -> _VatPathModule.Reader: ...
        @property
        def localRef(self) -> _SturdyRefModule._TokenModule.Reader: ...
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _SturdyRefModule.Builder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def vat(self) -> _VatPathModule.Builder: ...
        @vat.setter
        def vat(self, value: _VatPathModule.Builder | _VatPathModule.Reader | dict[str, Any]) -> None: ...
        @property
        def localRef(self) -> _SturdyRefModule._TokenModule.Builder: ...
        @localRef.setter
        def localRef(self, value: _SturdyRefModule._TokenModule.Builder | _SturdyRefModule._TokenModule.Reader | dict[str, Any]) -> None: ...
        @overload
        def init(self, field: Literal["vat"], size: int | None = None) -> _VatPathModule.Builder: ...
        @overload
        def init(self, field: Literal["localRef"], size: int | None = None) -> _SturdyRefModule._TokenModule.Builder: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> _SturdyRefModule.Reader: ...

    @override
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, vat: _VatPathModule.Builder | dict[str, Any] | None = None, localRef: _SturdyRefModule._TokenModule.Builder | dict[str, Any] | None = None) -> _SturdyRefModule.Builder: ...

SturdyRefReader: TypeAlias = _SturdyRefModule.Reader
SturdyRefBuilder: TypeAlias = _SturdyRefModule.Builder
SturdyRef: _SturdyRefModule

class _HeartbeatModule(_InterfaceModule):
    class BeatRequest(Protocol):
        def send(self) -> _HeartbeatModule.HeartbeatClient.BeatResult: ...

    @classmethod
    def _new_client(cls, server: _HeartbeatModule.Server) -> _HeartbeatModule.HeartbeatClient: ...
    class Server(_DynamicCapabilityServer):
        class BeatResult(Awaitable[None], Protocol): ...

        class BeatCallContext(Protocol):
            params: _HeartbeatModule.BeatRequest

        def beat(self, _context: _HeartbeatModule.Server.BeatCallContext, **kwargs: Any) -> Awaitable[None]: ...
        def beat_context(self, context: _HeartbeatModule.Server.BeatCallContext) -> Awaitable[None]: ...

    class HeartbeatClient(_DynamicCapabilityClient):
        class BeatResult(Awaitable[None], Protocol): ...

        def beat(self) -> _HeartbeatModule.HeartbeatClient.BeatResult: ...
        def beat_request(self) -> _HeartbeatModule.BeatRequest: ...

Heartbeat: _HeartbeatModule
HeartbeatClient: TypeAlias = _HeartbeatModule.HeartbeatClient

class _PersistentModule(_InterfaceModule):
    class _SaveParamsModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def sealFor(self) -> _SturdyRefModule._OwnerModule.Reader: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _PersistentModule._SaveParamsModule.Builder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def sealFor(self) -> _SturdyRefModule._OwnerModule.Builder: ...
            @sealFor.setter
            def sealFor(self, value: _SturdyRefModule._OwnerModule.Builder | _SturdyRefModule._OwnerModule.Reader | dict[str, Any]) -> None: ...
            def init(self, field: Literal["sealFor"], size: int | None = None) -> _SturdyRefModule._OwnerModule.Builder: ...
            @override
            def as_reader(self) -> _PersistentModule._SaveParamsModule.Reader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, sealFor: _SturdyRefModule._OwnerModule.Builder | dict[str, Any] | None = None) -> _PersistentModule._SaveParamsModule.Builder: ...

    SaveParamsReader: TypeAlias = _SaveParamsModule.Reader
    SaveParamsBuilder: TypeAlias = _SaveParamsModule.Builder
    SaveParams: _SaveParamsModule
    class _SaveResultsModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def sturdyRef(self) -> _SturdyRefModule.Reader: ...
            @property
            def unsaveSR(self) -> _SturdyRefModule.Reader: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _PersistentModule._SaveResultsModule.Builder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def sturdyRef(self) -> _SturdyRefModule.Builder: ...
            @sturdyRef.setter
            def sturdyRef(self, value: _SturdyRefModule.Builder | _SturdyRefModule.Reader | dict[str, Any]) -> None: ...
            @property
            def unsaveSR(self) -> _SturdyRefModule.Builder: ...
            @unsaveSR.setter
            def unsaveSR(self, value: _SturdyRefModule.Builder | _SturdyRefModule.Reader | dict[str, Any]) -> None: ...
            @overload
            def init(self, field: Literal["sturdyRef"], size: int | None = None) -> _SturdyRefModule.Builder: ...
            @overload
            def init(self, field: Literal["unsaveSR"], size: int | None = None) -> _SturdyRefModule.Builder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...
            @override
            def as_reader(self) -> _PersistentModule._SaveResultsModule.Reader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, sturdyRef: _SturdyRefModule.Builder | dict[str, Any] | None = None, unsaveSR: _SturdyRefModule.Builder | dict[str, Any] | None = None) -> _PersistentModule._SaveResultsModule.Builder: ...

    SaveResultsReader: TypeAlias = _SaveResultsModule.Reader
    SaveResultsBuilder: TypeAlias = _SaveResultsModule.Builder
    SaveResults: _SaveResultsModule
    class _ReleaseSturdyRefModule(_InterfaceModule):
        class ReleaseRequest(Protocol):
            def send(self) -> _PersistentModule._ReleaseSturdyRefModule.ReleaseSturdyRefClient.ReleaseResult: ...

        @classmethod
        def _new_client(cls, server: _PersistentModule._ReleaseSturdyRefModule.Server) -> _PersistentModule._ReleaseSturdyRefModule.ReleaseSturdyRefClient: ...
        class Server(_DynamicCapabilityServer):
            class ReleaseResult(Awaitable[ReleaseResult], Protocol):
                success: bool

            class ReleaseResultTuple(NamedTuple):
                success: bool

            class ReleaseCallContext(Protocol):
                params: _PersistentModule._ReleaseSturdyRefModule.ReleaseRequest
                results: _PersistentModule._ReleaseSturdyRefModule.Server.ReleaseResult

            def release(self, _context: _PersistentModule._ReleaseSturdyRefModule.Server.ReleaseCallContext, **kwargs: Any) -> Awaitable[bool | _PersistentModule._ReleaseSturdyRefModule.Server.ReleaseResultTuple | None]: ...
            def release_context(self, context: _PersistentModule._ReleaseSturdyRefModule.Server.ReleaseCallContext) -> Awaitable[None]: ...

        class ReleaseSturdyRefClient(_DynamicCapabilityClient):
            class ReleaseResult(Awaitable[ReleaseResult], Protocol):
                success: bool

            def release(self) -> _PersistentModule._ReleaseSturdyRefModule.ReleaseSturdyRefClient.ReleaseResult: ...
            def release_request(self) -> _PersistentModule._ReleaseSturdyRefModule.ReleaseRequest: ...

    ReleaseSturdyRef: _ReleaseSturdyRefModule
    ReleaseSturdyRefClient: TypeAlias = _PersistentModule._ReleaseSturdyRefModule.ReleaseSturdyRefClient
    class SaveRequest(Protocol):
        sealFor: _SturdyRefModule._OwnerModule.Builder
        @overload
        def init(self, name: Literal["sealFor"]) -> _SturdyRefModule._OwnerModule.Builder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> _PersistentModule.PersistentClient.SaveResult: ...

    @classmethod
    def _new_client(cls, server: _PersistentModule.Server) -> _PersistentModule.PersistentClient: ...
    class Server(_DynamicCapabilityServer):
        class SaveResult(Awaitable[SaveResult], Protocol):
            sturdyRef: _SturdyRefModule.Builder | _SturdyRefModule.Reader
            unsaveSR: _SturdyRefModule.Builder | _SturdyRefModule.Reader

        class SaveResultTuple(NamedTuple):
            sturdyRef: _SturdyRefModule.Builder | _SturdyRefModule.Reader
            unsaveSR: _SturdyRefModule.Builder | _SturdyRefModule.Reader

        class SaveCallContext(Protocol):
            params: _PersistentModule.SaveRequest
            results: _PersistentModule.Server.SaveResult

        def save(self, sealFor: _SturdyRefModule._OwnerModule.Reader, _context: _PersistentModule.Server.SaveCallContext, **kwargs: Any) -> Awaitable[_PersistentModule.Server.SaveResultTuple | None]: ...
        def save_context(self, context: _PersistentModule.Server.SaveCallContext) -> Awaitable[None]: ...

    class PersistentClient(_DynamicCapabilityClient):
        class SaveResult(Awaitable[SaveResult], Protocol):
            sturdyRef: _SturdyRefModule.Builder | _SturdyRefModule.Reader
            unsaveSR: _SturdyRefModule.Builder | _SturdyRefModule.Reader

        def save(self, sealFor: OwnerBuilder | OwnerReader | dict[str, Any] | None = None) -> _PersistentModule.PersistentClient.SaveResult: ...
        def save_request(self, sealFor: _SturdyRefModule._OwnerModule.Builder | None = None) -> _PersistentModule.SaveRequest: ...

Persistent: _PersistentModule
PersistentClient: TypeAlias = _PersistentModule.PersistentClient

class _RestorerModule(_InterfaceModule):
    class _RestoreParamsModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def localRef(self) -> _SturdyRefModule._TokenModule.Reader: ...
            @property
            def sealedBy(self) -> _SturdyRefModule._OwnerModule.Reader: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _RestorerModule._RestoreParamsModule.Builder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def localRef(self) -> _SturdyRefModule._TokenModule.Builder: ...
            @localRef.setter
            def localRef(self, value: _SturdyRefModule._TokenModule.Builder | _SturdyRefModule._TokenModule.Reader | dict[str, Any]) -> None: ...
            @property
            def sealedBy(self) -> _SturdyRefModule._OwnerModule.Builder: ...
            @sealedBy.setter
            def sealedBy(self, value: _SturdyRefModule._OwnerModule.Builder | _SturdyRefModule._OwnerModule.Reader | dict[str, Any]) -> None: ...
            @overload
            def init(self, field: Literal["localRef"], size: int | None = None) -> _SturdyRefModule._TokenModule.Builder: ...
            @overload
            def init(self, field: Literal["sealedBy"], size: int | None = None) -> _SturdyRefModule._OwnerModule.Builder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...
            @override
            def as_reader(self) -> _RestorerModule._RestoreParamsModule.Reader: ...

        @override
        def new_message(
            self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, localRef: _SturdyRefModule._TokenModule.Builder | dict[str, Any] | None = None, sealedBy: _SturdyRefModule._OwnerModule.Builder | dict[str, Any] | None = None
        ) -> _RestorerModule._RestoreParamsModule.Builder: ...

    RestoreParamsReader: TypeAlias = _RestoreParamsModule.Reader
    RestoreParamsBuilder: TypeAlias = _RestoreParamsModule.Builder
    RestoreParams: _RestoreParamsModule
    class RestoreRequest(Protocol):
        localRef: _SturdyRefModule._TokenModule.Builder
        sealedBy: _SturdyRefModule._OwnerModule.Builder
        @overload
        def init(self, name: Literal["localRef"]) -> _SturdyRefModule._TokenModule.Builder: ...
        @overload
        def init(self, name: Literal["sealedBy"]) -> _SturdyRefModule._OwnerModule.Builder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> _RestorerModule.RestorerClient.RestoreResult: ...

    @classmethod
    def _new_client(cls, server: _RestorerModule.Server) -> _RestorerModule.RestorerClient: ...
    class Server(_DynamicCapabilityServer):
        class RestoreResult(Awaitable[RestoreResult], Protocol):
            cap: str | bytes | _DynamicStructBuilder | _DynamicStructReader | _DynamicCapabilityClient | _DynamicCapabilityServer

        class RestoreResultTuple(NamedTuple):
            cap: str | bytes | _DynamicStructBuilder | _DynamicStructReader | _DynamicCapabilityClient | _DynamicCapabilityServer

        class RestoreCallContext(Protocol):
            params: _RestorerModule.RestoreRequest
            results: _RestorerModule.Server.RestoreResult

        def restore(self, localRef: _SturdyRefModule._TokenModule.Reader, sealedBy: _SturdyRefModule._OwnerModule.Reader, _context: _RestorerModule.Server.RestoreCallContext, **kwargs: Any) -> Awaitable[_RestorerModule.Server.RestoreResultTuple | None]: ...
        def restore_context(self, context: _RestorerModule.Server.RestoreCallContext) -> Awaitable[None]: ...

    class RestorerClient(_DynamicCapabilityClient):
        class RestoreResult(Awaitable[RestoreResult], Protocol):
            cap: _DynamicObjectReader

        def restore(self, localRef: TokenBuilder | TokenReader | dict[str, Any] | None = None, sealedBy: OwnerBuilder | OwnerReader | dict[str, Any] | None = None) -> _RestorerModule.RestorerClient.RestoreResult: ...
        def restore_request(self, localRef: _SturdyRefModule._TokenModule.Builder | None = None, sealedBy: _SturdyRefModule._OwnerModule.Builder | None = None) -> _RestorerModule.RestoreRequest: ...

Restorer: _RestorerModule
RestorerClient: TypeAlias = _RestorerModule.RestorerClient

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
                def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _HostPortResolverModule._RegistrarModule._RegisterParamsModule.Builder: ...

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
                def as_reader(self) -> _HostPortResolverModule._RegistrarModule._RegisterParamsModule.Reader: ...

            @override
            def new_message(
                self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, base64VatId: str | None = None, host: str | None = None, port: int | None = None, alias: str | None = None, identityProof: bytes | None = None
            ) -> _HostPortResolverModule._RegistrarModule._RegisterParamsModule.Builder: ...

        RegisterParamsReader: TypeAlias = _RegisterParamsModule.Reader
        RegisterParamsBuilder: TypeAlias = _RegisterParamsModule.Builder
        RegisterParams: _RegisterParamsModule
        class RegisterRequest(Protocol):
            base64VatId: str
            host: str
            port: int
            alias: str
            identityProof: bytes
            def send(self) -> _HostPortResolverModule._RegistrarModule.RegistrarClient.RegisterResult: ...

        @classmethod
        def _new_client(cls, server: _HostPortResolverModule._RegistrarModule.Server) -> _HostPortResolverModule._RegistrarModule.RegistrarClient: ...
        class Server(_DynamicCapabilityServer):
            class RegisterResult(Awaitable[RegisterResult], Protocol):
                heartbeat: _HeartbeatModule.HeartbeatClient
                secsHeartbeatInterval: int

            class RegisterResultTuple(NamedTuple):
                heartbeat: _HeartbeatModule.Server
                secsHeartbeatInterval: int

            class RegisterCallContext(Protocol):
                params: _HostPortResolverModule._RegistrarModule.RegisterRequest
                results: _HostPortResolverModule._RegistrarModule.Server.RegisterResult

            def register(self, base64VatId: str, host: str, port: int, alias: str, identityProof: bytes, _context: _HostPortResolverModule._RegistrarModule.Server.RegisterCallContext, **kwargs: Any) -> Awaitable[_HostPortResolverModule._RegistrarModule.Server.RegisterResultTuple | None]: ...
            def register_context(self, context: _HostPortResolverModule._RegistrarModule.Server.RegisterCallContext) -> Awaitable[None]: ...

        class RegistrarClient(_DynamicCapabilityClient):
            class RegisterResult(Awaitable[RegisterResult], Protocol):
                heartbeat: _HeartbeatModule.HeartbeatClient
                secsHeartbeatInterval: int

            def register(self, base64VatId: str | None = None, host: str | None = None, port: int | None = None, alias: str | None = None, identityProof: bytes | None = None) -> _HostPortResolverModule._RegistrarModule.RegistrarClient.RegisterResult: ...
            def register_request(self, base64VatId: str | None = None, host: str | None = None, port: int | None = None, alias: str | None = None, identityProof: bytes | None = None) -> _HostPortResolverModule._RegistrarModule.RegisterRequest: ...

    Registrar: _RegistrarModule
    RegistrarClient: TypeAlias = _HostPortResolverModule._RegistrarModule.RegistrarClient
    class ResolveRequest(Protocol):
        id: str
        def send(self) -> _HostPortResolverModule.HostPortResolverClient.ResolveResult: ...

    @classmethod
    def _new_client(cls, server: _HostPortResolverModule.Server | _IdentifiableModule.Server | _RestorerModule.Server) -> _HostPortResolverModule.HostPortResolverClient: ...
    class Server(_IdentifiableModule.Server, _RestorerModule.Server):
        class ResolveResult(Awaitable[ResolveResult], Protocol):
            host: str
            port: int

        class ResolveResultTuple(NamedTuple):
            host: str
            port: int

        class ResolveCallContext(Protocol):
            params: _HostPortResolverModule.ResolveRequest
            results: _HostPortResolverModule.Server.ResolveResult

        def resolve(self, id: str, _context: _HostPortResolverModule.Server.ResolveCallContext, **kwargs: Any) -> Awaitable[_HostPortResolverModule.Server.ResolveResultTuple | None]: ...
        def resolve_context(self, context: _HostPortResolverModule.Server.ResolveCallContext) -> Awaitable[None]: ...

    class HostPortResolverClient(_IdentifiableModule.IdentifiableClient, _RestorerModule.RestorerClient):
        class ResolveResult(Awaitable[ResolveResult], Protocol):
            host: str
            port: int

        def resolve(self, id: str | None = None) -> _HostPortResolverModule.HostPortResolverClient.ResolveResult: ...
        def resolve_request(self, id: str | None = None) -> _HostPortResolverModule.ResolveRequest: ...

HostPortResolver: _HostPortResolverModule
HostPortResolverClient: TypeAlias = _HostPortResolverModule.HostPortResolverClient

class _GatewayModule(_IdentifiableModule, _RestorerModule):
    class _RegResultsModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def sturdyRef(self) -> _SturdyRefModule.Reader: ...
            @property
            def heartbeat(self) -> _HeartbeatModule.HeartbeatClient: ...
            @property
            def secsHeartbeatInterval(self) -> int: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _GatewayModule._RegResultsModule.Builder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def sturdyRef(self) -> _SturdyRefModule.Builder: ...
            @sturdyRef.setter
            def sturdyRef(self, value: _SturdyRefModule.Builder | _SturdyRefModule.Reader | dict[str, Any]) -> None: ...
            @property
            def heartbeat(self) -> _HeartbeatModule.HeartbeatClient: ...
            @heartbeat.setter
            def heartbeat(self, value: _HeartbeatModule.HeartbeatClient | _HeartbeatModule.Server) -> None: ...
            @property
            def secsHeartbeatInterval(self) -> int: ...
            @secsHeartbeatInterval.setter
            def secsHeartbeatInterval(self, value: int) -> None: ...
            def init(self, field: Literal["sturdyRef"], size: int | None = None) -> _SturdyRefModule.Builder: ...
            @override
            def as_reader(self) -> _GatewayModule._RegResultsModule.Reader: ...

        @override
        def new_message(
            self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, sturdyRef: _SturdyRefModule.Builder | dict[str, Any] | None = None, heartbeat: _HeartbeatModule.HeartbeatClient | _HeartbeatModule.Server | None = None, secsHeartbeatInterval: int | None = None
        ) -> _GatewayModule._RegResultsModule.Builder: ...

    RegResultsReader: TypeAlias = _RegResultsModule.Reader
    RegResultsBuilder: TypeAlias = _RegResultsModule.Builder
    RegResults: _RegResultsModule
    class RegisterRequest(Protocol):
        cap: _DynamicObjectReader
        def send(self) -> _GatewayModule.GatewayClient.RegisterResult: ...

    @classmethod
    def _new_client(cls, server: _GatewayModule.Server | _IdentifiableModule.Server | _RestorerModule.Server) -> _GatewayModule.GatewayClient: ...
    class Server(_IdentifiableModule.Server, _RestorerModule.Server):
        class RegisterResult(Awaitable[RegisterResult], Protocol):
            sturdyRef: _SturdyRefModule.Builder | _SturdyRefModule.Reader
            heartbeat: _HeartbeatModule.HeartbeatClient
            secsHeartbeatInterval: int

        class RegisterResultTuple(NamedTuple):
            sturdyRef: _SturdyRefModule.Builder | _SturdyRefModule.Reader
            heartbeat: _HeartbeatModule.Server
            secsHeartbeatInterval: int

        class RegisterCallContext(Protocol):
            params: _GatewayModule.RegisterRequest
            results: _GatewayModule.Server.RegisterResult

        def register(self, cap: _DynamicObjectReader, _context: _GatewayModule.Server.RegisterCallContext, **kwargs: Any) -> Awaitable[_GatewayModule.Server.RegisterResultTuple | None]: ...
        def register_context(self, context: _GatewayModule.Server.RegisterCallContext) -> Awaitable[None]: ...

    class GatewayClient(_IdentifiableModule.IdentifiableClient, _RestorerModule.RestorerClient):
        class RegisterResult(Awaitable[RegisterResult], Protocol):
            sturdyRef: _SturdyRefModule.Builder | _SturdyRefModule.Reader
            heartbeat: _HeartbeatModule.HeartbeatClient
            secsHeartbeatInterval: int

        def register(self, cap: _DynamicObjectReader | None = None) -> _GatewayModule.GatewayClient.RegisterResult: ...
        def register_request(self, cap: _DynamicObjectReader | None = None) -> _GatewayModule.RegisterRequest: ...

Gateway: _GatewayModule
GatewayClient: TypeAlias = _GatewayModule.GatewayClient

# Top-level type aliases for use in type annotations
Ip6Builder: TypeAlias = _AddressModule._Ip6Module.Builder
Ip6Reader: TypeAlias = _AddressModule._Ip6Module.Reader
OwnerBuilder: TypeAlias = _SturdyRefModule._OwnerModule.Builder
OwnerReader: TypeAlias = _SturdyRefModule._OwnerModule.Reader
RegResultsBuilder: TypeAlias = _GatewayModule._RegResultsModule.Builder
RegResultsReader: TypeAlias = _GatewayModule._RegResultsModule.Reader
RegisterParamsBuilder: TypeAlias = _HostPortResolverModule._RegistrarModule._RegisterParamsModule.Builder
RegisterParamsReader: TypeAlias = _HostPortResolverModule._RegistrarModule._RegisterParamsModule.Reader
RegistrarClient: TypeAlias = _HostPortResolverModule._RegistrarModule.RegistrarClient
ReleaseSturdyRefClient: TypeAlias = _PersistentModule._ReleaseSturdyRefModule.ReleaseSturdyRefClient
RestoreParamsBuilder: TypeAlias = _RestorerModule._RestoreParamsModule.Builder
RestoreParamsReader: TypeAlias = _RestorerModule._RestoreParamsModule.Reader
SaveParamsBuilder: TypeAlias = _PersistentModule._SaveParamsModule.Builder
SaveParamsReader: TypeAlias = _PersistentModule._SaveParamsModule.Reader
SaveResultsBuilder: TypeAlias = _PersistentModule._SaveResultsModule.Builder
SaveResultsReader: TypeAlias = _PersistentModule._SaveResultsModule.Reader
TokenBuilder: TypeAlias = _SturdyRefModule._TokenModule.Builder
TokenReader: TypeAlias = _SturdyRefModule._TokenModule.Reader
