from abc import ABCMeta


class SingletonABCMeta(ABCMeta):
    _instance = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls._instance:
            cls._instance[cls] = super(SingletonABCMeta, cls).__call__(*args, **kwds)
        return cls._instance[cls]
