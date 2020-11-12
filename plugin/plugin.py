from abc import ABCMeta, abstractmethod

class AbstractPlugin(metaclass = ABCMeta):
    def __init__(self, config):
        self.config = config
        self.config.register(self)

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def update(self):
        pass