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
        self.clear_widgets()
        OpenObject(app.session.user, self.obj).execute()


class DirectoryScreen(Screen):
    def __init__(self, **kwargs):
        super(DirectoryScreen, self).__init__(**kwargs)

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
        app.root.add_widget(DirectoryScreen(name='%s' % self.object.path))
        app.root.current = self.object.path

    def success(self):
        print("Opening " + str(self.object))
