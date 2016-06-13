class User:

    users = []
    id_iterator = 0

    def __init__(self, name, password):
        self.id = self.__class__.id_iterator + 1
        self.username = name
        self.password = password
        self.assignments = []
        self.__class__.users.append(self)

    def has_privilege(self, obj, command):
        for assign in self.assignments:
            if assign.has_privilege(obj, command):
                return True
        return False

    def __repr__(self):
        return "<User:" + self.username + ">"
