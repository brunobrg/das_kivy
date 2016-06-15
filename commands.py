from model.command import *
from model.user import User
from controller.session import *
import os


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



class CreateNewRole(ObjectCommand):

    def __init__(self, user, obj, role_name):
        super().__init__('CreateNewRole', user, obj)
        self.role_name = role_name
        self()

    def __call__(self):
        self.execute()

    def run(self):
        sub_role = SubRole(self.role_name)
        self.object.add_sub_role(sub_role)

    def success(self):
        print("Role " + self.role + " created for " + str(self.object))
