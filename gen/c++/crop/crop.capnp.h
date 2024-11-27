// Generated by Cap'n Proto compiler, DO NOT EDIT
// source: crop.capnp

#pragma once

#include <capnp/generated-header-support.h>
#include <kj/windows-sanity.h>
#if !CAPNP_LITE
#include <capnp/capability.h>
#endif  // !CAPNP_LITE

#ifndef CAPNP_VERSION
#error "CAPNP_VERSION is not defined, is capnp/generated-header-support.h missing?"
#elif CAPNP_VERSION != 1000002
#error "Version mismatch between generated code and library headers.  You must use the same version of the Cap'n Proto compiler and library."
#endif

#include "common.capnp.h"
#include "persistence.capnp.h"
#include "registry.capnp.h"

CAPNP_BEGIN_HEADER

namespace capnp {
namespace schemas {

CAPNP_DECLARE_SCHEMA(e88d97a324bf5c84);
CAPNP_DECLARE_SCHEMA(c86e010e743c8e5b);
CAPNP_DECLARE_SCHEMA(e4fafc722d515486);
CAPNP_DECLARE_SCHEMA(f26ef117dfb4517a);
CAPNP_DECLARE_SCHEMA(bf3704bba52494ba);
CAPNP_DECLARE_SCHEMA(f4dd1c322a3130b4);
CAPNP_DECLARE_SCHEMA(b4aa895eeede6448);
CAPNP_DECLARE_SCHEMA(8ddcc2b6c0386bc4);

}  // namespace schemas
}  // namespace capnp

namespace mas {
namespace schema {
namespace crop {

struct Crop {
  Crop() = delete;

#if !CAPNP_LITE
  class Client;
  class Server;
#endif  // !CAPNP_LITE

  struct ParametersParams;
  struct ParametersResults;
  struct CultivarParams;
  struct CultivarResults;
  struct SpeciesParams;
  struct SpeciesResults;

  #if !CAPNP_LITE
  struct _capnpPrivate {
    CAPNP_DECLARE_INTERFACE_HEADER(e88d97a324bf5c84)
    static constexpr ::capnp::_::RawBrandedSchema const* brand() { return &schema->defaultBrand; }
  };
  #endif  // !CAPNP_LITE
};

struct Crop::ParametersParams {
  ParametersParams() = delete;

  class Reader;
  class Builder;
  class Pipeline;

  struct _capnpPrivate {
    CAPNP_DECLARE_STRUCT_HEADER(c86e010e743c8e5b, 0, 0)
    #if !CAPNP_LITE
    static constexpr ::capnp::_::RawBrandedSchema const* brand() { return &schema->defaultBrand; }
    #endif  // !CAPNP_LITE
  };
};

struct Crop::ParametersResults {
  ParametersResults() = delete;

  class Reader;
  class Builder;
  class Pipeline;

  struct _capnpPrivate {
    CAPNP_DECLARE_STRUCT_HEADER(e4fafc722d515486, 0, 1)
    #if !CAPNP_LITE
    static constexpr ::capnp::_::RawBrandedSchema const* brand() { return &schema->defaultBrand; }
    #endif  // !CAPNP_LITE
  };
};

struct Crop::CultivarParams {
  CultivarParams() = delete;

  class Reader;
  class Builder;
  class Pipeline;

  struct _capnpPrivate {
    CAPNP_DECLARE_STRUCT_HEADER(f26ef117dfb4517a, 0, 0)
    #if !CAPNP_LITE
    static constexpr ::capnp::_::RawBrandedSchema const* brand() { return &schema->defaultBrand; }
    #endif  // !CAPNP_LITE
  };
};

struct Crop::CultivarResults {
  CultivarResults() = delete;

  class Reader;
  class Builder;
  class Pipeline;

  struct _capnpPrivate {
    CAPNP_DECLARE_STRUCT_HEADER(bf3704bba52494ba, 0, 1)
    #if !CAPNP_LITE
    static constexpr ::capnp::_::RawBrandedSchema const* brand() { return &schema->defaultBrand; }
    #endif  // !CAPNP_LITE
  };
};

struct Crop::SpeciesParams {
  SpeciesParams() = delete;

  class Reader;
  class Builder;
  class Pipeline;

