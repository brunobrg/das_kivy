from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from model.command import LoginCommand
from model.user import User
from .object import OpenObject, DirectoryScreen

presentation = Builder.load_file("view/session.kv")

class LoginScreen(Screen):
    def login(self, username, password):
        app = App.get_running_app()
        if Login(username, password).execute():
            OpenObject(app.session.user, app.rootdir).execute()

class Login(LoginCommand):
    def __init__(self, username, password):
        super().__init__('Login', None, username, password)

    def run(self):
        for user in User.users:
            if user.username == self.username and user.password == self.password:
                app = App.get_running_app()
                app.session.user = user
                self.user = app.session.user
                return True
        return False

    def success(self):
        self.user.command_log.append(self)
        print("Welcome " + self.user.username + ".")
        return True

    def fail(self):
        print("Login invalido.")
        return False
