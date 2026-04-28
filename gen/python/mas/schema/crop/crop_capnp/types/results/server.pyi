"""Server result helper types for `crop.capnp`."""

from typing import Any, Literal, overload

from capnp.lib.capnp import (
    _DynamicObjectBuilder,
    _DynamicStructBuilder,
)

from mas.schema.common.common_capnp.types.builders import IdInformationBuilder
from mas.schema.common.common_capnp.types.readers import IdInformationReader
from mas.schema.crop.crop_capnp.types import common as common

class ParametersServerResult(_DynamicStructBuilder):
    @property
    def params(self) -> _DynamicObjectBuilder: ...
    @params.setter
    def params(self, value: common.AnyPointer) -> None: ...

class CultivarServerResult(_DynamicStructBuilder):
    @property
    def info(self) -> IdInformationBuilder: ...
    @info.setter
    def info(
        self,
        value: IdInformationBuilder | IdInformationReader | dict[str, Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["info"],
        size: int | None = None,
    ) -> IdInformationBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class SpeciesServerResult(_DynamicStructBuilder):
    @property
    def info(self) -> IdInformationBuilder: ...
    @info.setter
    def info(
        self,
        value: IdInformationBuilder | IdInformationReader | dict[str, Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["info"],
        size: int | None = None,
    ) -> IdInformationBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
