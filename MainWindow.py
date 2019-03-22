import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MainWindow(BoxLayout):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
     


class Home(App):
    def build(self):
        return MainWindow()
    
if __name__ == "__main__":
    Home().run()
