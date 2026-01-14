using System;
using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;
using Capnp;
using Capnp.Rpc;

namespace Mas.Schema.Dakis
{
    [
        System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"),
        TypeId(0xdb3fb36057abc378UL),
        Proxy(typeof(Mas.Schema.Dakis.ModamWrapperService_Proxy)),
        Skeleton(typeof(Mas.Schema.Dakis.ModamWrapperService_Skeleton))
    ]
    public interface IModamWrapperService : IDisposable
    {
        Task<string> Run(string input, CancellationToken cancellationToken_ = default);
    }

    [
        System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"),
        TypeId(0xdb3fb36057abc378UL)
    ]
    public class ModamWrapperService_Proxy : Proxy, IModamWrapperService
    {
        public async Task<string> Run(string input, CancellationToken cancellationToken_ = default)
        {
            var in_ =
                SerializerState.CreateForRpc<Mas.Schema.Dakis.ModamWrapperService.Params_Run.WRITER>();
            var arg_ = new Mas.Schema.Dakis.ModamWrapperService.Params_Run() { Input = input };
            arg_?.serialize(in_);
            using (
                var d_ = await Call(
                    15798543244208096120UL,
                    0,
                    in_.Rewrap<DynamicSerializerState>(),
                    false,
                    cancellationToken_
                ).WhenReturned
            )
            {
                var r_ = CapnpSerializable.Create<Mas.Schema.Dakis.ModamWrapperService.Result_Run>(
                    d_
                );
                return (r_.Output);
            }
        }
    }

    [
        System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"),
        TypeId(0xdb3fb36057abc378UL)
    ]
    public class ModamWrapperService_Skeleton : Skeleton<IModamWrapperService>
    {
        public ModamWrapperService_Skeleton()
        {
            SetMethodTable(Run);
        }

        public override ulong InterfaceId => 15798543244208096120UL;

        Task<AnswerOrCounterquestion> Run(
            DeserializerState d_,
            CancellationToken cancellationToken_
        )
        {
            using (d_)
            {
                var in_ = CapnpSerializable.Create<Mas.Schema.Dakis.ModamWrapperService.Params_Run>(
                    d_
                );
                return Impatient.MaybeTailCall(
                    Impl.Run(in_.Input, cancellationToken_),
                    output =>
                    {
                        var s_ =
                            SerializerState.CreateForRpc<Mas.Schema.Dakis.ModamWrapperService.Result_Run.WRITER>();
                        var r_ = new Mas.Schema.Dakis.ModamWrapperService.Result_Run
                        {
                            Output = output,
                        };
                        r_.serialize(s_);
                        return s_;
                    }
                );
            }
        }
    }

    public static class ModamWrapperService
    {
        [
            System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"),
            TypeId(0xda027c8ae9dacdccUL)
        ]
        public class Params_Run : ICapnpSerializable
        {
            public const UInt64 typeId = 0xda027c8ae9dacdccUL;

            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                Input = reader.Input;
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.Input = Input;
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults() { }

            public string Input { get; set; }

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

                public string Input => ctx.ReadText(0, null);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 1);
                }

                public string Input
                {
                    get => this.ReadText(0, null);
                    set => this.WriteText(0, value, null);
                }
            }
        }

        [
            System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"),
            TypeId(0x89dee76797d04686UL)
        ]
        public class Result_Run : ICapnpSerializable
        {
            public const UInt64 typeId = 0x89dee76797d04686UL;

            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                Output = reader.Output;
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.Output = Output;
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults() { }

            public string Output { get; set; }

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

                public string Output => ctx.ReadText(0, null);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 1);
                }

                public string Output
                {
                    get => this.ReadText(0, null);
                    set => this.WriteText(0, value, null);
                }
            }
        }
    }
}
