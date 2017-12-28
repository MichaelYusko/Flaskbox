"""Reader stuff"""

from flaskbox.decorators import file_not_exists
from flaskbox.reader_helper import get_name, read_file


class YAMLBaseReader:
    """Reader main class"""

    @file_not_exists
    def read(self):
        """Read the flaskbox.yml file"""
        return read_file()


class Config(YAMLBaseReader):
    """Config class which will collect an mock data"""
    def __init__(self):
        self.conf = self.read()

    @property
    def name(self):
        name = get_name(self.conf)
        return name
