FROM mcr.microsoft.com/dotnet/runtime:10.0-noble AS builder


RUN useradd --no-create-home odcompile

WORKDIR /opendream

COPY ./OpenDream/ .

RUN ln -s /opendream/DMCompiler_linux-x64/ /opendream/compiler
RUN ln -s /opendream/OpenDreamServer_linux-x64/ /opendream/server

FROM builder

WORKDIR /app

COPY docker/run.sh .

RUN chown -R odcompile: /opendream
RUN chown -R odcompile: /app

USER odcompile

ENTRYPOINT [ "/bin/sh", "/app/run.sh" ]
