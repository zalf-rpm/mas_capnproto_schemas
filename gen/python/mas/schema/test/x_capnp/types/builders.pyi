"""Builder helper types for `x.capnp`."""

from typing import override

from capnp.lib.capnp import (
    _DynamicStructBuilder,
)

from mas.schema.test.x_capnp.types import clients as clients
from mas.schema.test.x_capnp.types import modules as modules
from mas.schema.test.x_capnp.types import readers as readers

class SBuilder(_DynamicStructBuilder):
    @property
    def c(self) -> clients.XClient: ...
    @c.setter
    def c(self, value: clients.XClient | modules._XInterfaceModule.Server) -> None: ...
    @override
    def as_reader(self) -> readers.SReader: ...
