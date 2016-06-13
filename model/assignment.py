class Assignment:

    id_iterator = 0
    assignments = []

    def __init__(self, user, role):
        self.id = self.__class__.id_iterator + 1
        self.user = user
        self.role = role

        self.user.assignments.append(self)
        self.role.assignments.append(self)
        self.__class__.assignments.append(self)

    def has_privilege(self, obj, command):
        return self.role.has_privilege(obj, command)
