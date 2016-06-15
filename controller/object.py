from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from model.command import ObjectCommand

presentation = Builder.load_file("view/object.kv")

class Object(Button):
    obj = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Object, self).__init__(**kwargs)

    def click(self):
        app = App.get_running_app()
        OpenObject(app.session.user, self.obj).execute()


class DirectoryScreen(Screen):
    def __init__(self, **kwargs):
        super(DirectoryScreen, self).__init__(**kwargs)

    def update(self):
        app = App.get_running_app()
        objs = app.session.directory.containing_objects
        for _obj in objs[len(self.ids.stack.ids):]:
            self.ids.stack.add_widget(Object(obj=_obj, text=_obj.name, size_hint=(0.2,0.2)))

    def destroy(self):
        app = App.get_running_app()
        app.root.remove_widget(self)

class OpenObject(ObjectCommand):

    def __init__(self, user, obj):
        super().__init__('OpenObject', user, obj)

    def run(self):
        app = App.get_running_app()
        app.session.directory = self.object
        app.root.add_widget(DirectoryScreen(name='%s' % self.object.path, id=self.object.path))
        app.root.current = self.object.path

    def success(self):
        print("Opening " + str(self.object))