  struct _capnpPrivate {
    CAPNP_DECLARE_STRUCT_HEADER(f4dd1c322a3130b4, 0, 0)
    #if !CAPNP_LITE
    static constexpr ::capnp::_::RawBrandedSchema const* brand() { return &schema->defaultBrand; }
    #endif  // !CAPNP_LITE
  };
};

struct Crop::SpeciesResults {
  SpeciesResults() = delete;

  class Reader;
  class Builder;
  class Pipeline;

  struct _capnpPrivate {
    CAPNP_DECLARE_STRUCT_HEADER(b4aa895eeede6448, 0, 1)
    #if !CAPNP_LITE
    static constexpr ::capnp::_::RawBrandedSchema const* brand() { return &schema->defaultBrand; }
    #endif  // !CAPNP_LITE
  };
};

struct Service {
  Service() = delete;

#if !CAPNP_LITE
  class Client;
  class Server;
#endif  // !CAPNP_LITE


  #if !CAPNP_LITE
  struct _capnpPrivate {
    CAPNP_DECLARE_INTERFACE_HEADER(8ddcc2b6c0386bc4)
    static constexpr ::capnp::_::RawBrandedSchema const* brand() { return &schema->defaultBrand; }
  };
  #endif  // !CAPNP_LITE
};

// =======================================================================================

#if !CAPNP_LITE
class Crop::Client
    : public virtual ::capnp::Capability::Client,
      public virtual  ::mas::schema::common::Identifiable::Client,
      public virtual  ::mas::schema::persistence::Persistent::Client {
public:
  typedef Crop Calls;
  typedef Crop Reads;

  Client(decltype(nullptr));
  explicit Client(::kj::Own< ::capnp::ClientHook>&& hook);
  template <typename _t, typename = ::kj::EnableIf< ::kj::canConvert<_t*, Server*>()>>
  Client(::kj::Own<_t>&& server);
  template <typename _t, typename = ::kj::EnableIf< ::kj::canConvert<_t*, Client*>()>>
  Client(::kj::Promise<_t>&& promise);
  Client(::kj::Exception&& exception);
  Client(Client&) = default;
  Client(Client&&) = default;
  Client& operator=(Client& other);
  Client& operator=(Client&& other);

  ::capnp::Request< ::mas::schema::crop::Crop::ParametersParams,  ::mas::schema::crop::Crop::ParametersResults> parametersRequest(
      ::kj::Maybe< ::capnp::MessageSize> sizeHint = nullptr);
  ::capnp::Request< ::mas::schema::crop::Crop::CultivarParams,  ::mas::schema::crop::Crop::CultivarResults> cultivarRequest(
      ::kj::Maybe< ::capnp::MessageSize> sizeHint = nullptr);
  ::capnp::Request< ::mas::schema::crop::Crop::SpeciesParams,  ::mas::schema::crop::Crop::SpeciesResults> speciesRequest(
      ::kj::Maybe< ::capnp::MessageSize> sizeHint = nullptr);

protected:
  Client() = default;
};

class Crop::Server
    : public virtual ::capnp::Capability::Server,
      public virtual  ::mas::schema::common::Identifiable::Server,
      public virtual  ::mas::schema::persistence::Persistent::Server {
public:
  typedef Crop Serves;

  ::capnp::Capability::Server::DispatchCallResult dispatchCall(
      uint64_t interfaceId, uint16_t methodId,
      ::capnp::CallContext< ::capnp::AnyPointer, ::capnp::AnyPointer> context)
      override;

protected:
  typedef  ::mas::schema::crop::Crop::ParametersParams ParametersParams;
  typedef  ::mas::schema::crop::Crop::ParametersResults ParametersResults;
  typedef ::capnp::CallContext<ParametersParams, ParametersResults> ParametersContext;
  virtual ::kj::Promise<void> parameters(ParametersContext context);
  typedef  ::mas::schema::crop::Crop::CultivarParams CultivarParams;
  typedef  ::mas::schema::crop::Crop::CultivarResults CultivarResults;
  typedef ::capnp::CallContext<CultivarParams, CultivarResults> CultivarContext;
  virtual ::kj::Promise<void> cultivar(CultivarContext context);
  typedef  ::mas::schema::crop::Crop::SpeciesParams SpeciesParams;
  typedef  ::mas::schema::crop::Crop::SpeciesResults SpeciesResults;
  typedef ::capnp::CallContext<SpeciesParams, SpeciesResults> SpeciesContext;
  virtual ::kj::Promise<void> species(SpeciesContext context);

  inline  ::mas::schema::crop::Crop::Client thisCap() {
    return ::capnp::Capability::Server::thisCap()
        .template castAs< ::mas::schema::crop::Crop>();
  }

  ::capnp::Capability::Server::DispatchCallResult dispatchCallInternal(
      uint16_t methodId,
      ::capnp::CallContext< ::capnp::AnyPointer, ::capnp::AnyPointer> context);
};
#endif  // !CAPNP_LITE

class Crop::ParametersParams::Reader {
public:
  typedef ParametersParams Reads;

