from abc import ABCMeta, abstractmethod
from datetime import datetime

class Command(metaclass=ABCMeta):

    id_iterator = 0;

    def __init__(self, name, user):
        self.id = self.__class__.id_iterator + 1
        self.name = name
        self.user = user
        self.executed_date = str(datetime.now())

    @abstractmethod
    def execute():
        pass

    @abstractmethod
    def run():
        pass

    @abstractmethod
    def success():
        pass

    @abstractmethod
    def fail():
        pass

    def __repr__(self):
        return "<<Command:" + self.name + ">:" + self.executed_date + ">"

class ObjectCommand(Command, metaclass=ABCMeta):

    def __init__(self, name, user, obj):
        super().__init__(name, user)
        self.object = obj

    def has_privilege(self):
        return self.user.has_privilege(self.object, self)

    def execute(self):
        if self.has_privilege():
            self.success()
            self.run()
            self.user.command_log.append(self)
        else:
            self.fail()

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def success(self):
        pass

    def fail(self):
        print ("You can not " + self.name + " " + str(self.object))

class LoginCommand(Command, metaclass=ABCMeta):

    def __init__(self, name, user, username, password):
        super().__init__(name, user)
        self.username = username
        self.password = password

    def execute(self):
        self.success() if self.run() else self.fail()

    @abstractmethod
    def run():
        pass

    @abstractmethod
    def success():
        pass

    @abstractmethod
    def fail(self):
        pass

class UserCommand(Command, metaclass=ABCMeta):

    def __init__(self, name, user):
        super().__init__(name, user)

    def execute(self):
        self.success() if self.run() else self.fail()

    @abstractmethod
    def run():
        pass

    @abstractmethod
    def success():
        pass

    def fail(self):
        print("Ops ~~ something went terribly wrong!")
