import os

import pytest

from flaskbox.helpers import create_init_file
from flaskbox.reader import YAMLBaseReader


@pytest.yield_fixture(autouse=True)
def create_yaml_file():
    """Create the flaskbox yaml file, and after tests delete the file
    """
    yield create_init_file()
    os.remove('flaskbox.yml')


@pytest.fixture
def base_app():
    return YAMLBaseReader().read()


@pytest.fixture
def base_fields():
    fields = [
        {'name': 'string'},
        {'last_name': 'string'},
        {'users': 'array_str'},
        {'ids': 'array_int'},
        {'created_at': 'datetime'}
    ]
    return fields