  Reader() = default;
  inline explicit Reader(::capnp::_::StructReader base): _reader(base) {}

  inline ::capnp::MessageSize totalSize() const {
    return _reader.totalSize().asPublic();
  }

#if !CAPNP_LITE
  inline ::kj::StringTree toString() const {
    return ::capnp::_::structString(_reader, *_capnpPrivate::brand());
  }
#endif  // !CAPNP_LITE

private:
  ::capnp::_::StructReader _reader;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::ToDynamic_;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::_::PointerHelpers;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::List;
  friend class ::capnp::MessageBuilder;
  friend class ::capnp::Orphanage;
};

class Crop::ParametersParams::Builder {
public:
  typedef ParametersParams Builds;

  Builder() = delete;  // Deleted to discourage incorrect usage.
                       // You can explicitly initialize to nullptr instead.
  inline Builder(decltype(nullptr)) {}
  inline explicit Builder(::capnp::_::StructBuilder base): _builder(base) {}
  inline operator Reader() const { return Reader(_builder.asReader()); }
  inline Reader asReader() const { return *this; }

  inline ::capnp::MessageSize totalSize() const { return asReader().totalSize(); }
#if !CAPNP_LITE
  inline ::kj::StringTree toString() const { return asReader().toString(); }
#endif  // !CAPNP_LITE

private:
  ::capnp::_::StructBuilder _builder;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::ToDynamic_;
  friend class ::capnp::Orphanage;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::_::PointerHelpers;
};

#if !CAPNP_LITE
class Crop::ParametersParams::Pipeline {
public:
  typedef ParametersParams Pipelines;

  inline Pipeline(decltype(nullptr)): _typeless(nullptr) {}
  inline explicit Pipeline(::capnp::AnyPointer::Pipeline&& typeless)
      : _typeless(kj::mv(typeless)) {}

private:
  ::capnp::AnyPointer::Pipeline _typeless;
  friend class ::capnp::PipelineHook;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::ToDynamic_;
};
#endif  // !CAPNP_LITE

class Crop::ParametersResults::Reader {
public:
  typedef ParametersResults Reads;

  Reader() = default;
  inline explicit Reader(::capnp::_::StructReader base): _reader(base) {}

  inline ::capnp::MessageSize totalSize() const {
    return _reader.totalSize().asPublic();
  }

#if !CAPNP_LITE
  inline ::kj::StringTree toString() const {
    return ::capnp::_::structString(_reader, *_capnpPrivate::brand());
  }
#endif  // !CAPNP_LITE

  inline bool hasParams() const;
  inline ::capnp::AnyPointer::Reader getParams() const;

private:
  ::capnp::_::StructReader _reader;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::ToDynamic_;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::_::PointerHelpers;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::List;
  friend class ::capnp::MessageBuilder;
  friend class ::capnp::Orphanage;
};

class Crop::ParametersResults::Builder {
public:
  typedef ParametersResults Builds;

  Builder() = delete;  // Deleted to discourage incorrect usage.
                       // You can explicitly initialize to nullptr instead.
  inline Builder(decltype(nullptr)) {}
  inline explicit Builder(::capnp::_::StructBuilder base): _builder(base) {}
  inline operator Reader() const { return Reader(_builder.asReader()); }
  inline Reader asReader() const { return *this; }

  inline ::capnp::MessageSize totalSize() const { return asReader().totalSize(); }
#if !CAPNP_LITE
  inline ::kj::StringTree toString() const { return asReader().toString(); }
#endif  // !CAPNP_LITE

