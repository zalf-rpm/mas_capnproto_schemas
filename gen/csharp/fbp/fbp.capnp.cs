using Capnp;
using Capnp.Rpc;
using System;
using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;

namespace Mas.Schema.Fbp
{
    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xaf0a1dc4709a5ccfUL)]
    public class IP : ICapnpSerializable
    {
        public const UInt64 typeId = 0xaf0a1dc4709a5ccfUL;
        void ICapnpSerializable.Deserialize(DeserializerState arg_)
        {
            var reader = READER.create(arg_);
            Attributes = reader.Attributes?.ToReadOnlyList(_ => CapnpSerializable.Create<Mas.Schema.Fbp.IP.KV>(_));
            Content = CapnpSerializable.Create<object>(reader.Content);
            TheType = reader.TheType;
            applyDefaults();
        }

        public void serialize(WRITER writer)
        {
            writer.Attributes.Init(Attributes, (_s1, _v1) => _v1?.serialize(_s1));
            writer.Content.SetObject(Content);
            writer.TheType = TheType;
        }

        void ICapnpSerializable.Serialize(SerializerState arg_)
        {
            serialize(arg_.Rewrap<WRITER>());
        }

        public void applyDefaults()
        {
        }

        public IReadOnlyList<Mas.Schema.Fbp.IP.KV> Attributes
        {
            get;
            set;
        }

        public object Content
        {
            get;
            set;
        }

        public Mas.Schema.Fbp.IP.Type TheType
        {
            get;
            set;
        }

        = Mas.Schema.Fbp.IP.Type.standard;
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
            public IReadOnlyList<Mas.Schema.Fbp.IP.KV.READER> Attributes => ctx.ReadList(0).Cast(Mas.Schema.Fbp.IP.KV.READER.create);
            public bool HasAttributes => ctx.IsStructFieldNonNull(0);
            public DeserializerState Content => ctx.StructReadPointer(1);
            public Mas.Schema.Fbp.IP.Type TheType => (Mas.Schema.Fbp.IP.Type)ctx.ReadDataUShort(0UL, (ushort)0);
        }

        public class WRITER : SerializerState
        {
            public WRITER()
            {
                this.SetStruct(1, 2);
            }

            public ListOfStructsSerializer<Mas.Schema.Fbp.IP.KV.WRITER> Attributes
            {
                get => BuildPointer<ListOfStructsSerializer<Mas.Schema.Fbp.IP.KV.WRITER>>(0);
                set => Link(0, value);
            }

            public DynamicSerializerState Content
            {
                get => BuildPointer<DynamicSerializerState>(1);
                set => Link(1, value);
            }

            public Mas.Schema.Fbp.IP.Type TheType
            {
                get => (Mas.Schema.Fbp.IP.Type)this.ReadDataUShort(0UL, (ushort)0);
                set => this.WriteData(0UL, (ushort)value, (ushort)0);
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0x9e9e5391e0c499e6UL)]
        public class KV : ICapnpSerializable
        {
            public const UInt64 typeId = 0x9e9e5391e0c499e6UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                Key = reader.Key;
                Desc = reader.Desc;
                Value = CapnpSerializable.Create<object>(reader.Value);
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.Key = Key;
                writer.Desc = Desc;
                writer.Value.SetObject(Value);
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public string Key
            {
                get;
                set;
            }

            public string Desc
            {
                get;
                set;
            }

            public object Value
            {
                get;
                set;
            }

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
                public string Key => ctx.ReadText(0, null);
                public string Desc => ctx.ReadText(1, null);
                public DeserializerState Value => ctx.StructReadPointer(2);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 3);
                }

                public string Key
                {
                    get => this.ReadText(0, null);
                    set => this.WriteText(0, value, null);
                }

                public string Desc
                {
                    get => this.ReadText(1, null);
                    set => this.WriteText(1, value, null);
                }

                public DynamicSerializerState Value
                {
                    get => BuildPointer<DynamicSerializerState>(2);
                    set => Link(2, value);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xf684cae29bdc484eUL)]
        public enum Type : ushort
        {
            standard,
            openBracket,
            closeBracket
        }
    }

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xf3705fb36d44a21fUL)]
    public class IIP : ICapnpSerializable
    {
        public const UInt64 typeId = 0xf3705fb36d44a21fUL;
        void ICapnpSerializable.Deserialize(DeserializerState arg_)
        {
            var reader = READER.create(arg_);
            Content = CapnpSerializable.Create<object>(reader.Content);
            applyDefaults();
        }

        public void serialize(WRITER writer)
        {
            writer.Content.SetObject(Content);
        }

        void ICapnpSerializable.Serialize(SerializerState arg_)
        {
            serialize(arg_.Rewrap<WRITER>());
        }

        public void applyDefaults()
        {
        }

        public object Content
        {
            get;
            set;
        }

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
            public DeserializerState Content => ctx.StructReadPointer(0);
        }

        public class WRITER : SerializerState
        {
            public WRITER()
            {
                this.SetStruct(0, 1);
            }

            public DynamicSerializerState Content
            {
                get => BuildPointer<DynamicSerializerState>(0);
                set => Link(0, value);
            }
        }
    }

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0x9c62c32b2ff2b1e8UL), Proxy(typeof(Channel_Proxy<>)), Skeleton(typeof(Channel_Skeleton<>))]
    public interface IChannel<TV> : Mas.Schema.Common.IIdentifiable, Mas.Schema.Persistence.IPersistent where TV : class
    {
        Task SetBufferSize(ulong size, CancellationToken cancellationToken_ = default);
        Task<Mas.Schema.Fbp.Channel<TV>.IReader> Reader(CancellationToken cancellationToken_ = default);
        Task<Mas.Schema.Fbp.Channel<TV>.IWriter> Writer(CancellationToken cancellationToken_ = default);
        Task<(Mas.Schema.Fbp.Channel<TV>.IReader, Mas.Schema.Fbp.Channel<TV>.IWriter)> Endpoints(CancellationToken cancellationToken_ = default);
        Task SetAutoCloseSemantics(Mas.Schema.Fbp.Channel<TV>.CloseSemantics cs, CancellationToken cancellationToken_ = default);
        Task Close(bool waitForEmptyBuffer, CancellationToken cancellationToken_ = default);
    }

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0x9c62c32b2ff2b1e8UL)]
    public class Channel_Proxy<TV> : Proxy, IChannel<TV> where TV : class
    {
        public async Task SetBufferSize(ulong size, CancellationToken cancellationToken_ = default)
        {
            var in_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.Channel<TV>.Params_SetBufferSize.WRITER>();
            var arg_ = new Mas.Schema.Fbp.Channel<TV>.Params_SetBufferSize()
            {Size = size};
            arg_?.serialize(in_);
            using (var d_ = await Call(11268783807889846760UL, 0, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_).WhenReturned)
            {
                var r_ = CapnpSerializable.Create<Mas.Schema.Fbp.Channel<TV>.Result_SetBufferSize>(d_);
                return;
            }
        }

        public Task<Mas.Schema.Fbp.Channel<TV>.IReader> Reader(CancellationToken cancellationToken_ = default)
        {
            var in_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.Channel<TV>.Params_Reader.WRITER>();
            var arg_ = new Mas.Schema.Fbp.Channel<TV>.Params_Reader()
            {};
            arg_?.serialize(in_);
            return Impatient.MakePipelineAware(Call(11268783807889846760UL, 1, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_), d_ =>
            {
                using (d_)
                {
                    var r_ = CapnpSerializable.Create<Mas.Schema.Fbp.Channel<TV>.Result_Reader>(d_);
                    return (r_.R);
                }
            }

            );
        }

        public Task<Mas.Schema.Fbp.Channel<TV>.IWriter> Writer(CancellationToken cancellationToken_ = default)
        {
            var in_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.Channel<TV>.Params_Writer.WRITER>();
            var arg_ = new Mas.Schema.Fbp.Channel<TV>.Params_Writer()
            {};
            arg_?.serialize(in_);
            return Impatient.MakePipelineAware(Call(11268783807889846760UL, 2, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_), d_ =>
            {
                using (d_)
                {
                    var r_ = CapnpSerializable.Create<Mas.Schema.Fbp.Channel<TV>.Result_Writer>(d_);
                    return (r_.W);
                }
            }

            );
        }

        public Task<(Mas.Schema.Fbp.Channel<TV>.IReader, Mas.Schema.Fbp.Channel<TV>.IWriter)> Endpoints(CancellationToken cancellationToken_ = default)
        {
            var in_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.Channel<TV>.Params_Endpoints.WRITER>();
            var arg_ = new Mas.Schema.Fbp.Channel<TV>.Params_Endpoints()
            {};
            arg_?.serialize(in_);
            return Impatient.MakePipelineAware(Call(11268783807889846760UL, 3, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_), d_ =>
            {
                using (d_)
                {
                    var r_ = CapnpSerializable.Create<Mas.Schema.Fbp.Channel<TV>.Result_Endpoints>(d_);
                    return (r_.R, r_.W);
                }
            }

            );
        }

        public async Task SetAutoCloseSemantics(Mas.Schema.Fbp.Channel<TV>.CloseSemantics cs, CancellationToken cancellationToken_ = default)
        {
            var in_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.Channel<TV>.Params_SetAutoCloseSemantics.WRITER>();
            var arg_ = new Mas.Schema.Fbp.Channel<TV>.Params_SetAutoCloseSemantics()
            {Cs = cs};
            arg_?.serialize(in_);
            using (var d_ = await Call(11268783807889846760UL, 4, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_).WhenReturned)
            {
                var r_ = CapnpSerializable.Create<Mas.Schema.Fbp.Channel<TV>.Result_SetAutoCloseSemantics>(d_);
                return;
            }
        }

        public async Task Close(bool waitForEmptyBuffer, CancellationToken cancellationToken_ = default)
        {
            var in_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.Channel<TV>.Params_Close.WRITER>();
            var arg_ = new Mas.Schema.Fbp.Channel<TV>.Params_Close()
            {WaitForEmptyBuffer = waitForEmptyBuffer};
            arg_?.serialize(in_);
            using (var d_ = await Call(11268783807889846760UL, 5, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_).WhenReturned)
            {
                var r_ = CapnpSerializable.Create<Mas.Schema.Fbp.Channel<TV>.Result_Close>(d_);
                return;
            }
        }

        public async Task<Mas.Schema.Persistence.Persistent.SaveResults> Save(Mas.Schema.Persistence.Persistent.SaveParams arg_, CancellationToken cancellationToken_ = default)
        {
            var in_ = SerializerState.CreateForRpc<Mas.Schema.Persistence.Persistent.SaveParams.WRITER>();
            arg_?.serialize(in_);
            using (var d_ = await Call(13954362354854972261UL, 0, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_).WhenReturned)
            {
                var r_ = CapnpSerializable.Create<Mas.Schema.Persistence.Persistent.SaveResults>(d_);
                return r_;
            }
        }

        public async Task<Mas.Schema.Common.IdInformation> Info(CancellationToken cancellationToken_ = default)
        {
            var in_ = SerializerState.CreateForRpc<Mas.Schema.Common.Identifiable.Params_Info.WRITER>();
            var arg_ = new Mas.Schema.Common.Identifiable.Params_Info()
            {};
            arg_?.serialize(in_);
            using (var d_ = await Call(12875740530987518165UL, 0, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_).WhenReturned)
            {
                var r_ = CapnpSerializable.Create<Mas.Schema.Common.IdInformation>(d_);
                return r_;
            }
        }
    }

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0x9c62c32b2ff2b1e8UL)]
    public class Channel_Skeleton<TV> : Skeleton<IChannel<TV>> where TV : class
    {
        public Channel_Skeleton()
        {
            SetMethodTable(SetBufferSize, Reader, Writer, Endpoints, SetAutoCloseSemantics, Close);
        }

        public override ulong InterfaceId => 11268783807889846760UL;
        async Task<AnswerOrCounterquestion> SetBufferSize(DeserializerState d_, CancellationToken cancellationToken_)
        {
            using (d_)
            {
                var in_ = CapnpSerializable.Create<Mas.Schema.Fbp.Channel<TV>.Params_SetBufferSize>(d_);
                await Impl.SetBufferSize(in_.Size, cancellationToken_);
                var s_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.Channel<TV>.Result_SetBufferSize.WRITER>();
                return s_;
            }
        }

        Task<AnswerOrCounterquestion> Reader(DeserializerState d_, CancellationToken cancellationToken_)
        {
            using (d_)
            {
                return Impatient.MaybeTailCall(Impl.Reader(cancellationToken_), r =>
                {
                    var s_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.Channel<TV>.Result_Reader.WRITER>();
                    var r_ = new Mas.Schema.Fbp.Channel<TV>.Result_Reader{R = r};
                    r_.serialize(s_);
                    return s_;
                }

                );
            }
        }

        Task<AnswerOrCounterquestion> Writer(DeserializerState d_, CancellationToken cancellationToken_)
        {
            using (d_)
            {
                return Impatient.MaybeTailCall(Impl.Writer(cancellationToken_), w =>
                {
                    var s_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.Channel<TV>.Result_Writer.WRITER>();
                    var r_ = new Mas.Schema.Fbp.Channel<TV>.Result_Writer{W = w};
                    r_.serialize(s_);
                    return s_;
                }

                );
            }
        }

        Task<AnswerOrCounterquestion> Endpoints(DeserializerState d_, CancellationToken cancellationToken_)
        {
            using (d_)
            {
                return Impatient.MaybeTailCall(Impl.Endpoints(cancellationToken_), (r, w) =>
                {
                    var s_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.Channel<TV>.Result_Endpoints.WRITER>();
                    var r_ = new Mas.Schema.Fbp.Channel<TV>.Result_Endpoints{R = r, W = w};
                    r_.serialize(s_);
                    return s_;
                }

                );
            }
        }

        async Task<AnswerOrCounterquestion> SetAutoCloseSemantics(DeserializerState d_, CancellationToken cancellationToken_)
        {
            using (d_)
            {
                var in_ = CapnpSerializable.Create<Mas.Schema.Fbp.Channel<TV>.Params_SetAutoCloseSemantics>(d_);
                await Impl.SetAutoCloseSemantics(in_.Cs, cancellationToken_);
                var s_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.Channel<TV>.Result_SetAutoCloseSemantics.WRITER>();
                return s_;
            }
        }

        async Task<AnswerOrCounterquestion> Close(DeserializerState d_, CancellationToken cancellationToken_)
        {
            using (d_)
            {
                var in_ = CapnpSerializable.Create<Mas.Schema.Fbp.Channel<TV>.Params_Close>(d_);
                await Impl.Close(in_.WaitForEmptyBuffer, cancellationToken_);
                var s_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.Channel<TV>.Result_Close.WRITER>();
                return s_;
            }
        }
    }

    public static class Channel<TV>
        where TV : class
    {
        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xa8d787cae7e0b243UL)]
        public enum CloseSemantics : ushort
        {
            fbp,
            no
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xd5b512f4bcd0aa2eUL)]
        public class Msg : ICapnpSerializable
        {
            public const UInt64 typeId = 0xd5b512f4bcd0aa2eUL;
            public enum WHICH : ushort
            {
                Value = 0,
                Done = 1,
                NoMsg = 2,
                undefined = 65535
            }

            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                switch (reader.which)
                {
                    case WHICH.Value:
                        Value = CapnpSerializable.Create<TV>(reader.Value);
                        break;
                    case WHICH.Done:
                        which = reader.which;
                        break;
                    case WHICH.NoMsg:
                        which = reader.which;
                        break;
                }

                applyDefaults();
            }

            private WHICH _which = WHICH.undefined;
            private object _content;
            public WHICH which
            {
                get => _which;
                set
                {
                    if (value == _which)
                        return;
                    _which = value;
                    switch (value)
                    {
                        case WHICH.Value:
                            _content = null;
                            break;
                        case WHICH.Done:
                            break;
                        case WHICH.NoMsg:
                            break;
                    }
                }
            }

            public void serialize(WRITER writer)
            {
                writer.which = which;
                switch (which)
                {
                    case WHICH.Value:
                        writer.Value.SetObject(Value);
                        break;
                    case WHICH.Done:
                        break;
                    case WHICH.NoMsg:
                        break;
                }
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public TV Value
            {
                get => _which == WHICH.Value ? (TV)_content : null;
                set
                {
                    _which = WHICH.Value;
                    _content = value;
                }
            }

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
                public WHICH which => (WHICH)ctx.ReadDataUShort(0U, (ushort)0);
                public DeserializerState Value => which == WHICH.Value ? ctx.StructReadPointer(0) : default;
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(1, 1);
                }

                public WHICH which
                {
                    get => (WHICH)this.ReadDataUShort(0U, (ushort)0);
                    set => this.WriteData(0U, (ushort)value, (ushort)0);
                }

                public DynamicSerializerState Value
                {
                    get => which == WHICH.Value ? BuildPointer<DynamicSerializerState>(0) : default;
                    set => Link(0, value);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xe3d7a3237f175028UL)]
        public class StartupInfo : ICapnpSerializable
        {
            public const UInt64 typeId = 0xe3d7a3237f175028UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                BufferSize = reader.BufferSize;
                CloseSemantics = reader.CloseSemantics;
                ChannelSR = reader.ChannelSR;
                ReaderSRs = reader.ReaderSRs;
                WriterSRs = reader.WriterSRs;
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.BufferSize = BufferSize;
                writer.CloseSemantics = CloseSemantics;
                writer.ChannelSR = ChannelSR;
                writer.ReaderSRs.Init(ReaderSRs);
                writer.WriterSRs.Init(WriterSRs);
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public ulong BufferSize
            {
                get;
                set;
            }

            public Mas.Schema.Fbp.Channel<TV>.CloseSemantics CloseSemantics
            {
                get;
                set;
            }

            public string ChannelSR
            {
                get;
                set;
            }

            public IReadOnlyList<string> ReaderSRs
            {
                get;
                set;
            }

            public IReadOnlyList<string> WriterSRs
            {
                get;
                set;
            }

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
                public ulong BufferSize => ctx.ReadDataULong(0UL, 0UL);
                public Mas.Schema.Fbp.Channel<TV>.CloseSemantics CloseSemantics => (Mas.Schema.Fbp.Channel<TV>.CloseSemantics)ctx.ReadDataUShort(64UL, (ushort)0);
                public string ChannelSR => ctx.ReadText(0, null);
                public IReadOnlyList<string> ReaderSRs => ctx.ReadList(1).CastText2();
                public bool HasReaderSRs => ctx.IsStructFieldNonNull(1);
                public IReadOnlyList<string> WriterSRs => ctx.ReadList(2).CastText2();
                public bool HasWriterSRs => ctx.IsStructFieldNonNull(2);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(2, 3);
                }

                public ulong BufferSize
                {
                    get => this.ReadDataULong(0UL, 0UL);
                    set => this.WriteData(0UL, value, 0UL);
                }

                public Mas.Schema.Fbp.Channel<TV>.CloseSemantics CloseSemantics
                {
                    get => (Mas.Schema.Fbp.Channel<TV>.CloseSemantics)this.ReadDataUShort(64UL, (ushort)0);
                    set => this.WriteData(64UL, (ushort)value, (ushort)0);
                }

                public string ChannelSR
                {
                    get => this.ReadText(0, null);
                    set => this.WriteText(0, value, null);
                }

                public ListOfTextSerializer ReaderSRs
                {
                    get => BuildPointer<ListOfTextSerializer>(1);
                    set => Link(1, value);
                }

                public ListOfTextSerializer WriterSRs
                {
                    get => BuildPointer<ListOfTextSerializer>(2);
                    set => Link(2, value);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0x8bc69192f3bc97ccUL), Proxy(typeof(Channel<>.Reader_Proxy)), Skeleton(typeof(Channel<>.Reader_Skeleton))]
        public interface IReader : Mas.Schema.Common.IIdentifiable, Mas.Schema.Persistence.IPersistent
        {
            Task<Mas.Schema.Fbp.Channel<TV>.Msg> Read(CancellationToken cancellationToken_ = default);
            Task Close(CancellationToken cancellationToken_ = default);
            Task<Mas.Schema.Fbp.Channel<TV>.Msg> ReadIfMsg(CancellationToken cancellationToken_ = default);
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0x8bc69192f3bc97ccUL)]
        public class Reader_Proxy : Proxy, IReader
        {
            public Task<Mas.Schema.Fbp.Channel<TV>.Msg> Read(CancellationToken cancellationToken_ = default)
            {
                var in_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.Channel<TV>.Reader.Params_Read.WRITER>();
                var arg_ = new Mas.Schema.Fbp.Channel<TV>.Reader.Params_Read()
                {};
                arg_?.serialize(in_);
                return Impatient.MakePipelineAware(Call(10071897677001168844UL, 0, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_), d_ =>
                {
                    using (d_)
                    {
                        var r_ = CapnpSerializable.Create<Mas.Schema.Fbp.Channel<TV>.Msg>(d_);
                        return r_;
                    }
                }

                );
            }

            public async Task Close(CancellationToken cancellationToken_ = default)
            {
                var in_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.Channel<TV>.Reader.Params_Close.WRITER>();
                var arg_ = new Mas.Schema.Fbp.Channel<TV>.Reader.Params_Close()
                {};
                arg_?.serialize(in_);
                using (var d_ = await Call(10071897677001168844UL, 1, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_).WhenReturned)
                {
                    var r_ = CapnpSerializable.Create<Mas.Schema.Fbp.Channel<TV>.Reader.Result_Close>(d_);
                    return;
                }
            }

            public Task<Mas.Schema.Fbp.Channel<TV>.Msg> ReadIfMsg(CancellationToken cancellationToken_ = default)
            {
                var in_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.Channel<TV>.Reader.Params_ReadIfMsg.WRITER>();
                var arg_ = new Mas.Schema.Fbp.Channel<TV>.Reader.Params_ReadIfMsg()
                {};
                arg_?.serialize(in_);
                return Impatient.MakePipelineAware(Call(10071897677001168844UL, 2, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_), d_ =>
                {
                    using (d_)
                    {
                        var r_ = CapnpSerializable.Create<Mas.Schema.Fbp.Channel<TV>.Msg>(d_);
                        return r_;
                    }
                }

                );
            }

            public async Task<Mas.Schema.Persistence.Persistent.SaveResults> Save(Mas.Schema.Persistence.Persistent.SaveParams arg_, CancellationToken cancellationToken_ = default)
            {
                var in_ = SerializerState.CreateForRpc<Mas.Schema.Persistence.Persistent.SaveParams.WRITER>();
                arg_?.serialize(in_);
                using (var d_ = await Call(13954362354854972261UL, 0, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_).WhenReturned)
                {
                    var r_ = CapnpSerializable.Create<Mas.Schema.Persistence.Persistent.SaveResults>(d_);
                    return r_;
                }
            }

            public async Task<Mas.Schema.Common.IdInformation> Info(CancellationToken cancellationToken_ = default)
            {
                var in_ = SerializerState.CreateForRpc<Mas.Schema.Common.Identifiable.Params_Info.WRITER>();
                var arg_ = new Mas.Schema.Common.Identifiable.Params_Info()
                {};
                arg_?.serialize(in_);
                using (var d_ = await Call(12875740530987518165UL, 0, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_).WhenReturned)
                {
                    var r_ = CapnpSerializable.Create<Mas.Schema.Common.IdInformation>(d_);
                    return r_;
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0x8bc69192f3bc97ccUL)]
        public class Reader_Skeleton : Skeleton<IReader>
        {
            public Reader_Skeleton()
            {
                SetMethodTable(Read, Close, ReadIfMsg);
            }

            public override ulong InterfaceId => 10071897677001168844UL;
            Task<AnswerOrCounterquestion> Read(DeserializerState d_, CancellationToken cancellationToken_)
            {
                using (d_)
                {
                    return Impatient.MaybeTailCall(Impl.Read(cancellationToken_), r_ =>
                    {
                        var s_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.Channel<TV>.Msg.WRITER>();
                        r_.serialize(s_);
                        return s_;
                    }

                    );
                }
            }

            async Task<AnswerOrCounterquestion> Close(DeserializerState d_, CancellationToken cancellationToken_)
            {
                using (d_)
                {
                    await Impl.Close(cancellationToken_);
                    var s_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.Channel<TV>.Reader.Result_Close.WRITER>();
                    return s_;
                }
            }

            Task<AnswerOrCounterquestion> ReadIfMsg(DeserializerState d_, CancellationToken cancellationToken_)
            {
                using (d_)
                {
                    return Impatient.MaybeTailCall(Impl.ReadIfMsg(cancellationToken_), r_ =>
                    {
                        var s_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.Channel<TV>.Msg.WRITER>();
                        r_.serialize(s_);
                        return s_;
                    }

                    );
                }
            }
        }

        public static class Reader
        {
            [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xc0335d99db8b2ba5UL)]
            public class Params_Read : ICapnpSerializable
            {
                public const UInt64 typeId = 0xc0335d99db8b2ba5UL;
                void ICapnpSerializable.Deserialize(DeserializerState arg_)
                {
                    var reader = READER.create(arg_);
                    applyDefaults();
                }

                public void serialize(WRITER writer)
                {
                }

                void ICapnpSerializable.Serialize(SerializerState arg_)
                {
                    serialize(arg_.Rewrap<WRITER>());
                }

                public void applyDefaults()
                {
                }

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
                }

                public class WRITER : SerializerState
                {
                    public WRITER()
                    {
                        this.SetStruct(0, 0);
                    }
                }
            }

            [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0x9428ea64f18c41c8UL)]
            public class Params_Close : ICapnpSerializable
            {
                public const UInt64 typeId = 0x9428ea64f18c41c8UL;
                void ICapnpSerializable.Deserialize(DeserializerState arg_)
                {
                    var reader = READER.create(arg_);
                    applyDefaults();
                }

                public void serialize(WRITER writer)
                {
                }

                void ICapnpSerializable.Serialize(SerializerState arg_)
                {
                    serialize(arg_.Rewrap<WRITER>());
                }

                public void applyDefaults()
                {
                }

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
                }

                public class WRITER : SerializerState
                {
                    public WRITER()
                    {
                        this.SetStruct(0, 0);
                    }
                }
            }

            [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xb3fe08a1bf53821aUL)]
            public class Result_Close : ICapnpSerializable
            {
                public const UInt64 typeId = 0xb3fe08a1bf53821aUL;
                void ICapnpSerializable.Deserialize(DeserializerState arg_)
                {
                    var reader = READER.create(arg_);
                    applyDefaults();
                }

                public void serialize(WRITER writer)
                {
                }

                void ICapnpSerializable.Serialize(SerializerState arg_)
                {
                    serialize(arg_.Rewrap<WRITER>());
                }

                public void applyDefaults()
                {
                }

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
                }

                public class WRITER : SerializerState
                {
                    public WRITER()
                    {
                        this.SetStruct(0, 0);
                    }
                }
            }

            [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0x89e521a99fcc4044UL)]
            public class Params_ReadIfMsg : ICapnpSerializable
            {
                public const UInt64 typeId = 0x89e521a99fcc4044UL;
                void ICapnpSerializable.Deserialize(DeserializerState arg_)
                {
                    var reader = READER.create(arg_);
                    applyDefaults();
                }

                public void serialize(WRITER writer)
                {
                }

                void ICapnpSerializable.Serialize(SerializerState arg_)
                {
                    serialize(arg_.Rewrap<WRITER>());
                }

                public void applyDefaults()
                {
                }

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
                }

                public class WRITER : SerializerState
                {
                    public WRITER()
                    {
                        this.SetStruct(0, 0);
                    }
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xf7fec613b4a8c79fUL), Proxy(typeof(Channel<>.Writer_Proxy)), Skeleton(typeof(Channel<>.Writer_Skeleton))]
        public interface IWriter : Mas.Schema.Common.IIdentifiable, Mas.Schema.Persistence.IPersistent
        {
            Task Write(Mas.Schema.Fbp.Channel<TV>.Msg arg_, CancellationToken cancellationToken_ = default);
            Task Close(CancellationToken cancellationToken_ = default);
            Task<bool> WriteIfSpace(Mas.Schema.Fbp.Channel<TV>.Msg arg_, CancellationToken cancellationToken_ = default);
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xf7fec613b4a8c79fUL)]
        public class Writer_Proxy : Proxy, IWriter
        {
            public async Task Write(Mas.Schema.Fbp.Channel<TV>.Msg arg_, CancellationToken cancellationToken_ = default)
            {
                var in_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.Channel<TV>.Msg.WRITER>();
                arg_?.serialize(in_);
                using (var d_ = await Call(17869938159390345119UL, 0, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_).WhenReturned)
                {
                    var r_ = CapnpSerializable.Create<Mas.Schema.Fbp.Channel<TV>.Writer.Result_Write>(d_);
                    return;
                }
            }

            public async Task Close(CancellationToken cancellationToken_ = default)
            {
                var in_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.Channel<TV>.Writer.Params_Close.WRITER>();
                var arg_ = new Mas.Schema.Fbp.Channel<TV>.Writer.Params_Close()
                {};
                arg_?.serialize(in_);
                using (var d_ = await Call(17869938159390345119UL, 1, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_).WhenReturned)
                {
                    var r_ = CapnpSerializable.Create<Mas.Schema.Fbp.Channel<TV>.Writer.Result_Close>(d_);
                    return;
                }
            }

            public async Task<bool> WriteIfSpace(Mas.Schema.Fbp.Channel<TV>.Msg arg_, CancellationToken cancellationToken_ = default)
            {
                var in_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.Channel<TV>.Msg.WRITER>();
                arg_?.serialize(in_);
                using (var d_ = await Call(17869938159390345119UL, 2, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_).WhenReturned)
                {
                    var r_ = CapnpSerializable.Create<Mas.Schema.Fbp.Channel<TV>.Writer.Result_WriteIfSpace>(d_);
                    return (r_.Success);
                }
            }

            public async Task<Mas.Schema.Persistence.Persistent.SaveResults> Save(Mas.Schema.Persistence.Persistent.SaveParams arg_, CancellationToken cancellationToken_ = default)
            {
                var in_ = SerializerState.CreateForRpc<Mas.Schema.Persistence.Persistent.SaveParams.WRITER>();
                arg_?.serialize(in_);
                using (var d_ = await Call(13954362354854972261UL, 0, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_).WhenReturned)
                {
                    var r_ = CapnpSerializable.Create<Mas.Schema.Persistence.Persistent.SaveResults>(d_);
                    return r_;
                }
            }

            public async Task<Mas.Schema.Common.IdInformation> Info(CancellationToken cancellationToken_ = default)
            {
                var in_ = SerializerState.CreateForRpc<Mas.Schema.Common.Identifiable.Params_Info.WRITER>();
                var arg_ = new Mas.Schema.Common.Identifiable.Params_Info()
                {};
                arg_?.serialize(in_);
                using (var d_ = await Call(12875740530987518165UL, 0, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_).WhenReturned)
                {
                    var r_ = CapnpSerializable.Create<Mas.Schema.Common.IdInformation>(d_);
                    return r_;
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xf7fec613b4a8c79fUL)]
        public class Writer_Skeleton : Skeleton<IWriter>
        {
            public Writer_Skeleton()
            {
                SetMethodTable(Write, Close, WriteIfSpace);
            }

            public override ulong InterfaceId => 17869938159390345119UL;
            async Task<AnswerOrCounterquestion> Write(DeserializerState d_, CancellationToken cancellationToken_)
            {
                using (d_)
                {
                    await Impl.Write(CapnpSerializable.Create<Mas.Schema.Fbp.Channel<TV>.Msg>(d_), cancellationToken_);
                    var s_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.Channel<TV>.Writer.Result_Write.WRITER>();
                    return s_;
                }
            }

            async Task<AnswerOrCounterquestion> Close(DeserializerState d_, CancellationToken cancellationToken_)
            {
                using (d_)
                {
                    await Impl.Close(cancellationToken_);
                    var s_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.Channel<TV>.Writer.Result_Close.WRITER>();
                    return s_;
                }
            }

            Task<AnswerOrCounterquestion> WriteIfSpace(DeserializerState d_, CancellationToken cancellationToken_)
            {
                using (d_)
                {
                    return Impatient.MaybeTailCall(Impl.WriteIfSpace(CapnpSerializable.Create<Mas.Schema.Fbp.Channel<TV>.Msg>(d_), cancellationToken_), success =>
                    {
                        var s_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.Channel<TV>.Writer.Result_WriteIfSpace.WRITER>();
                        var r_ = new Mas.Schema.Fbp.Channel<TV>.Writer.Result_WriteIfSpace{Success = success};
                        r_.serialize(s_);
                        return s_;
                    }

                    );
                }
            }
        }

        public static class Writer
        {
            [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xce9f24b8ec149524UL)]
            public class Result_Write : ICapnpSerializable
            {
                public const UInt64 typeId = 0xce9f24b8ec149524UL;
                void ICapnpSerializable.Deserialize(DeserializerState arg_)
                {
                    var reader = READER.create(arg_);
                    applyDefaults();
                }

                public void serialize(WRITER writer)
                {
                }

                void ICapnpSerializable.Serialize(SerializerState arg_)
                {
                    serialize(arg_.Rewrap<WRITER>());
                }

                public void applyDefaults()
                {
                }

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
                }

                public class WRITER : SerializerState
                {
                    public WRITER()
                    {
                        this.SetStruct(0, 0);
                    }
                }
            }

            [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xbadc988dda3d1e50UL)]
            public class Params_Close : ICapnpSerializable
            {
                public const UInt64 typeId = 0xbadc988dda3d1e50UL;
                void ICapnpSerializable.Deserialize(DeserializerState arg_)
                {
                    var reader = READER.create(arg_);
                    applyDefaults();
                }

                public void serialize(WRITER writer)
                {
                }

                void ICapnpSerializable.Serialize(SerializerState arg_)
                {
                    serialize(arg_.Rewrap<WRITER>());
                }

                public void applyDefaults()
                {
                }

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
                }

                public class WRITER : SerializerState
                {
                    public WRITER()
                    {
                        this.SetStruct(0, 0);
                    }
                }
            }

            [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xcb02dc91e18e58c9UL)]
            public class Result_Close : ICapnpSerializable
            {
                public const UInt64 typeId = 0xcb02dc91e18e58c9UL;
                void ICapnpSerializable.Deserialize(DeserializerState arg_)
                {
                    var reader = READER.create(arg_);
                    applyDefaults();
                }

                public void serialize(WRITER writer)
                {
                }

                void ICapnpSerializable.Serialize(SerializerState arg_)
                {
                    serialize(arg_.Rewrap<WRITER>());
                }

                public void applyDefaults()
                {
                }

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
                }

                public class WRITER : SerializerState
                {
                    public WRITER()
                    {
                        this.SetStruct(0, 0);
                    }
                }
            }

            [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xc61c438f89d10281UL)]
            public class Result_WriteIfSpace : ICapnpSerializable
            {
                public const UInt64 typeId = 0xc61c438f89d10281UL;
                void ICapnpSerializable.Deserialize(DeserializerState arg_)
                {
                    var reader = READER.create(arg_);
                    Success = reader.Success;
                    applyDefaults();
                }

                public void serialize(WRITER writer)
                {
                    writer.Success = Success;
                }

                void ICapnpSerializable.Serialize(SerializerState arg_)
                {
                    serialize(arg_.Rewrap<WRITER>());
                }

                public void applyDefaults()
                {
                }

                public bool Success
                {
                    get;
                    set;
                }

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
                    public bool Success => ctx.ReadDataBool(0UL, false);
                }

                public class WRITER : SerializerState
                {
                    public WRITER()
                    {
                        this.SetStruct(1, 0);
                    }

                    public bool Success
                    {
                        get => this.ReadDataBool(0UL, false);
                        set => this.WriteData(0UL, value, false);
                    }
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0x92101e3b7a761333UL)]
        public class Params_SetBufferSize : ICapnpSerializable
        {
            public const UInt64 typeId = 0x92101e3b7a761333UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                Size = reader.Size;
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.Size = Size;
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public ulong Size
            {
                get;
                set;
            }

            = 1UL;
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
                public ulong Size => ctx.ReadDataULong(0UL, 1UL);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(1, 0);
                }

                public ulong Size
                {
                    get => this.ReadDataULong(0UL, 1UL);
                    set => this.WriteData(0UL, value, 1UL);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xfe6a08d5e0712c23UL)]
        public class Result_SetBufferSize : ICapnpSerializable
        {
            public const UInt64 typeId = 0xfe6a08d5e0712c23UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

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
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 0);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xe607c9dd64da04c4UL)]
        public class Params_Reader : ICapnpSerializable
        {
            public const UInt64 typeId = 0xe607c9dd64da04c4UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

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
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 0);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xb135ffc9ccc9eca6UL)]
        public class Result_Reader : ICapnpSerializable
        {
            public const UInt64 typeId = 0xb135ffc9ccc9eca6UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                R = reader.R;
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.R = R;
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public Mas.Schema.Fbp.Channel<TV>.IReader R
            {
                get;
                set;
            }

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
                public Mas.Schema.Fbp.Channel<TV>.IReader R => ctx.ReadCap<Mas.Schema.Fbp.Channel<TV>.IReader>(0);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 1);
                }

                public Mas.Schema.Fbp.Channel<TV>.IReader R
                {
                    get => ReadCap<Mas.Schema.Fbp.Channel<TV>.IReader>(0);
                    set => LinkObject(0, value);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xbe611d34e368e109UL)]
        public class Params_Writer : ICapnpSerializable
        {
            public const UInt64 typeId = 0xbe611d34e368e109UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

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
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 0);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xb47b53679e985c7eUL)]
        public class Result_Writer : ICapnpSerializable
        {
            public const UInt64 typeId = 0xb47b53679e985c7eUL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                W = reader.W;
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.W = W;
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public Mas.Schema.Fbp.Channel<TV>.IWriter W
            {
                get;
                set;
            }

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
                public Mas.Schema.Fbp.Channel<TV>.IWriter W => ctx.ReadCap<Mas.Schema.Fbp.Channel<TV>.IWriter>(0);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 1);
                }

                public Mas.Schema.Fbp.Channel<TV>.IWriter W
                {
                    get => ReadCap<Mas.Schema.Fbp.Channel<TV>.IWriter>(0);
                    set => LinkObject(0, value);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xd23f817e914373d8UL)]
        public class Params_Endpoints : ICapnpSerializable
        {
            public const UInt64 typeId = 0xd23f817e914373d8UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

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
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 0);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xf37401d21f8d97bbUL)]
        public class Result_Endpoints : ICapnpSerializable
        {
            public const UInt64 typeId = 0xf37401d21f8d97bbUL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                R = reader.R;
                W = reader.W;
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.R = R;
                writer.W = W;
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public Mas.Schema.Fbp.Channel<TV>.IReader R
            {
                get;
                set;
            }

            public Mas.Schema.Fbp.Channel<TV>.IWriter W
            {
                get;
                set;
            }

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
                public Mas.Schema.Fbp.Channel<TV>.IReader R => ctx.ReadCap<Mas.Schema.Fbp.Channel<TV>.IReader>(0);
                public Mas.Schema.Fbp.Channel<TV>.IWriter W => ctx.ReadCap<Mas.Schema.Fbp.Channel<TV>.IWriter>(1);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 2);
                }

                public Mas.Schema.Fbp.Channel<TV>.IReader R
                {
                    get => ReadCap<Mas.Schema.Fbp.Channel<TV>.IReader>(0);
                    set => LinkObject(0, value);
                }

                public Mas.Schema.Fbp.Channel<TV>.IWriter W
                {
                    get => ReadCap<Mas.Schema.Fbp.Channel<TV>.IWriter>(1);
                    set => LinkObject(1, value);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xb49836b545583addUL)]
        public class Params_SetAutoCloseSemantics : ICapnpSerializable
        {
            public const UInt64 typeId = 0xb49836b545583addUL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                Cs = reader.Cs;
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.Cs = Cs;
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public Mas.Schema.Fbp.Channel<TV>.CloseSemantics Cs
            {
                get;
                set;
            }

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
                public Mas.Schema.Fbp.Channel<TV>.CloseSemantics Cs => (Mas.Schema.Fbp.Channel<TV>.CloseSemantics)ctx.ReadDataUShort(0UL, (ushort)0);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(1, 0);
                }

                public Mas.Schema.Fbp.Channel<TV>.CloseSemantics Cs
                {
                    get => (Mas.Schema.Fbp.Channel<TV>.CloseSemantics)this.ReadDataUShort(0UL, (ushort)0);
                    set => this.WriteData(0UL, (ushort)value, (ushort)0);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xc0fc6e5a3fcb3206UL)]
        public class Result_SetAutoCloseSemantics : ICapnpSerializable
        {
            public const UInt64 typeId = 0xc0fc6e5a3fcb3206UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

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
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 0);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0x95d8ad01c1113d9cUL)]
        public class Params_Close : ICapnpSerializable
        {
            public const UInt64 typeId = 0x95d8ad01c1113d9cUL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                WaitForEmptyBuffer = reader.WaitForEmptyBuffer;
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.WaitForEmptyBuffer = WaitForEmptyBuffer;
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public bool WaitForEmptyBuffer
            {
                get;
                set;
            }

            = true;
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
                public bool WaitForEmptyBuffer => ctx.ReadDataBool(0UL, true);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(1, 0);
                }

                public bool WaitForEmptyBuffer
                {
                    get => this.ReadDataBool(0UL, true);
                    set => this.WriteData(0UL, value, true);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xcc079ad60f1363b7UL)]
        public class Result_Close : ICapnpSerializable
        {
            public const UInt64 typeId = 0xcc079ad60f1363b7UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

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
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 0);
                }
            }
        }
    }

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xd0cd6d829b810229UL), Proxy(typeof(StartChannelsService_Proxy)), Skeleton(typeof(StartChannelsService_Skeleton))]
    public interface IStartChannelsService : Mas.Schema.Common.IIdentifiable
    {
        Task<IReadOnlyList<Mas.Schema.Fbp.Channel<object>.StartupInfo>> Create(Mas.Schema.Fbp.StartChannelsService.Params arg_, CancellationToken cancellationToken_ = default);
    }

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xd0cd6d829b810229UL)]
    public class StartChannelsService_Proxy : Proxy, IStartChannelsService
    {
        public async Task<IReadOnlyList<Mas.Schema.Fbp.Channel<object>.StartupInfo>> Create(Mas.Schema.Fbp.StartChannelsService.Params arg_, CancellationToken cancellationToken_ = default)
        {
            var in_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.StartChannelsService.Params.WRITER>();
            arg_?.serialize(in_);
            using (var d_ = await Call(15045802337836794409UL, 0, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_).WhenReturned)
            {
                var r_ = CapnpSerializable.Create<Mas.Schema.Fbp.StartChannelsService.Result_Create>(d_);
                return (r_.StartupInfos);
            }
        }

        public async Task<Mas.Schema.Common.IdInformation> Info(CancellationToken cancellationToken_ = default)
        {
            var in_ = SerializerState.CreateForRpc<Mas.Schema.Common.Identifiable.Params_Info.WRITER>();
            var arg_ = new Mas.Schema.Common.Identifiable.Params_Info()
            {};
            arg_?.serialize(in_);
            using (var d_ = await Call(12875740530987518165UL, 0, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_).WhenReturned)
            {
                var r_ = CapnpSerializable.Create<Mas.Schema.Common.IdInformation>(d_);
                return r_;
            }
        }
    }

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xd0cd6d829b810229UL)]
    public class StartChannelsService_Skeleton : Skeleton<IStartChannelsService>
    {
        public StartChannelsService_Skeleton()
        {
            SetMethodTable(Create);
        }

        public override ulong InterfaceId => 15045802337836794409UL;
        Task<AnswerOrCounterquestion> Create(DeserializerState d_, CancellationToken cancellationToken_)
        {
            using (d_)
            {
                return Impatient.MaybeTailCall(Impl.Create(CapnpSerializable.Create<Mas.Schema.Fbp.StartChannelsService.Params>(d_), cancellationToken_), startupInfos =>
                {
                    var s_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.StartChannelsService.Result_Create.WRITER>();
                    var r_ = new Mas.Schema.Fbp.StartChannelsService.Result_Create{StartupInfos = startupInfos};
                    r_.serialize(s_);
                    return s_;
                }

                );
            }
        }
    }

    public static class StartChannelsService
    {
        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0x9576b9a98d58fba2UL)]
        public class Params : ICapnpSerializable
        {
            public const UInt64 typeId = 0x9576b9a98d58fba2UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                Name = reader.Name;
                NoOfChannels = reader.NoOfChannels;
                NoOfReaders = reader.NoOfReaders;
                NoOfWriters = reader.NoOfWriters;
                ReaderSrts = reader.ReaderSrts;
                WriterSrts = reader.WriterSrts;
                BufferSize = reader.BufferSize;
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.Name = Name;
                writer.NoOfChannels = NoOfChannels;
                writer.NoOfReaders = NoOfReaders;
                writer.NoOfWriters = NoOfWriters;
                writer.ReaderSrts.Init(ReaderSrts);
                writer.WriterSrts.Init(WriterSrts);
                writer.BufferSize = BufferSize;
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public string Name
            {
                get;
                set;
            }

            public ushort NoOfChannels
            {
                get;
                set;
            }

            = 1;
            public ushort NoOfReaders
            {
                get;
                set;
            }

            = 1;
            public ushort NoOfWriters
            {
                get;
                set;
            }

            = 1;
            public IReadOnlyList<string> ReaderSrts
            {
                get;
                set;
            }

            public IReadOnlyList<string> WriterSrts
            {
                get;
                set;
            }

            public ushort BufferSize
            {
                get;
                set;
            }

            = 1;
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
                public string Name => ctx.ReadText(0, null);
                public ushort NoOfChannels => ctx.ReadDataUShort(0UL, (ushort)1);
                public ushort NoOfReaders => ctx.ReadDataUShort(16UL, (ushort)1);
                public ushort NoOfWriters => ctx.ReadDataUShort(32UL, (ushort)1);
                public IReadOnlyList<string> ReaderSrts => ctx.ReadList(1).CastText2();
                public bool HasReaderSrts => ctx.IsStructFieldNonNull(1);
                public IReadOnlyList<string> WriterSrts => ctx.ReadList(2).CastText2();
                public bool HasWriterSrts => ctx.IsStructFieldNonNull(2);
                public ushort BufferSize => ctx.ReadDataUShort(48UL, (ushort)1);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(1, 3);
                }

                public string Name
                {
                    get => this.ReadText(0, null);
                    set => this.WriteText(0, value, null);
                }

                public ushort NoOfChannels
                {
                    get => this.ReadDataUShort(0UL, (ushort)1);
                    set => this.WriteData(0UL, value, (ushort)1);
                }

                public ushort NoOfReaders
                {
                    get => this.ReadDataUShort(16UL, (ushort)1);
                    set => this.WriteData(16UL, value, (ushort)1);
                }

                public ushort NoOfWriters
                {
                    get => this.ReadDataUShort(32UL, (ushort)1);
                    set => this.WriteData(32UL, value, (ushort)1);
                }

                public ListOfTextSerializer ReaderSrts
                {
                    get => BuildPointer<ListOfTextSerializer>(1);
                    set => Link(1, value);
                }

                public ListOfTextSerializer WriterSrts
                {
                    get => BuildPointer<ListOfTextSerializer>(2);
                    set => Link(2, value);
                }

                public ushort BufferSize
                {
                    get => this.ReadDataUShort(48UL, (ushort)1);
                    set => this.WriteData(48UL, value, (ushort)1);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xde5975c83de2b10cUL)]
        public class Result_Create : ICapnpSerializable
        {
            public const UInt64 typeId = 0xde5975c83de2b10cUL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                StartupInfos = reader.StartupInfos?.ToReadOnlyList(_ => CapnpSerializable.Create<Mas.Schema.Fbp.Channel<object>.StartupInfo>(_));
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.StartupInfos.Init(StartupInfos, (_s1, _v1) => _v1?.serialize(_s1));
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public IReadOnlyList<Mas.Schema.Fbp.Channel<object>.StartupInfo> StartupInfos
            {
                get;
                set;
            }

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
                public IReadOnlyList<Mas.Schema.Fbp.Channel<object>.StartupInfo.READER> StartupInfos => ctx.ReadList(0).Cast(Mas.Schema.Fbp.Channel<object>.StartupInfo.READER.create);
                public bool HasStartupInfos => ctx.IsStructFieldNonNull(0);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 1);
                }

                public ListOfStructsSerializer<Mas.Schema.Fbp.Channel<object>.StartupInfo.WRITER> StartupInfos
                {
                    get => BuildPointer<ListOfStructsSerializer<Mas.Schema.Fbp.Channel<object>.StartupInfo.WRITER>>(0);
                    set => Link(0, value);
                }
            }
        }
    }

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xece0efa9a922d4a8UL)]
    public class PortInfos : ICapnpSerializable
    {
        public const UInt64 typeId = 0xece0efa9a922d4a8UL;
        void ICapnpSerializable.Deserialize(DeserializerState arg_)
        {
            var reader = READER.create(arg_);
            InPorts = reader.InPorts?.ToReadOnlyList(_ => CapnpSerializable.Create<Mas.Schema.Fbp.PortInfos.NameAndSR>(_));
            OutPorts = reader.OutPorts?.ToReadOnlyList(_ => CapnpSerializable.Create<Mas.Schema.Fbp.PortInfos.NameAndSR>(_));
            applyDefaults();
        }

        public void serialize(WRITER writer)
        {
            writer.InPorts.Init(InPorts, (_s1, _v1) => _v1?.serialize(_s1));
            writer.OutPorts.Init(OutPorts, (_s1, _v1) => _v1?.serialize(_s1));
        }

        void ICapnpSerializable.Serialize(SerializerState arg_)
        {
            serialize(arg_.Rewrap<WRITER>());
        }

        public void applyDefaults()
        {
        }

        public IReadOnlyList<Mas.Schema.Fbp.PortInfos.NameAndSR> InPorts
        {
            get;
            set;
        }

        public IReadOnlyList<Mas.Schema.Fbp.PortInfos.NameAndSR> OutPorts
        {
            get;
            set;
        }

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
            public IReadOnlyList<Mas.Schema.Fbp.PortInfos.NameAndSR.READER> InPorts => ctx.ReadList(0).Cast(Mas.Schema.Fbp.PortInfos.NameAndSR.READER.create);
            public bool HasInPorts => ctx.IsStructFieldNonNull(0);
            public IReadOnlyList<Mas.Schema.Fbp.PortInfos.NameAndSR.READER> OutPorts => ctx.ReadList(1).Cast(Mas.Schema.Fbp.PortInfos.NameAndSR.READER.create);
            public bool HasOutPorts => ctx.IsStructFieldNonNull(1);
        }

        public class WRITER : SerializerState
        {
            public WRITER()
            {
                this.SetStruct(0, 2);
            }

            public ListOfStructsSerializer<Mas.Schema.Fbp.PortInfos.NameAndSR.WRITER> InPorts
            {
                get => BuildPointer<ListOfStructsSerializer<Mas.Schema.Fbp.PortInfos.NameAndSR.WRITER>>(0);
                set => Link(0, value);
            }

            public ListOfStructsSerializer<Mas.Schema.Fbp.PortInfos.NameAndSR.WRITER> OutPorts
            {
                get => BuildPointer<ListOfStructsSerializer<Mas.Schema.Fbp.PortInfos.NameAndSR.WRITER>>(1);
                set => Link(1, value);
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0x8a4d34c4b5eb1545UL)]
        public class NameAndSR : ICapnpSerializable
        {
            public const UInt64 typeId = 0x8a4d34c4b5eb1545UL;
            public enum WHICH : ushort
            {
                Sr = 0,
                Srs = 1,
                undefined = 65535
            }

            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                switch (reader.which)
                {
                    case WHICH.Sr:
                        Sr = reader.Sr;
                        break;
                    case WHICH.Srs:
                        Srs = reader.Srs;
                        break;
                }

                Name = reader.Name;
                applyDefaults();
            }

            private WHICH _which = WHICH.undefined;
            private object _content;
            public WHICH which
            {
                get => _which;
                set
                {
                    if (value == _which)
                        return;
                    _which = value;
                    switch (value)
                    {
                        case WHICH.Sr:
                            _content = null;
                            break;
                        case WHICH.Srs:
                            _content = null;
                            break;
                    }
                }
            }

            public void serialize(WRITER writer)
            {
                writer.which = which;
                switch (which)
                {
                    case WHICH.Sr:
                        writer.Sr = Sr;
                        break;
                    case WHICH.Srs:
                        writer.Srs.Init(Srs);
                        break;
                }

                writer.Name = Name;
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public string Name
            {
                get;
                set;
            }

            public string Sr
            {
                get => _which == WHICH.Sr ? (string)_content : null;
                set
                {
                    _which = WHICH.Sr;
                    _content = value;
                }
            }

            public IReadOnlyList<string> Srs
            {
                get => _which == WHICH.Srs ? (IReadOnlyList<string>)_content : null;
                set
                {
                    _which = WHICH.Srs;
                    _content = value;
                }
            }

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
                public WHICH which => (WHICH)ctx.ReadDataUShort(0U, (ushort)0);
                public string Name => ctx.ReadText(0, null);
                public string Sr => which == WHICH.Sr ? ctx.ReadText(1, null) : default;
                public IReadOnlyList<string> Srs => which == WHICH.Srs ? ctx.ReadList(1).CastText2() : default;
                public bool HasSrs => ctx.IsStructFieldNonNull(1);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(1, 2);
                }

                public WHICH which
                {
                    get => (WHICH)this.ReadDataUShort(0U, (ushort)0);
                    set => this.WriteData(0U, (ushort)value, (ushort)0);
                }

                public string Name
                {
                    get => this.ReadText(0, null);
                    set => this.WriteText(0, value, null);
                }

                public string Sr
                {
                    get => which == WHICH.Sr ? this.ReadText(1, null) : default;
                    set => this.WriteText(1, value, null);
                }

                public ListOfTextSerializer Srs
                {
                    get => which == WHICH.Srs ? BuildPointer<ListOfTextSerializer>(1) : default;
                    set => Link(1, value);
                }
            }
        }
    }

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xd717ff7d6815a6b0UL)]
    public class Component : ICapnpSerializable
    {
        public const UInt64 typeId = 0xd717ff7d6815a6b0UL;
        void ICapnpSerializable.Deserialize(DeserializerState arg_)
        {
            var reader = READER.create(arg_);
            Info = CapnpSerializable.Create<Mas.Schema.Common.IdInformation>(reader.Info);
            Type = reader.Type;
            InPorts = reader.InPorts?.ToReadOnlyList(_ => CapnpSerializable.Create<Mas.Schema.Fbp.Component.Port>(_));
            OutPorts = reader.OutPorts?.ToReadOnlyList(_ => CapnpSerializable.Create<Mas.Schema.Fbp.Component.Port>(_));
            Run = reader.Run;
            applyDefaults();
        }

        public void serialize(WRITER writer)
        {
            Info?.serialize(writer.Info);
            writer.Type = Type;
            writer.InPorts.Init(InPorts, (_s1, _v1) => _v1?.serialize(_s1));
            writer.OutPorts.Init(OutPorts, (_s1, _v1) => _v1?.serialize(_s1));
            writer.Run = Run;
        }

        void ICapnpSerializable.Serialize(SerializerState arg_)
        {
            serialize(arg_.Rewrap<WRITER>());
        }

        public void applyDefaults()
        {
        }

        public Mas.Schema.Common.IdInformation Info
        {
            get;
            set;
        }

        public Mas.Schema.Fbp.Component.ComponentType Type
        {
            get;
            set;
        }

        public IReadOnlyList<Mas.Schema.Fbp.Component.Port> InPorts
        {
            get;
            set;
        }

        public IReadOnlyList<Mas.Schema.Fbp.Component.Port> OutPorts
        {
            get;
            set;
        }

        public Mas.Schema.Fbp.Component.IRunnable Run
        {
            get;
            set;
        }

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
            public Mas.Schema.Common.IdInformation.READER Info => ctx.ReadStruct(0, Mas.Schema.Common.IdInformation.READER.create);
            public bool HasInfo => ctx.IsStructFieldNonNull(0);
            public Mas.Schema.Fbp.Component.ComponentType Type => (Mas.Schema.Fbp.Component.ComponentType)ctx.ReadDataUShort(0UL, (ushort)0);
            public IReadOnlyList<Mas.Schema.Fbp.Component.Port.READER> InPorts => ctx.ReadList(1).Cast(Mas.Schema.Fbp.Component.Port.READER.create);
            public bool HasInPorts => ctx.IsStructFieldNonNull(1);
            public IReadOnlyList<Mas.Schema.Fbp.Component.Port.READER> OutPorts => ctx.ReadList(2).Cast(Mas.Schema.Fbp.Component.Port.READER.create);
            public bool HasOutPorts => ctx.IsStructFieldNonNull(2);
            public Mas.Schema.Fbp.Component.IRunnable Run => ctx.ReadCap<Mas.Schema.Fbp.Component.IRunnable>(3);
        }

        public class WRITER : SerializerState
        {
            public WRITER()
            {
                this.SetStruct(1, 4);
            }

            public Mas.Schema.Common.IdInformation.WRITER Info
            {
                get => BuildPointer<Mas.Schema.Common.IdInformation.WRITER>(0);
                set => Link(0, value);
            }

            public Mas.Schema.Fbp.Component.ComponentType Type
            {
                get => (Mas.Schema.Fbp.Component.ComponentType)this.ReadDataUShort(0UL, (ushort)0);
                set => this.WriteData(0UL, (ushort)value, (ushort)0);
            }

            public ListOfStructsSerializer<Mas.Schema.Fbp.Component.Port.WRITER> InPorts
            {
                get => BuildPointer<ListOfStructsSerializer<Mas.Schema.Fbp.Component.Port.WRITER>>(1);
                set => Link(1, value);
            }

            public ListOfStructsSerializer<Mas.Schema.Fbp.Component.Port.WRITER> OutPorts
            {
                get => BuildPointer<ListOfStructsSerializer<Mas.Schema.Fbp.Component.Port.WRITER>>(2);
                set => Link(2, value);
            }

            public Mas.Schema.Fbp.Component.IRunnable Run
            {
                get => ReadCap<Mas.Schema.Fbp.Component.IRunnable>(3);
                set => LinkObject(3, value);
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xcb17668f2d39c70fUL), Proxy(typeof(Runnable_Proxy)), Skeleton(typeof(Runnable_Skeleton))]
        public interface IRunnable : Mas.Schema.Common.IIdentifiable
        {
            Task<bool> Start(string portInfosReaderSr, CancellationToken cancellationToken_ = default);
            Task<bool> Stop(CancellationToken cancellationToken_ = default);
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xcb17668f2d39c70fUL)]
        public class Runnable_Proxy : Proxy, IRunnable
        {
            public async Task<bool> Start(string portInfosReaderSr, CancellationToken cancellationToken_ = default)
            {
                var in_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.Component.Runnable.Params_Start.WRITER>();
                var arg_ = new Mas.Schema.Fbp.Component.Runnable.Params_Start()
                {PortInfosReaderSr = portInfosReaderSr};
                arg_?.serialize(in_);
                using (var d_ = await Call(14634278279288833807UL, 0, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_).WhenReturned)
                {
                    var r_ = CapnpSerializable.Create<Mas.Schema.Fbp.Component.Runnable.Result_Start>(d_);
                    return (r_.Success);
                }
            }

            public async Task<bool> Stop(CancellationToken cancellationToken_ = default)
            {
                var in_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.Component.Runnable.Params_Stop.WRITER>();
                var arg_ = new Mas.Schema.Fbp.Component.Runnable.Params_Stop()
                {};
                arg_?.serialize(in_);
                using (var d_ = await Call(14634278279288833807UL, 1, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_).WhenReturned)
                {
                    var r_ = CapnpSerializable.Create<Mas.Schema.Fbp.Component.Runnable.Result_Stop>(d_);
                    return (r_.Success);
                }
            }

            public async Task<Mas.Schema.Common.IdInformation> Info(CancellationToken cancellationToken_ = default)
            {
                var in_ = SerializerState.CreateForRpc<Mas.Schema.Common.Identifiable.Params_Info.WRITER>();
                var arg_ = new Mas.Schema.Common.Identifiable.Params_Info()
                {};
                arg_?.serialize(in_);
                using (var d_ = await Call(12875740530987518165UL, 0, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_).WhenReturned)
                {
                    var r_ = CapnpSerializable.Create<Mas.Schema.Common.IdInformation>(d_);
                    return r_;
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xcb17668f2d39c70fUL)]
        public class Runnable_Skeleton : Skeleton<IRunnable>
        {
            public Runnable_Skeleton()
            {
                SetMethodTable(Start, Stop);
            }

            public override ulong InterfaceId => 14634278279288833807UL;
            Task<AnswerOrCounterquestion> Start(DeserializerState d_, CancellationToken cancellationToken_)
            {
                using (d_)
                {
                    var in_ = CapnpSerializable.Create<Mas.Schema.Fbp.Component.Runnable.Params_Start>(d_);
                    return Impatient.MaybeTailCall(Impl.Start(in_.PortInfosReaderSr, cancellationToken_), success =>
                    {
                        var s_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.Component.Runnable.Result_Start.WRITER>();
                        var r_ = new Mas.Schema.Fbp.Component.Runnable.Result_Start{Success = success};
                        r_.serialize(s_);
                        return s_;
                    }

                    );
                }
            }

            Task<AnswerOrCounterquestion> Stop(DeserializerState d_, CancellationToken cancellationToken_)
            {
                using (d_)
                {
                    return Impatient.MaybeTailCall(Impl.Stop(cancellationToken_), success =>
                    {
                        var s_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.Component.Runnable.Result_Stop.WRITER>();
                        var r_ = new Mas.Schema.Fbp.Component.Runnable.Result_Stop{Success = success};
                        r_.serialize(s_);
                        return s_;
                    }

                    );
                }
            }
        }

        public static class Runnable
        {
            [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xdeb75f08b2540532UL)]
            public class Params_Start : ICapnpSerializable
            {
                public const UInt64 typeId = 0xdeb75f08b2540532UL;
                void ICapnpSerializable.Deserialize(DeserializerState arg_)
                {
                    var reader = READER.create(arg_);
                    PortInfosReaderSr = reader.PortInfosReaderSr;
                    applyDefaults();
                }

                public void serialize(WRITER writer)
                {
                    writer.PortInfosReaderSr = PortInfosReaderSr;
                }

                void ICapnpSerializable.Serialize(SerializerState arg_)
                {
                    serialize(arg_.Rewrap<WRITER>());
                }

                public void applyDefaults()
                {
                }

                public string PortInfosReaderSr
                {
                    get;
                    set;
                }

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
                    public string PortInfosReaderSr => ctx.ReadText(0, null);
                }

                public class WRITER : SerializerState
                {
                    public WRITER()
                    {
                        this.SetStruct(0, 1);
                    }

                    public string PortInfosReaderSr
                    {
                        get => this.ReadText(0, null);
                        set => this.WriteText(0, value, null);
                    }
                }
            }

            [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xbb18da359652a59cUL)]
            public class Result_Start : ICapnpSerializable
            {
                public const UInt64 typeId = 0xbb18da359652a59cUL;
                void ICapnpSerializable.Deserialize(DeserializerState arg_)
                {
                    var reader = READER.create(arg_);
                    Success = reader.Success;
                    applyDefaults();
                }

                public void serialize(WRITER writer)
                {
                    writer.Success = Success;
                }

                void ICapnpSerializable.Serialize(SerializerState arg_)
                {
                    serialize(arg_.Rewrap<WRITER>());
                }

                public void applyDefaults()
                {
                }

                public bool Success
                {
                    get;
                    set;
                }

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
                    public bool Success => ctx.ReadDataBool(0UL, false);
                }

                public class WRITER : SerializerState
                {
                    public WRITER()
                    {
                        this.SetStruct(1, 0);
                    }

                    public bool Success
                    {
                        get => this.ReadDataBool(0UL, false);
                        set => this.WriteData(0UL, value, false);
                    }
                }
            }

            [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xe6ba083a247c91eeUL)]
            public class Params_Stop : ICapnpSerializable
            {
                public const UInt64 typeId = 0xe6ba083a247c91eeUL;
                void ICapnpSerializable.Deserialize(DeserializerState arg_)
                {
                    var reader = READER.create(arg_);
                    applyDefaults();
                }

                public void serialize(WRITER writer)
                {
                }

                void ICapnpSerializable.Serialize(SerializerState arg_)
                {
                    serialize(arg_.Rewrap<WRITER>());
                }

                public void applyDefaults()
                {
                }

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
                }

                public class WRITER : SerializerState
                {
                    public WRITER()
                    {
                        this.SetStruct(0, 0);
                    }
                }
            }

            [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xcbf00f9ba87ee17eUL)]
            public class Result_Stop : ICapnpSerializable
            {
                public const UInt64 typeId = 0xcbf00f9ba87ee17eUL;
                void ICapnpSerializable.Deserialize(DeserializerState arg_)
                {
                    var reader = READER.create(arg_);
                    Success = reader.Success;
                    applyDefaults();
                }

                public void serialize(WRITER writer)
                {
                    writer.Success = Success;
                }

                void ICapnpSerializable.Serialize(SerializerState arg_)
                {
                    serialize(arg_.Rewrap<WRITER>());
                }

                public void applyDefaults()
                {
                }

                public bool Success
                {
                    get;
                    set;
                }

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
                    public bool Success => ctx.ReadDataBool(0UL, false);
                }

                public class WRITER : SerializerState
                {
                    public WRITER()
                    {
                        this.SetStruct(1, 0);
                    }

                    public bool Success
                    {
                        get => this.ReadDataBool(0UL, false);
                        set => this.WriteData(0UL, value, false);
                    }
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xc6976ac75246b450UL)]
        public enum ComponentType : ushort
        {
            standard,
            iip,
            subflow
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xc28d2829add1cd72UL)]
        public class Port : ICapnpSerializable
        {
            public const UInt64 typeId = 0xc28d2829add1cd72UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                Name = reader.Name;
                TheContentType = reader.TheContentType;
                Type = reader.Type;
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.Name = Name;
                writer.TheContentType = TheContentType;
                writer.Type = Type;
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public string Name
            {
                get;
                set;
            }

            public string TheContentType
            {
                get;
                set;
            }

            public Mas.Schema.Fbp.Component.Port.PortType Type
            {
                get;
                set;
            }

            = Mas.Schema.Fbp.Component.Port.PortType.standard;
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
                public string Name => ctx.ReadText(0, null);
                public string TheContentType => ctx.ReadText(1, null);
                public Mas.Schema.Fbp.Component.Port.PortType Type => (Mas.Schema.Fbp.Component.Port.PortType)ctx.ReadDataUShort(0UL, (ushort)0);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(1, 2);
                }

                public string Name
                {
                    get => this.ReadText(0, null);
                    set => this.WriteText(0, value, null);
                }

                public string TheContentType
                {
                    get => this.ReadText(1, null);
                    set => this.WriteText(1, value, null);
                }

                public Mas.Schema.Fbp.Component.Port.PortType Type
                {
                    get => (Mas.Schema.Fbp.Component.Port.PortType)this.ReadDataUShort(0UL, (ushort)0);
                    set => this.WriteData(0UL, (ushort)value, (ushort)0);
                }
            }

            [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xf58d7a7318a06224UL)]
            public enum PortType : ushort
            {
                standard
            }

            [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xf30610cf0ed94a2fUL)]
            public enum ContentType : ushort
            {
                structuredText
            }
        }
    }

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xfd32766446625ad7UL), Proxy(typeof(ComponentService_Proxy)), Skeleton(typeof(ComponentService_Skeleton))]
    public interface IComponentService : Mas.Schema.Common.IIdentifiable
    {
        Task<IReadOnlyList<Mas.Schema.Fbp.ComponentService.Entry>> List(CancellationToken cancellationToken_ = default);
        Task<Mas.Schema.Fbp.Component> Component(string id, CancellationToken cancellationToken_ = default);
        Task<IReadOnlyList<Mas.Schema.Common.IdInformation>> Categories(CancellationToken cancellationToken_ = default);
    }

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xfd32766446625ad7UL)]
    public class ComponentService_Proxy : Proxy, IComponentService
    {
        public Task<IReadOnlyList<Mas.Schema.Fbp.ComponentService.Entry>> List(CancellationToken cancellationToken_ = default)
        {
            var in_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.ComponentService.Params_List.WRITER>();
            var arg_ = new Mas.Schema.Fbp.ComponentService.Params_List()
            {};
            arg_?.serialize(in_);
            return Impatient.MakePipelineAware(Call(18244775213480958679UL, 0, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_), d_ =>
            {
                using (d_)
                {
                    var r_ = CapnpSerializable.Create<Mas.Schema.Fbp.ComponentService.Result_List>(d_);
                    return (r_.Entries);
                }
            }

            );
        }

        public Task<Mas.Schema.Fbp.Component> Component(string id, CancellationToken cancellationToken_ = default)
        {
            var in_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.ComponentService.Params_Component.WRITER>();
            var arg_ = new Mas.Schema.Fbp.ComponentService.Params_Component()
            {Id = id};
            arg_?.serialize(in_);
            return Impatient.MakePipelineAware(Call(18244775213480958679UL, 1, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_), d_ =>
            {
                using (d_)
                {
                    var r_ = CapnpSerializable.Create<Mas.Schema.Fbp.ComponentService.Result_Component>(d_);
                    return (r_.Comp);
                }
            }

            );
        }

        public async Task<IReadOnlyList<Mas.Schema.Common.IdInformation>> Categories(CancellationToken cancellationToken_ = default)
        {
            var in_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.ComponentService.Params_Categories.WRITER>();
            var arg_ = new Mas.Schema.Fbp.ComponentService.Params_Categories()
            {};
            arg_?.serialize(in_);
            using (var d_ = await Call(18244775213480958679UL, 2, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_).WhenReturned)
            {
                var r_ = CapnpSerializable.Create<Mas.Schema.Fbp.ComponentService.Result_Categories>(d_);
                return (r_.Categories);
            }
        }

        public async Task<Mas.Schema.Common.IdInformation> Info(CancellationToken cancellationToken_ = default)
        {
            var in_ = SerializerState.CreateForRpc<Mas.Schema.Common.Identifiable.Params_Info.WRITER>();
            var arg_ = new Mas.Schema.Common.Identifiable.Params_Info()
            {};
            arg_?.serialize(in_);
            using (var d_ = await Call(12875740530987518165UL, 0, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_).WhenReturned)
            {
                var r_ = CapnpSerializable.Create<Mas.Schema.Common.IdInformation>(d_);
                return r_;
            }
        }
    }

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xfd32766446625ad7UL)]
    public class ComponentService_Skeleton : Skeleton<IComponentService>
    {
        public ComponentService_Skeleton()
        {
            SetMethodTable(List, Component, Categories);
        }

        public override ulong InterfaceId => 18244775213480958679UL;
        Task<AnswerOrCounterquestion> List(DeserializerState d_, CancellationToken cancellationToken_)
        {
            using (d_)
            {
                return Impatient.MaybeTailCall(Impl.List(cancellationToken_), entries =>
                {
                    var s_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.ComponentService.Result_List.WRITER>();
                    var r_ = new Mas.Schema.Fbp.ComponentService.Result_List{Entries = entries};
                    r_.serialize(s_);
                    return s_;
                }

                );
            }
        }

        Task<AnswerOrCounterquestion> Component(DeserializerState d_, CancellationToken cancellationToken_)
        {
            using (d_)
            {
                var in_ = CapnpSerializable.Create<Mas.Schema.Fbp.ComponentService.Params_Component>(d_);
                return Impatient.MaybeTailCall(Impl.Component(in_.Id, cancellationToken_), comp =>
                {
                    var s_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.ComponentService.Result_Component.WRITER>();
                    var r_ = new Mas.Schema.Fbp.ComponentService.Result_Component{Comp = comp};
                    r_.serialize(s_);
                    return s_;
                }

                );
            }
        }

        Task<AnswerOrCounterquestion> Categories(DeserializerState d_, CancellationToken cancellationToken_)
        {
            using (d_)
            {
                return Impatient.MaybeTailCall(Impl.Categories(cancellationToken_), categories =>
                {
                    var s_ = SerializerState.CreateForRpc<Mas.Schema.Fbp.ComponentService.Result_Categories.WRITER>();
                    var r_ = new Mas.Schema.Fbp.ComponentService.Result_Categories{Categories = categories};
                    r_.serialize(s_);
                    return s_;
                }

                );
            }
        }
    }

    public static class ComponentService
    {
        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xeda3c43711165718UL)]
        public class Entry : ICapnpSerializable
        {
            public const UInt64 typeId = 0xeda3c43711165718UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                CategoryId = reader.CategoryId;
                Component = CapnpSerializable.Create<Mas.Schema.Fbp.Component>(reader.Component);
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.CategoryId = CategoryId;
                Component?.serialize(writer.Component);
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public string CategoryId
            {
                get;
                set;
            }

            public Mas.Schema.Fbp.Component Component
            {
                get;
                set;
            }

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
                public string CategoryId => ctx.ReadText(0, null);
                public Mas.Schema.Fbp.Component.READER Component => ctx.ReadStruct(1, Mas.Schema.Fbp.Component.READER.create);
                public bool HasComponent => ctx.IsStructFieldNonNull(1);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 2);
                }

                public string CategoryId
                {
                    get => this.ReadText(0, null);
                    set => this.WriteText(0, value, null);
                }

                public Mas.Schema.Fbp.Component.WRITER Component
                {
                    get => BuildPointer<Mas.Schema.Fbp.Component.WRITER>(1);
                    set => Link(1, value);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0x8fe5f30dda656838UL)]
        public class Params_List : ICapnpSerializable
        {
            public const UInt64 typeId = 0x8fe5f30dda656838UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

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
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 0);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xa99399396807d8c5UL)]
        public class Result_List : ICapnpSerializable
        {
            public const UInt64 typeId = 0xa99399396807d8c5UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                Entries = reader.Entries?.ToReadOnlyList(_ => CapnpSerializable.Create<Mas.Schema.Fbp.ComponentService.Entry>(_));
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.Entries.Init(Entries, (_s1, _v1) => _v1?.serialize(_s1));
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public IReadOnlyList<Mas.Schema.Fbp.ComponentService.Entry> Entries
            {
                get;
                set;
            }

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
                public IReadOnlyList<Mas.Schema.Fbp.ComponentService.Entry.READER> Entries => ctx.ReadList(0).Cast(Mas.Schema.Fbp.ComponentService.Entry.READER.create);
                public bool HasEntries => ctx.IsStructFieldNonNull(0);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 1);
                }

                public ListOfStructsSerializer<Mas.Schema.Fbp.ComponentService.Entry.WRITER> Entries
                {
                    get => BuildPointer<ListOfStructsSerializer<Mas.Schema.Fbp.ComponentService.Entry.WRITER>>(0);
                    set => Link(0, value);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0x973c5bebb677e106UL)]
        public class Params_Component : ICapnpSerializable
        {
            public const UInt64 typeId = 0x973c5bebb677e106UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                Id = reader.Id;
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.Id = Id;
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public string Id
            {
                get;
                set;
            }

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
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 1);
                }

                public string Id
                {
                    get => this.ReadText(0, null);
                    set => this.WriteText(0, value, null);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0x816f3a8598cfd055UL)]
        public class Result_Component : ICapnpSerializable
        {
            public const UInt64 typeId = 0x816f3a8598cfd055UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                Comp = CapnpSerializable.Create<Mas.Schema.Fbp.Component>(reader.Comp);
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                Comp?.serialize(writer.Comp);
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public Mas.Schema.Fbp.Component Comp
            {
                get;
                set;
            }

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
                public Mas.Schema.Fbp.Component.READER Comp => ctx.ReadStruct(0, Mas.Schema.Fbp.Component.READER.create);
                public bool HasComp => ctx.IsStructFieldNonNull(0);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 1);
                }

                public Mas.Schema.Fbp.Component.WRITER Comp
                {
                    get => BuildPointer<Mas.Schema.Fbp.Component.WRITER>(0);
                    set => Link(0, value);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xdd2951b8efe293aeUL)]
        public class Params_Categories : ICapnpSerializable
        {
            public const UInt64 typeId = 0xdd2951b8efe293aeUL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

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
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 0);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xb4315bf70ae26e84UL)]
        public class Result_Categories : ICapnpSerializable
        {
            public const UInt64 typeId = 0xb4315bf70ae26e84UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                Categories = reader.Categories?.ToReadOnlyList(_ => CapnpSerializable.Create<Mas.Schema.Common.IdInformation>(_));
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.Categories.Init(Categories, (_s1, _v1) => _v1?.serialize(_s1));
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public IReadOnlyList<Mas.Schema.Common.IdInformation> Categories
            {
                get;
                set;
            }

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
                public IReadOnlyList<Mas.Schema.Common.IdInformation.READER> Categories => ctx.ReadList(0).Cast(Mas.Schema.Common.IdInformation.READER.create);
                public bool HasCategories => ctx.IsStructFieldNonNull(0);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 1);
                }

                public ListOfStructsSerializer<Mas.Schema.Common.IdInformation.WRITER> Categories
                {
                    get => BuildPointer<ListOfStructsSerializer<Mas.Schema.Common.IdInformation.WRITER>>(0);
                    set => Link(0, value);
                }
            }
        }
    }

    public static partial class PipeliningSupportExtensions_fbp
    {
        static readonly MemberAccessPath Path_mas_schema_fbp_Channel_endpoints_W = new MemberAccessPath(1U);
        public static Mas.Schema.Fbp.Channel<TV>.IWriter W<TV>(this Task<(Mas.Schema.Fbp.Channel<TV>.IReader, Mas.Schema.Fbp.Channel<TV>.IWriter)> task)
        where TV : class
        {
            async Task<IDisposable> AwaitProxy() => (await task).Item2;
            return (Mas.Schema.Fbp.Channel<TV>.IWriter)CapabilityReflection.CreateProxy<Mas.Schema.Fbp.Channel<TV>.IWriter>(Impatient.Access(task, Path_mas_schema_fbp_Channel_endpoints_W, AwaitProxy()));
        }

        static readonly MemberAccessPath Path_mas_schema_fbp_ComponentService_component_Comp_Run = new MemberAccessPath(0U, 3U);
        public static Mas.Schema.Fbp.Component.IRunnable Comp_Run(this Task<Mas.Schema.Fbp.Component> task)
        {
            async Task<IDisposable> AwaitProxy() => (await task).Run;
            return (Mas.Schema.Fbp.Component.IRunnable)CapabilityReflection.CreateProxy<Mas.Schema.Fbp.Component.IRunnable>(Impatient.Access(task, Path_mas_schema_fbp_ComponentService_component_Comp_Run, AwaitProxy()));
        }
    }
}