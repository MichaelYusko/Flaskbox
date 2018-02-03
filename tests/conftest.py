import pytest

from flaskbox.helpers import create_init_file
from flaskbox.reader import YAMLBaseReader


@pytest.fixture(autouse=True)
def create_yaml_file():
    """Create Init file"""
    create_init_file()


@pytest.fixture
def base_app():
    return YAMLBaseReader().read()
