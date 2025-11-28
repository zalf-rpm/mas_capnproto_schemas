using System;
using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;
using Capnp;
using Capnp.Rpc;

namespace Mas.Schema.Data
{
    [
        System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"),
        TypeId(0xbfa2d703516408b8UL)
    ]
    public class WeatherStation : ICapnpSerializable
    {
        public const UInt64 typeId = 0xbfa2d703516408b8UL;

        void ICapnpSerializable.Deserialize(DeserializerState arg_)
        {
            var reader = READER.create(arg_);
            Id = reader.Id;
            Name = reader.Name;
            InstituteName = reader.InstituteName;
            Site = reader.Site;
            Country = reader.Country;
            Location2ndLevel = reader.Location2ndLevel;
            Location3rdLevel = reader.Location3rdLevel;
            LatitudeInDecDeg = reader.LatitudeInDecDeg;
            LongitudeInDecDeg = reader.LongitudeInDecDeg;
            ElevationM = reader.ElevationM;
            YearlyAvgTempInDegC = reader.YearlyAvgTempInDegC;
            AmplitudeOfMonthlyAvgTempsInDegC = reader.AmplitudeOfMonthlyAvgTempsInDegC;
            TempSensorHeightInM = reader.TempSensorHeightInM;
            RefHeightWeatherMeasurementInM = reader.RefHeightWeatherMeasurementInM;
            RefHeightWindspeedMeasurementInM = reader.RefHeightWindspeedMeasurementInM;
            AnnualCO2ConcentrationInPPM = reader.AnnualCO2ConcentrationInPPM;
            Notes = reader.Notes;
            applyDefaults();
        }

        public void serialize(WRITER writer)
        {
            writer.Id = Id;
            writer.Name = Name;
            writer.InstituteName = InstituteName;
            writer.Site = Site;
            writer.Country = Country;
            writer.Location2ndLevel = Location2ndLevel;
            writer.Location3rdLevel = Location3rdLevel;
            writer.LatitudeInDecDeg = LatitudeInDecDeg;
            writer.LongitudeInDecDeg = LongitudeInDecDeg;
            writer.ElevationM = ElevationM;
            writer.YearlyAvgTempInDegC = YearlyAvgTempInDegC;
            writer.AmplitudeOfMonthlyAvgTempsInDegC = AmplitudeOfMonthlyAvgTempsInDegC;
            writer.TempSensorHeightInM = TempSensorHeightInM;
            writer.RefHeightWeatherMeasurementInM = RefHeightWeatherMeasurementInM;
            writer.RefHeightWindspeedMeasurementInM = RefHeightWindspeedMeasurementInM;
            writer.AnnualCO2ConcentrationInPPM = AnnualCO2ConcentrationInPPM;
            writer.Notes = Notes;
        }

        void ICapnpSerializable.Serialize(SerializerState arg_)
        {
            serialize(arg_.Rewrap<WRITER>());
        }

        public void applyDefaults() { }

        public string Id { get; set; }

        public string Name { get; set; }

        public string InstituteName { get; set; }

        public string Site { get; set; }

        public string Country { get; set; }

        public string Location2ndLevel { get; set; }

        public string Location3rdLevel { get; set; }

        public double LatitudeInDecDeg { get; set; } = -9999;
        public double LongitudeInDecDeg { get; set; } = -9999;
        public double ElevationM { get; set; } = -9999;
        public double YearlyAvgTempInDegC { get; set; } = -9999;
        public double AmplitudeOfMonthlyAvgTempsInDegC { get; set; } = -9999;
        public double TempSensorHeightInM { get; set; } = -1;
        public double RefHeightWeatherMeasurementInM { get; set; } = -1;
        public double RefHeightWindspeedMeasurementInM { get; set; } = -1;
        public double AnnualCO2ConcentrationInPPM { get; set; } = -1;
        public string Notes { get; set; }

        public struct READER
        {
            readonly DeserializerState ctx;

            public READER(DeserializerState ctx)
            {
                this.ctx = ctx;
            }

            public static READER create(DeserializerState ctx) => new READER(ctx);

            public static implicit operator DeserializerState(READER reader) => reader.ctx;

            public static implicit operator READER(DeserializerState ctx) => new READER(ctx);

            public string Id => ctx.ReadText(0, null);
            public string Name => ctx.ReadText(1, null);
            public string InstituteName => ctx.ReadText(2, null);
            public string Site => ctx.ReadText(3, null);
            public string Country => ctx.ReadText(4, null);
            public string Location2ndLevel => ctx.ReadText(5, null);
            public string Location3rdLevel => ctx.ReadText(6, null);
            public double LatitudeInDecDeg => ctx.ReadDataDouble(0UL, -9999);
            public double LongitudeInDecDeg => ctx.ReadDataDouble(64UL, -9999);
            public double ElevationM => ctx.ReadDataDouble(128UL, -9999);
            public double YearlyAvgTempInDegC => ctx.ReadDataDouble(192UL, -9999);
            public double AmplitudeOfMonthlyAvgTempsInDegC => ctx.ReadDataDouble(256UL, -9999);
            public double TempSensorHeightInM => ctx.ReadDataDouble(320UL, -1);
            public double RefHeightWeatherMeasurementInM => ctx.ReadDataDouble(384UL, -1);
            public double RefHeightWindspeedMeasurementInM => ctx.ReadDataDouble(448UL, -1);
            public double AnnualCO2ConcentrationInPPM => ctx.ReadDataDouble(512UL, -1);
            public string Notes => ctx.ReadText(7, null);
        }

        public class WRITER : SerializerState
        {
            public WRITER()
            {
                this.SetStruct(9, 8);
            }

            public string Id
            {
                get => this.ReadText(0, null);
                set => this.WriteText(0, value, null);
            }

            public string Name
            {
                get => this.ReadText(1, null);
                set => this.WriteText(1, value, null);
            }

            public string InstituteName
            {
                get => this.ReadText(2, null);
                set => this.WriteText(2, value, null);
            }

            public string Site
            {
                get => this.ReadText(3, null);
                set => this.WriteText(3, value, null);
            }

            public string Country
            {
                get => this.ReadText(4, null);
                set => this.WriteText(4, value, null);
            }

            public string Location2ndLevel
            {
                get => this.ReadText(5, null);
                set => this.WriteText(5, value, null);
            }

            public string Location3rdLevel
            {
                get => this.ReadText(6, null);
                set => this.WriteText(6, value, null);
            }

            public double LatitudeInDecDeg
            {
                get => this.ReadDataDouble(0UL, -9999);
                set => this.WriteData(0UL, value, -9999);
            }

            public double LongitudeInDecDeg
            {
                get => this.ReadDataDouble(64UL, -9999);
                set => this.WriteData(64UL, value, -9999);
            }

            public double ElevationM
            {
                get => this.ReadDataDouble(128UL, -9999);
                set => this.WriteData(128UL, value, -9999);
            }

            public double YearlyAvgTempInDegC
            {
                get => this.ReadDataDouble(192UL, -9999);
                set => this.WriteData(192UL, value, -9999);
            }

            public double AmplitudeOfMonthlyAvgTempsInDegC
            {
                get => this.ReadDataDouble(256UL, -9999);
                set => this.WriteData(256UL, value, -9999);
            }

            public double TempSensorHeightInM
            {
                get => this.ReadDataDouble(320UL, -1);
                set => this.WriteData(320UL, value, -1);
            }

            public double RefHeightWeatherMeasurementInM
            {
                get => this.ReadDataDouble(384UL, -1);
                set => this.WriteData(384UL, value, -1);
            }

            public double RefHeightWindspeedMeasurementInM
            {
                get => this.ReadDataDouble(448UL, -1);
                set => this.WriteData(448UL, value, -1);
            }

            public double AnnualCO2ConcentrationInPPM
            {
                get => this.ReadDataDouble(512UL, -1);
                set => this.WriteData(512UL, value, -1);
            }

            public string Notes
            {
                get => this.ReadText(7, null);
                set => this.WriteText(7, value, null);
            }
        }
    }

    [
        System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"),
        TypeId(0x86836f1366e5f73fUL)
    ]
    public class SoilMetadata : ICapnpSerializable
    {
        public const UInt64 typeId = 0x86836f1366e5f73fUL;

        void ICapnpSerializable.Deserialize(DeserializerState arg_)
        {
            var reader = READER.create(arg_);
            Id = reader.Id;
            Name = reader.Name;
            Source = reader.Source;
            DepthInCM = reader.DepthInCM;
            ObstableDepthInCM = reader.ObstableDepthInCM;
            DepthOfTopsoilInCM = reader.DepthOfTopsoilInCM;
            DrainageRatePerDay = reader.DrainageRatePerDay;
            RunoffCureNoSCS = reader.RunoffCureNoSCS;
            SoilAvailableWaterContentInCM = reader.SoilAvailableWaterContentInCM;
            SurfaceStoneCoverAsFraction = reader.SurfaceStoneCoverAsFraction;
            SoilAlbedo = reader.SoilAlbedo;
            SoilEvaporationLimitInMM = reader.SoilEvaporationLimitInMM;
            MineralizationFactor = reader.MineralizationFactor;
            SoilFertilityOnFoto = reader.SoilFertilityOnFoto;
            SoilClassificationSystem = reader.SoilClassificationSystem;
            SoilTexture = reader.SoilTexture;
            Classification = reader.Classification;
            Notes = reader.Notes;
            Profile = reader.Profile;
            applyDefaults();
        }

        public void serialize(WRITER writer)
        {
            writer.Id = Id;
            writer.Name = Name;
            writer.Source = Source;
            writer.DepthInCM = DepthInCM;
            writer.ObstableDepthInCM = ObstableDepthInCM;
            writer.DepthOfTopsoilInCM = DepthOfTopsoilInCM;
            writer.DrainageRatePerDay = DrainageRatePerDay;
            writer.RunoffCureNoSCS = RunoffCureNoSCS;
            writer.SoilAvailableWaterContentInCM = SoilAvailableWaterContentInCM;
            writer.SurfaceStoneCoverAsFraction = SurfaceStoneCoverAsFraction;
            writer.SoilAlbedo = SoilAlbedo;
            writer.SoilEvaporationLimitInMM = SoilEvaporationLimitInMM;
            writer.MineralizationFactor = MineralizationFactor;
            writer.SoilFertilityOnFoto = SoilFertilityOnFoto;
            writer.SoilClassificationSystem = SoilClassificationSystem;
            writer.SoilTexture = SoilTexture;
            writer.Classification = Classification;
            writer.Notes = Notes;
            writer.Profile = Profile;
        }

        void ICapnpSerializable.Serialize(SerializerState arg_)
        {
            serialize(arg_.Rewrap<WRITER>());
        }

        public void applyDefaults() { }

        public string Id { get; set; }

        public string Name { get; set; }

        public string Source { get; set; }

        public short DepthInCM { get; set; } = -1;
        public short ObstableDepthInCM { get; set; } = -1;
        public short DepthOfTopsoilInCM { get; set; } = -1;
        public double DrainageRatePerDay { get; set; } = -1;
        public double RunoffCureNoSCS { get; set; } = -1;
        public double SoilAvailableWaterContentInCM { get; set; } = -1;
        public double SurfaceStoneCoverAsFraction { get; set; } = -1;
        public double SoilAlbedo { get; set; } = -1;
        public double SoilEvaporationLimitInMM { get; set; } = -1;
        public double MineralizationFactor { get; set; } = -1;
        public double SoilFertilityOnFoto { get; set; } = -1;
        public string SoilClassificationSystem { get; set; }

