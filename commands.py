from model.command import *
from model.user import User
from session import *
import settings
import os

class Login(LoginCommand):
    def __init__(self, username, password):
        super().__init__('Login', None, username, password)
        self()

    def __call__(self):
        self.execute()

    def run(self):
        for user in User.users:
            if user.username == self.username and user.password == self.password:
                Session.current_user = user
                OpenObject(Session.current_user, settings.rootdir)
                return True
        return False

    def success(self):
        self.user = Session.current_user
        self.user.command_log.append(self)
        print("Welcome " + self.user.username + ".")

    def fail(self):
        print("Login invalido.")

###### User Commands

class Logout(UserCommand):
    def __init__(self, user):
        super().__init__('Logout', user)
        self()

    def __call__(self):
        self.execute()

    def run(self):
        if self.user:
            Session.current_user = None
            self.user.command_log.append(self)
            return True
        else:
            return False

    def success(self):
        print("Exiting the system...")


class MyInformation(UserCommand):
    def __init__(self, user):
        super().__init__('MyInformation', user)
        self()

    def __call__(self):
        self.execute()

    def run(self):
        if self.user:
            self.user.command_log.append(self)
            return True
        else:
            return False

    def success(self):
        print()


###### Object Commands

class OpenObject(ObjectCommand):
    def __init__(self, user, obj):
        super().__init__('OpenObject', user, obj)
        self()

    def __call__(self):
        self.execute()

    def run (self):
        Session.current_directory = self.object

    def success (self):
        print("Opening " + str(self.object))

class ShowDirectory(ObjectCommand):
    def __init__(self, user, obj):
        super().__init__('ShowDirectory', user, obj)
        self()

    def __call__(self):
        self.execute()

    def run (self):
        print(os.listdir(self.object._real_path))

    def success (self):
        print("Showing " + str(self.object) + " objects")
