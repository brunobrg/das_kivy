from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from model.session import Session
from model.user import User
from model.role import Administrator
from model.object import Directory
from model.assignment import Assignment
from model.privilege import Privilege
from controller.session import LoginScreen
from controller.object import DirectoryScreen
from commands import *


presentation = Builder.load_file("view/main.kv")

class ScreenManagement(ScreenManager):
    main_screen = ObjectProperty(None)
    directory_screen = ObjectProperty(None)

class MainScreen(Screen):
    pass


class MainApp(App):

    session = Session()

    admin_user = User("admin", "12345")
    admin_role = Administrator()
    admin_assign = Assignment(admin_user, admin_role)
    rootpath = "/home/gagos/unb/git/das/das_ep0/objects/organization"
    rootdir = Directory(rootpath, None, admin_role)
    admin_privilege = Privilege(admin_role, rootdir)
    admin_privilege.add_command('OpenObject')
    rootdir.update_directory()

    def build(self):
        return ScreenManagement()

if __name__ == "__main__":
    MainApp().run()