        public string SoilTexture { get; set; }

        public string Classification { get; set; }

        public string Notes { get; set; }

        public Mas.Schema.Soil.IProfile Profile { get; set; }

        public struct READER
        {
            readonly DeserializerState ctx;

            public READER(DeserializerState ctx)
            {
                this.ctx = ctx;
            }

            public static READER create(DeserializerState ctx) => new READER(ctx);

            public static implicit operator DeserializerState(READER reader) => reader.ctx;

            public static implicit operator READER(DeserializerState ctx) => new READER(ctx);

            public string Id => ctx.ReadText(0, null);
            public string Name => ctx.ReadText(1, null);
            public string Source => ctx.ReadText(2, null);
            public short DepthInCM => ctx.ReadDataShort(0UL, (short)-1);
            public short ObstableDepthInCM => ctx.ReadDataShort(16UL, (short)-1);
            public short DepthOfTopsoilInCM => ctx.ReadDataShort(32UL, (short)-1);
            public double DrainageRatePerDay => ctx.ReadDataDouble(64UL, -1);
            public double RunoffCureNoSCS => ctx.ReadDataDouble(128UL, -1);
            public double SoilAvailableWaterContentInCM => ctx.ReadDataDouble(192UL, -1);
            public double SurfaceStoneCoverAsFraction => ctx.ReadDataDouble(256UL, -1);
            public double SoilAlbedo => ctx.ReadDataDouble(320UL, -1);
            public double SoilEvaporationLimitInMM => ctx.ReadDataDouble(384UL, -1);
            public double MineralizationFactor => ctx.ReadDataDouble(448UL, -1);
            public double SoilFertilityOnFoto => ctx.ReadDataDouble(512UL, -1);
            public string SoilClassificationSystem => ctx.ReadText(3, null);
            public string SoilTexture => ctx.ReadText(4, null);
            public string Classification => ctx.ReadText(5, null);
            public string Notes => ctx.ReadText(6, null);
            public Mas.Schema.Soil.IProfile Profile => ctx.ReadCap<Mas.Schema.Soil.IProfile>(7);
        }

        public class WRITER : SerializerState
        {
            public WRITER()
            {
                this.SetStruct(9, 8);
            }

            public string Id
            {
                get => this.ReadText(0, null);
                set => this.WriteText(0, value, null);
            }

            public string Name
            {
                get => this.ReadText(1, null);
                set => this.WriteText(1, value, null);
            }

            public string Source
            {
                get => this.ReadText(2, null);
                set => this.WriteText(2, value, null);
            }

            public short DepthInCM
            {
                get => this.ReadDataShort(0UL, (short)-1);
                set => this.WriteData(0UL, value, (short)-1);
            }

            public short ObstableDepthInCM
            {
                get => this.ReadDataShort(16UL, (short)-1);
                set => this.WriteData(16UL, value, (short)-1);
            }

            public short DepthOfTopsoilInCM
            {
                get => this.ReadDataShort(32UL, (short)-1);
                set => this.WriteData(32UL, value, (short)-1);
            }

            public double DrainageRatePerDay
            {
                get => this.ReadDataDouble(64UL, -1);
                set => this.WriteData(64UL, value, -1);
            }

            public double RunoffCureNoSCS
            {
                get => this.ReadDataDouble(128UL, -1);
                set => this.WriteData(128UL, value, -1);
            }

            public double SoilAvailableWaterContentInCM
            {
                get => this.ReadDataDouble(192UL, -1);
                set => this.WriteData(192UL, value, -1);
            }

            public double SurfaceStoneCoverAsFraction
            {
                get => this.ReadDataDouble(256UL, -1);
                set => this.WriteData(256UL, value, -1);
            }

            public double SoilAlbedo
            {
                get => this.ReadDataDouble(320UL, -1);
                set => this.WriteData(320UL, value, -1);
            }

            public double SoilEvaporationLimitInMM
            {
                get => this.ReadDataDouble(384UL, -1);
                set => this.WriteData(384UL, value, -1);
            }

            public double MineralizationFactor
            {
                get => this.ReadDataDouble(448UL, -1);
                set => this.WriteData(448UL, value, -1);
            }

            public double SoilFertilityOnFoto
            {
                get => this.ReadDataDouble(512UL, -1);
                set => this.WriteData(512UL, value, -1);
            }

            public string SoilClassificationSystem
            {
                get => this.ReadText(3, null);
                set => this.WriteText(3, value, null);
            }

            public string SoilTexture
            {
                get => this.ReadText(4, null);
                set => this.WriteText(4, value, null);
            }

            public string Classification
            {
                get => this.ReadText(5, null);
                set => this.WriteText(5, value, null);
            }

            public string Notes
            {
                get => this.ReadText(6, null);
                set => this.WriteText(6, value, null);
            }

            public Mas.Schema.Soil.IProfile Profile
            {
                get => ReadCap<Mas.Schema.Soil.IProfile>(7);
                set => LinkObject(7, value);
            }
        }
    }

    [
        System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"),
        TypeId(0xc158bd732092cde5UL)
    ]
    public class Field : ICapnpSerializable
    {
        public const UInt64 typeId = 0xc158bd732092cde5UL;

        void ICapnpSerializable.Deserialize(DeserializerState arg_)
        {
            var reader = READER.create(arg_);
            Id = reader.Id;
            Name = reader.Name;
            LatitudeInDecDeg = reader.LatitudeInDecDeg;
            LongitudeInDecDeg = reader.LongitudeInDecDeg;
            ElevationInM = reader.ElevationInM;
            SlopeDegreeInDeg = reader.SlopeDegreeInDeg;
            DrainageType = reader.DrainageType;
            DistanceToWeatherStationInKM = reader.DistanceToWeatherStationInKM;
            Country = reader.Country;
            SubCountry = reader.SubCountry;
            SubSubCountry = reader.SubSubCountry;
            Notes = reader.Notes;
            applyDefaults();
        }

        public void serialize(WRITER writer)
        {
            writer.Id = Id;
            writer.Name = Name;
            writer.LatitudeInDecDeg = LatitudeInDecDeg;
            writer.LongitudeInDecDeg = LongitudeInDecDeg;
            writer.ElevationInM = ElevationInM;
            writer.SlopeDegreeInDeg = SlopeDegreeInDeg;
            writer.DrainageType = DrainageType;
            writer.DistanceToWeatherStationInKM = DistanceToWeatherStationInKM;
            writer.Country = Country;
            writer.SubCountry = SubCountry;
            writer.SubSubCountry = SubSubCountry;
            writer.Notes = Notes;
        }

        void ICapnpSerializable.Serialize(SerializerState arg_)
        {
            serialize(arg_.Rewrap<WRITER>());
        }

        public void applyDefaults() { }

        public string Id { get; set; }

        public string Name { get; set; }

        public double LatitudeInDecDeg { get; set; } = -9999;
        public double LongitudeInDecDeg { get; set; } = -9999;
        public double ElevationInM { get; set; } = -9999;
        public double SlopeDegreeInDeg { get; set; } = -1;
        public string DrainageType { get; set; }

        public double DistanceToWeatherStationInKM { get; set; } = -1;
        public string Country { get; set; }

        public string SubCountry { get; set; }

        public string SubSubCountry { get; set; }

        public string Notes { get; set; }

        public struct READER
        {
            readonly DeserializerState ctx;

            public READER(DeserializerState ctx)
            {
                this.ctx = ctx;
            }

            public static READER create(DeserializerState ctx) => new READER(ctx);

            public static implicit operator DeserializerState(READER reader) => reader.ctx;

            public static implicit operator READER(DeserializerState ctx) => new READER(ctx);

            public string Id => ctx.ReadText(0, null);
            public string Name => ctx.ReadText(1, null);
            public double LatitudeInDecDeg => ctx.ReadDataDouble(0UL, -9999);
            public double LongitudeInDecDeg => ctx.ReadDataDouble(64UL, -9999);
            public double ElevationInM => ctx.ReadDataDouble(128UL, -9999);
            public double SlopeDegreeInDeg => ctx.ReadDataDouble(192UL, -1);
            public string DrainageType => ctx.ReadText(2, null);
            public double DistanceToWeatherStationInKM => ctx.ReadDataDouble(256UL, -1);
            public string Country => ctx.ReadText(3, null);
            public string SubCountry => ctx.ReadText(4, null);
            public string SubSubCountry => ctx.ReadText(5, null);
            public string Notes => ctx.ReadText(6, null);
        }

        public class WRITER : SerializerState
        {
            public WRITER()
            {
                this.SetStruct(5, 7);
            }

            public string Id
            {
                get => this.ReadText(0, null);
                set => this.WriteText(0, value, null);
            }

            public string Name
            {
                get => this.ReadText(1, null);
                set => this.WriteText(1, value, null);
            }

            public double LatitudeInDecDeg
            {
                get => this.ReadDataDouble(0UL, -9999);
                set => this.WriteData(0UL, value, -9999);
            }

            public double LongitudeInDecDeg
            {
                get => this.ReadDataDouble(64UL, -9999);
                set => this.WriteData(64UL, value, -9999);
            }

            public double ElevationInM
            {
                get => this.ReadDataDouble(128UL, -9999);
                set => this.WriteData(128UL, value, -9999);
            }

            public double SlopeDegreeInDeg
            {
                get => this.ReadDataDouble(192UL, -1);
                set => this.WriteData(192UL, value, -1);
            }

            public string DrainageType
            {
                get => this.ReadText(2, null);
                set => this.WriteText(2, value, null);
            }

            public double DistanceToWeatherStationInKM
            {
                get => this.ReadDataDouble(256UL, -1);
                set => this.WriteData(256UL, value, -1);
            }

            public string Country
            {
                get => this.ReadText(3, null);
                set => this.WriteText(3, value, null);
            }

            public string SubCountry
            {
                get => this.ReadText(4, null);
                set => this.WriteText(4, value, null);
            }

            public string SubSubCountry
            {
                get => this.ReadText(5, null);
                set => this.WriteText(5, value, null);
            }

            public string Notes
            {
                get => this.ReadText(6, null);
                set => this.WriteText(6, value, null);
            }
        }
    }

    [
        System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"),
        TypeId(0x9d795a72a27f67d7UL)
    ]
    public class ExperimentDescription : ICapnpSerializable
    {
        public const UInt64 typeId = 0x9d795a72a27f67d7UL;

        void ICapnpSerializable.Deserialize(DeserializerState arg_)
        {
            var reader = READER.create(arg_);
            Id = reader.Id;
            SuiteId = reader.SuiteId;
            Name = reader.Name;
            ResearchInfrastructureName = reader.ResearchInfrastructureName;
            InstituteName = reader.InstituteName;
            ResearchUnitName = reader.ResearchUnitName;
            ExperimentalFacilityName = reader.ExperimentalFacilityName;
            SiteName = reader.SiteName;
            SiteType = reader.SiteType;
            MainExperimentFactor = reader.MainExperimentFactor;
            ExperimentalFactorCombinations = reader.ExperimentalFactorCombinations;
            ExperimentType = reader.ExperimentType;
            ManagementType = reader.ManagementType;
            CroppingSystem = reader.CroppingSystem;
            PlantingYear = reader.PlantingYear;
            HarvestOperationYear = reader.HarvestOperationYear;
            Notes = reader.Notes;
            Treatments = reader.Treatments?.ToReadOnlyList(_ =>
                CapnpSerializable.Create<Mas.Schema.Data.Treatment>(_)
            );
            applyDefaults();
        }

