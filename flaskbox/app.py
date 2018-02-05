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
        self.port = self.config.port

    def add_blueprints(self):
        """Adde a blueprint objects to an flask application
        :return: An flask application with blueprints routes
        """
        blueprints = blueprint.make_blueprints()
        for route in blueprints:
            self.app.register_blueprint(route)
        self.app.add_url_rule('/', 'base_route', blueprint.base_route)
        return self.app

    def run_server(self):
        """
        :return: Start an flask server
        """
        self.add_blueprints()
        return self.app.run(port=self.port)


# Object of Application class
application = Application
