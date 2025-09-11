############################
# Stage 1: build capnproto #
############################
FROM ubuntu:24.04 AS capnp-builder

ARG CAPNP_VERSION=1.2.0
ARG JOBS=6
# Go plugin (capnpc-go) version/pkg (keep separate so we can pin later if needed)
ARG CAPNPC_GO_PKG=capnproto.org/go/capnp/v3/capnpc-go
ARG CAPNPC_GO_VERSION=latest
ENV DEBIAN_FRONTEND=noninteractive \
    CAPNP_SRC=capnproto-c++-${CAPNP_VERSION} \
    GOBIN=/usr/local/bin

WORKDIR /build
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl build-essential pkg-config autoconf automake libtool git ca-certificates golang-go && \
    rm -rf /var/lib/apt/lists/*
RUN curl -fsSLO https://capnproto.org/${CAPNP_SRC}.tar.gz && \
    tar zxf ${CAPNP_SRC}.tar.gz && \
    cd ${CAPNP_SRC} && ./configure && \
    make -j"${JOBS}" check && \
    make install && \
    go install ${CAPNPC_GO_PKG}@${CAPNPC_GO_VERSION}

#############################
# Stage 2: runtime (minimal) #
#############################
FROM ubuntu:24.04 AS capnp-runtime
ARG CAPNP_VERSION=1.2.0
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /workspace

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 ca-certificates libstdc++6 && \
    rm -rf /var/lib/apt/lists/*

# Copy capnp installation from builder
COPY --from=capnp-builder /usr/local/ /usr/local/
RUN ldconfig

# Default entrypoint runs code generation (expects repo mounted at /workspace)
# Override languages via: docker run ... capnp-gen --lang c++ go
# capnpc-go plugin installed in /usr/local/bin (already in default PATH)
ENTRYPOINT ["python3", "capnp_compile.py"]
CMD ["--lang", "c++"]

# Usage examples (no repo copy -> mount at runtime):
# docker build -t capnp-gen .
# docker run --rm -u $(id -u):$(id -g) -v "$(pwd)":/workspace -w /workspace capnp-gen \
#   python3 capnp_compile.py --lang c++
# Multi-language:
# docker run --rm -u $(id -u):$(id -g) -v "$(pwd)":/workspace -w /workspace capnp-gen \
#   python3 capnp_compile.py --lang c++ go
# Direct capnp usage:
# docker run --rm -u $(id -u):$(id -g) -v "$(pwd)":/workspace -w /workspace capnp-gen \
#   capnp compile -I zalfmas_capnp_schemas -oc++:gen/c++ zalfmas_capnp_schemas/common.capnp