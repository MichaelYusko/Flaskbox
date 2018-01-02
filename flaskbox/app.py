"""Application stuff"""
from flask import Flask

from flaskbox.config import Config
from flaskbox.generators import BlueprintGenerator


class Application:
    """Main class for an application"""
    def __init__(self):
        self.config = Config()
        self.app = Flask(self.config.name)

    def add_blueprints(self):
        self.app.register_blueprint(BlueprintGenerator('/').make_blueprint())

    def run_server(self):
        """Start a mock server"""
        self.add_blueprints()
        return self.app.run()


# Object of Application class
application = Application
