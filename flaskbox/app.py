"""Application stuff"""
from flaskbox.reader import Config
from flask import Flask


class Application:
    """Main class for an application"""
    def __init__(self):
        self.config = Config()
        self.app = Flask(self.config.name)

    def run_server(self):
        """Start a mock server"""
        return self.app.run()

application = Application
