@0xe14a1fcaee034d63;

using Cxx = import "/capnp/c++.capnp";
$Cxx.namespace("mas::schema::data");

using Go = import "/capnp/go.capnp";
$Go.package("data");
$Go.import("github.com/zalf-rpm/mas-infrastructure/capnproto_schemas/gen/go/data");

using Date = import "/date.capnp".Date;

struct WeatherStation {
  id                                      @0  :Text;            # WST_ID [text] weather station code
  name                                    @1  :Text;            # WST_NAME [text] weather station name
  instituteName                           @2  :Text;            # INST_NAME [text] institute name
  site                                    @3  :Text;            # WST_SITE [text] weather station site
  country                                 @4  :Text;            # WST_LOC_1 [text] weather station location country
  location2ndLevel                        @5  :Text;            # WST_LOC_2 [text] weather station location 2nd level
  location3rdLevel                        @6  :Text;            # WST_LOC_3 [text] weather station location 3rd level
  latitudeInDecDeg                        @7  :Float64 = -9999; # WST_LAT [decimal degrees] weather station latitude
  longitudeInDecDeg                       @8  :Float64 = -9999; # WST_LONG [decimal degrees] weather station longitude
  elevationM                              @9  :Float64 = -9999; # WST_ELEV [m] weather station elevation
  yearlyAvgTempInDegC                     @10 :Float64 = -9999; # TAV [°C] temperature avg year
  amplitudeOfMonthlyAvgTempsInDegC        @11 :Float64 = -9999; # TAMP [°C] temperature amplitude month avg
  tempSensorHeightInM                     @12 :Float64 = -1;    # REFHT [m] reference height weather measurement
  refHeightWeatherMeasurementInM          @13 :Float64 = -1;    # WNDHT [m] reference height windspeed measurement
  refHeightWindspeedMeasurementInM        @14 :Float64 = -1;    # TEMHT [m] temperature sensor height
  annualCO2ConcentrationInPPM             @15 :Float64 = -1;    # CO2Y [ppm] CO2 concentration annual
  notes                                   @16 :Text;            # WST_NOTES [text] weather notes
}

struct SoilMetadata {
  profileId                     @0  :Text;          # SOIL_ID [text] soil profile id
  name                          @1  :Text;          # SOIL_NAME [text] name of soil
  source                        @2  :Text;          # SL_SOURCE [text] soil source
  depthInCM                     @3  :Int16 = -1;    # SLDP [cm] soil depth
  obstableDepthInCM             @4  :Int16 = -1;    # SLOBS [cm] soil obstacle depth
  depthOfTopsoilInCM            @5  :Int16 = -1;    # SLTOP [cm] depth of topsoil
  drainageRatePerDay            @6  :Float64 = -1;  # SADR [1/day] drainage rate per day
  runoffCureNoSCS               @7  :Float64 = -1;  # SLRO [number] runoff curve no SCS
  soilAvailableWaterContentInCM @8  :Float64 = -1;  # SAWC [cm] soil available water content
  surfaceStoneCoverAsFraction   @9  :Float64 = -1;  # FLST [m2/m2] surface stones (cover)
  soilAlbedo                    @10 :Float64 = -1;  # SALB [] soil albedo
  soilEvaporationLimitInMM      @11 :Float64 = -1;  # SLU1 [mm] soil evaporation limit
  mineralizationFactor          @12 :Float64 = -1;  # SLNF [number] mineralization factor
  soilFertilityOnFoto           @13 :Float64 = -1;  # SLPF [number] soil fertility on foto
  soilClassificationSystem      @14 :Text;          # SL_SYSTEM [text] soil classification system
  soilTexture                   @15 :Text;          # SLTX [code] soil texture
  classification                @16 :Text;          # CLASSIFICATION [text] soil classification
  notes                         @17 :Text;          # SL_NOTES [text] soil notes
}

