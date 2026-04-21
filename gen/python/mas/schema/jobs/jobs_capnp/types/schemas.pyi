"""Schema helper types for `jobs.capnp`."""

from mas.schema.jobs.jobs_capnp.types import modules as modules

type _JobSchema = modules._JobStructModule._JobSchema

type _ServiceSchema = modules._ServiceInterfaceModule._ServiceSchema