        public void serialize(WRITER writer)
        {
            writer.Id = Id;
            writer.SuiteId = SuiteId;
            writer.Name = Name;
            writer.ResearchInfrastructureName = ResearchInfrastructureName;
            writer.InstituteName = InstituteName;
            writer.ResearchUnitName = ResearchUnitName;
            writer.ExperimentalFacilityName = ExperimentalFacilityName;
            writer.SiteName = SiteName;
            writer.SiteType = SiteType;
            writer.MainExperimentFactor = MainExperimentFactor;
            writer.ExperimentalFactorCombinations = ExperimentalFactorCombinations;
            writer.ExperimentType = ExperimentType;
            writer.ManagementType = ManagementType;
            writer.CroppingSystem = CroppingSystem;
            writer.PlantingYear = PlantingYear;
            writer.HarvestOperationYear = HarvestOperationYear;
            writer.Notes = Notes;
            writer.Treatments.Init(Treatments, (_s1, _v1) => _v1?.serialize(_s1));
        }

        void ICapnpSerializable.Serialize(SerializerState arg_)
        {
            serialize(arg_.Rewrap<WRITER>());
        }

        public void applyDefaults() { }

        public string Id { get; set; }

        public string SuiteId { get; set; }

        public string Name { get; set; }

        public string ResearchInfrastructureName { get; set; }

        public string InstituteName { get; set; }

        public string ResearchUnitName { get; set; }

        public string ExperimentalFacilityName { get; set; }

        public string SiteName { get; set; }

        public string SiteType { get; set; }

        public string MainExperimentFactor { get; set; }

        public string ExperimentalFactorCombinations { get; set; }

        public string ExperimentType { get; set; }

        public string ManagementType { get; set; }

        public string CroppingSystem { get; set; }

        public short PlantingYear { get; set; } = -1;
        public short HarvestOperationYear { get; set; } = -1;
        public string Notes { get; set; }

        public IReadOnlyList<Mas.Schema.Data.Treatment> Treatments { get; set; }

        public struct READER
        {
            readonly DeserializerState ctx;

            public READER(DeserializerState ctx)
            {
                this.ctx = ctx;
            }

            public static READER create(DeserializerState ctx) => new READER(ctx);

            public static implicit operator DeserializerState(READER reader) => reader.ctx;

            public static implicit operator READER(DeserializerState ctx) => new READER(ctx);

            public string Id => ctx.ReadText(0, null);
            public string SuiteId => ctx.ReadText(1, null);
            public string Name => ctx.ReadText(2, null);
            public string ResearchInfrastructureName => ctx.ReadText(3, null);
            public string InstituteName => ctx.ReadText(4, null);
            public string ResearchUnitName => ctx.ReadText(5, null);
            public string ExperimentalFacilityName => ctx.ReadText(6, null);
            public string SiteName => ctx.ReadText(7, null);
            public string SiteType => ctx.ReadText(8, null);
            public string MainExperimentFactor => ctx.ReadText(9, null);
            public string ExperimentalFactorCombinations => ctx.ReadText(10, null);
            public string ExperimentType => ctx.ReadText(11, null);
            public string ManagementType => ctx.ReadText(12, null);
            public string CroppingSystem => ctx.ReadText(13, null);
            public short PlantingYear => ctx.ReadDataShort(0UL, (short)-1);
            public short HarvestOperationYear => ctx.ReadDataShort(16UL, (short)-1);
            public string Notes => ctx.ReadText(14, null);
            public IReadOnlyList<Mas.Schema.Data.Treatment.READER> Treatments =>
                ctx.ReadList(15).Cast(Mas.Schema.Data.Treatment.READER.create);
            public bool HasTreatments => ctx.IsStructFieldNonNull(15);
        }

        public class WRITER : SerializerState
        {
            public WRITER()
            {
                this.SetStruct(1, 16);
            }

            public string Id
            {
                get => this.ReadText(0, null);
                set => this.WriteText(0, value, null);
            }

            public string SuiteId
            {
                get => this.ReadText(1, null);
                set => this.WriteText(1, value, null);
            }

            public string Name
            {
                get => this.ReadText(2, null);
                set => this.WriteText(2, value, null);
            }

            public string ResearchInfrastructureName
            {
                get => this.ReadText(3, null);
                set => this.WriteText(3, value, null);
            }

            public string InstituteName
            {
                get => this.ReadText(4, null);
                set => this.WriteText(4, value, null);
            }

            public string ResearchUnitName
            {
                get => this.ReadText(5, null);
                set => this.WriteText(5, value, null);
            }

            public string ExperimentalFacilityName
            {
                get => this.ReadText(6, null);
                set => this.WriteText(6, value, null);
            }

            public string SiteName
            {
                get => this.ReadText(7, null);
                set => this.WriteText(7, value, null);
            }

            public string SiteType
            {
                get => this.ReadText(8, null);
                set => this.WriteText(8, value, null);
            }

            public string MainExperimentFactor
            {
                get => this.ReadText(9, null);
                set => this.WriteText(9, value, null);
            }

            public string ExperimentalFactorCombinations
            {
                get => this.ReadText(10, null);
                set => this.WriteText(10, value, null);
            }

            public string ExperimentType
            {
                get => this.ReadText(11, null);
                set => this.WriteText(11, value, null);
            }

            public string ManagementType
            {
                get => this.ReadText(12, null);
                set => this.WriteText(12, value, null);
            }

            public string CroppingSystem
            {
                get => this.ReadText(13, null);
                set => this.WriteText(13, value, null);
            }

            public short PlantingYear
            {
                get => this.ReadDataShort(0UL, (short)-1);
                set => this.WriteData(0UL, value, (short)-1);
            }

            public short HarvestOperationYear
            {
                get => this.ReadDataShort(16UL, (short)-1);
                set => this.WriteData(16UL, value, (short)-1);
            }

            public string Notes
            {
                get => this.ReadText(14, null);
                set => this.WriteText(14, value, null);
            }

            public ListOfStructsSerializer<Mas.Schema.Data.Treatment.WRITER> Treatments
            {
                get => BuildPointer<ListOfStructsSerializer<Mas.Schema.Data.Treatment.WRITER>>(15);
                set => Link(15, value);
            }
        }
    }

    [
        System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"),
        TypeId(0xff1381363c7abd06UL)
    ]
    public class Treatment : ICapnpSerializable
    {
        public const UInt64 typeId = 0xff1381363c7abd06UL;

        void ICapnpSerializable.Deserialize(DeserializerState arg_)
        {
            var reader = READER.create(arg_);
            Id = reader.Id;
            Field = CapnpSerializable.Create<Mas.Schema.Data.Field>(reader.Field);
            WeatherStation = CapnpSerializable.Create<Mas.Schema.Data.WeatherStation>(
                reader.WeatherStation
            );
            WeatherStationTimeseries = reader.WeatherStationTimeseries;
            Name = reader.Name;
            SimulationStartDate = CapnpSerializable.Create<Mas.Schema.Common.Date>(
                reader.SimulationStartDate
            );
            SimulationEndDate = CapnpSerializable.Create<Mas.Schema.Common.Date>(
                reader.SimulationEndDate
            );
            IrrigationApplied = reader.IrrigationApplied;
            FertilizerApplied = reader.FertilizerApplied;
            IrrigationLevel = reader.IrrigationLevel;
            FertilizerLevel = reader.FertilizerLevel;
            PlantingDateLevel = reader.PlantingDateLevel;
            EnvironmentalModificationsLevel = reader.EnvironmentalModificationsLevel;
            InitialConditionsLevel = reader.InitialConditionsLevel;
            PlantingDensityLevel = reader.PlantingDensityLevel;
            NumberOfBlocksOrReplicates = reader.NumberOfBlocksOrReplicates;
            Notes = reader.Notes;
            Plots = reader.Plots?.ToReadOnlyList(_ =>
                CapnpSerializable.Create<Mas.Schema.Data.Plot>(_)
            );
            Residue = CapnpSerializable.Create<Mas.Schema.Data.Residue>(reader.Residue);
            InitialConditionsLayers = reader.InitialConditionsLayers?.ToReadOnlyList(_ =>
                CapnpSerializable.Create<Mas.Schema.Data.InitialConditionsLayer>(_)
            );
            PlantingEvents = reader.PlantingEvents?.ToReadOnlyList(_ =>
                CapnpSerializable.Create<Mas.Schema.Data.PlantingEvent>(_)
            );
            HarvestEvents = reader.HarvestEvents?.ToReadOnlyList(_ =>
                CapnpSerializable.Create<Mas.Schema.Data.HarvestEvent>(_)
            );
            IrrigationEvents = reader.IrrigationEvents?.ToReadOnlyList(_ =>
                CapnpSerializable.Create<Mas.Schema.Data.IrrigationEvent>(_)
            );
            FertilizerEvents = reader.FertilizerEvents?.ToReadOnlyList(_ =>
                CapnpSerializable.Create<Mas.Schema.Data.FertilizerEvent>(_)
            );
            EnvironmentModifications = reader.EnvironmentModifications?.ToReadOnlyList(_ =>
                CapnpSerializable.Create<Mas.Schema.Data.EnvironmentModification>(_)
            );
            ExperimentId = reader.ExperimentId;
            FieldId = reader.FieldId;
            WeatherStationId = reader.WeatherStationId;
            WeatherStationDataset = reader.WeatherStationDataset;
            applyDefaults();
        }

        public void serialize(WRITER writer)
        {
            writer.Id = Id;
            Field?.serialize(writer.Field);
            WeatherStation?.serialize(writer.WeatherStation);
            writer.WeatherStationTimeseries = WeatherStationTimeseries;
            writer.Name = Name;
            SimulationStartDate?.serialize(writer.SimulationStartDate);
            SimulationEndDate?.serialize(writer.SimulationEndDate);
            writer.IrrigationApplied = IrrigationApplied;
            writer.FertilizerApplied = FertilizerApplied;
            writer.IrrigationLevel = IrrigationLevel;
            writer.FertilizerLevel = FertilizerLevel;
            writer.PlantingDateLevel = PlantingDateLevel;
            writer.EnvironmentalModificationsLevel = EnvironmentalModificationsLevel;
            writer.InitialConditionsLevel = InitialConditionsLevel;
            writer.PlantingDensityLevel = PlantingDensityLevel;
            writer.NumberOfBlocksOrReplicates = NumberOfBlocksOrReplicates;
            writer.Notes = Notes;
            writer.Plots.Init(Plots, (_s1, _v1) => _v1?.serialize(_s1));
            Residue?.serialize(writer.Residue);
            writer.InitialConditionsLayers.Init(
                InitialConditionsLayers,
                (_s1, _v1) => _v1?.serialize(_s1)
            );
            writer.PlantingEvents.Init(PlantingEvents, (_s1, _v1) => _v1?.serialize(_s1));
            writer.HarvestEvents.Init(HarvestEvents, (_s1, _v1) => _v1?.serialize(_s1));
            writer.IrrigationEvents.Init(IrrigationEvents, (_s1, _v1) => _v1?.serialize(_s1));
            writer.FertilizerEvents.Init(FertilizerEvents, (_s1, _v1) => _v1?.serialize(_s1));
            writer.EnvironmentModifications.Init(
                EnvironmentModifications,
                (_s1, _v1) => _v1?.serialize(_s1)
            );
            writer.ExperimentId = ExperimentId;
            writer.FieldId = FieldId;
            writer.WeatherStationId = WeatherStationId;
            writer.WeatherStationDataset = WeatherStationDataset;
        }

