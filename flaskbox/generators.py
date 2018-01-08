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
    """
        Warning:: Just mocked the flow, class will be rewritten
    """

    def response(self):
        # TODO Add a fake data, based on type.
        return jsonify({'data': [1, 2, 3, 4, 5, 6]})

    def make_blueprints(self):
        blueprints = []
        for ob in config.routes:
            bp = Blueprint(ob['route']['name'], __name__)
            route_name = '/' + ob['route']['name'],
            bp.add_url_rule(route_name, 'response', self.response)
            blueprints.append(bp)
        return blueprints


# instance of blueprint class
blueprint = BlueprintGenerator()
