"""Server result helper types for `model.capnp`."""

from collections.abc import Sequence
from typing import Any, Literal, overload

from capnp.lib.capnp import (
    _DynamicObjectBuilder,
    _DynamicStructBuilder,
)

from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.model.model_capnp.types import builders as builders
from mas.schema.model.model_capnp.types import clients as clients
from mas.schema.model.model_capnp.types import common as common
from mas.schema.model.model_capnp.types import modules as modules
from mas.schema.model.model_capnp.types import readers as readers

class ClimateInstanceRunServerResult(_DynamicStructBuilder):
    @property
    def result(self) -> builders.XYResultBuilder: ...
    @result.setter
    def result(
        self,
        value: builders.XYResultBuilder | readers.XYResultReader | dict[str, Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["result"],
        size: int | None = None,
    ) -> builders.XYResultBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class RunsetServerResult(_DynamicStructBuilder):
    @property
    def result(self) -> builders.XYPlusResultBuilder: ...
    @result.setter
    def result(
        self,
        value: builders.XYPlusResultBuilder
        | readers.XYPlusResultReader
        | dict[str, Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["result"],
        size: int | None = None,
    ) -> builders.XYPlusResultBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class EnvInstanceRunServerResult(_DynamicStructBuilder):
    @property
    def result(self) -> _DynamicObjectBuilder: ...
    @result.setter
    def result(self, value: common.AnyPointer) -> None: ...

class UnregisterServerResult(_DynamicStructBuilder):
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class RegisterenvinstanceServerResult(_DynamicStructBuilder):
    @property
    def unregister(
        self,
    ) -> (
        modules._EnvInstanceProxyInterfaceModule._UnregisterInterfaceModule.Server
        | clients.UnregisterClient
    ): ...
    @unregister.setter
    def unregister(
        self,
        value: modules._EnvInstanceProxyInterfaceModule._UnregisterInterfaceModule.Server
        | clients.UnregisterClient,
    ) -> None: ...

class NewinstanceServerResult(_DynamicStructBuilder):
    @property
    def instance(self) -> _IdentifiableInterfaceModule.Server | IdentifiableClient: ...
    @instance.setter
    def instance(
        self,
        value: _IdentifiableInterfaceModule.Server | IdentifiableClient,
    ) -> None: ...

class NewinstancesServerResult(_DynamicStructBuilder):
    @property
    def instances(self) -> builders.IdentifiableClientListBuilder: ...
    @instances.setter
    def instances(
        self,
        value: builders.IdentifiableClientListBuilder
        | readers.IdentifiableClientListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["instances"],
        size: int | None = None,
    ) -> builders.IdentifiableClientListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
