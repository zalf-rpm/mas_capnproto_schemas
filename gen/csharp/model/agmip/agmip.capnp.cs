using System;
using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;
using Capnp;
using Capnp.Rpc;

namespace Mas.Schema.Model.Agmip
{
    [
        System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"),
        TypeId(0xdee9ee5191b1e4a2UL)
    ]
    public class FieldExperimentDataTemplate : ICapnpSerializable
    {
        public const UInt64 typeId = 0xdee9ee5191b1e4a2UL;

        void ICapnpSerializable.Deserialize(DeserializerState arg_)
        {
            var reader = READER.create(arg_);
            SoilProfile = reader.SoilProfile;
            Soil = CapnpSerializable.Create<Mas.Schema.Common.StructuredText>(reader.Soil);
            Plot = CapnpSerializable.Create<Mas.Schema.Common.StructuredText>(reader.Plot);
            Timeseries = reader.Timeseries;
            Treatment = CapnpSerializable.Create<Mas.Schema.Common.StructuredText>(
                reader.Treatment
            );
            Experiment = CapnpSerializable.Create<Mas.Schema.Common.StructuredText>(
                reader.Experiment
            );
            applyDefaults();
        }

        public void serialize(WRITER writer)
        {
            writer.SoilProfile = SoilProfile;
            Soil?.serialize(writer.Soil);
            Plot?.serialize(writer.Plot);
            writer.Timeseries = Timeseries;
            Treatment?.serialize(writer.Treatment);
            Experiment?.serialize(writer.Experiment);
        }

        void ICapnpSerializable.Serialize(SerializerState arg_)
        {
            serialize(arg_.Rewrap<WRITER>());
        }

        public void applyDefaults() { }

        public Mas.Schema.Soil.IProfile SoilProfile { get; set; }
        public Mas.Schema.Common.StructuredText Soil { get; set; }
        public Mas.Schema.Common.StructuredText Plot { get; set; }
        public Mas.Schema.Climate.ITimeSeries Timeseries { get; set; }
        public Mas.Schema.Common.StructuredText Treatment { get; set; }
        public Mas.Schema.Common.StructuredText Experiment { get; set; }

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

            public Mas.Schema.Soil.IProfile SoilProfile => ctx.ReadCap<Mas.Schema.Soil.IProfile>(0);
            public Mas.Schema.Common.StructuredText.READER Soil =>
                ctx.ReadStruct(1, Mas.Schema.Common.StructuredText.READER.create);
            public bool HasSoil => ctx.IsStructFieldNonNull(1);
            public Mas.Schema.Common.StructuredText.READER Plot =>
                ctx.ReadStruct(2, Mas.Schema.Common.StructuredText.READER.create);
            public bool HasPlot => ctx.IsStructFieldNonNull(2);
            public Mas.Schema.Climate.ITimeSeries Timeseries =>
                ctx.ReadCap<Mas.Schema.Climate.ITimeSeries>(3);
            public Mas.Schema.Common.StructuredText.READER Treatment =>
                ctx.ReadStruct(4, Mas.Schema.Common.StructuredText.READER.create);
            public bool HasTreatment => ctx.IsStructFieldNonNull(4);
            public Mas.Schema.Common.StructuredText.READER Experiment =>
                ctx.ReadStruct(5, Mas.Schema.Common.StructuredText.READER.create);
            public bool HasExperiment => ctx.IsStructFieldNonNull(5);
        }

        public class WRITER : SerializerState
        {
            public WRITER()
            {
                this.SetStruct(0, 6);
            }

            public Mas.Schema.Soil.IProfile SoilProfile
            {
                get => ReadCap<Mas.Schema.Soil.IProfile>(0);
                set => LinkObject(0, value);
            }
            public Mas.Schema.Common.StructuredText.WRITER Soil
            {
                get => BuildPointer<Mas.Schema.Common.StructuredText.WRITER>(1);
                set => Link(1, value);
            }
            public Mas.Schema.Common.StructuredText.WRITER Plot
            {
                get => BuildPointer<Mas.Schema.Common.StructuredText.WRITER>(2);
                set => Link(2, value);
            }
            public Mas.Schema.Climate.ITimeSeries Timeseries
            {
                get => ReadCap<Mas.Schema.Climate.ITimeSeries>(3);
                set => LinkObject(3, value);
            }
            public Mas.Schema.Common.StructuredText.WRITER Treatment
            {
                get => BuildPointer<Mas.Schema.Common.StructuredText.WRITER>(4);
                set => Link(4, value);
            }
            public Mas.Schema.Common.StructuredText.WRITER Experiment
            {
                get => BuildPointer<Mas.Schema.Common.StructuredText.WRITER>(5);
                set => Link(5, value);
            }
        }
    }
}