  inline bool hasParams();
  inline ::capnp::AnyPointer::Builder getParams();
  inline ::capnp::AnyPointer::Builder initParams();

private:
  ::capnp::_::StructBuilder _builder;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::ToDynamic_;
  friend class ::capnp::Orphanage;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::_::PointerHelpers;
};

#if !CAPNP_LITE
class Crop::ParametersResults::Pipeline {
public:
  typedef ParametersResults Pipelines;

  inline Pipeline(decltype(nullptr)): _typeless(nullptr) {}
  inline explicit Pipeline(::capnp::AnyPointer::Pipeline&& typeless)
      : _typeless(kj::mv(typeless)) {}

private:
  ::capnp::AnyPointer::Pipeline _typeless;
  friend class ::capnp::PipelineHook;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::ToDynamic_;
};
#endif  // !CAPNP_LITE

class Crop::CultivarParams::Reader {
public:
  typedef CultivarParams Reads;

  Reader() = default;
  inline explicit Reader(::capnp::_::StructReader base): _reader(base) {}

  inline ::capnp::MessageSize totalSize() const {
    return _reader.totalSize().asPublic();
  }

#if !CAPNP_LITE
  inline ::kj::StringTree toString() const {
    return ::capnp::_::structString(_reader, *_capnpPrivate::brand());
  }
#endif  // !CAPNP_LITE

private:
  ::capnp::_::StructReader _reader;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::ToDynamic_;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::_::PointerHelpers;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::List;
  friend class ::capnp::MessageBuilder;
  friend class ::capnp::Orphanage;
};

class Crop::CultivarParams::Builder {
public:
  typedef CultivarParams Builds;

  Builder() = delete;  // Deleted to discourage incorrect usage.
                       // You can explicitly initialize to nullptr instead.
  inline Builder(decltype(nullptr)) {}
  inline explicit Builder(::capnp::_::StructBuilder base): _builder(base) {}
  inline operator Reader() const { return Reader(_builder.asReader()); }
  inline Reader asReader() const { return *this; }

  inline ::capnp::MessageSize totalSize() const { return asReader().totalSize(); }
#if !CAPNP_LITE
  inline ::kj::StringTree toString() const { return asReader().toString(); }
#endif  // !CAPNP_LITE

private:
  ::capnp::_::StructBuilder _builder;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::ToDynamic_;
  friend class ::capnp::Orphanage;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::_::PointerHelpers;
};

#if !CAPNP_LITE
class Crop::CultivarParams::Pipeline {
public:
  typedef CultivarParams Pipelines;

  inline Pipeline(decltype(nullptr)): _typeless(nullptr) {}
  inline explicit Pipeline(::capnp::AnyPointer::Pipeline&& typeless)
      : _typeless(kj::mv(typeless)) {}

private:
  ::capnp::AnyPointer::Pipeline _typeless;
  friend class ::capnp::PipelineHook;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::ToDynamic_;
};
#endif  // !CAPNP_LITE

class Crop::CultivarResults::Reader {
public:
  typedef CultivarResults Reads;

  Reader() = default;
  inline explicit Reader(::capnp::_::StructReader base): _reader(base) {}

  inline ::capnp::MessageSize totalSize() const {
    return _reader.totalSize().asPublic();
  }

#if !CAPNP_LITE
  inline ::kj::StringTree toString() const {
    return ::capnp::_::structString(_reader, *_capnpPrivate::brand());
  }
#endif  // !CAPNP_LITE

  inline bool hasInfo() const;
  inline  ::mas::schema::common::IdInformation::Reader getInfo() const;

private:
  ::capnp::_::StructReader _reader;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::ToDynamic_;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::_::PointerHelpers;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::List;
  friend class ::capnp::MessageBuilder;
  friend class ::capnp::Orphanage;
};

class Crop::CultivarResults::Builder {
public:
  typedef CultivarResults Builds;

  Builder() = delete;  // Deleted to discourage incorrect usage.
                       // You can explicitly initialize to nullptr instead.
  inline Builder(decltype(nullptr)) {}
  inline explicit Builder(::capnp::_::StructBuilder base): _builder(base) {}
  inline operator Reader() const { return Reader(_builder.asReader()); }
  inline Reader asReader() const { return *this; }

