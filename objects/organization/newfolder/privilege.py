from . import role, command

class Privilege:

    def __init__(self, role, command):
        self.command = role
        self.role = command

    def role(self):
        print (self.role.name)

    def command(self):
        print (self.command.name)

    def __repr__(self):
        return "<" + self.role.name + self.command.name + ">"
