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
        Task<string> RunAemModel(string input, CancellationToken cancellationToken_ = default);
        Task<string> RunFieldModel(string input, CancellationToken cancellationToken_ = default);
    }

    [
        System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"),
        TypeId(0xdb3fb36057abc378UL)
    ]
    public class ModamWrapperService_Proxy : Proxy, IModamWrapperService
    {
        public async Task<string> RunAemModel(
            string input,
            CancellationToken cancellationToken_ = default
        )
        {
            var in_ =
                SerializerState.CreateForRpc<Mas.Schema.Dakis.ModamWrapperService.Params_RunAemModel.WRITER>();
            var arg_ = new Mas.Schema.Dakis.ModamWrapperService.Params_RunAemModel()
            {
                Input = input,
            };
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
                var r_ =
                    CapnpSerializable.Create<Mas.Schema.Dakis.ModamWrapperService.Result_RunAemModel>(
                        d_
                    );
                return (r_.Output);
            }
        }

        public async Task<string> RunFieldModel(
            string input,
            CancellationToken cancellationToken_ = default
        )
        {
            var in_ =
                SerializerState.CreateForRpc<Mas.Schema.Dakis.ModamWrapperService.Params_RunFieldModel.WRITER>();
            var arg_ = new Mas.Schema.Dakis.ModamWrapperService.Params_RunFieldModel()
            {
                Input = input,
            };
            arg_?.serialize(in_);
            using (
                var d_ = await Call(
                    15798543244208096120UL,
                    1,
                    in_.Rewrap<DynamicSerializerState>(),
                    false,
                    cancellationToken_
                ).WhenReturned
            )
            {
                var r_ =
                    CapnpSerializable.Create<Mas.Schema.Dakis.ModamWrapperService.Result_RunFieldModel>(
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
            SetMethodTable(RunAemModel, RunFieldModel);
        }

        public override ulong InterfaceId => 15798543244208096120UL;

        Task<AnswerOrCounterquestion> RunAemModel(
            DeserializerState d_,
            CancellationToken cancellationToken_
        )
        {
            using (d_)
            {
                var in_ =
                    CapnpSerializable.Create<Mas.Schema.Dakis.ModamWrapperService.Params_RunAemModel>(
                        d_
                    );
                return Impatient.MaybeTailCall(
                    Impl.RunAemModel(in_.Input, cancellationToken_),
                    output =>
                    {
                        var s_ =
                            SerializerState.CreateForRpc<Mas.Schema.Dakis.ModamWrapperService.Result_RunAemModel.WRITER>();
                        var r_ = new Mas.Schema.Dakis.ModamWrapperService.Result_RunAemModel
                        {
                            Output = output,
                        };
                        r_.serialize(s_);
                        return s_;
                    }
                );
            }
        }

        Task<AnswerOrCounterquestion> RunFieldModel(
            DeserializerState d_,
            CancellationToken cancellationToken_
        )
        {
            using (d_)
            {
                var in_ =
                    CapnpSerializable.Create<Mas.Schema.Dakis.ModamWrapperService.Params_RunFieldModel>(
                        d_
                    );
                return Impatient.MaybeTailCall(
                    Impl.RunFieldModel(in_.Input, cancellationToken_),
                    output =>
                    {
                        var s_ =
                            SerializerState.CreateForRpc<Mas.Schema.Dakis.ModamWrapperService.Result_RunFieldModel.WRITER>();
                        var r_ = new Mas.Schema.Dakis.ModamWrapperService.Result_RunFieldModel
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
        public class Params_RunAemModel : ICapnpSerializable
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
        public class Result_RunAemModel : ICapnpSerializable
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

        [
            System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"),
            TypeId(0x943b0ea4d050f605UL)
        ]
        public class Params_RunFieldModel : ICapnpSerializable
        {
            public const UInt64 typeId = 0x943b0ea4d050f605UL;

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
            TypeId(0x96ba69d12ba4187eUL)
        ]
        public class Result_RunFieldModel : ICapnpSerializable
        {
            public const UInt64 typeId = 0x96ba69d12ba4187eUL;

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
