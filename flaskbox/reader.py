"""Reader stuff"""
import yaml

from flaskbox.reader_helper import get_name, get_routes


class ApplicationReader:
    """
    Helper class for yml read/write actions.
    """
    def __init__(self):
        self.app_yml = 'flaskbox.yml'
        self.blueprints = []

    def _read(self):
        """Read the yml file
        :return: The yml file in dictionary representation
        """
        try:
            with open(self.app_yml, 'r') as config:
                yml = yaml.load(config)
            return yml
        except FileNotFoundError:
            return None

    @property
    def name(self):
        """Get name of application name
        :return: An name of application
        """
        name = get_name(self._read())
        if name is None:
            name = 'Flaskbox API'
        return name

    @property
    def routes(self):
        """
        :return: An array with route objects
        """
        routes = get_routes(self._read())
        return routes