        void ICapnpSerializable.Serialize(SerializerState arg_)
        {
            serialize(arg_.Rewrap<WRITER>());
        }

        public void applyDefaults() { }

        public string Id { get; set; }

        public Mas.Schema.Data.Field Field { get; set; }

        public Mas.Schema.Data.WeatherStation WeatherStation { get; set; }

        public Mas.Schema.Climate.ITimeSeries WeatherStationTimeseries { get; set; }

        public string Name { get; set; }

        public Mas.Schema.Common.Date SimulationStartDate { get; set; }

        public Mas.Schema.Common.Date SimulationEndDate { get; set; }

        public bool IrrigationApplied { get; set; }

        public bool FertilizerApplied { get; set; }

        public sbyte IrrigationLevel { get; set; } = -1;
        public sbyte FertilizerLevel { get; set; } = -1;
        public sbyte PlantingDateLevel { get; set; } = -1;
        public sbyte EnvironmentalModificationsLevel { get; set; } = -1;
        public sbyte InitialConditionsLevel { get; set; } = -1;
        public sbyte PlantingDensityLevel { get; set; } = -1;
        public sbyte NumberOfBlocksOrReplicates { get; set; } = -1;
        public string Notes { get; set; }

        public IReadOnlyList<Mas.Schema.Data.Plot> Plots { get; set; }

        public Mas.Schema.Data.Residue Residue { get; set; }

        public IReadOnlyList<Mas.Schema.Data.InitialConditionsLayer> InitialConditionsLayers { get; set; }

        public IReadOnlyList<Mas.Schema.Data.PlantingEvent> PlantingEvents { get; set; }

        public IReadOnlyList<Mas.Schema.Data.HarvestEvent> HarvestEvents { get; set; }

        public IReadOnlyList<Mas.Schema.Data.IrrigationEvent> IrrigationEvents { get; set; }

        public IReadOnlyList<Mas.Schema.Data.FertilizerEvent> FertilizerEvents { get; set; }

        public IReadOnlyList<Mas.Schema.Data.EnvironmentModification> EnvironmentModifications { get; set; }

        public string ExperimentId { get; set; }

        public string FieldId { get; set; }

        public string WeatherStationId { get; set; }

        public string WeatherStationDataset { get; set; }

        public struct READER
        {
            readonly DeserializerState ctx;

            public READER(DeserializerState ctx)
            {
                this.ctx = ctx;
            }

            public static READER create(DeserializerState ctx) => new READER(ctx);

            public static implicit operator DeserializerState(READER reader) => reader.ctx;

            public static implicit operator READER(DeserializerState ctx) => new READER(ctx);

            public string Id => ctx.ReadText(0, null);
            public Mas.Schema.Data.Field.READER Field =>
                ctx.ReadStruct(1, Mas.Schema.Data.Field.READER.create);
            public bool HasField => ctx.IsStructFieldNonNull(1);
            public Mas.Schema.Data.WeatherStation.READER WeatherStation =>
                ctx.ReadStruct(2, Mas.Schema.Data.WeatherStation.READER.create);
            public bool HasWeatherStation => ctx.IsStructFieldNonNull(2);
            public Mas.Schema.Climate.ITimeSeries WeatherStationTimeseries =>
                ctx.ReadCap<Mas.Schema.Climate.ITimeSeries>(3);
            public string Name => ctx.ReadText(4, null);
            public Mas.Schema.Common.Date.READER SimulationStartDate =>
                ctx.ReadStruct(5, Mas.Schema.Common.Date.READER.create);
            public bool HasSimulationStartDate => ctx.IsStructFieldNonNull(5);
            public Mas.Schema.Common.Date.READER SimulationEndDate =>
                ctx.ReadStruct(6, Mas.Schema.Common.Date.READER.create);
            public bool HasSimulationEndDate => ctx.IsStructFieldNonNull(6);
            public bool IrrigationApplied => ctx.ReadDataBool(0UL, false);
            public bool FertilizerApplied => ctx.ReadDataBool(1UL, false);
            public sbyte IrrigationLevel => ctx.ReadDataSByte(8UL, (sbyte)-1);
            public sbyte FertilizerLevel => ctx.ReadDataSByte(16UL, (sbyte)-1);
            public sbyte PlantingDateLevel => ctx.ReadDataSByte(24UL, (sbyte)-1);
            public sbyte EnvironmentalModificationsLevel => ctx.ReadDataSByte(32UL, (sbyte)-1);
            public sbyte InitialConditionsLevel => ctx.ReadDataSByte(40UL, (sbyte)-1);
            public sbyte PlantingDensityLevel => ctx.ReadDataSByte(48UL, (sbyte)-1);
            public sbyte NumberOfBlocksOrReplicates => ctx.ReadDataSByte(56UL, (sbyte)-1);
            public string Notes => ctx.ReadText(7, null);
            public IReadOnlyList<Mas.Schema.Data.Plot.READER> Plots =>
                ctx.ReadList(8).Cast(Mas.Schema.Data.Plot.READER.create);
            public bool HasPlots => ctx.IsStructFieldNonNull(8);
            public Mas.Schema.Data.Residue.READER Residue =>
                ctx.ReadStruct(9, Mas.Schema.Data.Residue.READER.create);
            public bool HasResidue => ctx.IsStructFieldNonNull(9);
            public IReadOnlyList<Mas.Schema.Data.InitialConditionsLayer.READER> InitialConditionsLayers =>
                ctx.ReadList(10).Cast(Mas.Schema.Data.InitialConditionsLayer.READER.create);
            public bool HasInitialConditionsLayers => ctx.IsStructFieldNonNull(10);
            public IReadOnlyList<Mas.Schema.Data.PlantingEvent.READER> PlantingEvents =>
                ctx.ReadList(11).Cast(Mas.Schema.Data.PlantingEvent.READER.create);
            public bool HasPlantingEvents => ctx.IsStructFieldNonNull(11);
            public IReadOnlyList<Mas.Schema.Data.HarvestEvent.READER> HarvestEvents =>
                ctx.ReadList(12).Cast(Mas.Schema.Data.HarvestEvent.READER.create);
            public bool HasHarvestEvents => ctx.IsStructFieldNonNull(12);
            public IReadOnlyList<Mas.Schema.Data.IrrigationEvent.READER> IrrigationEvents =>
                ctx.ReadList(13).Cast(Mas.Schema.Data.IrrigationEvent.READER.create);
            public bool HasIrrigationEvents => ctx.IsStructFieldNonNull(13);
            public IReadOnlyList<Mas.Schema.Data.FertilizerEvent.READER> FertilizerEvents =>
                ctx.ReadList(14).Cast(Mas.Schema.Data.FertilizerEvent.READER.create);
            public bool HasFertilizerEvents => ctx.IsStructFieldNonNull(14);
            public IReadOnlyList<Mas.Schema.Data.EnvironmentModification.READER> EnvironmentModifications =>
                ctx.ReadList(15).Cast(Mas.Schema.Data.EnvironmentModification.READER.create);
            public bool HasEnvironmentModifications => ctx.IsStructFieldNonNull(15);
            public string ExperimentId => ctx.ReadText(16, null);
            public string FieldId => ctx.ReadText(17, null);
            public string WeatherStationId => ctx.ReadText(18, null);
            public string WeatherStationDataset => ctx.ReadText(19, null);
        }

        public class WRITER : SerializerState
        {
            public WRITER()
            {
                this.SetStruct(1, 20);
            }

            public string Id
            {
                get => this.ReadText(0, null);
                set => this.WriteText(0, value, null);
            }

            public Mas.Schema.Data.Field.WRITER Field
            {
                get => BuildPointer<Mas.Schema.Data.Field.WRITER>(1);
                set => Link(1, value);
            }

            public Mas.Schema.Data.WeatherStation.WRITER WeatherStation
            {
                get => BuildPointer<Mas.Schema.Data.WeatherStation.WRITER>(2);
                set => Link(2, value);
            }

            public Mas.Schema.Climate.ITimeSeries WeatherStationTimeseries
            {
                get => ReadCap<Mas.Schema.Climate.ITimeSeries>(3);
                set => LinkObject(3, value);
            }

            public string Name
            {
                get => this.ReadText(4, null);
                set => this.WriteText(4, value, null);
            }

            public Mas.Schema.Common.Date.WRITER SimulationStartDate
            {
                get => BuildPointer<Mas.Schema.Common.Date.WRITER>(5);
                set => Link(5, value);
            }

            public Mas.Schema.Common.Date.WRITER SimulationEndDate
            {
                get => BuildPointer<Mas.Schema.Common.Date.WRITER>(6);
                set => Link(6, value);
            }

            public bool IrrigationApplied
            {
                get => this.ReadDataBool(0UL, false);
                set => this.WriteData(0UL, value, false);
            }

            public bool FertilizerApplied
            {
                get => this.ReadDataBool(1UL, false);
                set => this.WriteData(1UL, value, false);
            }

            public sbyte IrrigationLevel
            {
                get => this.ReadDataSByte(8UL, (sbyte)-1);
                set => this.WriteData(8UL, value, (sbyte)-1);
            }

            public sbyte FertilizerLevel
            {
                get => this.ReadDataSByte(16UL, (sbyte)-1);
                set => this.WriteData(16UL, value, (sbyte)-1);
            }

            public sbyte PlantingDateLevel
            {
                get => this.ReadDataSByte(24UL, (sbyte)-1);
                set => this.WriteData(24UL, value, (sbyte)-1);
            }

            public sbyte EnvironmentalModificationsLevel
            {
                get => this.ReadDataSByte(32UL, (sbyte)-1);
                set => this.WriteData(32UL, value, (sbyte)-1);
            }

            public sbyte InitialConditionsLevel
            {
                get => this.ReadDataSByte(40UL, (sbyte)-1);
                set => this.WriteData(40UL, value, (sbyte)-1);
            }

            public sbyte PlantingDensityLevel
            {
                get => this.ReadDataSByte(48UL, (sbyte)-1);
                set => this.WriteData(48UL, value, (sbyte)-1);
            }

            public sbyte NumberOfBlocksOrReplicates
            {
                get => this.ReadDataSByte(56UL, (sbyte)-1);
                set => this.WriteData(56UL, value, (sbyte)-1);
            }

            public string Notes
            {
                get => this.ReadText(7, null);
                set => this.WriteText(7, value, null);
            }

            public ListOfStructsSerializer<Mas.Schema.Data.Plot.WRITER> Plots
            {
                get => BuildPointer<ListOfStructsSerializer<Mas.Schema.Data.Plot.WRITER>>(8);
                set => Link(8, value);
            }

            public Mas.Schema.Data.Residue.WRITER Residue
            {
                get => BuildPointer<Mas.Schema.Data.Residue.WRITER>(9);
                set => Link(9, value);
            }

            public ListOfStructsSerializer<Mas.Schema.Data.InitialConditionsLayer.WRITER> InitialConditionsLayers
            {
                get =>
                    BuildPointer<
                        ListOfStructsSerializer<Mas.Schema.Data.InitialConditionsLayer.WRITER>
                    >(10);
                set => Link(10, value);
            }

            public ListOfStructsSerializer<Mas.Schema.Data.PlantingEvent.WRITER> PlantingEvents
            {
                get =>
                    BuildPointer<ListOfStructsSerializer<Mas.Schema.Data.PlantingEvent.WRITER>>(11);
                set => Link(11, value);
            }

            public ListOfStructsSerializer<Mas.Schema.Data.HarvestEvent.WRITER> HarvestEvents
            {
                get =>
                    BuildPointer<ListOfStructsSerializer<Mas.Schema.Data.HarvestEvent.WRITER>>(12);
                set => Link(12, value);
            }

