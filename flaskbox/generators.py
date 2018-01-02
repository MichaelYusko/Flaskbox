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
        """Create the init file"""
        return create_init_file()


class BlueprintGenerator:
    def __init__(self, name):
        self.name = name
        self.bp = Blueprint(name, __name__)
        self.config = config

    def response(self):
        return jsonify({'data': {'message': [1, 2, 3, 4]}})

    def blueprint(self):
        return self.bp

    def make_blueprint(self):
        self.bp.add_url_rule('/', 'index', self.response)
        return self.bp
