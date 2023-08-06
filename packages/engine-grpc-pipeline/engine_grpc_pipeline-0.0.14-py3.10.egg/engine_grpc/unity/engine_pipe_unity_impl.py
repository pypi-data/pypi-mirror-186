from ..engine_pipe_impl import SimulationEngineImpl
from ..engine_pipe_abstract import EnginePlatform


class UnityEngineImpl(SimulationEngineImpl):

    asset_root_folder_name: str = "Assets"

    @property
    def engine_platform(self) -> EnginePlatform:
        return EnginePlatform.unity