  inline ::capnp::MessageSize totalSize() const { return asReader().totalSize(); }
#if !CAPNP_LITE
  inline ::kj::StringTree toString() const { return asReader().toString(); }
#endif  // !CAPNP_LITE

  inline bool hasInfo();
  inline  ::mas::schema::common::IdInformation::Builder getInfo();
  inline void setInfo( ::mas::schema::common::IdInformation::Reader value);
  inline  ::mas::schema::common::IdInformation::Builder initInfo();
  inline void adoptInfo(::capnp::Orphan< ::mas::schema::common::IdInformation>&& value);
  inline ::capnp::Orphan< ::mas::schema::common::IdInformation> disownInfo();

private:
  ::capnp::_::StructBuilder _builder;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::ToDynamic_;
  friend class ::capnp::Orphanage;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::_::PointerHelpers;
};

#if !CAPNP_LITE
class Crop::CultivarResults::Pipeline {
public:
  typedef CultivarResults Pipelines;

  inline Pipeline(decltype(nullptr)): _typeless(nullptr) {}
  inline explicit Pipeline(::capnp::AnyPointer::Pipeline&& typeless)
      : _typeless(kj::mv(typeless)) {}

  inline  ::mas::schema::common::IdInformation::Pipeline getInfo();
private:
  ::capnp::AnyPointer::Pipeline _typeless;
  friend class ::capnp::PipelineHook;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::ToDynamic_;
};
#endif  // !CAPNP_LITE

class Crop::SpeciesParams::Reader {
public:
  typedef SpeciesParams Reads;

  Reader() = default;
  inline explicit Reader(::capnp::_::StructReader base): _reader(base) {}

  inline ::capnp::MessageSize totalSize() const {
    return _reader.totalSize().asPublic();
  }

#if !CAPNP_LITE
  inline ::kj::StringTree toString() const {
    return ::capnp::_::structString(_reader, *_capnpPrivate::brand());
  }
#endif  // !CAPNP_LITE

private:
  ::capnp::_::StructReader _reader;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::ToDynamic_;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::_::PointerHelpers;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::List;
  friend class ::capnp::MessageBuilder;
  friend class ::capnp::Orphanage;
};

class Crop::SpeciesParams::Builder {
public:
  typedef SpeciesParams Builds;

  Builder() = delete;  // Deleted to discourage incorrect usage.
                       // You can explicitly initialize to nullptr instead.
  inline Builder(decltype(nullptr)) {}
  inline explicit Builder(::capnp::_::StructBuilder base): _builder(base) {}
  inline operator Reader() const { return Reader(_builder.asReader()); }
  inline Reader asReader() const { return *this; }

  inline ::capnp::MessageSize totalSize() const { return asReader().totalSize(); }
#if !CAPNP_LITE
  inline ::kj::StringTree toString() const { return asReader().toString(); }
#endif  // !CAPNP_LITE

private:
  ::capnp::_::StructBuilder _builder;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::ToDynamic_;
  friend class ::capnp::Orphanage;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::_::PointerHelpers;
};

#if !CAPNP_LITE
class Crop::SpeciesParams::Pipeline {
public:
  typedef SpeciesParams Pipelines;

  inline Pipeline(decltype(nullptr)): _typeless(nullptr) {}
  inline explicit Pipeline(::capnp::AnyPointer::Pipeline&& typeless)
      : _typeless(kj::mv(typeless)) {}

private:
  ::capnp::AnyPointer::Pipeline _typeless;
  friend class ::capnp::PipelineHook;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::ToDynamic_;
};
#endif  // !CAPNP_LITE

class Crop::SpeciesResults::Reader {
public:
  typedef SpeciesResults Reads;

  Reader() = default;
  inline explicit Reader(::capnp::_::StructReader base): _reader(base) {}

  inline ::capnp::MessageSize totalSize() const {
    return _reader.totalSize().asPublic();
  }

#if !CAPNP_LITE
  inline ::kj::StringTree toString() const {
    return ::capnp::_::structString(_reader, *_capnpPrivate::brand());
  }
#endif  // !CAPNP_LITE

