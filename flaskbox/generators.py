"""Generator stuff"""

from flaskbox.decorators import if_file_exists
from flaskbox.helpers import create_init_file


class YamlGenerator:
    """Yaml generator class"""

    @staticmethod
    @if_file_exists
    def create_file():
        """Create the init file"""
        return create_init_file()
