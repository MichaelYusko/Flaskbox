"""Reader stuff"""

from flaskbox.decorators import file_not_exists
from flaskbox.reader_helper import read_file


class YAMLBaseReader:
    """Reader main class"""

    @file_not_exists
    def _read(self):
        """Read the flaskbox.yml file"""
        return read_file()