  inline bool hasInfo() const;
  inline  ::mas::schema::common::IdInformation::Reader getInfo() const;

private:
  ::capnp::_::StructReader _reader;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::ToDynamic_;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::_::PointerHelpers;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::List;
  friend class ::capnp::MessageBuilder;
  friend class ::capnp::Orphanage;
};

class Crop::SpeciesResults::Builder {
public:
  typedef SpeciesResults Builds;

  Builder() = delete;  // Deleted to discourage incorrect usage.
                       // You can explicitly initialize to nullptr instead.
  inline Builder(decltype(nullptr)) {}
  inline explicit Builder(::capnp::_::StructBuilder base): _builder(base) {}
  inline operator Reader() const { return Reader(_builder.asReader()); }
  inline Reader asReader() const { return *this; }

  inline ::capnp::MessageSize totalSize() const { return asReader().totalSize(); }
#if !CAPNP_LITE
  inline ::kj::StringTree toString() const { return asReader().toString(); }
#endif  // !CAPNP_LITE

  inline bool hasInfo();
  inline  ::mas::schema::common::IdInformation::Builder getInfo();
  inline void setInfo( ::mas::schema::common::IdInformation::Reader value);
  inline  ::mas::schema::common::IdInformation::Builder initInfo();
  inline void adoptInfo(::capnp::Orphan< ::mas::schema::common::IdInformation>&& value);
  inline ::capnp::Orphan< ::mas::schema::common::IdInformation> disownInfo();

private:
  ::capnp::_::StructBuilder _builder;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::ToDynamic_;
  friend class ::capnp::Orphanage;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::_::PointerHelpers;
};

#if !CAPNP_LITE
class Crop::SpeciesResults::Pipeline {
public:
  typedef SpeciesResults Pipelines;

  inline Pipeline(decltype(nullptr)): _typeless(nullptr) {}
  inline explicit Pipeline(::capnp::AnyPointer::Pipeline&& typeless)
      : _typeless(kj::mv(typeless)) {}

