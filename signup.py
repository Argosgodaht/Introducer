import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen


class Signup(BoxLayout):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
     


class Reg(App):
    def build(self):
        return Signup()
if __name__=="__main__":
    Reg().run()
