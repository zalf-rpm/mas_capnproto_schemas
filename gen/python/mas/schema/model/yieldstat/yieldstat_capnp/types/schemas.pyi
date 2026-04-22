"""Schema helper types for `yieldstat.capnp`."""

from mas.schema.model.yieldstat.yieldstat_capnp.types import modules as modules

type _OutputSchema = modules._OutputStructModule._OutputSchema

type _OutputYearToResultSchema = (
    modules._OutputStructModule._YearToResultStructModule._YearToResultSchema
)

type _RestInputSchema = modules._RestInputStructModule._RestInputSchema

type _ResultIdEnumSchema = modules._ResultIdEnumModule._ResultIdSchema

type _ResultResultToValueSchema = (
    modules._ResultStructModule._ResultToValueStructModule._ResultToValueSchema
)

type _ResultSchema = modules._ResultStructModule._ResultSchema
