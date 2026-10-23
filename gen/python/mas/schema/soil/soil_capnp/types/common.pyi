"""Common typing aliases for `soil.capnp`."""

from typing import Literal, override

from capnp.lib.capnp import _DynamicEnumField

class _PropertyWhich(_DynamicEnumField):
    @override
    def __call__(self) -> Literal["f32Value", "bValue", "type", "unset"]: ...