struct Field {
  id                            @0  :Text;            # FIELD_ID [text] field id
  name                          @1  :Text;            # FL_NAME [text] field name
  latitudeInDecDeg              @2  :Float64 = -9999; # FL_LAT[degree] field latitude
  longitudeInDecDeg             @3  :Float64 = -9999; # FL_LONG[degree] field longitude
  elevationInM                  @4  :Float64 = -9999; # FLELE [m] field elevation
  slopeDegreeInDeg              @5  :Float64 = -1;    # FLSL [degree angle] field slope
  drainageType                  @6  :Text;            # FL_DRNTYPE [code] drainage type
  distanceToWeatherStationInKM  @7  :Float64 = -1;    # WST_DIST [km] weather station distance
  country                       @8  :Text;            # FL_LOC_1 [text] field country
  subCountry                    @9  :Text;            # FL_LOC_2 [text] field sub country
  subSubCountry                 @10 :Text;            # FL_LOC_3 [text] field sub sub country
  notes                         @11 :Text;            # FL_NOTES [text] field notes
}

struct ExperimentDescription {
  id                              @0  :Text;        # EID [text] experiment id
  suiteId                         @1  :Text;        # SUITEID [text] suite id
  name                            @2  :Text;        # EXNAME [text] name of experiment
  researchInfrastructureName      @3  :Text;        # INFRANAME [text] research infrastructure name
  instituteName                   @4  :Text;        # INNAME [text] institute name
  researchUnitName                @5  :Text;        # RUNAME [text] research unit name
  experimentalFacilityName        @6  :Text;        # FANAME [text] experimental facility name
  siteName                        @7  :Text;        # SITE_NAME [text] site name
  siteType                        @8  :Text;        # SITE_TYPE [code] site type
  mainExperimentFactor            @9  :Text;        # MAIN_FACTOR [text] main experimental factor
  experimentalFactorCombinations  @10 :Text;        # FACTORS [text] experimental factor combinations
  experimentType                  @11 :Text;        # EXPER_TYPE [code] experiment type
  managementType                  @12 :Text;        # MGMT_TYPE [code] management type
  croppingSystem                  @13 :Text;        # CR_SYSTEM [text] cropping system
  plantingYear                    @14 :Int16 = -1;  # PLYR [year] planting year
  harvestOperationYear            @15 :Int16 = -1;  # HAYR [year] harvest operation year
  notes                           @16 :Text;        # EXP_NOTES [text] experiment notes
}

struct Treatment {
  id                              @0  :Text;      # TREAT_ID [text] treatment id
  experimentId                    @1  :Text;      # EID [text] experiment id
  fieldId                         @2  :Text;      # FIELD_ID [text] field id
  weatherStationId                @3  :Text;      # WST_ID [text] weather station code
  weatherStationDataset           @4  :Text;      # WST_DATASET [text] weather file
  name                            @5  :Text;      # TRT_NAME [text] treatment name
  simulationStartDate             @6  :Date;      # SDAT [date] simulation start date
  simulationEndDate               @7  :Date;      # ENDAT [date] simulation end date
  irrigationApplied               @8  :Bool;      # IRRIG [code] irrigatin applied
  fertilizerApplied               @9  :Bool;      # FERTILIZER [code] fertilizer applied
  irrigationLevel                 @10 :Int8 = -1; # IR [number] irrigation level
  fertilizerLevel                 @11 :Int8 = -1; # FE [number] fertilizer level
  plantingDateLevel               @12 :Int8 = -1; # PD [number] planting date level
  environmentalModificationsLevel @13 :Int8 = -1; # EM [number] environmental modifications level
  initialConditionsLevel          @14 :Int8 = -1; # IC [number] initial conditions level
  plantingDensityLevel            @15 :Int8 = -1; # PL [number] planting density level
  numberOfBlocksOrReplicates      @16 :Int8 = -1; # REP_NO [number] number of replicates
  notes                           @17 :Text;      # TR_NOTES [text] treatment comment
}

