from uow.uow import UnitOfWork as uow
from domain.domain_object import DomainObject
from mapper.mapper import MapperRegistry, AbstractMapper

class AlbumMapper(AbstractMapper):
    def __init__(self):
        super().__init__()

    def do_load(self, what):
        print('Album mapper loading')

    def insert(self, obj):
        print(f'In album mapper insert: {obj}')
        print(f'Inserting new album')

    def update(self, obj):
        print('Updating dirty album')

    def delete(self, obj):
        print('Deleting removed album')


@MapperRegistry.register(AlbumMapper)
class Album(DomainObject):
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
        self.mark_new()

    def __setattr__(self, key, value):
        if key in self.__dict__:
            self.mark_dirty()
        self.__dict__[key] = value

    def get_id(self):
        return hash(self.title)

    def __str__(self):
        return f'{self.title}: {self.genre}'



if __name__ == '__main__':
    a = Album('Wish you were here', 'Psychedelic')
    unit = uow.new_current()
    a.title = 'Some other tile'
    unit.commit()
