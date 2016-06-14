from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from controller.login import LoginScreen

presentation = Builder.load_file("main.kv")


class MainApp(App):
    def build(self):
        manager = ScreenManager()
        manager.add_widget(LoginScreen())
        return manager

if __name__ == "__main__":
    MainApp().run()
