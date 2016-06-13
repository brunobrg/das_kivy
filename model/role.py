from abc import ABCMeta
class Role(metaclass=ABCMeta):

    id_iterator = 0

    def __init__(self, name):
        self.id = self.__class__.id_iterator + 1
        self.name = name
        self.privileges = []
        self.assignments = []

class Administrator(Role):

    def __init__(self):
        super().__init__("Administrator")
        self.sub_roles = []

class SubRole(role):

    def __init__(self, name):
        super().__init__(name)