            public ListOfStructsSerializer<Mas.Schema.Data.IrrigationEvent.WRITER> IrrigationEvents
            {
                get =>
                    BuildPointer<ListOfStructsSerializer<Mas.Schema.Data.IrrigationEvent.WRITER>>(
                        13
                    );
                set => Link(13, value);
            }

            public ListOfStructsSerializer<Mas.Schema.Data.FertilizerEvent.WRITER> FertilizerEvents
            {
                get =>
                    BuildPointer<ListOfStructsSerializer<Mas.Schema.Data.FertilizerEvent.WRITER>>(
                        14
                    );
                set => Link(14, value);
            }

            public ListOfStructsSerializer<Mas.Schema.Data.EnvironmentModification.WRITER> EnvironmentModifications
            {
                get =>
                    BuildPointer<
                        ListOfStructsSerializer<Mas.Schema.Data.EnvironmentModification.WRITER>
                    >(15);
                set => Link(15, value);
            }

            public string ExperimentId
            {
                get => this.ReadText(16, null);
                set => this.WriteText(16, value, null);
            }

            public string FieldId
            {
                get => this.ReadText(17, null);
                set => this.WriteText(17, value, null);
            }

            public string WeatherStationId
            {
                get => this.ReadText(18, null);
                set => this.WriteText(18, value, null);
            }

            public string WeatherStationDataset
            {
                get => this.ReadText(19, null);
                set => this.WriteText(19, value, null);
            }
        }
    }

    [
        System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"),
        TypeId(0xab7ea2bfa7965af8UL)
    ]
    public class Cultivar : ICapnpSerializable
    {
        public const UInt64 typeId = 0xab7ea2bfa7965af8UL;

        void ICapnpSerializable.Deserialize(DeserializerState arg_)
        {
            var reader = READER.create(arg_);
            Id = reader.Id;
            Name = reader.Name;
            AccessionId = reader.AccessionId;
            AccessionLocation = reader.AccessionLocation;
            CropIdentifierICASA = reader.CropIdentifierICASA;
            SeedLot = reader.SeedLot;
            BreedingProgram = reader.BreedingProgram;
            OriginalName = reader.OriginalName;
            ReleaseYear = reader.ReleaseYear;
            Synonym = reader.Synonym;
            Notes = reader.Notes;
            applyDefaults();
        }

        public void serialize(WRITER writer)
        {
            writer.Id = Id;
            writer.Name = Name;
            writer.AccessionId = AccessionId;
            writer.AccessionLocation = AccessionLocation;
            writer.CropIdentifierICASA = CropIdentifierICASA;
            writer.SeedLot = SeedLot;
            writer.BreedingProgram = BreedingProgram;
            writer.OriginalName = OriginalName;
            writer.ReleaseYear = ReleaseYear;
            writer.Synonym = Synonym;
            writer.Notes = Notes;
        }

        void ICapnpSerializable.Serialize(SerializerState arg_)
        {
            serialize(arg_.Rewrap<WRITER>());
        }

        public void applyDefaults() { }

        public string Id { get; set; }

        public string Name { get; set; }

        public string AccessionId { get; set; }

        public string AccessionLocation { get; set; }

        public string CropIdentifierICASA { get; set; }

        public string SeedLot { get; set; }

        public string BreedingProgram { get; set; }

        public string OriginalName { get; set; }

        public short ReleaseYear { get; set; } = -1;
        public string Synonym { get; set; }

        public string Notes { get; set; }

        public struct READER
        {
            readonly DeserializerState ctx;

            public READER(DeserializerState ctx)
            {
                this.ctx = ctx;
            }

            public static READER create(DeserializerState ctx) => new READER(ctx);

            public static implicit operator DeserializerState(READER reader) => reader.ctx;

            public static implicit operator READER(DeserializerState ctx) => new READER(ctx);

            public string Id => ctx.ReadText(0, null);
            public string Name => ctx.ReadText(1, null);
            public string AccessionId => ctx.ReadText(2, null);
            public string AccessionLocation => ctx.ReadText(3, null);
            public string CropIdentifierICASA => ctx.ReadText(4, null);
            public string SeedLot => ctx.ReadText(5, null);
            public string BreedingProgram => ctx.ReadText(6, null);
            public string OriginalName => ctx.ReadText(7, null);
            public short ReleaseYear => ctx.ReadDataShort(0UL, (short)-1);
            public string Synonym => ctx.ReadText(8, null);
            public string Notes => ctx.ReadText(9, null);
        }

        public class WRITER : SerializerState
        {
            public WRITER()
            {
                this.SetStruct(1, 10);
            }

            public string Id
            {
                get => this.ReadText(0, null);
                set => this.WriteText(0, value, null);
            }

            public string Name
            {
                get => this.ReadText(1, null);
                set => this.WriteText(1, value, null);
            }

            public string AccessionId
            {
                get => this.ReadText(2, null);
                set => this.WriteText(2, value, null);
            }

            public string AccessionLocation
            {
                get => this.ReadText(3, null);
                set => this.WriteText(3, value, null);
            }

            public string CropIdentifierICASA
            {
                get => this.ReadText(4, null);
                set => this.WriteText(4, value, null);
            }

            public string SeedLot
            {
                get => this.ReadText(5, null);
                set => this.WriteText(5, value, null);
            }

            public string BreedingProgram
            {
                get => this.ReadText(6, null);
                set => this.WriteText(6, value, null);
            }

            public string OriginalName
            {
                get => this.ReadText(7, null);
                set => this.WriteText(7, value, null);
            }

            public short ReleaseYear
            {
                get => this.ReadDataShort(0UL, (short)-1);
                set => this.WriteData(0UL, value, (short)-1);
            }

            public string Synonym
            {
                get => this.ReadText(8, null);
                set => this.WriteText(8, value, null);
            }

            public string Notes
            {
                get => this.ReadText(9, null);
                set => this.WriteText(9, value, null);
            }
        }
    }

    [
        System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"),
        TypeId(0xa7a2210fb1e289f2UL)
    ]
    public class Plot : ICapnpSerializable
    {
        public const UInt64 typeId = 0xa7a2210fb1e289f2UL;

        void ICapnpSerializable.Deserialize(DeserializerState arg_)
        {
            var reader = READER.create(arg_);
            Id = reader.Id;
            Cultivar = CapnpSerializable.Create<Mas.Schema.Data.Cultivar>(reader.Cultivar);
            Soil = CapnpSerializable.Create<Mas.Schema.Data.SoilMetadata>(reader.Soil);
            BlockNumber = reader.BlockNumber;
            PlotNumber = reader.PlotNumber;
            ReplicateNumber = reader.ReplicateNumber;
            RowNumber = reader.RowNumber;
            ColumnNumber = reader.ColumnNumber;
            HarvestMethod = reader.HarvestMethod;
            Notes = reader.Notes;
            ExperimentId = reader.ExperimentId;
            TreatmentId = reader.TreatmentId;
            CultivarId = reader.CultivarId;
            SoilId = reader.SoilId;
            applyDefaults();
        }

        public void serialize(WRITER writer)
        {
            writer.Id = Id;
            Cultivar?.serialize(writer.Cultivar);
            Soil?.serialize(writer.Soil);
            writer.BlockNumber = BlockNumber;
            writer.PlotNumber = PlotNumber;
            writer.ReplicateNumber = ReplicateNumber;
            writer.RowNumber = RowNumber;
            writer.ColumnNumber = ColumnNumber;
            writer.HarvestMethod = HarvestMethod;
            writer.Notes = Notes;
            writer.ExperimentId = ExperimentId;
            writer.TreatmentId = TreatmentId;
            writer.CultivarId = CultivarId;
            writer.SoilId = SoilId;
        }

        void ICapnpSerializable.Serialize(SerializerState arg_)
        {
            serialize(arg_.Rewrap<WRITER>());
        }

        public void applyDefaults() { }

        public string Id { get; set; }

        public Mas.Schema.Data.Cultivar Cultivar { get; set; }

        public Mas.Schema.Data.SoilMetadata Soil { get; set; }

        public sbyte BlockNumber { get; set; } = -1;
        public sbyte PlotNumber { get; set; } = -1;
        public sbyte ReplicateNumber { get; set; } = -1;
        public sbyte RowNumber { get; set; } = -1;
        public sbyte ColumnNumber { get; set; } = -1;
        public string HarvestMethod { get; set; }

        public string Notes { get; set; }

        public string ExperimentId { get; set; }

        public string TreatmentId { get; set; }

        public string CultivarId { get; set; }

        public string SoilId { get; set; }

        public struct READER
        {
            readonly DeserializerState ctx;

            public READER(DeserializerState ctx)
            {
                this.ctx = ctx;
            }

            public static READER create(DeserializerState ctx) => new READER(ctx);

            public static implicit operator DeserializerState(READER reader) => reader.ctx;

            public static implicit operator READER(DeserializerState ctx) => new READER(ctx);

            public string Id => ctx.ReadText(0, null);
            public Mas.Schema.Data.Cultivar.READER Cultivar =>
                ctx.ReadStruct(1, Mas.Schema.Data.Cultivar.READER.create);
            public bool HasCultivar => ctx.IsStructFieldNonNull(1);
            public Mas.Schema.Data.SoilMetadata.READER Soil =>
                ctx.ReadStruct(2, Mas.Schema.Data.SoilMetadata.READER.create);
            public bool HasSoil => ctx.IsStructFieldNonNull(2);
            public sbyte BlockNumber => ctx.ReadDataSByte(0UL, (sbyte)-1);
            public sbyte PlotNumber => ctx.ReadDataSByte(8UL, (sbyte)-1);
            public sbyte ReplicateNumber => ctx.ReadDataSByte(16UL, (sbyte)-1);
            public sbyte RowNumber => ctx.ReadDataSByte(24UL, (sbyte)-1);
            public sbyte ColumnNumber => ctx.ReadDataSByte(32UL, (sbyte)-1);
            public string HarvestMethod => ctx.ReadText(3, null);
            public string Notes => ctx.ReadText(4, null);
            public string ExperimentId => ctx.ReadText(5, null);
            public string TreatmentId => ctx.ReadText(6, null);
            public string CultivarId => ctx.ReadText(7, null);
            public string SoilId => ctx.ReadText(8, null);
        }

        public class WRITER : SerializerState
        {
            public WRITER()
            {
                this.SetStruct(1, 9);
            }

            public string Id
            {
                get => this.ReadText(0, null);
                set => this.WriteText(0, value, null);
            }

            public Mas.Schema.Data.Cultivar.WRITER Cultivar
            {
                get => BuildPointer<Mas.Schema.Data.Cultivar.WRITER>(1);
                set => Link(1, value);
            }

            public Mas.Schema.Data.SoilMetadata.WRITER Soil
            {
                get => BuildPointer<Mas.Schema.Data.SoilMetadata.WRITER>(2);
                set => Link(2, value);
            }

            public sbyte BlockNumber
            {
                get => this.ReadDataSByte(0UL, (sbyte)-1);
                set => this.WriteData(0UL, value, (sbyte)-1);
            }

            public sbyte PlotNumber
            {
                get => this.ReadDataSByte(8UL, (sbyte)-1);
                set => this.WriteData(8UL, value, (sbyte)-1);
            }

            public sbyte ReplicateNumber
            {
                get => this.ReadDataSByte(16UL, (sbyte)-1);
                set => this.WriteData(16UL, value, (sbyte)-1);
            }

