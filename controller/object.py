from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from model.command import ObjectCommand

presentation = Builder.load_file("view/object.kv")

class Directory(Button):
    obj = ObjectProperty(None)

    def click(self):
        app = App.get_running_app()
        OpenObject(app.session.user, self.obj).execute()


class DirectoryScreen(Screen):
    def update(self):
        app = App.get_running_app()
        stack = StackLayout(orientation='lr-tb', spacing=[10,10])
        objs = app.session.directory.containing_objects
        for _obj in objs:
            stack.add_widget(Directory(obj=_obj, text=_obj.name, size_hint=(1/len(objs),1/len(objs))))
        self.add_widget(stack)

class OpenObject(ObjectCommand):

    def __init__(self, user, obj):
        super().__init__('OpenObject', user, obj)

    def run(self):
        app = App.get_running_app()
        app.session.directory = self.object
        app.root.current = 'directory_screen'

    def success(self):
        print("Opening " + str(self.object))

# class ShowDirectory(ObjectCommand):
#
#     def __init__(self, user, obj):
#         super().__init__('ShowDirectory', user, obj)
#
#     def run(self):
#         print(os.listdir(self.object._real_path))
#
#     def success(self):
#         print("Showing " + str(self.object) + " objects")

# class Login(LoginCommand):
#     def __init__(self, username, password):
#         super().__init__('Login', None, username, password)
#
#     def run(self):
#         for user in User.users:
#             if user.username == self.username and user.password == self.password:
#                 app = App.get_running_app()
#                 app.session.user = user
#                 self.user = app.session.user
#                 return True
#         return False
#
#     def success(self):
#         self.user.command_log.append(self)
#         print("Welcome " + self.user.username + ".")
#         return True
#
#     def fail(self):
#         print("Login invalido.")
#         return False
