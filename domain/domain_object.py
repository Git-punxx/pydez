from abc import ABCMeta, abstractmethod
from uow.uow import UnitOfWork as uow

class DomainObject(metaclass = ABCMeta):

    @abstractmethod
    def get_id(self):
        pass

    def mark_new(self):
        uow.get_current().register_new(self)

    def mark_clean(self):
        uow.get_current().register_clean(self)

    def mark_dirty(self):
        uow.get_current().register_dirty(self)

    def mark_removed(self):
        uow.get_current().register_removed(self)