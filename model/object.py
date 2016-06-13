from abc import ABCMeta
class Object(metaclass=ABCMeta):

    id_iterator = 0
    objects = []

    def __init__(self, real_path, parent_directory):
        self.id = self.__clas__.id_iterator + 1
        self._real_path = real_path
        self.parent_directory = parent_directory
        self.path = self.get_path_from_real_path()
        self.name = self.get_name_from_path()
        self.__class__.objects.append(self)

    def get_name_from_path(self):
        name = self.path if self.path[-1] != '/' else self.path[:-1]
        name = name.split('/')
        return name[-1]

    def get_path_from_real_path(self):
        path_split = self._real_path.split('objects/', 1)
        path = path_split[1]
        return path

    def get_type(self):
        return 'directory' if os.path.isdir(self._real_path) else 'file'

class File(Object):

    def __init__(self, path, parent_directory):
        super().__init__(path, parent_directory)

    def information(self):
        return self.name
