 import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database1 import DataBase
from kivy.properties import ObjectProperty

class SigninWindow(BoxLayout,Screen):
    name = ObjectProperty(None)
    email = ObjectProperty(None)
    pwd = ObjectProperty(None)
    branch = ObjectProperty(None)
    contact = ObjectProperty(None)
    user_name = ObjectProperty(None)
    pwd1 = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()
    
    
    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

        
class Signup(BoxLayout,Screen):
    def __init__(self, **kwargs):
          super().__init__(**kwargs)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.pwd.text, self.namee.text)

                self.reset()

                app.root.current = "second"
            else:
                invalidForm()
        else:
            invalidForm()
    

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


class WindowManager(ScreenManager):
    pass

def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()


kv = Builder.load_file("signin.kv")

sm = WindowManager()
db = DataBase("users.txt")


class SigninApp(App):
    def build(self):
        return 


if __name__ == "__main__":
    SigninApp().run() 