  inline  ::mas::schema::common::IdInformation::Pipeline getInfo();
private:
  ::capnp::AnyPointer::Pipeline _typeless;
  friend class ::capnp::PipelineHook;
  template <typename, ::capnp::Kind>
  friend struct ::capnp::ToDynamic_;
};
#endif  // !CAPNP_LITE

#if !CAPNP_LITE
class Service::Client
    : public virtual ::capnp::Capability::Client,
      public virtual  ::mas::schema::registry::Registry::Client {
public:
  typedef Service Calls;
  typedef Service Reads;

  Client(decltype(nullptr));
  explicit Client(::kj::Own< ::capnp::ClientHook>&& hook);
  template <typename _t, typename = ::kj::EnableIf< ::kj::canConvert<_t*, Server*>()>>
  Client(::kj::Own<_t>&& server);
  template <typename _t, typename = ::kj::EnableIf< ::kj::canConvert<_t*, Client*>()>>
  Client(::kj::Promise<_t>&& promise);
  Client(::kj::Exception&& exception);
  Client(Client&) = default;
  Client(Client&&) = default;
  Client& operator=(Client& other);
  Client& operator=(Client&& other);


protected:
  Client() = default;
};

class Service::Server
    : public virtual ::capnp::Capability::Server,
      public virtual  ::mas::schema::registry::Registry::Server {
public:
  typedef Service Serves;

  ::capnp::Capability::Server::DispatchCallResult dispatchCall(
      uint64_t interfaceId, uint16_t methodId,
      ::capnp::CallContext< ::capnp::AnyPointer, ::capnp::AnyPointer> context)
      override;

protected:

  inline  ::mas::schema::crop::Service::Client thisCap() {
    return ::capnp::Capability::Server::thisCap()
        .template castAs< ::mas::schema::crop::Service>();
  }

  ::capnp::Capability::Server::DispatchCallResult dispatchCallInternal(
      uint16_t methodId,
      ::capnp::CallContext< ::capnp::AnyPointer, ::capnp::AnyPointer> context);
};
#endif  // !CAPNP_LITE

// =======================================================================================

#if !CAPNP_LITE
inline Crop::Client::Client(decltype(nullptr))
    : ::capnp::Capability::Client(nullptr) {}
inline Crop::Client::Client(
    ::kj::Own< ::capnp::ClientHook>&& hook)
    : ::capnp::Capability::Client(::kj::mv(hook)) {}
template <typename _t, typename>
inline Crop::Client::Client(::kj::Own<_t>&& server)
    : ::capnp::Capability::Client(::kj::mv(server)) {}
template <typename _t, typename>
inline Crop::Client::Client(::kj::Promise<_t>&& promise)
    : ::capnp::Capability::Client(::kj::mv(promise)) {}
inline Crop::Client::Client(::kj::Exception&& exception)
    : ::capnp::Capability::Client(::kj::mv(exception)) {}
inline  ::mas::schema::crop::Crop::Client& Crop::Client::operator=(Client& other) {
  ::capnp::Capability::Client::operator=(other);
  return *this;
}
inline  ::mas::schema::crop::Crop::Client& Crop::Client::operator=(Client&& other) {
  ::capnp::Capability::Client::operator=(kj::mv(other));
  return *this;
}

#endif  // !CAPNP_LITE
inline bool Crop::ParametersResults::Reader::hasParams() const {
  return !_reader.getPointerField(
      ::capnp::bounded<0>() * ::capnp::POINTERS).isNull();
}
inline bool Crop::ParametersResults::Builder::hasParams() {
  return !_builder.getPointerField(
      ::capnp::bounded<0>() * ::capnp::POINTERS).isNull();
}
inline ::capnp::AnyPointer::Reader Crop::ParametersResults::Reader::getParams() const {
  return ::capnp::AnyPointer::Reader(_reader.getPointerField(
      ::capnp::bounded<0>() * ::capnp::POINTERS));
}
inline ::capnp::AnyPointer::Builder Crop::ParametersResults::Builder::getParams() {
  return ::capnp::AnyPointer::Builder(_builder.getPointerField(
      ::capnp::bounded<0>() * ::capnp::POINTERS));
}
inline ::capnp::AnyPointer::Builder Crop::ParametersResults::Builder::initParams() {
  auto result = ::capnp::AnyPointer::Builder(_builder.getPointerField(
      ::capnp::bounded<0>() * ::capnp::POINTERS));
  result.clear();
  return result;
}

inline bool Crop::CultivarResults::Reader::hasInfo() const {
  return !_reader.getPointerField(
      ::capnp::bounded<0>() * ::capnp::POINTERS).isNull();
}
inline bool Crop::CultivarResults::Builder::hasInfo() {
  return !_builder.getPointerField(
      ::capnp::bounded<0>() * ::capnp::POINTERS).isNull();
}
inline  ::mas::schema::common::IdInformation::Reader Crop::CultivarResults::Reader::getInfo() const {
  return ::capnp::_::PointerHelpers< ::mas::schema::common::IdInformation>::get(_reader.getPointerField(
      ::capnp::bounded<0>() * ::capnp::POINTERS));
}
inline  ::mas::schema::common::IdInformation::Builder Crop::CultivarResults::Builder::getInfo() {
  return ::capnp::_::PointerHelpers< ::mas::schema::common::IdInformation>::get(_builder.getPointerField(
      ::capnp::bounded<0>() * ::capnp::POINTERS));
}
#if !CAPNP_LITE
inline  ::mas::schema::common::IdInformation::Pipeline Crop::CultivarResults::Pipeline::getInfo() {
  return  ::mas::schema::common::IdInformation::Pipeline(_typeless.getPointerField(0));
}
#endif  // !CAPNP_LITE
inline void Crop::CultivarResults::Builder::setInfo( ::mas::schema::common::IdInformation::Reader value) {
  ::capnp::_::PointerHelpers< ::mas::schema::common::IdInformation>::set(_builder.getPointerField(
      ::capnp::bounded<0>() * ::capnp::POINTERS), value);
}
inline  ::mas::schema::common::IdInformation::Builder Crop::CultivarResults::Builder::initInfo() {
  return ::capnp::_::PointerHelpers< ::mas::schema::common::IdInformation>::init(_builder.getPointerField(
      ::capnp::bounded<0>() * ::capnp::POINTERS));
}
inline void Crop::CultivarResults::Builder::adoptInfo(
    ::capnp::Orphan< ::mas::schema::common::IdInformation>&& value) {
  ::capnp::_::PointerHelpers< ::mas::schema::common::IdInformation>::adopt(_builder.getPointerField(
      ::capnp::bounded<0>() * ::capnp::POINTERS), kj::mv(value));
}
inline ::capnp::Orphan< ::mas::schema::common::IdInformation> Crop::CultivarResults::Builder::disownInfo() {
  return ::capnp::_::PointerHelpers< ::mas::schema::common::IdInformation>::disown(_builder.getPointerField(
      ::capnp::bounded<0>() * ::capnp::POINTERS));
}

inline bool Crop::SpeciesResults::Reader::hasInfo() const {
  return !_reader.getPointerField(
      ::capnp::bounded<0>() * ::capnp::POINTERS).isNull();
}
inline bool Crop::SpeciesResults::Builder::hasInfo() {
  return !_builder.getPointerField(
      ::capnp::bounded<0>() * ::capnp::POINTERS).isNull();
}
inline  ::mas::schema::common::IdInformation::Reader Crop::SpeciesResults::Reader::getInfo() const {
  return ::capnp::_::PointerHelpers< ::mas::schema::common::IdInformation>::get(_reader.getPointerField(
      ::capnp::bounded<0>() * ::capnp::POINTERS));
}
inline  ::mas::schema::common::IdInformation::Builder Crop::SpeciesResults::Builder::getInfo() {
  return ::capnp::_::PointerHelpers< ::mas::schema::common::IdInformation>::get(_builder.getPointerField(
      ::capnp::bounded<0>() * ::capnp::POINTERS));
}
#if !CAPNP_LITE
inline  ::mas::schema::common::IdInformation::Pipeline Crop::SpeciesResults::Pipeline::getInfo() {
  return  ::mas::schema::common::IdInformation::Pipeline(_typeless.getPointerField(0));
}
#endif  // !CAPNP_LITE
inline void Crop::SpeciesResults::Builder::setInfo( ::mas::schema::common::IdInformation::Reader value) {
  ::capnp::_::PointerHelpers< ::mas::schema::common::IdInformation>::set(_builder.getPointerField(
      ::capnp::bounded<0>() * ::capnp::POINTERS), value);
}
inline  ::mas::schema::common::IdInformation::Builder Crop::SpeciesResults::Builder::initInfo() {
  return ::capnp::_::PointerHelpers< ::mas::schema::common::IdInformation>::init(_builder.getPointerField(
      ::capnp::bounded<0>() * ::capnp::POINTERS));
}
inline void Crop::SpeciesResults::Builder::adoptInfo(
    ::capnp::Orphan< ::mas::schema::common::IdInformation>&& value) {
  ::capnp::_::PointerHelpers< ::mas::schema::common::IdInformation>::adopt(_builder.getPointerField(
      ::capnp::bounded<0>() * ::capnp::POINTERS), kj::mv(value));
}
inline ::capnp::Orphan< ::mas::schema::common::IdInformation> Crop::SpeciesResults::Builder::disownInfo() {
  return ::capnp::_::PointerHelpers< ::mas::schema::common::IdInformation>::disown(_builder.getPointerField(
      ::capnp::bounded<0>() * ::capnp::POINTERS));
}

#if !CAPNP_LITE
inline Service::Client::Client(decltype(nullptr))
    : ::capnp::Capability::Client(nullptr) {}
inline Service::Client::Client(
    ::kj::Own< ::capnp::ClientHook>&& hook)
    : ::capnp::Capability::Client(::kj::mv(hook)) {}
template <typename _t, typename>
inline Service::Client::Client(::kj::Own<_t>&& server)
    : ::capnp::Capability::Client(::kj::mv(server)) {}
template <typename _t, typename>
inline Service::Client::Client(::kj::Promise<_t>&& promise)
    : ::capnp::Capability::Client(::kj::mv(promise)) {}
inline Service::Client::Client(::kj::Exception&& exception)
    : ::capnp::Capability::Client(::kj::mv(exception)) {}
inline  ::mas::schema::crop::Service::Client& Service::Client::operator=(Client& other) {
  ::capnp::Capability::Client::operator=(other);
  return *this;
}
inline  ::mas::schema::crop::Service::Client& Service::Client::operator=(Client&& other) {
  ::capnp::Capability::Client::operator=(kj::mv(other));
  return *this;
}

#endif  // !CAPNP_LITE
}  // namespace
}  // namespace
}  // namespace

CAPNP_END_HEADER
