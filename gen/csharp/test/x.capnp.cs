using Capnp;
using Capnp.Rpc;
using System;
using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;

namespace Mas.Schema.Test
{
    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xd227ef68de0bc647UL)]
    public class S : ICapnpSerializable
    {
        public const UInt64 typeId = 0xd227ef68de0bc647UL;
        void ICapnpSerializable.Deserialize(DeserializerState arg_)
        {
            var reader = READER.create(arg_);
            C = reader.C;
            applyDefaults();
        }

        public void serialize(WRITER writer)
        {
            writer.C = C;
        }

        void ICapnpSerializable.Serialize(SerializerState arg_)
        {
            serialize(arg_.Rewrap<WRITER>());
        }

        public void applyDefaults()
        {
        }

        public Mas.Schema.Test.IX C
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
            public Mas.Schema.Test.IX C => ctx.ReadCap<Mas.Schema.Test.IX>(0);
        }

        public class WRITER : SerializerState
        {
            public WRITER()
            {
                this.SetStruct(0, 1);
            }

            public Mas.Schema.Test.IX C
            {
                get => ReadCap<Mas.Schema.Test.IX>(0);
                set => LinkObject(0, value);
            }
        }
    }

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xdcf28e81fa4de615UL), Proxy(typeof(X_Proxy)), Skeleton(typeof(X_Skeleton))]
    public interface IX : IDisposable
    {
        Task<string> M(long i, CancellationToken cancellationToken_ = default);
    }

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xdcf28e81fa4de615UL)]
    public class X_Proxy : Proxy, IX
    {
        public async Task<string> M(long i, CancellationToken cancellationToken_ = default)
        {
            var in_ = SerializerState.CreateForRpc<Mas.Schema.Test.X.Params_M.WRITER>();
            var arg_ = new Mas.Schema.Test.X.Params_M()
            {I = i};
            arg_?.serialize(in_);
            using (var d_ = await Call(15920944321609459221UL, 0, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_).WhenReturned)
            {
                var r_ = CapnpSerializable.Create<Mas.Schema.Test.X.Result_M>(d_);
                return (r_.T);
            }
        }
    }

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xdcf28e81fa4de615UL)]
    public class X_Skeleton : Skeleton<IX>
    {
        public X_Skeleton()
        {
            SetMethodTable(M);
        }

        public override ulong InterfaceId => 15920944321609459221UL;
        Task<AnswerOrCounterquestion> M(DeserializerState d_, CancellationToken cancellationToken_)
        {
            using (d_)
            {
                var in_ = CapnpSerializable.Create<Mas.Schema.Test.X.Params_M>(d_);
                return Impatient.MaybeTailCall(Impl.M(in_.I, cancellationToken_), t =>
                {
                    var s_ = SerializerState.CreateForRpc<Mas.Schema.Test.X.Result_M.WRITER>();
                    var r_ = new Mas.Schema.Test.X.Result_M{T = t};
                    r_.serialize(s_);
                    return s_;
                }

                );
            }
        }
    }

    public static class X
    {
        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xc68563695ada2a40UL)]
        public class Params_M : ICapnpSerializable
        {
            public const UInt64 typeId = 0xc68563695ada2a40UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                I = reader.I;
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.I = I;
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public long I
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
                public long I => ctx.ReadDataLong(0UL, 0L);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(1, 0);
                }

                public long I
                {
                    get => this.ReadDataLong(0UL, 0L);
                    set => this.WriteData(0UL, value, 0L);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0x86aae6bcee1a970dUL)]
        public class Result_M : ICapnpSerializable
        {
            public const UInt64 typeId = 0x86aae6bcee1a970dUL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                T = reader.T;
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.T = T;
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public string T
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
                public string T => ctx.ReadText(0, null);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 1);
                }

                public string T
                {
                    get => this.ReadText(0, null);
                    set => this.WriteText(0, value, null);
                }
            }
        }
    }

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xac121e5aa82ca6bdUL), Proxy(typeof(Y_Proxy)), Skeleton(typeof(Y_Skeleton))]
    public interface IY : IDisposable
    {
        Task M(string hello, CancellationToken cancellationToken_ = default);
    }

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xac121e5aa82ca6bdUL)]
    public class Y_Proxy : Proxy, IY
    {
        public async Task M(string hello, CancellationToken cancellationToken_ = default)
        {
            var in_ = SerializerState.CreateForRpc<Mas.Schema.Test.Y.Params_M.WRITER>();
            var arg_ = new Mas.Schema.Test.Y.Params_M()
            {Hello = hello};
            arg_?.serialize(in_);
            using (var d_ = await Call(12399006098821785277UL, 0, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_).WhenReturned)
            {
                var r_ = CapnpSerializable.Create<Mas.Schema.Test.Y.Result_M>(d_);
                return;
            }
        }
    }

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xac121e5aa82ca6bdUL)]
    public class Y_Skeleton : Skeleton<IY>
    {
        public Y_Skeleton()
        {
            SetMethodTable(M);
        }

        public override ulong InterfaceId => 12399006098821785277UL;
        async Task<AnswerOrCounterquestion> M(DeserializerState d_, CancellationToken cancellationToken_)
        {
            using (d_)
            {
                var in_ = CapnpSerializable.Create<Mas.Schema.Test.Y.Params_M>(d_);
                await Impl.M(in_.Hello, cancellationToken_);
                var s_ = SerializerState.CreateForRpc<Mas.Schema.Test.Y.Result_M.WRITER>();
                return s_;
            }
        }
    }

    public static class Y
    {
        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xc102bb9ca7ace092UL)]
        public class Params_M : ICapnpSerializable
        {
            public const UInt64 typeId = 0xc102bb9ca7ace092UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                Hello = reader.Hello;
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.Hello = Hello;
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public string Hello
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
                public string Hello => ctx.ReadText(0, null);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 1);
                }

                public string Hello
                {
                    get => this.ReadText(0, null);
                    set => this.WriteText(0, value, null);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xdcf58b9bef546812UL)]
        public class Result_M : ICapnpSerializable
        {
            public const UInt64 typeId = 0xdcf58b9bef546812UL;
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

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xc64526206425c2abUL), Proxy(typeof(Z_Proxy)), Skeleton(typeof(Z_Skeleton))]
    public interface IZ : IDisposable
    {
        Task<double> M(long n, CancellationToken cancellationToken_ = default);
    }

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xc64526206425c2abUL)]
    public class Z_Proxy : Proxy, IZ
    {
        public async Task<double> M(long n, CancellationToken cancellationToken_ = default)
        {
            var in_ = SerializerState.CreateForRpc<Mas.Schema.Test.Z.Params_M.WRITER>();
            var arg_ = new Mas.Schema.Test.Z.Params_M()
            {N = n};
            arg_?.serialize(in_);
            using (var d_ = await Call(14286867313463771819UL, 0, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_).WhenReturned)
            {
                var r_ = CapnpSerializable.Create<Mas.Schema.Test.Z.Result_M>(d_);
                return (r_.R);
            }
        }
    }

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xc64526206425c2abUL)]
    public class Z_Skeleton : Skeleton<IZ>
    {
        public Z_Skeleton()
        {
            SetMethodTable(M);
        }

        public override ulong InterfaceId => 14286867313463771819UL;
        Task<AnswerOrCounterquestion> M(DeserializerState d_, CancellationToken cancellationToken_)
        {
            using (d_)
            {
                var in_ = CapnpSerializable.Create<Mas.Schema.Test.Z.Params_M>(d_);
                return Impatient.MaybeTailCall(Impl.M(in_.N, cancellationToken_), r =>
                {
                    var s_ = SerializerState.CreateForRpc<Mas.Schema.Test.Z.Result_M.WRITER>();
                    var r_ = new Mas.Schema.Test.Z.Result_M{R = r};
                    r_.serialize(s_);
                    return s_;
                }

                );
            }
        }
    }

    public static class Z
    {
        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xf01d08c96dc98cc9UL)]
        public class Params_M : ICapnpSerializable
        {
            public const UInt64 typeId = 0xf01d08c96dc98cc9UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                N = reader.N;
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.N = N;
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public long N
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
                public long N => ctx.ReadDataLong(0UL, 0L);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(1, 0);
                }

                public long N
                {
                    get => this.ReadDataLong(0UL, 0L);
                    set => this.WriteData(0UL, value, 0L);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xd444a663531a6b53UL)]
        public class Result_M : ICapnpSerializable
        {
            public const UInt64 typeId = 0xd444a663531a6b53UL;
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

            public double R
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
                public double R => ctx.ReadDataDouble(0UL, 0);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(1, 0);
                }

                public double R
                {
                    get => this.ReadDataDouble(0UL, 0);
                    set => this.WriteData(0UL, value, 0);
                }
            }
        }
    }
}