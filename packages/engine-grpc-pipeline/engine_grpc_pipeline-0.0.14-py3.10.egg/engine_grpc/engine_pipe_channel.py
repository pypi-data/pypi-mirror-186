from __future__ import annotations

import asyncio
from dataclasses import dataclass

from compipe.runtime_env import Environment as env
from compipe.utils.logging import logger
from grpclib.client import Channel
from grpclib.config import Configuration
from ugrpc_pipe import UGrpcPipeStub

from .engine_pipe_abstract import EngineAbstract, EnginePlatform


@dataclass
class GrpcChannelConfig:
    description: str
    channel: str
    max_msg_length: int

    @classmethod
    def retrieve_grpc_cfg(cls, engine: EnginePlatform) -> GrpcChannelConfig:
        if (grpc_cfg_json := env().get_value_by_path(['grpc', engine.name], None)) == None:
            raise ValueError(f"Not found matched grpc config for engine: {engine}")

        return GrpcChannelConfig(**grpc_cfg_json)


@dataclass
class base_channel(object):

    engine: EngineAbstract

    channel: str

    def __post_init__(self):
        if not self.channel:
            self.grpc_cfg: GrpcChannelConfig = GrpcChannelConfig.retrieve_grpc_cfg(engine=self.engine.engine_platform)
            self.channel = self.grpc_cfg.channel
            logger.warning(f"Initialize gRPC channel by passing default values {self.channel}")

        if ':' not in self.channel:
            raise ValueError('The specified channel content is invalid. Only accept format <ip>:<port> e.g., 127.0.0.1:50051')

        # declare the maximum message length by passing the values from config
        cfg = Configuration(http2_stream_window_size=self.grpc_cfg.max_msg_length,
                            http2_connection_window_size=self.grpc_cfg.max_msg_length)

        # parse host address and port from the specified channel definition

        host, port = tuple(self.channel.split(':'))

        # construct a channel instance
        self.grpc_channel = Channel(host=host, port=port, config=cfg, loop=self.engine.event_loop)

    def __enter__(self):
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb):
        # make sure the grpc channel gets closed
        self.grpc_channel.close()


class general_channel(base_channel):

    def __post_init__(self):

        # try to retrieve the existing event loop. or create a new one.
        try:
            self.engine.event_loop = asyncio.get_event_loop()
        except RuntimeError:
            self.engine.event_loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self.engine.event_loop)

        super().__post_init__()

    def __enter__(self):
        # make a grpc stub and return it
        self.engine.stub = UGrpcPipeStub(channel=self.grpc_channel)
