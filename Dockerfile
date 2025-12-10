############################
# Stage 1: build capnproto #
############################
FROM debian:13 AS capnp-builder

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

# Install Dotnet SDK and build capnpc-csharp
RUN curl -fsSLO https://packages.microsoft.com/config/debian/13/packages-microsoft-prod.deb && \
    dpkg -i packages-microsoft-prod.deb && \
    rm packages-microsoft-prod.deb && \
    apt-get update && \
    apt-get install -y dotnet-sdk-10.0

RUN git clone -b net9.0 https://github.com/zalf-rpm/capnproto-dotnetcore.git && \
    cd capnproto-dotnetcore && \
    dotnet publish -c Release capnpc-csharp/capnpc-csharp.csproj --framework net10.0 -o /out/capnpc-csharp

#############################
# Stage 2: runtime (minimal) #
#############################
FROM debian:13 AS capnp-runtime
ARG CAPNP_VERSION=1.2.0
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /workspace

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-venv ca-certificates libstdc++6 curl git && \
    curl -fsSLO https://packages.microsoft.com/config/debian/13/packages-microsoft-prod.deb && \
    dpkg -i packages-microsoft-prod.deb && \
    rm packages-microsoft-prod.deb && \
    apt-get update && \
    apt-get install -y dotnet-runtime-10.0 && \
    rm -rf /var/lib/apt/lists/*

# Copy capnp installation from builder
COPY --from=capnp-builder /usr/local/ /usr/local/
COPY --from=capnp-builder /out/capnpc-csharp /opt/capnpc-csharp
RUN ln -s /opt/capnpc-csharp/capnpc-csharp /usr/local/bin/capnpc-csharp
RUN ldconfig

# Install capnpc-python plugin
RUN pip3 install --no-cache-dir --break-system-packages "git+https://github.com/zalf-rpm/capnp-stub-generator.git@feature/capnpc-plugin-support"

# Default entrypoint runs code generation (expects repo mounted at /workspace)
# Override languages via: docker run ... capnp-gen --lang c++ go python
# capnpc-go and capnpc-python plugins installed in /usr/local/bin (already in default PATH)
ENTRYPOINT ["python3", "capnp_compile.py"]
CMD ["--lang", "c++", "go", "csharp", "python"]