struct Cultivar {
  id                  @0  :Text;        # CUL_ID [text] cultivar identifier
  name                @1  :Text;        # CUL_NAME [text] cultivar name
  accessionId         @2  :Text;        # ACCES_ID [number] accession id
  accessionLocation   @3  :Text;        # ACCES_LOC [text] accession location
  cropIdentifierICASA @4  :Text;        # CRID [code] crop identifier ICASA
  seedLot             @5  :Text;        # SEED_LOT [text] seed lot
  breedingProgram     @6  :Text;        # BREED_PRG [text] breeding program
  originalName        @7  :Text;        # CUL_ORIG [text] cultivar name orig
  releaseYear         @8  :Int16 = -1;  # CUL_YEAR [year] cultivar release year
  synonym             @9  :Text;        # CUL_SYN [text] cultivar synonym
  notes               @10 :Text;        # CUL_NOTES [text] cultivar notes
}

struct Plot {
  id              @0  :Text;      # PLTID [text] plot id
  experimentId    @1  :Text;      # EID [text] experiment id
  treatmentId     @2  :Text;      # TREAT_ID [text] treatment id
  cultivarId      @3  :Text;      # CUL_ID [text] cultivar identifier
  soilId          @4  :Text;      # SOIL_ID [text] soil profile id
  blockNumber     @5  :Int8 = -1; # BLOCK [number] block number
  plotNumber      @6  :Int8 = -1; # PLOTno [number] plot number
  replicateNumber @7  :Int8 = -1; # RP [number] replicate number
  rowNumber       @8  :Int8 = -1; # PLOT_X [number] plot row number
  columnNumber    @9  :Int8 = -1; # PLOT_Y [number] plot column number
  harvestMethod   @10 :Text;      # PLTHM [code] harvest method plot
  notes           @11 :Text;      # PLOT_NOTES [text] plot notes
}

struct InitialConditionsLayer {
  experimentId            @0  :Text;          # EID [text] experiment id
  treatmentId             @1  :Text;          # TREAT_ID [text] treatment id
  date                    @2  :Date;          # ICDAT [date] initial conditions date
  soilLayerTopDepthInCM   @3  :Int16 = -1;    # ICTL [cm] soil layer top depth
  soilLayerBaseDepthInCM  @4  :Int16 = -1;    # ICBL [cm] soil layer base depth
  waterConcentration      @5  :Float64 = -1;  # ICH2O [mm3/mm3] initial water concentration by layer
  totalNInKGperHA         @6  :Float64 = -1;  # ICN_TOT [kg[N]/ha] initial Ntot layer
  massNH4InKGperHA        @7  :Float64 = -1;  # ICNH4M [kg[N]/ha] initial NH4 mass layer
  massNO3InKGperHA        @8  :Float64 = -1;  # ICNO3M [kg[N]/ha] initial NO3 mass layer
  concNH4InPPM            @9  :Float64 = -1;  # ICNH4 [ppm] initial NH4 concentration layer
  concNO3InPPM            @10 :Float64 = -1;  # ICNO3 [ppm] initial NO3 concentration layer
}

struct PlantingEvent {
  experimentId                                @0  :Text;            # EID [text] experiment id
  treatmentId                                 @1  :Text;            # TREAT_ID [text] treatment id
  plantingDistribution                        @2  :Text;            # PLDS [code] planting distribution
  rowSpacingInCM                              @3  :Float64 = -1;    # PLRS [cm] row spacing
  rowDirectionInArcDeg                        @4  :Float64 = -9999; # PLRD [arc degrees] row direction
  plantingDepthInMM                           @5  :Int16 = -1;      # PLDP [mm] planting depth
  plotLayout                                  @6  :Text;            # PLLAY [text] plot layout
  plantingDate                                @7  :Date;            # PDATE [date] planting date
  plantPopulationAtPlantingInNoPerM2          @8  :Int16 = -1;      # PLPOP [number/m2] plant population at planting
  averageEmergenceDate                        @9  :Date;            # APLDAE [date] average emergence date
  averagePlantPopulationAtEmergenceInNoPerM2  @10 :Int16 = -1;      # APLPOE [number/m2] average plant population at emergence
  notes                                       @11 :Text;            # PL_NOTES [text] planting notes
}

