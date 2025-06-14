using Capnp;
using Capnp.Rpc;
using System;
using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;

namespace Mas.Schema.Registry
{
    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xf503f3237666574eUL), Proxy(typeof(Admin_Proxy)), Skeleton(typeof(Admin_Skeleton))]
    public interface IAdmin : Mas.Schema.Common.IIdentifiable
    {
        Task<bool> AddCategory(Mas.Schema.Common.IdInformation category, bool upsert, CancellationToken cancellationToken_ = default);
        Task<IReadOnlyList<Mas.Schema.Common.IIdentifiable>> RemoveCategory(string categoryId, string moveObjectsToCategoryId, CancellationToken cancellationToken_ = default);
        Task<IReadOnlyList<string>> MoveObjects(IReadOnlyList<string> objectIds, string toCatId, CancellationToken cancellationToken_ = default);
        Task<IReadOnlyList<Mas.Schema.Common.IIdentifiable>> RemoveObjects(IReadOnlyList<string> objectIds, CancellationToken cancellationToken_ = default);
        Task<Mas.Schema.Registry.IRegistry> Registry(CancellationToken cancellationToken_ = default);
    }

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xf503f3237666574eUL)]
    public class Admin_Proxy : Proxy, IAdmin
    {
        public async Task<bool> AddCategory(Mas.Schema.Common.IdInformation category, bool upsert, CancellationToken cancellationToken_ = default)
        {
            var in_ = SerializerState.CreateForRpc<Mas.Schema.Registry.Admin.Params_AddCategory.WRITER>();
            var arg_ = new Mas.Schema.Registry.Admin.Params_AddCategory()
            {Category = category, Upsert = upsert};
            arg_?.serialize(in_);
            using (var d_ = await Call(17655222297858299726UL, 0, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_).WhenReturned)
            {
                var r_ = CapnpSerializable.Create<Mas.Schema.Registry.Admin.Result_AddCategory>(d_);
                return (r_.Success);
            }
        }

        public Task<IReadOnlyList<Mas.Schema.Common.IIdentifiable>> RemoveCategory(string categoryId, string moveObjectsToCategoryId, CancellationToken cancellationToken_ = default)
        {
            var in_ = SerializerState.CreateForRpc<Mas.Schema.Registry.Admin.Params_RemoveCategory.WRITER>();
            var arg_ = new Mas.Schema.Registry.Admin.Params_RemoveCategory()
            {CategoryId = categoryId, MoveObjectsToCategoryId = moveObjectsToCategoryId};
            arg_?.serialize(in_);
            return Impatient.MakePipelineAware(Call(17655222297858299726UL, 1, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_), d_ =>
            {
                using (d_)
                {
                    var r_ = CapnpSerializable.Create<Mas.Schema.Registry.Admin.Result_RemoveCategory>(d_);
                    return (r_.RemovedObjects);
                }
            }

            );
        }

        public async Task<IReadOnlyList<string>> MoveObjects(IReadOnlyList<string> objectIds, string toCatId, CancellationToken cancellationToken_ = default)
        {
            var in_ = SerializerState.CreateForRpc<Mas.Schema.Registry.Admin.Params_MoveObjects.WRITER>();
            var arg_ = new Mas.Schema.Registry.Admin.Params_MoveObjects()
            {ObjectIds = objectIds, ToCatId = toCatId};
            arg_?.serialize(in_);
            using (var d_ = await Call(17655222297858299726UL, 2, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_).WhenReturned)
            {
                var r_ = CapnpSerializable.Create<Mas.Schema.Registry.Admin.Result_MoveObjects>(d_);
                return (r_.MovedObjectIds);
            }
        }

        public Task<IReadOnlyList<Mas.Schema.Common.IIdentifiable>> RemoveObjects(IReadOnlyList<string> objectIds, CancellationToken cancellationToken_ = default)
        {
            var in_ = SerializerState.CreateForRpc<Mas.Schema.Registry.Admin.Params_RemoveObjects.WRITER>();
            var arg_ = new Mas.Schema.Registry.Admin.Params_RemoveObjects()
            {ObjectIds = objectIds};
            arg_?.serialize(in_);
            return Impatient.MakePipelineAware(Call(17655222297858299726UL, 3, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_), d_ =>
            {
                using (d_)
                {
                    var r_ = CapnpSerializable.Create<Mas.Schema.Registry.Admin.Result_RemoveObjects>(d_);
                    return (r_.RemovedObjects);
                }
            }

            );
        }

        public Task<Mas.Schema.Registry.IRegistry> Registry(CancellationToken cancellationToken_ = default)
        {
            var in_ = SerializerState.CreateForRpc<Mas.Schema.Registry.Admin.Params_Registry.WRITER>();
            var arg_ = new Mas.Schema.Registry.Admin.Params_Registry()
            {};
            arg_?.serialize(in_);
            return Impatient.MakePipelineAware(Call(17655222297858299726UL, 4, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_), d_ =>
            {
                using (d_)
                {
                    var r_ = CapnpSerializable.Create<Mas.Schema.Registry.Admin.Result_Registry>(d_);
                    return (r_.Registry);
                }
            }

            );
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

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xf503f3237666574eUL)]
    public class Admin_Skeleton : Skeleton<IAdmin>
    {
        public Admin_Skeleton()
        {
            SetMethodTable(AddCategory, RemoveCategory, MoveObjects, RemoveObjects, Registry);
        }

        public override ulong InterfaceId => 17655222297858299726UL;
        Task<AnswerOrCounterquestion> AddCategory(DeserializerState d_, CancellationToken cancellationToken_)
        {
            using (d_)
            {
                var in_ = CapnpSerializable.Create<Mas.Schema.Registry.Admin.Params_AddCategory>(d_);
                return Impatient.MaybeTailCall(Impl.AddCategory(in_.Category, in_.Upsert, cancellationToken_), success =>
                {
                    var s_ = SerializerState.CreateForRpc<Mas.Schema.Registry.Admin.Result_AddCategory.WRITER>();
                    var r_ = new Mas.Schema.Registry.Admin.Result_AddCategory{Success = success};
                    r_.serialize(s_);
                    return s_;
                }

                );
            }
        }

        Task<AnswerOrCounterquestion> RemoveCategory(DeserializerState d_, CancellationToken cancellationToken_)
        {
            using (d_)
            {
                var in_ = CapnpSerializable.Create<Mas.Schema.Registry.Admin.Params_RemoveCategory>(d_);
                return Impatient.MaybeTailCall(Impl.RemoveCategory(in_.CategoryId, in_.MoveObjectsToCategoryId, cancellationToken_), removedObjects =>
                {
                    var s_ = SerializerState.CreateForRpc<Mas.Schema.Registry.Admin.Result_RemoveCategory.WRITER>();
                    var r_ = new Mas.Schema.Registry.Admin.Result_RemoveCategory{RemovedObjects = removedObjects};
                    r_.serialize(s_);
                    return s_;
                }

                );
            }
        }

        Task<AnswerOrCounterquestion> MoveObjects(DeserializerState d_, CancellationToken cancellationToken_)
        {
            using (d_)
            {
                var in_ = CapnpSerializable.Create<Mas.Schema.Registry.Admin.Params_MoveObjects>(d_);
                return Impatient.MaybeTailCall(Impl.MoveObjects(in_.ObjectIds, in_.ToCatId, cancellationToken_), movedObjectIds =>
                {
                    var s_ = SerializerState.CreateForRpc<Mas.Schema.Registry.Admin.Result_MoveObjects.WRITER>();
                    var r_ = new Mas.Schema.Registry.Admin.Result_MoveObjects{MovedObjectIds = movedObjectIds};
                    r_.serialize(s_);
                    return s_;
                }

                );
            }
        }

        Task<AnswerOrCounterquestion> RemoveObjects(DeserializerState d_, CancellationToken cancellationToken_)
        {
            using (d_)
            {
                var in_ = CapnpSerializable.Create<Mas.Schema.Registry.Admin.Params_RemoveObjects>(d_);
                return Impatient.MaybeTailCall(Impl.RemoveObjects(in_.ObjectIds, cancellationToken_), removedObjects =>
                {
                    var s_ = SerializerState.CreateForRpc<Mas.Schema.Registry.Admin.Result_RemoveObjects.WRITER>();
                    var r_ = new Mas.Schema.Registry.Admin.Result_RemoveObjects{RemovedObjects = removedObjects};
                    r_.serialize(s_);
                    return s_;
                }

                );
            }
        }

        Task<AnswerOrCounterquestion> Registry(DeserializerState d_, CancellationToken cancellationToken_)
        {
            using (d_)
            {
                return Impatient.MaybeTailCall(Impl.Registry(cancellationToken_), registry =>
                {
                    var s_ = SerializerState.CreateForRpc<Mas.Schema.Registry.Admin.Result_Registry.WRITER>();
                    var r_ = new Mas.Schema.Registry.Admin.Result_Registry{Registry = registry};
                    r_.serialize(s_);
                    return s_;
                }

                );
            }
        }
    }

    public static class Admin
    {
        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xdb16d4fbb18486f6UL)]
        public class Params_AddCategory : ICapnpSerializable
        {
            public const UInt64 typeId = 0xdb16d4fbb18486f6UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                Category = CapnpSerializable.Create<Mas.Schema.Common.IdInformation>(reader.Category);
                Upsert = reader.Upsert;
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                Category?.serialize(writer.Category);
                writer.Upsert = Upsert;
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public Mas.Schema.Common.IdInformation Category
            {
                get;
                set;
            }

            public bool Upsert
            {
                get;
                set;
            }

            = false;
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
                public Mas.Schema.Common.IdInformation.READER Category => ctx.ReadStruct(0, Mas.Schema.Common.IdInformation.READER.create);
                public bool HasCategory => ctx.IsStructFieldNonNull(0);
                public bool Upsert => ctx.ReadDataBool(0UL, false);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(1, 1);
                }

                public Mas.Schema.Common.IdInformation.WRITER Category
                {
                    get => BuildPointer<Mas.Schema.Common.IdInformation.WRITER>(0);
                    set => Link(0, value);
                }

                public bool Upsert
                {
                    get => this.ReadDataBool(0UL, false);
                    set => this.WriteData(0UL, value, false);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xbd3d832f7a7235b5UL)]
        public class Result_AddCategory : ICapnpSerializable
        {
            public const UInt64 typeId = 0xbd3d832f7a7235b5UL;
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

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xd5be1b8e0180ded6UL)]
        public class Params_RemoveCategory : ICapnpSerializable
        {
            public const UInt64 typeId = 0xd5be1b8e0180ded6UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                CategoryId = reader.CategoryId;
                MoveObjectsToCategoryId = reader.MoveObjectsToCategoryId;
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.CategoryId = CategoryId;
                writer.MoveObjectsToCategoryId = MoveObjectsToCategoryId;
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

            public string MoveObjectsToCategoryId
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
                public string MoveObjectsToCategoryId => ctx.ReadText(1, null);
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

                public string MoveObjectsToCategoryId
                {
                    get => this.ReadText(1, null);
                    set => this.WriteText(1, value, null);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xa9aca103106c8f05UL)]
        public class Result_RemoveCategory : ICapnpSerializable
        {
            public const UInt64 typeId = 0xa9aca103106c8f05UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                RemovedObjects = reader.RemovedObjects;
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.RemovedObjects.Init(RemovedObjects);
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public IReadOnlyList<Mas.Schema.Common.IIdentifiable> RemovedObjects
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
                public IReadOnlyList<Mas.Schema.Common.IIdentifiable> RemovedObjects => ctx.ReadCapList<Mas.Schema.Common.IIdentifiable>(0);
                public bool HasRemovedObjects => ctx.IsStructFieldNonNull(0);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 1);
                }

                public ListOfCapsSerializer<Mas.Schema.Common.IIdentifiable> RemovedObjects
                {
                    get => BuildPointer<ListOfCapsSerializer<Mas.Schema.Common.IIdentifiable>>(0);
                    set => Link(0, value);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0x8ebfd50c805adbc3UL)]
        public class Params_MoveObjects : ICapnpSerializable
        {
            public const UInt64 typeId = 0x8ebfd50c805adbc3UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                ObjectIds = reader.ObjectIds;
                ToCatId = reader.ToCatId;
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.ObjectIds.Init(ObjectIds);
                writer.ToCatId = ToCatId;
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public IReadOnlyList<string> ObjectIds
            {
                get;
                set;
            }

            public string ToCatId
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
                public IReadOnlyList<string> ObjectIds => ctx.ReadList(0).CastText2();
                public bool HasObjectIds => ctx.IsStructFieldNonNull(0);
                public string ToCatId => ctx.ReadText(1, null);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 2);
                }

                public ListOfTextSerializer ObjectIds
                {
                    get => BuildPointer<ListOfTextSerializer>(0);
                    set => Link(0, value);
                }

                public string ToCatId
                {
                    get => this.ReadText(1, null);
                    set => this.WriteText(1, value, null);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xd887d79a7ed3f45fUL)]
        public class Result_MoveObjects : ICapnpSerializable
        {
            public const UInt64 typeId = 0xd887d79a7ed3f45fUL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                MovedObjectIds = reader.MovedObjectIds;
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.MovedObjectIds.Init(MovedObjectIds);
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public IReadOnlyList<string> MovedObjectIds
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
                public IReadOnlyList<string> MovedObjectIds => ctx.ReadList(0).CastText2();
                public bool HasMovedObjectIds => ctx.IsStructFieldNonNull(0);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 1);
                }

                public ListOfTextSerializer MovedObjectIds
                {
                    get => BuildPointer<ListOfTextSerializer>(0);
                    set => Link(0, value);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0x96a5b17eee7ee1a3UL)]
        public class Params_RemoveObjects : ICapnpSerializable
        {
            public const UInt64 typeId = 0x96a5b17eee7ee1a3UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                ObjectIds = reader.ObjectIds;
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.ObjectIds.Init(ObjectIds);
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public IReadOnlyList<string> ObjectIds
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
                public IReadOnlyList<string> ObjectIds => ctx.ReadList(0).CastText2();
                public bool HasObjectIds => ctx.IsStructFieldNonNull(0);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 1);
                }

                public ListOfTextSerializer ObjectIds
                {
                    get => BuildPointer<ListOfTextSerializer>(0);
                    set => Link(0, value);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xa092f60656bb0db4UL)]
        public class Result_RemoveObjects : ICapnpSerializable
        {
            public const UInt64 typeId = 0xa092f60656bb0db4UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                RemovedObjects = reader.RemovedObjects;
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.RemovedObjects.Init(RemovedObjects);
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public IReadOnlyList<Mas.Schema.Common.IIdentifiable> RemovedObjects
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
                public IReadOnlyList<Mas.Schema.Common.IIdentifiable> RemovedObjects => ctx.ReadCapList<Mas.Schema.Common.IIdentifiable>(0);
                public bool HasRemovedObjects => ctx.IsStructFieldNonNull(0);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 1);
                }

                public ListOfCapsSerializer<Mas.Schema.Common.IIdentifiable> RemovedObjects
                {
                    get => BuildPointer<ListOfCapsSerializer<Mas.Schema.Common.IIdentifiable>>(0);
                    set => Link(0, value);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xee2cf8cf148921b5UL)]
        public class Params_Registry : ICapnpSerializable
        {
            public const UInt64 typeId = 0xee2cf8cf148921b5UL;
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

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xfe62caefab7dfdadUL)]
        public class Result_Registry : ICapnpSerializable
        {
            public const UInt64 typeId = 0xfe62caefab7dfdadUL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                Registry = reader.Registry;
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.Registry = Registry;
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public Mas.Schema.Registry.IRegistry Registry
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
                public Mas.Schema.Registry.IRegistry Registry => ctx.ReadCap<Mas.Schema.Registry.IRegistry>(0);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 1);
                }

                public Mas.Schema.Registry.IRegistry Registry
                {
                    get => ReadCap<Mas.Schema.Registry.IRegistry>(0);
                    set => LinkObject(0, value);
                }
            }
        }
    }

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xca7b4bd1600633b8UL), Proxy(typeof(Registry_Proxy)), Skeleton(typeof(Registry_Skeleton))]
    public interface IRegistry : Mas.Schema.Common.IIdentifiable
    {
        Task<IReadOnlyList<Mas.Schema.Common.IdInformation>> SupportedCategories(CancellationToken cancellationToken_ = default);
        Task<Mas.Schema.Common.IdInformation> CategoryInfo(string categoryId, CancellationToken cancellationToken_ = default);
        Task<IReadOnlyList<Mas.Schema.Registry.Registry.Entry>> Entries(string categoryId, CancellationToken cancellationToken_ = default);
    }

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xca7b4bd1600633b8UL)]
    public class Registry_Proxy : Proxy, IRegistry
    {
        public async Task<IReadOnlyList<Mas.Schema.Common.IdInformation>> SupportedCategories(CancellationToken cancellationToken_ = default)
        {
            var in_ = SerializerState.CreateForRpc<Mas.Schema.Registry.Registry.Params_SupportedCategories.WRITER>();
            var arg_ = new Mas.Schema.Registry.Registry.Params_SupportedCategories()
            {};
            arg_?.serialize(in_);
            using (var d_ = await Call(14590338780428121016UL, 0, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_).WhenReturned)
            {
                var r_ = CapnpSerializable.Create<Mas.Schema.Registry.Registry.Result_SupportedCategories>(d_);
                return (r_.Cats);
            }
        }

        public async Task<Mas.Schema.Common.IdInformation> CategoryInfo(string categoryId, CancellationToken cancellationToken_ = default)
        {
            var in_ = SerializerState.CreateForRpc<Mas.Schema.Registry.Registry.Params_CategoryInfo.WRITER>();
            var arg_ = new Mas.Schema.Registry.Registry.Params_CategoryInfo()
            {CategoryId = categoryId};
            arg_?.serialize(in_);
            using (var d_ = await Call(14590338780428121016UL, 1, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_).WhenReturned)
            {
                var r_ = CapnpSerializable.Create<Mas.Schema.Common.IdInformation>(d_);
                return r_;
            }
        }

        public Task<IReadOnlyList<Mas.Schema.Registry.Registry.Entry>> Entries(string categoryId, CancellationToken cancellationToken_ = default)
        {
            var in_ = SerializerState.CreateForRpc<Mas.Schema.Registry.Registry.Params_Entries.WRITER>();
            var arg_ = new Mas.Schema.Registry.Registry.Params_Entries()
            {CategoryId = categoryId};
            arg_?.serialize(in_);
            return Impatient.MakePipelineAware(Call(14590338780428121016UL, 2, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_), d_ =>
            {
                using (d_)
                {
                    var r_ = CapnpSerializable.Create<Mas.Schema.Registry.Registry.Result_Entries>(d_);
                    return (r_.Entries);
                }
            }

            );
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

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xca7b4bd1600633b8UL)]
    public class Registry_Skeleton : Skeleton<IRegistry>
    {
        public Registry_Skeleton()
        {
            SetMethodTable(SupportedCategories, CategoryInfo, Entries);
        }

        public override ulong InterfaceId => 14590338780428121016UL;
        Task<AnswerOrCounterquestion> SupportedCategories(DeserializerState d_, CancellationToken cancellationToken_)
        {
            using (d_)
            {
                return Impatient.MaybeTailCall(Impl.SupportedCategories(cancellationToken_), cats =>
                {
                    var s_ = SerializerState.CreateForRpc<Mas.Schema.Registry.Registry.Result_SupportedCategories.WRITER>();
                    var r_ = new Mas.Schema.Registry.Registry.Result_SupportedCategories{Cats = cats};
                    r_.serialize(s_);
                    return s_;
                }

                );
            }
        }

        Task<AnswerOrCounterquestion> CategoryInfo(DeserializerState d_, CancellationToken cancellationToken_)
        {
            using (d_)
            {
                var in_ = CapnpSerializable.Create<Mas.Schema.Registry.Registry.Params_CategoryInfo>(d_);
                return Impatient.MaybeTailCall(Impl.CategoryInfo(in_.CategoryId, cancellationToken_), r_ =>
                {
                    var s_ = SerializerState.CreateForRpc<Mas.Schema.Common.IdInformation.WRITER>();
                    r_.serialize(s_);
                    return s_;
                }

                );
            }
        }

        Task<AnswerOrCounterquestion> Entries(DeserializerState d_, CancellationToken cancellationToken_)
        {
            using (d_)
            {
                var in_ = CapnpSerializable.Create<Mas.Schema.Registry.Registry.Params_Entries>(d_);
                return Impatient.MaybeTailCall(Impl.Entries(in_.CategoryId, cancellationToken_), entries =>
                {
                    var s_ = SerializerState.CreateForRpc<Mas.Schema.Registry.Registry.Result_Entries.WRITER>();
                    var r_ = new Mas.Schema.Registry.Registry.Result_Entries{Entries = entries};
                    r_.serialize(s_);
                    return s_;
                }

                );
            }
        }
    }

    public static class Registry
    {
        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xc17987510cf7ac13UL)]
        public class Entry : ICapnpSerializable
        {
            public const UInt64 typeId = 0xc17987510cf7ac13UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                CategoryId = reader.CategoryId;
                Ref = reader.Ref;
                Name = reader.Name;
                Id = reader.Id;
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.CategoryId = CategoryId;
                writer.Ref = Ref;
                writer.Name = Name;
                writer.Id = Id;
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

            public Mas.Schema.Common.IIdentifiable Ref
            {
                get;
                set;
            }

            public string Name
            {
                get;
                set;
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
                public string CategoryId => ctx.ReadText(0, null);
                public Mas.Schema.Common.IIdentifiable Ref => ctx.ReadCap<Mas.Schema.Common.IIdentifiable>(1);
                public string Name => ctx.ReadText(2, null);
                public string Id => ctx.ReadText(3, null);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 4);
                }

                public string CategoryId
                {
                    get => this.ReadText(0, null);
                    set => this.WriteText(0, value, null);
                }

                public Mas.Schema.Common.IIdentifiable Ref
                {
                    get => ReadCap<Mas.Schema.Common.IIdentifiable>(1);
                    set => LinkObject(1, value);
                }

                public string Name
                {
                    get => this.ReadText(2, null);
                    set => this.WriteText(2, value, null);
                }

                public string Id
                {
                    get => this.ReadText(3, null);
                    set => this.WriteText(3, value, null);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0x9c49e6e65e34c29bUL)]
        public class Params_SupportedCategories : ICapnpSerializable
        {
            public const UInt64 typeId = 0x9c49e6e65e34c29bUL;
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

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xb2bf60b5817330b0UL)]
        public class Result_SupportedCategories : ICapnpSerializable
        {
            public const UInt64 typeId = 0xb2bf60b5817330b0UL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                Cats = reader.Cats?.ToReadOnlyList(_ => CapnpSerializable.Create<Mas.Schema.Common.IdInformation>(_));
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.Cats.Init(Cats, (_s1, _v1) => _v1?.serialize(_s1));
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public IReadOnlyList<Mas.Schema.Common.IdInformation> Cats
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
                public IReadOnlyList<Mas.Schema.Common.IdInformation.READER> Cats => ctx.ReadList(0).Cast(Mas.Schema.Common.IdInformation.READER.create);
                public bool HasCats => ctx.IsStructFieldNonNull(0);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 1);
                }

                public ListOfStructsSerializer<Mas.Schema.Common.IdInformation.WRITER> Cats
                {
                    get => BuildPointer<ListOfStructsSerializer<Mas.Schema.Common.IdInformation.WRITER>>(0);
                    set => Link(0, value);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0x891283e1b248bc9dUL)]
        public class Params_CategoryInfo : ICapnpSerializable
        {
            public const UInt64 typeId = 0x891283e1b248bc9dUL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                CategoryId = reader.CategoryId;
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.CategoryId = CategoryId;
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
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 1);
                }

                public string CategoryId
                {
                    get => this.ReadText(0, null);
                    set => this.WriteText(0, value, null);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0x9ffc53716151c5faUL)]
        public class Params_Entries : ICapnpSerializable
        {
            public const UInt64 typeId = 0x9ffc53716151c5faUL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                CategoryId = reader.CategoryId;
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.CategoryId = CategoryId;
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
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 1);
                }

                public string CategoryId
                {
                    get => this.ReadText(0, null);
                    set => this.WriteText(0, value, null);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xe4eaf56eb486064dUL)]
        public class Result_Entries : ICapnpSerializable
        {
            public const UInt64 typeId = 0xe4eaf56eb486064dUL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                Entries = reader.Entries?.ToReadOnlyList(_ => CapnpSerializable.Create<Mas.Schema.Registry.Registry.Entry>(_));
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

            public IReadOnlyList<Mas.Schema.Registry.Registry.Entry> Entries
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
                public IReadOnlyList<Mas.Schema.Registry.Registry.Entry.READER> Entries => ctx.ReadList(0).Cast(Mas.Schema.Registry.Registry.Entry.READER.create);
                public bool HasEntries => ctx.IsStructFieldNonNull(0);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 1);
                }

                public ListOfStructsSerializer<Mas.Schema.Registry.Registry.Entry.WRITER> Entries
                {
                    get => BuildPointer<ListOfStructsSerializer<Mas.Schema.Registry.Registry.Entry.WRITER>>(0);
                    set => Link(0, value);
                }
            }
        }
    }

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xabaef93c36f2d1eaUL), Proxy(typeof(Registrar_Proxy)), Skeleton(typeof(Registrar_Skeleton))]
    public interface IRegistrar : Mas.Schema.Common.IIdentifiable
    {
        Task<(Mas.Schema.Registry.Registrar.IUnregister, Mas.Schema.Persistence.SturdyRef)> Register(Mas.Schema.Registry.Registrar.RegParams arg_, CancellationToken cancellationToken_ = default);
    }

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xabaef93c36f2d1eaUL)]
    public class Registrar_Proxy : Proxy, IRegistrar
    {
        public Task<(Mas.Schema.Registry.Registrar.IUnregister, Mas.Schema.Persistence.SturdyRef)> Register(Mas.Schema.Registry.Registrar.RegParams arg_, CancellationToken cancellationToken_ = default)
        {
            var in_ = SerializerState.CreateForRpc<Mas.Schema.Registry.Registrar.RegParams.WRITER>();
            arg_?.serialize(in_);
            return Impatient.MakePipelineAware(Call(12371099263448568298UL, 0, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_), d_ =>
            {
                using (d_)
                {
                    var r_ = CapnpSerializable.Create<Mas.Schema.Registry.Registrar.Result_Register>(d_);
                    return (r_.Unreg, r_.ReregSR);
                }
            }

            );
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

    [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xabaef93c36f2d1eaUL)]
    public class Registrar_Skeleton : Skeleton<IRegistrar>
    {
        public Registrar_Skeleton()
        {
            SetMethodTable(Register);
        }

        public override ulong InterfaceId => 12371099263448568298UL;
        Task<AnswerOrCounterquestion> Register(DeserializerState d_, CancellationToken cancellationToken_)
        {
            using (d_)
            {
                return Impatient.MaybeTailCall(Impl.Register(CapnpSerializable.Create<Mas.Schema.Registry.Registrar.RegParams>(d_), cancellationToken_), (unreg, reregSR) =>
                {
                    var s_ = SerializerState.CreateForRpc<Mas.Schema.Registry.Registrar.Result_Register.WRITER>();
                    var r_ = new Mas.Schema.Registry.Registrar.Result_Register{Unreg = unreg, ReregSR = reregSR};
                    r_.serialize(s_);
                    return s_;
                }

                );
            }
        }
    }

    public static class Registrar
    {
        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xaa1198dd7e71b20eUL)]
        public class CrossDomainRestore : ICapnpSerializable
        {
            public const UInt64 typeId = 0xaa1198dd7e71b20eUL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                VatId = CapnpSerializable.Create<Mas.Schema.Persistence.VatId>(reader.VatId);
                Restorer = reader.Restorer;
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                VatId?.serialize(writer.VatId);
                writer.Restorer = Restorer;
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public Mas.Schema.Persistence.VatId VatId
            {
                get;
                set;
            }

            public Mas.Schema.Persistence.IRestorer Restorer
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
                public Mas.Schema.Persistence.VatId.READER VatId => ctx.ReadStruct(0, Mas.Schema.Persistence.VatId.READER.create);
                public bool HasVatId => ctx.IsStructFieldNonNull(0);
                public Mas.Schema.Persistence.IRestorer Restorer => ctx.ReadCap<Mas.Schema.Persistence.IRestorer>(1);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 2);
                }

                public Mas.Schema.Persistence.VatId.WRITER VatId
                {
                    get => BuildPointer<Mas.Schema.Persistence.VatId.WRITER>(0);
                    set => Link(0, value);
                }

                public Mas.Schema.Persistence.IRestorer Restorer
                {
                    get => ReadCap<Mas.Schema.Persistence.IRestorer>(1);
                    set => LinkObject(1, value);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xe5a84717ea75fb0dUL)]
        public class RegParams : ICapnpSerializable
        {
            public const UInt64 typeId = 0xe5a84717ea75fb0dUL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                Cap = reader.Cap;
                RegName = reader.RegName;
                CategoryId = reader.CategoryId;
                XDomain = CapnpSerializable.Create<Mas.Schema.Registry.Registrar.CrossDomainRestore>(reader.XDomain);
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.Cap = Cap;
                writer.RegName = RegName;
                writer.CategoryId = CategoryId;
                XDomain?.serialize(writer.XDomain);
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public Mas.Schema.Common.IIdentifiable Cap
            {
                get;
                set;
            }

            public string RegName
            {
                get;
                set;
            }

            public string CategoryId
            {
                get;
                set;
            }

            public Mas.Schema.Registry.Registrar.CrossDomainRestore XDomain
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
                public Mas.Schema.Common.IIdentifiable Cap => ctx.ReadCap<Mas.Schema.Common.IIdentifiable>(0);
                public string RegName => ctx.ReadText(1, null);
                public string CategoryId => ctx.ReadText(2, null);
                public Mas.Schema.Registry.Registrar.CrossDomainRestore.READER XDomain => ctx.ReadStruct(3, Mas.Schema.Registry.Registrar.CrossDomainRestore.READER.create);
                public bool HasXDomain => ctx.IsStructFieldNonNull(3);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 4);
                }

                public Mas.Schema.Common.IIdentifiable Cap
                {
                    get => ReadCap<Mas.Schema.Common.IIdentifiable>(0);
                    set => LinkObject(0, value);
                }

                public string RegName
                {
                    get => this.ReadText(1, null);
                    set => this.WriteText(1, value, null);
                }

                public string CategoryId
                {
                    get => this.ReadText(2, null);
                    set => this.WriteText(2, value, null);
                }

                public Mas.Schema.Registry.Registrar.CrossDomainRestore.WRITER XDomain
                {
                    get => BuildPointer<Mas.Schema.Registry.Registrar.CrossDomainRestore.WRITER>(3);
                    set => Link(3, value);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xc7597e4462528489UL), Proxy(typeof(Unregister_Proxy)), Skeleton(typeof(Unregister_Skeleton))]
        public interface IUnregister : IDisposable
        {
            Task<bool> Unregister(CancellationToken cancellationToken_ = default);
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xc7597e4462528489UL)]
        public class Unregister_Proxy : Proxy, IUnregister
        {
            public async Task<bool> Unregister(CancellationToken cancellationToken_ = default)
            {
                var in_ = SerializerState.CreateForRpc<Mas.Schema.Registry.Registrar.Unregister.Params_Unregister.WRITER>();
                var arg_ = new Mas.Schema.Registry.Registrar.Unregister.Params_Unregister()
                {};
                arg_?.serialize(in_);
                using (var d_ = await Call(14364651318647358601UL, 0, in_.Rewrap<DynamicSerializerState>(), false, cancellationToken_).WhenReturned)
                {
                    var r_ = CapnpSerializable.Create<Mas.Schema.Registry.Registrar.Unregister.Result_Unregister>(d_);
                    return (r_.Success);
                }
            }
        }

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xc7597e4462528489UL)]
        public class Unregister_Skeleton : Skeleton<IUnregister>
        {
            public Unregister_Skeleton()
            {
                SetMethodTable(Unregister);
            }

            public override ulong InterfaceId => 14364651318647358601UL;
            Task<AnswerOrCounterquestion> Unregister(DeserializerState d_, CancellationToken cancellationToken_)
            {
                using (d_)
                {
                    return Impatient.MaybeTailCall(Impl.Unregister(cancellationToken_), success =>
                    {
                        var s_ = SerializerState.CreateForRpc<Mas.Schema.Registry.Registrar.Unregister.Result_Unregister.WRITER>();
                        var r_ = new Mas.Schema.Registry.Registrar.Unregister.Result_Unregister{Success = success};
                        r_.serialize(s_);
                        return s_;
                    }

                    );
                }
            }
        }

        public static class Unregister
        {
            [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xd023a1df5e372a7eUL)]
            public class Params_Unregister : ICapnpSerializable
            {
                public const UInt64 typeId = 0xd023a1df5e372a7eUL;
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

            [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xa19166b9981b0854UL)]
            public class Result_Unregister : ICapnpSerializable
            {
                public const UInt64 typeId = 0xa19166b9981b0854UL;
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

        [System.CodeDom.Compiler.GeneratedCode("capnpc-csharp", "1.3.0.0"), TypeId(0xb2a9b080f0c4013cUL)]
        public class Result_Register : ICapnpSerializable
        {
            public const UInt64 typeId = 0xb2a9b080f0c4013cUL;
            void ICapnpSerializable.Deserialize(DeserializerState arg_)
            {
                var reader = READER.create(arg_);
                Unreg = reader.Unreg;
                ReregSR = CapnpSerializable.Create<Mas.Schema.Persistence.SturdyRef>(reader.ReregSR);
                applyDefaults();
            }

            public void serialize(WRITER writer)
            {
                writer.Unreg = Unreg;
                ReregSR?.serialize(writer.ReregSR);
            }

            void ICapnpSerializable.Serialize(SerializerState arg_)
            {
                serialize(arg_.Rewrap<WRITER>());
            }

            public void applyDefaults()
            {
            }

            public Mas.Schema.Registry.Registrar.IUnregister Unreg
            {
                get;
                set;
            }

            public Mas.Schema.Persistence.SturdyRef ReregSR
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
                public Mas.Schema.Registry.Registrar.IUnregister Unreg => ctx.ReadCap<Mas.Schema.Registry.Registrar.IUnregister>(0);
                public Mas.Schema.Persistence.SturdyRef.READER ReregSR => ctx.ReadStruct(1, Mas.Schema.Persistence.SturdyRef.READER.create);
                public bool HasReregSR => ctx.IsStructFieldNonNull(1);
            }

            public class WRITER : SerializerState
            {
                public WRITER()
                {
                    this.SetStruct(0, 2);
                }

                public Mas.Schema.Registry.Registrar.IUnregister Unreg
                {
                    get => ReadCap<Mas.Schema.Registry.Registrar.IUnregister>(0);
                    set => LinkObject(0, value);
                }

                public Mas.Schema.Persistence.SturdyRef.WRITER ReregSR
                {
                    get => BuildPointer<Mas.Schema.Persistence.SturdyRef.WRITER>(1);
                    set => Link(1, value);
                }
            }
        }
    }
}