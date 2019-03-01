# Perform HTTP requests and print responses

# URL
# Dropdown: GET, POST, PUT, PATCH, DELETE
# Response Body:
import requests
from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.widget import Widget
from requests import Session


class HttpMethodDropDown(DropDown):
    def select(self, data):
        print("Dropdown option was selected: %s" % data)


class BaseWindow(Widget):

    method = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def perform_http_request(self, method):
        # TODO predefine the request, update the method accordingly

        request = requests.Request(method, url=self.url.text)
        response = Session().send(request.prepare())
        self.response_body.text = response.text

        # def perform_http_Request
        # Get the URL from the textfield
        # perform request
        # put output in a result field


class WebtesterApp(App):
    def build(self):
        base_window = BaseWindow()
        return base_window


if __name__ == '__main__':
    webtester = WebtesterApp()
    webtester.run()
