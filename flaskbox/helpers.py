"""Helpers stuff"""

import yaml

base_configuration = [
    {
        'application': {
            'name': 'Flaskbox API',
        }
    },
    {
        'route': {
            'name': 'users',
            'fields': [
                {'name': 'string'},
                {'last_name': 'string'},
                {'users': 'array_str'},
                {'ids': 'array_int'},
                {'created_at': 'datetime'}
            ]
        }
    }
]


def _create_yml_file(file_name: str = 'flaskbox.yml'):
    """
    :param file_name: Name for a file.
    """
    with open(file_name, 'w') as file:
        yaml.dump(base_configuration, file, default_flow_style=False)


def create_init_file():
    """Create the flaskbox.yml file
    """
    _create_yml_file()
