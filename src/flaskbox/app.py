from flask import Flask


class Application:
    def __init__(self, application):
        self.app = application

    def __start_server(self, app):
        app.run()

    def run(self):
        f = Flask(__name__)
        return self.__start_server(f)
