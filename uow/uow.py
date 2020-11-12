from mapper.mapper import MapperRegistry
import threading

class UnitOfWork:
    current = threading.local()

    @staticmethod
    def new_current():
        UnitOfWork.set_current(UnitOfWork())
        return UnitOfWork.current.uow

    @staticmethod
    def set_current(uow):
        UnitOfWork.current.uow = uow

    @staticmethod
    def get_current():
        return UnitOfWork.current.uow

    def __init__(self):
        self.new_objects = []
        self.dirty_objects = []
        self.removed_objects = []

    def register_new(self, obj):
        assert obj.get_id() is not None
        assert obj not in self.dirty_objects
        assert obj not in self.removed_objects
        assert obj not in self.new_objects
        self.new_objects.append(obj)

    def register_dirty(self, obj):
        assert obj.get_id() is not None
        assert obj not in self.removed_objects
        if obj not in self.new_objects and obj not in self.dirty_objects:
            self.dirty_objects.append(obj)

    def register_removed(self, obj):
        assert obj.get_id() is not None
        try:
            self.new_objects.remove(obj)
        except ValueError:
            pass

        try:
            self.dirty_objects.remove(obj)
        except ValueError:
            pass

        if obj not in self.removed_objects:
            self.removed_objects.append(obj)

    def register_clean(self, obj):
        assert obj.get_id() is not None

    def commit(self):
        self.insert_new()
        self.update_dirty()
        self.delete_removed()

    def insert_new(self):
        for obj in self.new_objects:
            mapper = MapperRegistry.get_mapper(obj)
            mapper.insert(obj)

    def update_dirty(self):
        for obj in self.dirty_objects:
            mapper = MapperRegistry.get_mapper(obj)
            mapper.update(obj)

    def delete_removed(self):
        for obj in self.removed_objects:
            mapper = MapperRegistry.get_mapper(obj)
            mapper.remove(obj)

UnitOfWork.new_current()
