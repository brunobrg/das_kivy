from abc import ABCMeta, abstractmethod
from datetime import datetime

class Command(metaclass=ABCMeta):

    id_iterator = 0;

    def __init__(self, name, user, obj):
        self.id = self.__class__.id_iterator + 1
        self.name = name
        self.user = user
        self.object = obj
        self.executed_date = str(datetime.now())

    def has_privilege(self):
        return self.user.has_privilege(self.object, self)

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
