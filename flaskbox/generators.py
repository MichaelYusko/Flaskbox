"""Generator stuff"""

import os
import sys

from flask import Blueprint, jsonify

from flaskbox import constants
from flaskbox.config import config
from flaskbox.fake_data import fake_data
from flaskbox.helpers import create_init_file


class YAMLGenerator:
    """Generator class for the flaskbox stuff

        Methods::
            create_file Create the flaskbox yaml file
    """

    @staticmethod
    def create_file():
        """
        :return: The flaskbox.yml file
        """
        """Create the init file"""
        if os.path.isfile('flaskbox.yml'):
            print(constants.FILE_EXISTS_MESSAGE)
            sys.exit(1)
        return create_init_file()


class BlueprintGenerator:
    """Class for a blueprints stuff

        Methods::
            response Return an fake data base on data type,
                     not completed yet
            make_blueprints Make a blueprint object,
                            add route name, and fake data.
            base_route Add base route for a flask application
    """

    @staticmethod
    def base_route():
        """Base route for an flaskbox API
        :return: an dictionary, with welcome message
        """
        return jsonify({'data': {'message': 'Flaskbox mock server'}})

    @staticmethod
    def response():
        """
        :return: Return an response, based on fields, see fake_data.FakeData class
        """
        data = None
        for route in config.routes:
            fields = config.get_fields(route)
            fake_objects = fake_data.generate_value(fields)
            data = dict([(key, field[key]) for field in fake_objects for key in field])
        return jsonify({'data': data})

    def make_blueprints(self):
        """"Iterate the config routes object,
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
