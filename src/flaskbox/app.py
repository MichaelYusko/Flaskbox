from flask import Flask

from .reader import ApplicationReader


class Application:
    """Main class"""
    def __init__(self):
        self.reader = ApplicationReader()
        self.app = Flask(self.reader.name)

    def __start_server(self):
        """Custom method, for starting flask application"""
        self.app.run()

    def run(self):
        """Run the server"""
        return self.__start_server()
