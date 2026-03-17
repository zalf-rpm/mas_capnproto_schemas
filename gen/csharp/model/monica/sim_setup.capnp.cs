using System;
using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;
using Capnp;
using Capnp.Rpc;

namespace CapnpGen
{
    [
        System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"),
        TypeId(0xa4b1a2ad9a77fdc7UL)
    ]
    public class Setup : ICapnpSerializable
    {
        public const UInt64 typeId = 0xa4b1a2ad9a77fdc7UL;

        void ICapnpSerializable.Deserialize(DeserializerState arg_)
        {
            var reader = READER.create(arg_);
            RunId = reader.RunId;
            SowingTime = reader.SowingTime;
            HarvestTime = reader.HarvestTime;
            CropId = reader.CropId;
            SimJson = reader.SimJson;
            CropJson = reader.CropJson;
            SiteJson = reader.SiteJson;
            StartDate = reader.StartDate;
            EndDate = reader.EndDate;
            GroundwaterLevel = reader.GroundwaterLevel;
            ImpenetrableLayer = reader.ImpenetrableLayer;
            Elevation = reader.Elevation;
            Slope = reader.Slope;
            Latitude = reader.Latitude;
            Landcover = reader.Landcover;
            Fertilization = reader.Fertilization;
            NitrogenResponseOn = reader.NitrogenResponseOn;
            Irrigation = reader.Irrigation;
            WaterDeficitResponseOn = reader.WaterDeficitResponseOn;
            EmergenceMoistureControlOn = reader.EmergenceMoistureControlOn;
            EmergenceFloodingControlOn = reader.EmergenceFloodingControlOn;
            LeafExtensionModifier = reader.LeafExtensionModifier;
            Co2 = reader.Co2;
            O3 = reader.O3;
            FieldConditionModifier = reader.FieldConditionModifier;
            StageTemperatureSum = reader.StageTemperatureSum;
            UseVernalisationFix = reader.UseVernalisationFix;
            Comment = reader.Comment;
            applyDefaults();
        }

        public void serialize(WRITER writer)
        {
            writer.RunId = RunId;
            writer.SowingTime = SowingTime;
            writer.HarvestTime = HarvestTime;
            writer.CropId = CropId;
            writer.SimJson = SimJson;
            writer.CropJson = CropJson;
            writer.SiteJson = SiteJson;
            writer.StartDate = StartDate;
            writer.EndDate = EndDate;
            writer.GroundwaterLevel = GroundwaterLevel;
            writer.ImpenetrableLayer = ImpenetrableLayer;
            writer.Elevation = Elevation;
            writer.Slope = Slope;
            writer.Latitude = Latitude;
            writer.Landcover = Landcover;
            writer.Fertilization = Fertilization;
            writer.NitrogenResponseOn = NitrogenResponseOn;
            writer.Irrigation = Irrigation;
            writer.WaterDeficitResponseOn = WaterDeficitResponseOn;
            writer.EmergenceMoistureControlOn = EmergenceMoistureControlOn;
            writer.EmergenceFloodingControlOn = EmergenceFloodingControlOn;
            writer.LeafExtensionModifier = LeafExtensionModifier;
            writer.Co2 = Co2;
            writer.O3 = O3;
            writer.FieldConditionModifier = FieldConditionModifier;
            writer.StageTemperatureSum = StageTemperatureSum;
            writer.UseVernalisationFix = UseVernalisationFix;
            writer.Comment = Comment;
        }

        void ICapnpSerializable.Serialize(SerializerState arg_)
        {
            serialize(arg_.Rewrap<WRITER>());
        }

        public void applyDefaults() { }

        public long RunId { get; set; }
        public string SowingTime { get; set; }
        public string HarvestTime { get; set; }
        public string CropId { get; set; }
        public string SimJson { get; set; }
        public string CropJson { get; set; }
        public string SiteJson { get; set; }
        public string StartDate { get; set; }
        public string EndDate { get; set; }
        public bool GroundwaterLevel { get; set; }
        public bool ImpenetrableLayer { get; set; }
        public bool Elevation { get; set; }
        public bool Slope { get; set; }
        public bool Latitude { get; set; }
        public bool Landcover { get; set; }
        public bool Fertilization { get; set; }
        public bool NitrogenResponseOn { get; set; }
        public bool Irrigation { get; set; }
        public bool WaterDeficitResponseOn { get; set; }
        public bool EmergenceMoistureControlOn { get; set; }
        public bool EmergenceFloodingControlOn { get; set; }
        public bool LeafExtensionModifier { get; set; }
        public float Co2 { get; set; }
        public float O3 { get; set; }
        public float FieldConditionModifier { get; set; }
        public string StageTemperatureSum { get; set; }
        public bool UseVernalisationFix { get; set; }
        public string Comment { get; set; }

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

