"""This is an automatically generated stub for `soil.capnp`."""

import os

import capnp

capnp.remove_import_hook()
here = os.path.dirname(os.path.abspath(__file__))
module_file = os.path.abspath(
    os.path.join(here, "../../zalfmas_capnp_schemas/soil.capnp")
)
import_path = [
    here,
    os.path.join(here, "../../zalfmas_capnp_schemas"),
    os.path.join(here, "../../zalfmas_capnp_schemas"),
]
Layer = capnp.load(module_file, imports=import_path).Layer
LayerBuilder = Layer
LayerReader = Layer
Query = capnp.load(module_file, imports=import_path).Query
QueryBuilder = Query
QueryReader = Query
ProfileData = capnp.load(module_file, imports=import_path).ProfileData
ProfileDataBuilder = ProfileData
ProfileDataReader = ProfileData
Profile = capnp.load(module_file, imports=import_path).Profile
ProfileBuilder = Profile
ProfileReader = Profile
Service = capnp.load(module_file, imports=import_path).Service
ServiceBuilder = Service
ServiceReader = Service
