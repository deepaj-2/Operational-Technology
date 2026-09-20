FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    git \
    python3 \
    python3-pip \
    python3-venv \
    build-essential \
    pkg-config \
    bison \
    flex \
    autoconf \
    automake \
    libtool \
    cmake \
    sqlite3 \
    curl \
    openssl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workdir

RUN git clone https://github.com/thiagoralves/OpenPLC_v3.git .

RUN ./install.sh docker

EXPOSE 8080
EXPOSE 502

VOLUME ["/docker_persistent"]

CMD ["/workdir/start_openplc.sh"]
