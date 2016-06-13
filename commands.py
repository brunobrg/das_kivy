from model.command import Command

class OpenObject(Command):
    def __init__(self, user, obj):
        super().__init__('OpenObject', user, obj)

    def run (self):
        pass

    def success (self):
        print("Opening " + str(self.object))

    def __repr__(self):
        return "<Command:" + self.name + ">"