            public sbyte RowNumber
            {
                get => this.ReadDataSByte(24UL, (sbyte)-1);
                set => this.WriteData(24UL, value, (sbyte)-1);
            }

            public sbyte ColumnNumber
            {
                get => this.ReadDataSByte(32UL, (sbyte)-1);
                set => this.WriteData(32UL, value, (sbyte)-1);
            }

            public string HarvestMethod
            {
                get => this.ReadText(3, null);
                set => this.WriteText(3, value, null);
            }

            public string Notes
            {
                get => this.ReadText(4, null);
                set => this.WriteText(4, value, null);
            }

            public string ExperimentId
            {
                get => this.ReadText(5, null);
                set => this.WriteText(5, value, null);
            }

            public string TreatmentId
            {
                get => this.ReadText(6, null);
                set => this.WriteText(6, value, null);
            }

            public string CultivarId
            {
                get => this.ReadText(7, null);
                set => this.WriteText(7, value, null);
            }

            public string SoilId
            {
                get => this.ReadText(8, null);
                set => this.WriteText(8, value, null);
            }
        }
    }

    [
        System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"),
        TypeId(0xd1c0bc9f5b332a6eUL)
    ]
    public class InitialConditionsLayer : ICapnpSerializable
    {
        public const UInt64 typeId = 0xd1c0bc9f5b332a6eUL;

        void ICapnpSerializable.Deserialize(DeserializerState arg_)
        {
            var reader = READER.create(arg_);
            Date = CapnpSerializable.Create<Mas.Schema.Common.Date>(reader.Date);
            SoilLayerTopDepthInCM = reader.SoilLayerTopDepthInCM;
            SoilLayerBaseDepthInCM = reader.SoilLayerBaseDepthInCM;
            WaterConcentration = reader.WaterConcentration;
            TotalNInKGperHA = reader.TotalNInKGperHA;
            MassNH4InKGperHA = reader.MassNH4InKGperHA;
            MassNO3InKGperHA = reader.MassNO3InKGperHA;
            ConcNH4InPPM = reader.ConcNH4InPPM;
            ConcNO3InPPM = reader.ConcNO3InPPM;
            ExperimentId = reader.ExperimentId;
            TreatmentId = reader.TreatmentId;
            applyDefaults();
        }

        public void serialize(WRITER writer)
        {
            Date?.serialize(writer.Date);
            writer.SoilLayerTopDepthInCM = SoilLayerTopDepthInCM;
            writer.SoilLayerBaseDepthInCM = SoilLayerBaseDepthInCM;
            writer.WaterConcentration = WaterConcentration;
            writer.TotalNInKGperHA = TotalNInKGperHA;
            writer.MassNH4InKGperHA = MassNH4InKGperHA;
            writer.MassNO3InKGperHA = MassNO3InKGperHA;
            writer.ConcNH4InPPM = ConcNH4InPPM;
            writer.ConcNO3InPPM = ConcNO3InPPM;
            writer.ExperimentId = ExperimentId;
            writer.TreatmentId = TreatmentId;
        }

        void ICapnpSerializable.Serialize(SerializerState arg_)
        {
            serialize(arg_.Rewrap<WRITER>());
        }

        public void applyDefaults() { }

        public Mas.Schema.Common.Date Date { get; set; }

        public short SoilLayerTopDepthInCM { get; set; } = -1;
        public short SoilLayerBaseDepthInCM { get; set; } = -1;
        public double WaterConcentration { get; set; } = -1;
        public double TotalNInKGperHA { get; set; } = -1;
        public double MassNH4InKGperHA { get; set; } = -1;
        public double MassNO3InKGperHA { get; set; } = -1;
        public double ConcNH4InPPM { get; set; } = -1;
        public double ConcNO3InPPM { get; set; } = -1;
        public string ExperimentId { get; set; }

        public string TreatmentId { get; set; }

        public struct READER
        {
            readonly DeserializerState ctx;

            public READER(DeserializerState ctx)
            {
                this.ctx = ctx;
            }

            public static READER create(DeserializerState ctx) => new READER(ctx);

            public static implicit operator DeserializerState(READER reader) => reader.ctx;

            public static implicit operator READER(DeserializerState ctx) => new READER(ctx);

            public Mas.Schema.Common.Date.READER Date =>
                ctx.ReadStruct(0, Mas.Schema.Common.Date.READER.create);
            public bool HasDate => ctx.IsStructFieldNonNull(0);
            public short SoilLayerTopDepthInCM => ctx.ReadDataShort(0UL, (short)-1);
            public short SoilLayerBaseDepthInCM => ctx.ReadDataShort(16UL, (short)-1);
            public double WaterConcentration => ctx.ReadDataDouble(64UL, -1);
            public double TotalNInKGperHA => ctx.ReadDataDouble(128UL, -1);
            public double MassNH4InKGperHA => ctx.ReadDataDouble(192UL, -1);
            public double MassNO3InKGperHA => ctx.ReadDataDouble(256UL, -1);
            public double ConcNH4InPPM => ctx.ReadDataDouble(320UL, -1);
            public double ConcNO3InPPM => ctx.ReadDataDouble(384UL, -1);
            public string ExperimentId => ctx.ReadText(1, null);
            public string TreatmentId => ctx.ReadText(2, null);
        }

        public class WRITER : SerializerState
        {
            public WRITER()
            {
                this.SetStruct(7, 3);
            }

            public Mas.Schema.Common.Date.WRITER Date
            {
                get => BuildPointer<Mas.Schema.Common.Date.WRITER>(0);
                set => Link(0, value);
            }

            public short SoilLayerTopDepthInCM
            {
                get => this.ReadDataShort(0UL, (short)-1);
                set => this.WriteData(0UL, value, (short)-1);
            }

            public short SoilLayerBaseDepthInCM
            {
                get => this.ReadDataShort(16UL, (short)-1);
                set => this.WriteData(16UL, value, (short)-1);
            }

            public double WaterConcentration
            {
                get => this.ReadDataDouble(64UL, -1);
                set => this.WriteData(64UL, value, -1);
            }

            public double TotalNInKGperHA
            {
                get => this.ReadDataDouble(128UL, -1);
                set => this.WriteData(128UL, value, -1);
            }

            public double MassNH4InKGperHA
            {
                get => this.ReadDataDouble(192UL, -1);
                set => this.WriteData(192UL, value, -1);
            }

            public double MassNO3InKGperHA
            {
                get => this.ReadDataDouble(256UL, -1);
                set => this.WriteData(256UL, value, -1);
            }

            public double ConcNH4InPPM
            {
                get => this.ReadDataDouble(320UL, -1);
                set => this.WriteData(320UL, value, -1);
            }

            public double ConcNO3InPPM
            {
                get => this.ReadDataDouble(384UL, -1);
                set => this.WriteData(384UL, value, -1);
            }

            public string ExperimentId
            {
                get => this.ReadText(1, null);
                set => this.WriteText(1, value, null);
            }

            public string TreatmentId
            {
                get => this.ReadText(2, null);
                set => this.WriteText(2, value, null);
            }
        }
    }

    [
        System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"),
        TypeId(0xf6b17c769768d8ffUL)
    ]
    public class PlantingEvent : ICapnpSerializable
    {
        public const UInt64 typeId = 0xf6b17c769768d8ffUL;

        void ICapnpSerializable.Deserialize(DeserializerState arg_)
        {
            var reader = READER.create(arg_);
            PlantingDistribution = reader.PlantingDistribution;
            RowSpacingInCM = reader.RowSpacingInCM;
            RowDirectionInArcDeg = reader.RowDirectionInArcDeg;
            PlantingDepthInMM = reader.PlantingDepthInMM;
            PlotLayout = reader.PlotLayout;
            PlantingDate = CapnpSerializable.Create<Mas.Schema.Common.Date>(reader.PlantingDate);
            PlantPopulationAtPlantingInNoPerM2 = reader.PlantPopulationAtPlantingInNoPerM2;
            AverageEmergenceDate = CapnpSerializable.Create<Mas.Schema.Common.Date>(
                reader.AverageEmergenceDate
            );
            AveragePlantPopulationAtEmergenceInNoPerM2 =
                reader.AveragePlantPopulationAtEmergenceInNoPerM2;
            Notes = reader.Notes;
            ExperimentId = reader.ExperimentId;
            TreatmentId = reader.TreatmentId;
            applyDefaults();
        }

        public void serialize(WRITER writer)
        {
            writer.PlantingDistribution = PlantingDistribution;
            writer.RowSpacingInCM = RowSpacingInCM;
            writer.RowDirectionInArcDeg = RowDirectionInArcDeg;
            writer.PlantingDepthInMM = PlantingDepthInMM;
            writer.PlotLayout = PlotLayout;
            PlantingDate?.serialize(writer.PlantingDate);
            writer.PlantPopulationAtPlantingInNoPerM2 = PlantPopulationAtPlantingInNoPerM2;
            AverageEmergenceDate?.serialize(writer.AverageEmergenceDate);
            writer.AveragePlantPopulationAtEmergenceInNoPerM2 =
                AveragePlantPopulationAtEmergenceInNoPerM2;
            writer.Notes = Notes;
            writer.ExperimentId = ExperimentId;
            writer.TreatmentId = TreatmentId;
        }

        void ICapnpSerializable.Serialize(SerializerState arg_)
        {
            serialize(arg_.Rewrap<WRITER>());
        }

        public void applyDefaults() { }

        public string PlantingDistribution { get; set; }

        public double RowSpacingInCM { get; set; } = -1;
        public double RowDirectionInArcDeg { get; set; } = -9999;
        public short PlantingDepthInMM { get; set; } = -1;
        public string PlotLayout { get; set; }

        public Mas.Schema.Common.Date PlantingDate { get; set; }

        public short PlantPopulationAtPlantingInNoPerM2 { get; set; } = -1;
        public Mas.Schema.Common.Date AverageEmergenceDate { get; set; }

        public short AveragePlantPopulationAtEmergenceInNoPerM2 { get; set; } = -1;
        public string Notes { get; set; }

        public string ExperimentId { get; set; }

        public string TreatmentId { get; set; }

        public struct READER
        {
            readonly DeserializerState ctx;

            public READER(DeserializerState ctx)
            {
                this.ctx = ctx;
            }

            public static READER create(DeserializerState ctx) => new READER(ctx);

            public static implicit operator DeserializerState(READER reader) => reader.ctx;

            public static implicit operator READER(DeserializerState ctx) => new READER(ctx);

            public string PlantingDistribution => ctx.ReadText(0, null);
            public double RowSpacingInCM => ctx.ReadDataDouble(0UL, -1);
            public double RowDirectionInArcDeg => ctx.ReadDataDouble(64UL, -9999);
            public short PlantingDepthInMM => ctx.ReadDataShort(128UL, (short)-1);
            public string PlotLayout => ctx.ReadText(1, null);
            public Mas.Schema.Common.Date.READER PlantingDate =>
                ctx.ReadStruct(2, Mas.Schema.Common.Date.READER.create);
            public bool HasPlantingDate => ctx.IsStructFieldNonNull(2);
            public short PlantPopulationAtPlantingInNoPerM2 => ctx.ReadDataShort(144UL, (short)-1);
            public Mas.Schema.Common.Date.READER AverageEmergenceDate =>
                ctx.ReadStruct(3, Mas.Schema.Common.Date.READER.create);
            public bool HasAverageEmergenceDate => ctx.IsStructFieldNonNull(3);
            public short AveragePlantPopulationAtEmergenceInNoPerM2 =>
                ctx.ReadDataShort(160UL, (short)-1);
            public string Notes => ctx.ReadText(4, null);
            public string ExperimentId => ctx.ReadText(5, null);
            public string TreatmentId => ctx.ReadText(6, null);
        }