            public long RunId => ctx.ReadDataLong(0UL, 0L);
            public string SowingTime => ctx.ReadText(0, null);
            public string HarvestTime => ctx.ReadText(1, null);
            public string CropId => ctx.ReadText(2, null);
            public string SimJson => ctx.ReadText(3, null);
            public string CropJson => ctx.ReadText(4, null);
            public string SiteJson => ctx.ReadText(5, null);
            public string StartDate => ctx.ReadText(6, null);
            public string EndDate => ctx.ReadText(7, null);
            public bool GroundwaterLevel => ctx.ReadDataBool(64UL, false);
            public bool ImpenetrableLayer => ctx.ReadDataBool(65UL, false);
            public bool Elevation => ctx.ReadDataBool(66UL, false);
            public bool Slope => ctx.ReadDataBool(67UL, false);
            public bool Latitude => ctx.ReadDataBool(68UL, false);
            public bool Landcover => ctx.ReadDataBool(69UL, false);
            public bool Fertilization => ctx.ReadDataBool(70UL, false);
            public bool NitrogenResponseOn => ctx.ReadDataBool(71UL, false);
            public bool Irrigation => ctx.ReadDataBool(72UL, false);
            public bool WaterDeficitResponseOn => ctx.ReadDataBool(73UL, false);
            public bool EmergenceMoistureControlOn => ctx.ReadDataBool(74UL, false);
            public bool EmergenceFloodingControlOn => ctx.ReadDataBool(75UL, false);
            public bool LeafExtensionModifier => ctx.ReadDataBool(76UL, false);
            public float Co2 => ctx.ReadDataFloat(96UL, 0F);
            public float O3 => ctx.ReadDataFloat(128UL, 0F);
            public float FieldConditionModifier => ctx.ReadDataFloat(160UL, 0F);
            public string StageTemperatureSum => ctx.ReadText(8, null);
            public bool UseVernalisationFix => ctx.ReadDataBool(77UL, false);
            public string Comment => ctx.ReadText(9, null);
        }

        public class WRITER : SerializerState
        {
            public WRITER()
            {
                this.SetStruct(3, 10);
            }

            public long RunId
            {
                get => this.ReadDataLong(0UL, 0L);
                set => this.WriteData(0UL, value, 0L);
            }
            public string SowingTime
            {
                get => this.ReadText(0, null);
                set => this.WriteText(0, value, null);
            }
            public string HarvestTime
            {
                get => this.ReadText(1, null);
                set => this.WriteText(1, value, null);
            }
            public string CropId
            {
                get => this.ReadText(2, null);
                set => this.WriteText(2, value, null);
            }
            public string SimJson
            {
                get => this.ReadText(3, null);
                set => this.WriteText(3, value, null);
            }
            public string CropJson
            {
                get => this.ReadText(4, null);
                set => this.WriteText(4, value, null);
            }
            public string SiteJson
            {
                get => this.ReadText(5, null);
                set => this.WriteText(5, value, null);
            }
            public string StartDate
            {
                get => this.ReadText(6, null);
                set => this.WriteText(6, value, null);
            }
            public string EndDate
            {
                get => this.ReadText(7, null);
                set => this.WriteText(7, value, null);
            }
            public bool GroundwaterLevel
            {
                get => this.ReadDataBool(64UL, false);
                set => this.WriteData(64UL, value, false);
            }
            public bool ImpenetrableLayer
            {
                get => this.ReadDataBool(65UL, false);
                set => this.WriteData(65UL, value, false);
            }
            public bool Elevation
            {
                get => this.ReadDataBool(66UL, false);
                set => this.WriteData(66UL, value, false);
            }
            public bool Slope
            {
                get => this.ReadDataBool(67UL, false);
                set => this.WriteData(67UL, value, false);
            }
            public bool Latitude
            {
                get => this.ReadDataBool(68UL, false);
                set => this.WriteData(68UL, value, false);
            }
            public bool Landcover
            {
                get => this.ReadDataBool(69UL, false);
                set => this.WriteData(69UL, value, false);
            }
            public bool Fertilization
            {
                get => this.ReadDataBool(70UL, false);
                set => this.WriteData(70UL, value, false);
            }
            public bool NitrogenResponseOn
            {
                get => this.ReadDataBool(71UL, false);
                set => this.WriteData(71UL, value, false);
            }
            public bool Irrigation
            {
                get => this.ReadDataBool(72UL, false);
                set => this.WriteData(72UL, value, false);
            }
            public bool WaterDeficitResponseOn
            {
                get => this.ReadDataBool(73UL, false);
                set => this.WriteData(73UL, value, false);
            }
            public bool EmergenceMoistureControlOn
            {
                get => this.ReadDataBool(74UL, false);
                set => this.WriteData(74UL, value, false);
            }
            public bool EmergenceFloodingControlOn
            {
                get => this.ReadDataBool(75UL, false);
                set => this.WriteData(75UL, value, false);
            }
            public bool LeafExtensionModifier
            {
                get => this.ReadDataBool(76UL, false);
                set => this.WriteData(76UL, value, false);
            }
            public float Co2
            {
                get => this.ReadDataFloat(96UL, 0F);
                set => this.WriteData(96UL, value, 0F);
            }
            public float O3
            {
                get => this.ReadDataFloat(128UL, 0F);
                set => this.WriteData(128UL, value, 0F);
            }
            public float FieldConditionModifier
            {
                get => this.ReadDataFloat(160UL, 0F);
                set => this.WriteData(160UL, value, 0F);
            }
            public string StageTemperatureSum
            {
                get => this.ReadText(8, null);
                set => this.WriteText(8, value, null);
            }
            public bool UseVernalisationFix
            {
                get => this.ReadDataBool(77UL, false);
                set => this.WriteData(77UL, value, false);
            }
            public string Comment
            {
                get => this.ReadText(9, null);
                set => this.WriteText(9, value, null);
            }
        }
    }
}
