"""This is an automatically generated stub for `config.capnp`."""

import os
from typing import NamedTuple

import capnp

capnp.remove_import_hook()
here = os.path.dirname(os.path.abspath(__file__))
module_file = os.path.abspath(
    os.path.join(here, "../zalfmas_capnp_schemas/config.capnp")
)
import_path = [here, os.path.abspath(os.path.join(here, "../zalfmas_capnp_schemas"))]
Service = capnp.load(module_file, imports=import_path).Service

Service.Server.NextconfigResultTuple = NamedTuple(
    "NextconfigResultTuple", [("config", object), ("noFurtherConfigs", object)]
)
