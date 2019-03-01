from kivy.app import App
from kivy.uix.button import Button


class HelloApp(App):

    def build(self):
        return Button(text='My first button')


if __name__ == '__main__':
    my_app = HelloApp()
    my_app.run()
