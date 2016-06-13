class Privilege:

    id_iterator = 0
    privileges = []

    def __init__(self, role, new_object):
        self.id = self.__class__.id_iterator + 1
        self.role = role
        self.object = new_object
        self.__class__privileges.append(self)