        public class WRITER : SerializerState
        {
            public WRITER()
            {
                this.SetStruct(3, 7);
            }

            public string PlantingDistribution
            {
                get => this.ReadText(0, null);
                set => this.WriteText(0, value, null);
            }

            public double RowSpacingInCM
            {
                get => this.ReadDataDouble(0UL, -1);
                set => this.WriteData(0UL, value, -1);
            }

            public double RowDirectionInArcDeg
            {
                get => this.ReadDataDouble(64UL, -9999);
                set => this.WriteData(64UL, value, -9999);
            }

            public short PlantingDepthInMM
            {
                get => this.ReadDataShort(128UL, (short)-1);
                set => this.WriteData(128UL, value, (short)-1);
            }

            public string PlotLayout
            {
                get => this.ReadText(1, null);
                set => this.WriteText(1, value, null);
            }

            public Mas.Schema.Common.Date.WRITER PlantingDate
            {
                get => BuildPointer<Mas.Schema.Common.Date.WRITER>(2);
                set => Link(2, value);
            }

            public short PlantPopulationAtPlantingInNoPerM2
            {
                get => this.ReadDataShort(144UL, (short)-1);
                set => this.WriteData(144UL, value, (short)-1);
            }

            public Mas.Schema.Common.Date.WRITER AverageEmergenceDate
            {
                get => BuildPointer<Mas.Schema.Common.Date.WRITER>(3);
                set => Link(3, value);
            }

            public short AveragePlantPopulationAtEmergenceInNoPerM2
            {
                get => this.ReadDataShort(160UL, (short)-1);
                set => this.WriteData(160UL, value, (short)-1);
            }

            public string Notes
            {
                get => this.ReadText(4, null);
                set => this.WriteText(4, value, null);
            }

            public string ExperimentId
            {
                get => this.ReadText(5, null);
                set => this.WriteText(5, value, null);
            }

            public string TreatmentId
            {
                get => this.ReadText(6, null);
                set => this.WriteText(6, value, null);
            }
        }
    }

    [
        System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"),
        TypeId(0x97eb30dbcf87911aUL)
    ]
    public class HarvestEvent : ICapnpSerializable
    {
        public const UInt64 typeId = 0x97eb30dbcf87911aUL;

        void ICapnpSerializable.Deserialize(DeserializerState arg_)
        {
            var reader = READER.create(arg_);
            Date = CapnpSerializable.Create<Mas.Schema.Common.Date>(reader.Date);
            HarvestMethod = reader.HarvestMethod;
            HarvestArea = reader.HarvestArea;
            Notes = reader.Notes;
            Comments = reader.Comments;
            ExperimentId = reader.ExperimentId;
            TreatmentId = reader.TreatmentId;
            applyDefaults();
        }

        public void serialize(WRITER writer)
        {
            Date?.serialize(writer.Date);
            writer.HarvestMethod = HarvestMethod;
            writer.HarvestArea = HarvestArea;
            writer.Notes = Notes;
            writer.Comments = Comments;
            writer.ExperimentId = ExperimentId;
            writer.TreatmentId = TreatmentId;
        }

        void ICapnpSerializable.Serialize(SerializerState arg_)
        {
            serialize(arg_.Rewrap<WRITER>());
        }

        public void applyDefaults() { }

        public Mas.Schema.Common.Date Date { get; set; }

        public string HarvestMethod { get; set; }

        public double HarvestArea { get; set; } = -1;
        public string Notes { get; set; }

        public string Comments { get; set; }

        public string ExperimentId { get; set; }

        public string TreatmentId { get; set; }

        public struct READER
        {
            readonly DeserializerState ctx;

            public READER(DeserializerState ctx)
            {
                this.ctx = ctx;
            }

            public static READER create(DeserializerState ctx) => new READER(ctx);

            public static implicit operator DeserializerState(READER reader) => reader.ctx;

            public static implicit operator READER(DeserializerState ctx) => new READER(ctx);

            public Mas.Schema.Common.Date.READER Date =>
                ctx.ReadStruct(0, Mas.Schema.Common.Date.READER.create);
            public bool HasDate => ctx.IsStructFieldNonNull(0);
            public string HarvestMethod => ctx.ReadText(1, null);
            public double HarvestArea => ctx.ReadDataDouble(0UL, -1);
            public string Notes => ctx.ReadText(2, null);
            public string Comments => ctx.ReadText(3, null);
            public string ExperimentId => ctx.ReadText(4, null);
            public string TreatmentId => ctx.ReadText(5, null);
        }

        public class WRITER : SerializerState
        {
            public WRITER()
            {
                this.SetStruct(1, 6);
            }

            public Mas.Schema.Common.Date.WRITER Date
            {
                get => BuildPointer<Mas.Schema.Common.Date.WRITER>(0);
                set => Link(0, value);
            }

            public string HarvestMethod
            {
                get => this.ReadText(1, null);
                set => this.WriteText(1, value, null);
            }

            public double HarvestArea
            {
                get => this.ReadDataDouble(0UL, -1);
                set => this.WriteData(0UL, value, -1);
            }

            public string Notes
            {
                get => this.ReadText(2, null);
                set => this.WriteText(2, value, null);
            }

            public string Comments
            {
                get => this.ReadText(3, null);
                set => this.WriteText(3, value, null);
            }

            public string ExperimentId
            {
                get => this.ReadText(4, null);
                set => this.WriteText(4, value, null);
            }

            public string TreatmentId
            {
                get => this.ReadText(5, null);
                set => this.WriteText(5, value, null);
            }
        }
    }

    [
        System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"),
        TypeId(0xcf2547b626594655UL)
    ]
    public class IrrigationEvent : ICapnpSerializable
    {
        public const UInt64 typeId = 0xcf2547b626594655UL;

        void ICapnpSerializable.Deserialize(DeserializerState arg_)
        {
            var reader = READER.create(arg_);
            Date = CapnpSerializable.Create<Mas.Schema.Common.Date>(reader.Date);
            Operation = reader.Operation;
            ApplicationDepth = reader.ApplicationDepth;
            Amount = reader.Amount;
            WaterNConcentrationInPerc = reader.WaterNConcentrationInPerc;
            Notes = reader.Notes;
            ExperimentId = reader.ExperimentId;
            TreatmentId = reader.TreatmentId;
            applyDefaults();
        }

        public void serialize(WRITER writer)
        {
            Date?.serialize(writer.Date);
            writer.Operation = Operation;
            writer.ApplicationDepth = ApplicationDepth;
            writer.Amount = Amount;
            writer.WaterNConcentrationInPerc = WaterNConcentrationInPerc;
            writer.Notes = Notes;
            writer.ExperimentId = ExperimentId;
            writer.TreatmentId = TreatmentId;
        }

        void ICapnpSerializable.Serialize(SerializerState arg_)
        {
            serialize(arg_.Rewrap<WRITER>());
        }

        public void applyDefaults() { }

        public Mas.Schema.Common.Date Date { get; set; }

        public string Operation { get; set; }

        public short ApplicationDepth { get; set; } = -9999;
        public short Amount { get; set; } = -1;
        public double WaterNConcentrationInPerc { get; set; } = -1;
        public string Notes { get; set; }

        public string ExperimentId { get; set; }

        public string TreatmentId { get; set; }

        public struct READER
        {
            readonly DeserializerState ctx;

            public READER(DeserializerState ctx)
            {
                this.ctx = ctx;
            }

            public static READER create(DeserializerState ctx) => new READER(ctx);

            public static implicit operator DeserializerState(READER reader) => reader.ctx;

            public static implicit operator READER(DeserializerState ctx) => new READER(ctx);

            public Mas.Schema.Common.Date.READER Date =>
                ctx.ReadStruct(0, Mas.Schema.Common.Date.READER.create);
            public bool HasDate => ctx.IsStructFieldNonNull(0);
            public string Operation => ctx.ReadText(1, null);
            public short ApplicationDepth => ctx.ReadDataShort(0UL, (short)-9999);
            public short Amount => ctx.ReadDataShort(16UL, (short)-1);
            public double WaterNConcentrationInPerc => ctx.ReadDataDouble(64UL, -1);
            public string Notes => ctx.ReadText(2, null);
            public string ExperimentId => ctx.ReadText(3, null);
            public string TreatmentId => ctx.ReadText(4, null);
        }

        public class WRITER : SerializerState
        {
            public WRITER()
            {
                this.SetStruct(2, 5);
            }

            public Mas.Schema.Common.Date.WRITER Date
            {
                get => BuildPointer<Mas.Schema.Common.Date.WRITER>(0);
                set => Link(0, value);
            }

            public string Operation
            {
                get => this.ReadText(1, null);
                set => this.WriteText(1, value, null);
            }

            public short ApplicationDepth
            {
                get => this.ReadDataShort(0UL, (short)-9999);
                set => this.WriteData(0UL, value, (short)-9999);
            }

            public short Amount
            {
                get => this.ReadDataShort(16UL, (short)-1);
                set => this.WriteData(16UL, value, (short)-1);
            }

            public double WaterNConcentrationInPerc
            {
                get => this.ReadDataDouble(64UL, -1);
                set => this.WriteData(64UL, value, -1);
            }

            public string Notes
            {
                get => this.ReadText(2, null);
                set => this.WriteText(2, value, null);
            }

            public string ExperimentId
            {
                get => this.ReadText(3, null);
                set => this.WriteText(3, value, null);
            }

            public string TreatmentId
            {
                get => this.ReadText(4, null);
                set => this.WriteText(4, value, null);
            }
        }
    }

    [
        System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"),
        TypeId(0xa5df81bae928e6daUL)
    ]
    public class FertilizerEvent : ICapnpSerializable
    {
        public const UInt64 typeId = 0xa5df81bae928e6daUL;

        void ICapnpSerializable.Deserialize(DeserializerState arg_)
        {
            var reader = READER.create(arg_);
            Date = CapnpSerializable.Create<Mas.Schema.Common.Date>(reader.Date);
            ApplicationMethod = reader.ApplicationMethod;
            ApplicationDepthInCM = reader.ApplicationDepthInCM;
            Material = reader.Material;
            AppliedNInKGNPerHA = reader.AppliedNInKGNPerHA;
            AppliedNO3InKGNperHA = reader.AppliedNO3InKGNperHA;
            AppliedNH4InKGNperHA = reader.AppliedNH4InKGNperHA;
            Notes = reader.Notes;
            ExperimentId = reader.ExperimentId;
            TreatmentId = reader.TreatmentId;
            applyDefaults();
        }

        public void serialize(WRITER writer)
        {
            Date?.serialize(writer.Date);
            writer.ApplicationMethod = ApplicationMethod;
            writer.ApplicationDepthInCM = ApplicationDepthInCM;
            writer.Material = Material;
            writer.AppliedNInKGNPerHA = AppliedNInKGNPerHA;
            writer.AppliedNO3InKGNperHA = AppliedNO3InKGNperHA;
            writer.AppliedNH4InKGNperHA = AppliedNH4InKGNperHA;
            writer.Notes = Notes;
            writer.ExperimentId = ExperimentId;
            writer.TreatmentId = TreatmentId;
        }

        void ICapnpSerializable.Serialize(SerializerState arg_)
        {
            serialize(arg_.Rewrap<WRITER>());
        }

        public void applyDefaults() { }

        public Mas.Schema.Common.Date Date { get; set; }

