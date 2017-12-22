from flask import Flask

from .reader import ApplicationReader


class Application:
    """Main class"""
    def __init__(self):
        self.reader = ApplicationReader()
        self.app = Flask(self.reader.name)

    def __start_server(self):
        """Custom method, for starting flask application"""
        self.app.run(debug=True)

    def run(self):
        """Run the server"""
        return self.__start_server()


# Instance of Application class
application = Application()


def start_app():
    """Start the mock server
    """
    return application.run()
