"""Reader helper types for `persistence.capnp`."""

from collections.abc import Callable
from typing import Literal, override

from capnp.lib.capnp import (
    _DynamicStructReader,
)

from mas.schema.persistence.persistence_capnp.types import builders as builders
from mas.schema.persistence.persistence_capnp.types import clients as clients

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
    ) -> builders.VatIdBuilder: ...

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
    ) -> builders.AddressIp6Builder: ...

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
    ) -> builders.AddressBuilder: ...

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
    ) -> builders.VatPathBuilder: ...

class OwnerReader(_DynamicStructReader):
    @property
    def guid(self) -> str: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.OwnerBuilder: ...

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
    ) -> builders.TokenBuilder: ...

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
    ) -> builders.SturdyRefBuilder: ...

class SaveParamsReader(_DynamicStructReader):
    @property
    def sealFor(self) -> OwnerReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.SaveParamsBuilder: ...

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
    ) -> builders.SaveResultsBuilder: ...

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
    ) -> builders.RestoreParamsBuilder: ...

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
    ) -> builders.RegisterParamsBuilder: ...

class RegResultsReader(_DynamicStructReader):
    @property
    def sturdyRef(self) -> SturdyRefReader: ...
    @property
    def heartbeat(self) -> clients.HeartbeatClient: ...
    @property
    def secsHeartbeatInterval(self) -> int: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.RegResultsBuilder: ...
