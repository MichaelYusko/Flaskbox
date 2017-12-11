"""Helpers stuff"""
import os
import sys

import yaml


def _create_yml_file(file_name: str = 'flaskbox.yml'):
    """
    :param file_name: An yml file, default is flaskbox.yml
    Create an yml file.
    """
    if os.path.isfile(file_name):
        path = os.path.abspath(file_name)
        print(
            f'File {file_name} already exists,',
            f'path: {path}'
        )
        sys.exit(1)

    base_app = {'application': 'My restful API'}
    with open(file_name, 'w') as file:
        yaml.dump(base_app, file, default_flow_style=False)


def create_init_file():
    """Create the flaskbox.yml file
    """
    _create_yml_file()
