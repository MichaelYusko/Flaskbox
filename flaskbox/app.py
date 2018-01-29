"""Application stuff"""
from flask import Flask

from flaskbox.config import Config
from flaskbox.generators import blueprint


class Application:
    """Main class for an application, run/add blueprints here.

        Methods::
            add_blueprints Add blueprints for a flask application
            run_server Add blueprints, and start a flask server.
    """
    def __init__(self):
        self.config = Config()
        self.app = Flask(self.config.name)

    def add_blueprints(self):
        """
        :return: An flask instance
        """
        bp = blueprint.make_blueprints()
        for route in bp:
            self.app.register_blueprint(route)
        return self.app

    def run_server(self):
        """
        :return: Start an flask server
        """
        self.add_blueprints()
        return self.app.run()


# Object of Application class
application = Application
