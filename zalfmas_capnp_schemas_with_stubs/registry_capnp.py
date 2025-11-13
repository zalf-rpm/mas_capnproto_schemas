"""This is an automatically generated stub for `registry.capnp`."""

import os
from typing import NamedTuple

import capnp

capnp.remove_import_hook()
here = os.path.dirname(os.path.abspath(__file__))
module_file = os.path.abspath(
    os.path.join(here, "../zalfmas_capnp_schemas/registry.capnp")
)
import_path = [
    here,
    os.path.join(here, "../zalfmas_capnp_schemas"),
    os.path.join(here, "../zalfmas_capnp_schemas"),
]
Admin = capnp.load(module_file, imports=import_path).Admin
Registry = capnp.load(module_file, imports=import_path).Registry
Registrar = capnp.load(module_file, imports=import_path).Registrar

Admin.Server.AddcategoryResultTuple = NamedTuple(
    "AddcategoryResultTuple", [("success", object)]
)
Admin.Server.MoveobjectsResultTuple = NamedTuple(
    "MoveobjectsResultTuple", [("movedObjectIds", object)]
)
Admin.Server.RegistryResultTuple = NamedTuple("RegistryResultTuple", [])
Admin.Server.RemovecategoryResultTuple = NamedTuple(
    "RemovecategoryResultTuple", [("removedObjects", object)]
)
Admin.Server.RemoveobjectsResultTuple = NamedTuple(
    "RemoveobjectsResultTuple", [("removedObjects", object)]
)
Registrar.Server.RegisterResultTuple = NamedTuple(
    "RegisterResultTuple", [("unreg", object)]
)
Registrar.Unregister.Server.UnregisterResultTuple = NamedTuple(
    "UnregisterResultTuple", [("success", object)]
)
Registry.Server.CategoryinfoResultTuple = NamedTuple(
    "CategoryinfoResultTuple",
    [("id", object), ("name", object), ("description", object)],
)
Registry.Server.EntriesResultTuple = NamedTuple(
    "EntriesResultTuple", [("entries", object)]
)
Registry.Server.SupportedcategoriesResultTuple = NamedTuple(
    "SupportedcategoriesResultTuple", []
)
