from model.command import Command
from model.user import User
from session import *
import settings
import os

def login(username, password):
    for user in User.users:
        if user.username == username and user.password == password:
            Session.current_user = user
            OpenObject(Session.current_user, settings.rootdir).execute()
            return "Welcome " + Session.current_user.username
        else:
            return "Login invalido."

class OpenObject(Command):
    def __init__(self, user, obj):
        super().__init__('OpenObject', user, obj)

    def run (self):
        Session.current_directory = self.object

    def success (self):
        print("Opening " + str(self.object))

class ShowCurrentDirectory(Command):
    def __init__(self, user):
        super().__init__('ShowCurrentDirectory', user, Session.current_directory)

    def run (self):
        print(os.listdir(Session.current_directory._real_path))

    def success (self):
        print("Showing " + str(self.object) + " objects")
