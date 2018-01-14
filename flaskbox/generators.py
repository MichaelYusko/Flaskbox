"""Generator stuff"""

from flask import Blueprint, jsonify

from flaskbox.config import config
from flaskbox.decorators import if_file_exists
from flaskbox.helpers import create_init_file


class YAMLGenerator:
    """Yaml generator class"""

    @staticmethod
    @if_file_exists
    def create_file():
        """
        :return: The flaskbox.yml file
        """
        """Create the init file"""
        return create_init_file()


class BlueprintGenerator:
    """Blueprint generator"""

    def response(self):
        # TODO Add a fake data, based on type.
        return jsonify({'data': [1, 2, 3, 4, 5, 6]})

    def make_blueprints(self):
        """"
        Iterate the config routes object,
        and make an Blueprint objects, also add into the blueprints array.
        :return: An array with Blueprint objects
        """
        blueprints = []
        for route in config.routes:
            name = config.get_route_name(route)
            bp = Blueprint(name, __name__)
            bp.add_url_rule(name, 'response', self.response)
            blueprints.append(bp)
        return blueprints


# instance of blueprint class
blueprint = BlueprintGenerator()
