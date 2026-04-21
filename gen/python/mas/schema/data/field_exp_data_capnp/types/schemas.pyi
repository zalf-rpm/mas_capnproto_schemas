"""Schema helper types for `field_exp_data.capnp`."""

from mas.schema.data.field_exp_data_capnp.types import modules as modules

type _CultivarSchema = modules._CultivarStructModule._CultivarSchema

type _EnvironmentModificationSchema = (
    modules._EnvironmentModificationStructModule._EnvironmentModificationSchema
)

type _ExperimentDescriptionSchema = (
    modules._ExperimentDescriptionStructModule._ExperimentDescriptionSchema
)

type _FertilizerEventSchema = (
    modules._FertilizerEventStructModule._FertilizerEventSchema
)

type _FieldSchema = modules._FieldStructModule._FieldSchema

type _HarvestEventSchema = modules._HarvestEventStructModule._HarvestEventSchema

type _InitialConditionsLayerSchema = (
    modules._InitialConditionsLayerStructModule._InitialConditionsLayerSchema
)

type _IrrigationEventSchema = (
    modules._IrrigationEventStructModule._IrrigationEventSchema
)

type _PlantingEventSchema = modules._PlantingEventStructModule._PlantingEventSchema

type _PlotSchema = modules._PlotStructModule._PlotSchema

type _ResidueSchema = modules._ResidueStructModule._ResidueSchema

type _SoilMetadataSchema = modules._SoilMetadataStructModule._SoilMetadataSchema

type _TreatmentSchema = modules._TreatmentStructModule._TreatmentSchema

type _WeatherStationSchema = modules._WeatherStationStructModule._WeatherStationSchema
