"""Application stuff"""
from flask import Flask

from flaskbox.reader import Config


class Application:
    """Main class for an application"""
    def __init__(self):
        self.config = Config()
        self.app = Flask(self.config.name)

    def run_server(self):
        """Start a mock server"""
        return self.app.run()


# Object of Application class
application = Application
