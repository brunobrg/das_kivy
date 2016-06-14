from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

presentation = Builder.load_file("view/session.kv")

class Session:
    current_user = None
    current_directory = None


class LoginScreen(Screen):
    pass
