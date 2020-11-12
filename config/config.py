from abc import ABCMeta, abstractmethod

class AbstractConfig(metaclass = ABCMeta):
    environ = {}

    def __init__(self):
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

    def __setattr__(self, key, value):
        self.environ[key] = value
        self.notify()

    def __getattr__(self, item):
        '''
        Wrapper function to access the environ dictionary
        It may throw a KeyError.
        It is the client's responsiblity to handle the exception
        :param item: A hashable type
        :return: The corresponding configuration value
        '''
        return self.environ[item]
