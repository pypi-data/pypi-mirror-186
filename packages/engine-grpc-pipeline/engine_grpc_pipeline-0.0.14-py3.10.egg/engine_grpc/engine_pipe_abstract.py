from abc import ABC, abstractmethod
from enum import Enum

from .utils.singleton import SingletonABCMeta


class EnginePlatform(Enum):
    unknown = 0
    unity = 1
    unreal = 2
    godot = 3
    blender = 4  # refer to https://ciesie.com/post/blender_python_rpc/


class EngineAbstract(ABC):
    __metaclass__ = SingletonABCMeta

    @property
    @abstractmethod
    def stub(self):
        pass

    @property
    @abstractmethod
    def event_loop(self):
        pass

    @property
    @abstractmethod
    def engine_platform(self) -> EnginePlatform:
        raise NotImplementedError
