class User:

    users = []
    id_iterator = 0

    def __init__(self, name, password):
        self.id = self.__class__.id_iterator + 1
        self.username = name
        self.password = password
        self.assignments = []
        self.__class__.users.append(self)
