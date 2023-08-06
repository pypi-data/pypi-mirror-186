from abc import ABC
from typing import Any

from .engine_pipe_abstract import EnginePlatform
from .engine_pipe_impl import SimulationEngineImpl
from .unity.engine_pipe_unity_impl import UnityEngineImpl
from .unreal.engine_pipe_unreal_impl import UnrealEngineImpl
from .utils.singleton import SingletonABCMeta

ENGINE_MAPPINGS = {
    EnginePlatform.unity: UnityEngineImpl,
    EnginePlatform.unreal: UnrealEngineImpl
}


class EnginePipeResolver(ABC):

    __metaclass__ = SingletonABCMeta

    current_engine: Any = None

    @property
    def engine(self) -> UnrealEngineImpl | UnityEngineImpl:

        if not self.current_engine:
            # resolve the engine impl by retrieving the platform name
            current_platform = EnginePlatform(SimulationEngineImpl().get_project_info().platform)

            # get the interface implementation of the corresponding platform
            self.current_engine = ENGINE_MAPPINGS[current_platform]()

        return self.current_engine