struct HarvestEvent {
  experimentId  @0 :Text;         # EID[text] experiment id
  treatmentId   @1 :Text;         # TREAT_ID [text] tre atment id
  date          @2 :Date;         # HADAT [date] harvest operations date
  harvestMethod @3 :Text;         # HARM [code] harvest method
  harvestArea   @4 :Float64 = -1; # HAREA [cm2] harvest area
  notes         @5 :Text;         # HA_NOTES [text] harvest notes
  comments      @6 :Text;         # HA_COMMENTS[text] harvest comments
}

struct IrrigationEvent {
  experimentId              @0 :Text; # EID [text] experiment id
  treatmentId               @1 :Text; # TREAT_ID [text] treatment id
  date                      @2 :Date; # IDATE [date] irrigation date
  operation                 @3 :Text; # IROP [code] irrigation operation
  applicationDepth          @4 :Int16 = -9999; # IRADP [cm] irrigation application depth
  amount                    @5 :Int16 = -1; # IRVAL [mm] irrigation amount
  waterNConcentrationInPerc @6 :Float64 = -1; # IRNPC [%] irrigation H2O N concentration
  notes                     @7 :Text; # IR_NOTES [text] irrigation notes
}

struct FertilizerEvent {
  experimentId          @0 :Text;       # EID [text] experiment id
  treatmentId           @1 :Text;       # TREAT_ID [text] treatment id
  date                  @2 :Date;       # FEDATE [date] fertilization date
  applicationMethod     @3 :Text;       # FEACD [code] fertilizer application method
  applicationDepthInCM  @4 :Int16 = -1; # FEDEP [cm] application depth fertilizer
  material              @5 :Text;       # FECD [code] fertilizer material
  appliedNInKGNPerHA    @6 :Int16 = -1; # FEAMN [kg[N]/ha] N in applied fertilizer
  appliedNO3InKGNperHA  @7 :Int16 = -1; # FENO3 [kg[N]/ha] NO3 in applied fertilizer
  appliedNH4InKGNperHA  @8 :Int16 = -1; # FENH4 [kg[N]/ha] NH4 in applied fertilizer
  notes                 @9 :Text;       # FE_NOTES [text] fertilizer notes
}

struct Residue {
  experimentId                    @0 :Text;         # EID [text] experiment id
  treatmentId                     @1 :Text;         # TREAT_ID [text] treatment id
  initialMeasureDate              @2 :Date;         # ICRDAT [date] initial residue measure date
  incorporationDepth              @3 :Int16 = -1;   # ICRDP [cm] residue incorporation depth
  percentIncorporated             @4 :Float64 = -1; # ICRIP [%] residue incorporated
  prevCropCode                    @5 :Text;         # ICPCR [code] residue nature prev crop
  aboveGroundWeight               @6 :Float64 = -1; # ICRAG [kg[dry matter]/ha] residue above-ground weight
  aboveGroundNConcentrationInPerc @7 :Float64 = -1; # ICRN [%] residue above-ground N concentration
  rootWeightPreviousCrop          @8 :Float64 = -1; # ICRT [kg[dry matter]/ha] root weight previous crop
}

struct EnvironmentModification {
  experimentId  @0 :Text;       # EID [text] experiment id
  treatmentId   @1 :Text;       # TREAT_ID [text] treatment id
  date          @2 :Date;       # EMDATE [date] environment modification date
  codeCO2       @3 :Text;       # ECCO2 [code] environment modification code CO2
  valueCO2      @4 :Int16 = -1; # EMCO2 [ppm] environment modification CO2
  notes         @5 :Text;       # EM_NOTES [text] environment modification notes
}