        public string ApplicationMethod { get; set; }

        public short ApplicationDepthInCM { get; set; } = -1;
        public string Material { get; set; }

        public short AppliedNInKGNPerHA { get; set; } = -1;
        public short AppliedNO3InKGNperHA { get; set; } = -1;
        public short AppliedNH4InKGNperHA { get; set; } = -1;
        public string Notes { get; set; }

        public string ExperimentId { get; set; }

        public string TreatmentId { get; set; }

        public struct READER
        {
            readonly DeserializerState ctx;

            public READER(DeserializerState ctx)
            {
                this.ctx = ctx;
            }

            public static READER create(DeserializerState ctx) => new READER(ctx);

            public static implicit operator DeserializerState(READER reader) => reader.ctx;

            public static implicit operator READER(DeserializerState ctx) => new READER(ctx);

            public Mas.Schema.Common.Date.READER Date =>
                ctx.ReadStruct(0, Mas.Schema.Common.Date.READER.create);
            public bool HasDate => ctx.IsStructFieldNonNull(0);
            public string ApplicationMethod => ctx.ReadText(1, null);
            public short ApplicationDepthInCM => ctx.ReadDataShort(0UL, (short)-1);
            public string Material => ctx.ReadText(2, null);
            public short AppliedNInKGNPerHA => ctx.ReadDataShort(16UL, (short)-1);
            public short AppliedNO3InKGNperHA => ctx.ReadDataShort(32UL, (short)-1);
            public short AppliedNH4InKGNperHA => ctx.ReadDataShort(48UL, (short)-1);
            public string Notes => ctx.ReadText(3, null);
            public string ExperimentId => ctx.ReadText(4, null);
            public string TreatmentId => ctx.ReadText(5, null);
        }

        public class WRITER : SerializerState
        {
            public WRITER()
            {
                this.SetStruct(1, 6);
            }

            public Mas.Schema.Common.Date.WRITER Date
            {
                get => BuildPointer<Mas.Schema.Common.Date.WRITER>(0);
                set => Link(0, value);
            }

            public string ApplicationMethod
            {
                get => this.ReadText(1, null);
                set => this.WriteText(1, value, null);
            }

            public short ApplicationDepthInCM
            {
                get => this.ReadDataShort(0UL, (short)-1);
                set => this.WriteData(0UL, value, (short)-1);
            }

            public string Material
            {
                get => this.ReadText(2, null);
                set => this.WriteText(2, value, null);
            }

            public short AppliedNInKGNPerHA
            {
                get => this.ReadDataShort(16UL, (short)-1);
                set => this.WriteData(16UL, value, (short)-1);
            }

            public short AppliedNO3InKGNperHA
            {
                get => this.ReadDataShort(32UL, (short)-1);
                set => this.WriteData(32UL, value, (short)-1);
            }

            public short AppliedNH4InKGNperHA
            {
                get => this.ReadDataShort(48UL, (short)-1);
                set => this.WriteData(48UL, value, (short)-1);
            }

            public string Notes
            {
                get => this.ReadText(3, null);
                set => this.WriteText(3, value, null);
            }

            public string ExperimentId
            {
                get => this.ReadText(4, null);
                set => this.WriteText(4, value, null);
            }

            public string TreatmentId
            {
                get => this.ReadText(5, null);
                set => this.WriteText(5, value, null);
            }
        }
    }

    [
        System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"),
        TypeId(0xe82432f4ef15a586UL)
    ]
    public class Residue : ICapnpSerializable
    {
        public const UInt64 typeId = 0xe82432f4ef15a586UL;

        void ICapnpSerializable.Deserialize(DeserializerState arg_)
        {
            var reader = READER.create(arg_);
            InitialMeasureDate = CapnpSerializable.Create<Mas.Schema.Common.Date>(
                reader.InitialMeasureDate
            );
            IncorporationDepth = reader.IncorporationDepth;
            PercentIncorporated = reader.PercentIncorporated;
            PrevCropCode = reader.PrevCropCode;
            AboveGroundWeight = reader.AboveGroundWeight;
            AboveGroundNConcentrationInPerc = reader.AboveGroundNConcentrationInPerc;
            RootWeightPreviousCrop = reader.RootWeightPreviousCrop;
            ExperimentId = reader.ExperimentId;
            TreatmentId = reader.TreatmentId;
            applyDefaults();
        }

        public void serialize(WRITER writer)
        {
            InitialMeasureDate?.serialize(writer.InitialMeasureDate);
            writer.IncorporationDepth = IncorporationDepth;
            writer.PercentIncorporated = PercentIncorporated;
            writer.PrevCropCode = PrevCropCode;
            writer.AboveGroundWeight = AboveGroundWeight;
            writer.AboveGroundNConcentrationInPerc = AboveGroundNConcentrationInPerc;
            writer.RootWeightPreviousCrop = RootWeightPreviousCrop;
            writer.ExperimentId = ExperimentId;
            writer.TreatmentId = TreatmentId;
        }

        void ICapnpSerializable.Serialize(SerializerState arg_)
        {
            serialize(arg_.Rewrap<WRITER>());
        }

        public void applyDefaults() { }

        public Mas.Schema.Common.Date InitialMeasureDate { get; set; }

        public short IncorporationDepth { get; set; } = -1;
        public double PercentIncorporated { get; set; } = -1;
        public string PrevCropCode { get; set; }

        public double AboveGroundWeight { get; set; } = -1;
        public double AboveGroundNConcentrationInPerc { get; set; } = -1;
        public double RootWeightPreviousCrop { get; set; } = -1;
        public string ExperimentId { get; set; }

        public string TreatmentId { get; set; }

        public struct READER
        {
            readonly DeserializerState ctx;

            public READER(DeserializerState ctx)
            {
                this.ctx = ctx;
            }

            public static READER create(DeserializerState ctx) => new READER(ctx);

            public static implicit operator DeserializerState(READER reader) => reader.ctx;

            public static implicit operator READER(DeserializerState ctx) => new READER(ctx);

            public Mas.Schema.Common.Date.READER InitialMeasureDate =>
                ctx.ReadStruct(0, Mas.Schema.Common.Date.READER.create);
            public bool HasInitialMeasureDate => ctx.IsStructFieldNonNull(0);
            public short IncorporationDepth => ctx.ReadDataShort(0UL, (short)-1);
            public double PercentIncorporated => ctx.ReadDataDouble(64UL, -1);
            public string PrevCropCode => ctx.ReadText(1, null);
            public double AboveGroundWeight => ctx.ReadDataDouble(128UL, -1);
            public double AboveGroundNConcentrationInPerc => ctx.ReadDataDouble(192UL, -1);
            public double RootWeightPreviousCrop => ctx.ReadDataDouble(256UL, -1);
            public string ExperimentId => ctx.ReadText(2, null);
            public string TreatmentId => ctx.ReadText(3, null);
        }

        public class WRITER : SerializerState
        {
            public WRITER()
            {
                this.SetStruct(5, 4);
            }

            public Mas.Schema.Common.Date.WRITER InitialMeasureDate
            {
                get => BuildPointer<Mas.Schema.Common.Date.WRITER>(0);
                set => Link(0, value);
            }

            public short IncorporationDepth
            {
                get => this.ReadDataShort(0UL, (short)-1);
                set => this.WriteData(0UL, value, (short)-1);
            }

            public double PercentIncorporated
            {
                get => this.ReadDataDouble(64UL, -1);
                set => this.WriteData(64UL, value, -1);
            }

            public string PrevCropCode
            {
                get => this.ReadText(1, null);
                set => this.WriteText(1, value, null);
            }

            public double AboveGroundWeight
            {
                get => this.ReadDataDouble(128UL, -1);
                set => this.WriteData(128UL, value, -1);
            }

            public double AboveGroundNConcentrationInPerc
            {
                get => this.ReadDataDouble(192UL, -1);
                set => this.WriteData(192UL, value, -1);
            }

            public double RootWeightPreviousCrop
            {
                get => this.ReadDataDouble(256UL, -1);
                set => this.WriteData(256UL, value, -1);
            }

            public string ExperimentId
            {
                get => this.ReadText(2, null);
                set => this.WriteText(2, value, null);
            }

            public string TreatmentId
            {
                get => this.ReadText(3, null);
                set => this.WriteText(3, value, null);
            }
        }
    }

    [
        System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"),
        TypeId(0xb52867725b843050UL)
    ]
    public class EnvironmentModification : ICapnpSerializable
    {
        public const UInt64 typeId = 0xb52867725b843050UL;

        void ICapnpSerializable.Deserialize(DeserializerState arg_)
        {
            var reader = READER.create(arg_);
            Date = CapnpSerializable.Create<Mas.Schema.Common.Date>(reader.Date);
            CodeCO2 = reader.CodeCO2;
            ValueCO2 = reader.ValueCO2;
            Notes = reader.Notes;
            ExperimentId = reader.ExperimentId;
            TreatmentId = reader.TreatmentId;
            applyDefaults();
        }

        public void serialize(WRITER writer)
        {
            Date?.serialize(writer.Date);
            writer.CodeCO2 = CodeCO2;
            writer.ValueCO2 = ValueCO2;
            writer.Notes = Notes;
            writer.ExperimentId = ExperimentId;
            writer.TreatmentId = TreatmentId;
        }

        void ICapnpSerializable.Serialize(SerializerState arg_)
        {
            serialize(arg_.Rewrap<WRITER>());
        }

        public void applyDefaults() { }

        public Mas.Schema.Common.Date Date { get; set; }

        public string CodeCO2 { get; set; }

        public short ValueCO2 { get; set; } = -1;
        public string Notes { get; set; }

        public string ExperimentId { get; set; }

        public string TreatmentId { get; set; }

        public struct READER
        {
            readonly DeserializerState ctx;

            public READER(DeserializerState ctx)
            {
                this.ctx = ctx;
            }

            public static READER create(DeserializerState ctx) => new READER(ctx);

            public static implicit operator DeserializerState(READER reader) => reader.ctx;

            public static implicit operator READER(DeserializerState ctx) => new READER(ctx);

            public Mas.Schema.Common.Date.READER Date =>
                ctx.ReadStruct(0, Mas.Schema.Common.Date.READER.create);
            public bool HasDate => ctx.IsStructFieldNonNull(0);
            public string CodeCO2 => ctx.ReadText(1, null);
            public short ValueCO2 => ctx.ReadDataShort(0UL, (short)-1);
            public string Notes => ctx.ReadText(2, null);
            public string ExperimentId => ctx.ReadText(3, null);
            public string TreatmentId => ctx.ReadText(4, null);
        }

        public class WRITER : SerializerState
        {
            public WRITER()
            {
                this.SetStruct(1, 5);
            }

            public Mas.Schema.Common.Date.WRITER Date
            {
                get => BuildPointer<Mas.Schema.Common.Date.WRITER>(0);
                set => Link(0, value);
            }

            public string CodeCO2
            {
                get => this.ReadText(1, null);
                set => this.WriteText(1, value, null);
            }

            public short ValueCO2
            {
                get => this.ReadDataShort(0UL, (short)-1);
                set => this.WriteData(0UL, value, (short)-1);
            }

            public string Notes
            {
                get => this.ReadText(2, null);
                set => this.WriteText(2, value, null);
            }

            public string ExperimentId
            {
                get => this.ReadText(3, null);
                set => this.WriteText(3, value, null);
            }

            public string TreatmentId
            {
                get => this.ReadText(4, null);
                set => this.WriteText(4, value, null);
            }
        }
    }
}
