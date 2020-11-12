from abc import ABCMeta, abstractmethod

class MapperRegistry:
    registry = {}

    @classmethod
    def register(cls, mapper):
        def wrapper(klass):
            cls.registry[klass] = mapper
            return klass
        return wrapper

    @classmethod
    def get_mapper(cls, obj):
        return cls.registry.get(obj.__class__)()


class AbstractMapper(metaclass = ABCMeta):

    def __init__(self):
        self.loaded_map = {}

    def load(self, _id):
        result = self.loaded_map.get(_id) is not None
        if result is not None:
            return result
        else:
            self.do_load(_id)

    @abstractmethod
    def do_load(self, what):
        pass

    @abstractmethod
    def insert(self, obj):
        pass

    @abstractmethod
    def update(self, obj):
        pass

    @abstractmethod
    def delete(self, obj):
        pass