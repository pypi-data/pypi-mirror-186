
import json
import os
import re
from asyncio import AbstractEventLoop
from typing import Any, List

from betterproto import Message
from compipe.utils.logging import logger
from ugrpc_pipe import (CommandParserReq, GenericResp, ProjectInfoResp,
                        UGrpcPipeStub)

from .engine_pipe_abstract import EngineAbstract, EnginePlatform
from .engine_pipe_decorator import grpc_call_general
from .engine_stub_interface import (GRPC_INTERFACE_METHOD_HEADER,
                                    INTERFACE_MAPPINGS, GRPCInterface)


class BaseEngineImpl(EngineAbstract):
    _event_loop: AbstractEventLoop = None
    _stub: Any = None

    @property
    def stub(self):
        return self._stub

    @stub.setter
    def stub(self, value):
        self._stub = value

    @property
    def event_loop(self) -> AbstractEventLoop:
        return self._event_loop

    @event_loop.setter
    def event_loop(self, value):
        self._event_loop = value

    @property
    def engine_platform(self) -> EnginePlatform:
        raise NotImplementedError


class SimulationEngineImpl(BaseEngineImpl):

    @property
    def stub(self) -> UGrpcPipeStub:
        return self._stub

    @stub.setter
    def stub(self, value):
        self._stub = value

    @property
    def asset_root_folder_name(self) -> str:
        pass

    # keep a copy of the cached project info
    _project_info: ProjectInfoResp = None

    # retrieve full command chains from the specified name
    def resolve_command_name(self, cmd: GRPCInterface):
        if cmd not in INTERFACE_MAPPINGS:
            raise KeyError("Not found the specific key: {cmd}")
        return INTERFACE_MAPPINGS[cmd][self.engine_platform]

    @grpc_call_general()
    def command_parser(self, cmd: GRPCInterface, params: List = [], return_type: Any = None, verbose: bool = False) -> GenericResp:

        logger.debug(f"Execute command: {cmd.name} : {params}")

        # parse full command str from the specific engine platform
        cmd_str = self.resolve_command_name(cmd=cmd)

        # parse command mode: method/property(static)
        # to involve the correct way to call through reflection
        is_method: bool = bool(re.match(fr'{GRPC_INTERFACE_METHOD_HEADER}_.*', cmd.name, re.IGNORECASE))

        # parse the module type name and method name from the full command str
        # i.e., UGrpc.SystemUtils.GetProjectInfo
        # -> cls: UGrpc.SystemUtils
        # -> method: GetProjectInfo
        # The method can be resolved through the reflection / delegate on the specific engine platform
        type_name, method_name = os.path.splitext(cmd_str)

        payload = {
            'type': type_name,
            'isMethod': is_method,
            'method': method_name[1:],  # remove the '.' from method name segment
            'parameters': [value for value in map(lambda n: '%@%'.join(n) if isinstance(n, List) else n, params)]
        }

        if verbose:
            logger.debug(f"Command command: {cmd}")
            logger.debug(f"Command payload: {json.dumps(payload,indent=4)}")

        resp = self.event_loop.run_until_complete(
            self.stub.command_parser(CommandParserReq(payload=json.dumps(payload)))
        )

        if not return_type:
            return resp
            # # try to cast payload into the specific type
            # caller_code_obj = inspect.stack()[2].frame.f_code
            # # retrieve function from the gc referrers list
            # upper_callers = [obj for obj in gc.get_referrers(caller_code_obj) if hasattr(
            #     obj, '__code__') and obj.__code__ is caller_code_obj][0]

        if not issubclass(return_type, Message):
            raise ValueError("The specified return_type should be a subclass of [betterproto.Message]")

        # support casting into the message object
        return return_type().parse(resp.payload.value)

    @grpc_call_general()
    def get_project_info(self, is_reload: bool = False) -> ProjectInfoResp:
        """Retrieve the current project context of the connected engine.

        Args:
            is_reload (bool, optional): Represent the flag of force re-retrieving project info. Defaults to False.

        Returns:
            ProjectInfoResp: Represent the returned project context
        """
        if not self._project_info or is_reload:

            # retrieve the project info from the engine / platform
            self._project_info = self.command_parser(cmd=GRPCInterface.method_system_get_projectinfo, return_type=ProjectInfoResp)

        return self._project_info
