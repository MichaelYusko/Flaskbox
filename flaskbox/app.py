"""Application stuff"""
from flask import Flask

from flaskbox.config import Config
from flaskbox.generators import blueprint


class Application:
    """Main class for an application"""
    def __init__(self):
        self.config = Config()
        self.app = Flask(self.config.name)

    def add_blueprints(self):
        bp = blueprint.make_blueprints()
        for route in bp:
            self.app.register_blueprint(route)
        return self.app

    def run_server(self):
        """Start a mock server"""
        self.add_blueprints()
        return self.app.run()


# Object of Application class
application = Application
