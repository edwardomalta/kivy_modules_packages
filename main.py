from kivy.app import App
from kivy.lang import Builder

Builder.load_file("boton_especial.kv")

class MyApp(App):
    pass

if __name__ == "__main__":
    MyApp().run()