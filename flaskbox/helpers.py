"""Helpers stuff"""

import yaml


def _create_yml_file(file_name: str = 'flaskbox.yml'):
    """
    :param file_name: Name for a file.
    """
    base_app = [
        {'application': {'name': 'Flaskbox API'}},
        {'route': {'name': 'users', 'type': 'string'}}
    ]
    with open(file_name, 'w') as file:
        yaml.dump(base_app, file, default_flow_style=False)


def create_init_file():
    """Create the flaskbox.yml file
    """
    _create_yml_file()
