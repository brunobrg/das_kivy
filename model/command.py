from abc import ABCMeta, abstractmethod
from datetime import datetime

class Command(metaclass=ABCMeta):

    id_iterator = 0;

    def __init__(self, name):
        self.id = self.__class__.id_iterator + 1
        self.name = name
        self.executed_date = str(datetime.now())

    @abstractmethod
    def success(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def execute(self):
        if self.has_privilege():
            self.success()
            self.run()
        else:
            self.fail()

    def fail(self):
        print ("You can not " + self.name)


class Open_obj_by_path(Command):
    def __init__(self, user, obj):
        super().__init__("open object by path: " + obj)
        self.user = user
        self.obj = obj

    def run (self):
        pass

    def success (self):
        print("Opening " + self.obj)
