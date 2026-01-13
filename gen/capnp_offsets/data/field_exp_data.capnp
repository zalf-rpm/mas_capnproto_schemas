# data/field_exp_data.capnp
@0xe14a1fcaee034d63;
$import "/capnp/c++.capnp".namespace("mas::schema::data");
$import "/capnp/python.capnp".module("mas.schema.data");
$import "/capnp/go.capnp".package("data");
$import "/capnp/go.capnp".import("github.com/zalf-rpm/mas_capnproto_schemas/gen/go/data");
struct WeatherStation @0xbfa2d703516408b8 {  # 72 bytes, 8 ptrs
  id @0 :Text;  # ptr[0]
  name @1 :Text;  # ptr[1]
  instituteName @2 :Text;  # ptr[2]
  site @3 :Text;  # ptr[3]
  country @4 :Text;  # ptr[4]
  location2ndLevel @5 :Text;  # ptr[5]
  location3rdLevel @6 :Text;  # ptr[6]
  latitudeInDecDeg @7 :Float64 = -9999;  # bits[0, 64)
  longitudeInDecDeg @8 :Float64 = -9999;  # bits[64, 128)
  elevationM @9 :Float64 = -9999;  # bits[128, 192)
  yearlyAvgTempInDegC @10 :Float64 = -9999;  # bits[192, 256)
  amplitudeOfMonthlyAvgTempsInDegC @11 :Float64 = -9999;  # bits[256, 320)
  tempSensorHeightInM @12 :Float64 = -1;  # bits[320, 384)
  refHeightWeatherMeasurementInM @13 :Float64 = -1;  # bits[384, 448)
  refHeightWindspeedMeasurementInM @14 :Float64 = -1;  # bits[448, 512)
  annualCO2ConcentrationInPPM @15 :Float64 = -1;  # bits[512, 576)
  notes @16 :Text;  # ptr[7]
}
struct SoilMetadata @0x86836f1366e5f73f {  # 72 bytes, 8 ptrs
  id @0 :Text;  # ptr[0]
  name @1 :Text;  # ptr[1]
  source @2 :Text;  # ptr[2]
  depthInCM @3 :Int16 = -1;  # bits[0, 16)
  obstableDepthInCM @4 :Int16 = -1;  # bits[16, 32)
  depthOfTopsoilInCM @5 :Int16 = -1;  # bits[32, 48)
  drainageRatePerDay @6 :Float64 = -1;  # bits[64, 128)
  runoffCureNoSCS @7 :Float64 = -1;  # bits[128, 192)
  soilAvailableWaterContentInCM @8 :Float64 = -1;  # bits[192, 256)
  surfaceStoneCoverAsFraction @9 :Float64 = -1;  # bits[256, 320)
  soilAlbedo @10 :Float64 = -1;  # bits[320, 384)
  soilEvaporationLimitInMM @11 :Float64 = -1;  # bits[384, 448)
  mineralizationFactor @12 :Float64 = -1;  # bits[448, 512)
  soilFertilityOnFoto @13 :Float64 = -1;  # bits[512, 576)
  soilClassificationSystem @14 :Text;  # ptr[3]
  soilTexture @15 :Text;  # ptr[4]
  classification @16 :Text;  # ptr[5]
  notes @17 :Text;  # ptr[6]
  profile @18 :import "/soil/soil.capnp".Profile;  # ptr[7]
}
struct Field @0xc158bd732092cde5 {  # 40 bytes, 7 ptrs
  id @0 :Text;  # ptr[0]
  name @1 :Text;  # ptr[1]
  latitudeInDecDeg @2 :Float64 = -9999;  # bits[0, 64)
  longitudeInDecDeg @3 :Float64 = -9999;  # bits[64, 128)
  elevationInM @4 :Float64 = -9999;  # bits[128, 192)
  slopeDegreeInDeg @5 :Float64 = -1;  # bits[192, 256)
  drainageType @6 :Text;  # ptr[2]
  distanceToWeatherStationInKM @7 :Float64 = -1;  # bits[256, 320)
  country @8 :Text;  # ptr[3]
  subCountry @9 :Text;  # ptr[4]
  subSubCountry @10 :Text;  # ptr[5]
  notes @11 :Text;  # ptr[6]
}
struct ExperimentDescription @0x9d795a72a27f67d7 {  # 8 bytes, 16 ptrs
  id @0 :Text;  # ptr[0]
  suiteId @1 :Text;  # ptr[1]
  name @2 :Text;  # ptr[2]
  researchInfrastructureName @3 :Text;  # ptr[3]
  instituteName @4 :Text;  # ptr[4]
  researchUnitName @5 :Text;  # ptr[5]
  experimentalFacilityName @6 :Text;  # ptr[6]
  siteName @7 :Text;  # ptr[7]
  siteType @8 :Text;  # ptr[8]
  mainExperimentFactor @9 :Text;  # ptr[9]
  experimentalFactorCombinations @10 :Text;  # ptr[10]
  experimentType @11 :Text;  # ptr[11]
  managementType @12 :Text;  # ptr[12]
  croppingSystem @13 :Text;  # ptr[13]
  plantingYear @14 :Int16 = -1;  # bits[0, 16)
  harvestOperationYear @15 :Int16 = -1;  # bits[16, 32)
  notes @16 :Text;  # ptr[14]
  treatments @17 :List(Treatment);  # ptr[15]
}
struct Treatment @0xff1381363c7abd06 {  # 8 bytes, 20 ptrs
  id @0 :Text;  # ptr[0]
  experimentId @25 :Text;  # ptr[16]
  fieldId @26 :Text;  # ptr[17]
  field @1 :Field;  # ptr[1]
  weatherStationId @27 :Text;  # ptr[18]
  weatherStation @2 :WeatherStation;  # ptr[2]
  weatherStationDataset @28 :Text;  # ptr[19]
  weatherStationTimeseries @3 :import "/climate/climate.capnp".TimeSeries;  # ptr[3]
  name @4 :Text;  # ptr[4]
  simulationStartDate @5 :import "/common/date.capnp".Date;  # ptr[5]
  simulationEndDate @6 :import "/common/date.capnp".Date;  # ptr[6]
  irrigationApplied @7 :Bool;  # bits[0, 1)
  fertilizerApplied @8 :Bool;  # bits[1, 2)
  irrigationLevel @9 :Int8 = -1;  # bits[8, 16)
  fertilizerLevel @10 :Int8 = -1;  # bits[16, 24)
  plantingDateLevel @11 :Int8 = -1;  # bits[24, 32)
  environmentalModificationsLevel @12 :Int8 = -1;  # bits[32, 40)
  initialConditionsLevel @13 :Int8 = -1;  # bits[40, 48)
  plantingDensityLevel @14 :Int8 = -1;  # bits[48, 56)
  numberOfBlocksOrReplicates @15 :Int8 = -1;  # bits[56, 64)
  notes @16 :Text;  # ptr[7]
  plots @17 :List(Plot);  # ptr[8]
  residue @18 :Residue;  # ptr[9]
  initialConditionsLayers @19 :List(InitialConditionsLayer);  # ptr[10]
  plantingEvents @20 :List(PlantingEvent);  # ptr[11]
  harvestEvents @21 :List(HarvestEvent);  # ptr[12]
  irrigationEvents @22 :List(IrrigationEvent);  # ptr[13]
  fertilizerEvents @23 :List(FertilizerEvent);  # ptr[14]
  environmentModifications @24 :List(EnvironmentModification);  # ptr[15]
}
struct Cultivar @0xab7ea2bfa7965af8 {  # 8 bytes, 10 ptrs
  id @0 :Text;  # ptr[0]
  name @1 :Text;  # ptr[1]
  accessionId @2 :Text;  # ptr[2]
  accessionLocation @3 :Text;  # ptr[3]
  cropIdentifierICASA @4 :Text;  # ptr[4]
  seedLot @5 :Text;  # ptr[5]
  breedingProgram @6 :Text;  # ptr[6]
  originalName @7 :Text;  # ptr[7]
  releaseYear @8 :Int16 = -1;  # bits[0, 16)
  synonym @9 :Text;  # ptr[8]
  notes @10 :Text;  # ptr[9]
}
struct Plot @0xa7a2210fb1e289f2 {  # 8 bytes, 9 ptrs
  id @0 :Text;  # ptr[0]
  experimentId @10 :Text;  # ptr[5]
  treatmentId @11 :Text;  # ptr[6]
  cultivarId @12 :Text;  # ptr[7]
  cultivar @1 :Cultivar;  # ptr[1]
  soilId @13 :Text;  # ptr[8]
  soil @2 :SoilMetadata;  # ptr[2]
  blockNumber @3 :Int8 = -1;  # bits[0, 8)
  plotNumber @4 :Int8 = -1;  # bits[8, 16)
  replicateNumber @5 :Int8 = -1;  # bits[16, 24)
  rowNumber @6 :Int8 = -1;  # bits[24, 32)
  columnNumber @7 :Int8 = -1;  # bits[32, 40)
  harvestMethod @8 :Text;  # ptr[3]
  notes @9 :Text;  # ptr[4]
}
struct InitialConditionsLayer @0xd1c0bc9f5b332a6e {  # 56 bytes, 3 ptrs
  experimentId @9 :Text;  # ptr[1]
  treatmentId @10 :Text;  # ptr[2]
  date @0 :import "/common/date.capnp".Date;  # ptr[0]
  soilLayerTopDepthInCM @1 :Int16 = -1;  # bits[0, 16)
  soilLayerBaseDepthInCM @2 :Int16 = -1;  # bits[16, 32)
  waterConcentration @3 :Float64 = -1;  # bits[64, 128)
  totalNInKGperHA @4 :Float64 = -1;  # bits[128, 192)
  massNH4InKGperHA @5 :Float64 = -1;  # bits[192, 256)
  massNO3InKGperHA @6 :Float64 = -1;  # bits[256, 320)
  concNH4InPPM @7 :Float64 = -1;  # bits[320, 384)
  concNO3InPPM @8 :Float64 = -1;  # bits[384, 448)
}
struct PlantingEvent @0xf6b17c769768d8ff {  # 24 bytes, 7 ptrs
  experimentId @10 :Text;  # ptr[5]
  treatmentId @11 :Text;  # ptr[6]
  plantingDistribution @0 :Text;  # ptr[0]
  rowSpacingInCM @1 :Float64 = -1;  # bits[0, 64)
  rowDirectionInArcDeg @2 :Float64 = -9999;  # bits[64, 128)
  plantingDepthInMM @3 :Int16 = -1;  # bits[128, 144)
  plotLayout @4 :Text;  # ptr[1]
  plantingDate @5 :import "/common/date.capnp".Date;  # ptr[2]
  plantPopulationAtPlantingInNoPerM2 @6 :Int16 = -1;  # bits[144, 160)
  averageEmergenceDate @7 :import "/common/date.capnp".Date;  # ptr[3]
  averagePlantPopulationAtEmergenceInNoPerM2 @8 :Int16 = -1;  # bits[160, 176)
  notes @9 :Text;  # ptr[4]
}
struct HarvestEvent @0x97eb30dbcf87911a {  # 8 bytes, 6 ptrs
  experimentId @5 :Text;  # ptr[4]
  treatmentId @6 :Text;  # ptr[5]
  date @0 :import "/common/date.capnp".Date;  # ptr[0]
  harvestMethod @1 :Text;  # ptr[1]
  harvestArea @2 :Float64 = -1;  # bits[0, 64)
  notes @3 :Text;  # ptr[2]
  comments @4 :Text;  # ptr[3]
}
struct IrrigationEvent @0xcf2547b626594655 {  # 16 bytes, 5 ptrs
  experimentId @6 :Text;  # ptr[3]
  treatmentId @7 :Text;  # ptr[4]
  date @0 :import "/common/date.capnp".Date;  # ptr[0]
  operation @1 :Text;  # ptr[1]
  applicationDepth @2 :Int16 = -9999;  # bits[0, 16)
  amount @3 :Int16 = -1;  # bits[16, 32)
  waterNConcentrationInPerc @4 :Float64 = -1;  # bits[64, 128)
  notes @5 :Text;  # ptr[2]
}
struct FertilizerEvent @0xa5df81bae928e6da {  # 8 bytes, 6 ptrs
  experimentId @8 :Text;  # ptr[4]
  treatmentId @9 :Text;  # ptr[5]
  date @0 :import "/common/date.capnp".Date;  # ptr[0]
  applicationMethod @1 :Text;  # ptr[1]
  applicationDepthInCM @2 :Int16 = -1;  # bits[0, 16)
  material @3 :Text;  # ptr[2]
  appliedNInKGNPerHA @4 :Int16 = -1;  # bits[16, 32)
  appliedNO3InKGNperHA @5 :Int16 = -1;  # bits[32, 48)
  appliedNH4InKGNperHA @6 :Int16 = -1;  # bits[48, 64)
  notes @7 :Text;  # ptr[3]
}
struct Residue @0xe82432f4ef15a586 {  # 40 bytes, 4 ptrs
  experimentId @7 :Text;  # ptr[2]
  treatmentId @8 :Text;  # ptr[3]
  initialMeasureDate @0 :import "/common/date.capnp".Date;  # ptr[0]
  incorporationDepth @1 :Int16 = -1;  # bits[0, 16)
  percentIncorporated @2 :Float64 = -1;  # bits[64, 128)
  prevCropCode @3 :Text;  # ptr[1]
  aboveGroundWeight @4 :Float64 = -1;  # bits[128, 192)
  aboveGroundNConcentrationInPerc @5 :Float64 = -1;  # bits[192, 256)
  rootWeightPreviousCrop @6 :Float64 = -1;  # bits[256, 320)
}
struct EnvironmentModification @0xb52867725b843050 {  # 8 bytes, 5 ptrs
  experimentId @4 :Text;  # ptr[3]
  treatmentId @5 :Text;  # ptr[4]
  date @0 :import "/common/date.capnp".Date;  # ptr[0]
  codeCO2 @1 :Text;  # ptr[1]
  valueCO2 @2 :Int16 = -1;  # bits[0, 16)
  notes @3 :Text;  # ptr[2]
}
