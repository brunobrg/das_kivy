class User:

    users = []

    def __init__(self, name, password):
        self.username = name
        self.password = password
        self.__class__.users.append(self)
