"""Reader stuff"""

from flaskbox.decorators import file_not_exists
from flaskbox.reader_helper import read_file


class YAMLBaseReader:
    """Reader main class"""

    @file_not_exists
    def read(self):
        """Read the flaskbox.yml file"""
        return read_file()

    def get_name(self, data):
        """
        :param data: An array with data of application
        :return: An application name
        """
        name = None
        for obj in data:
            if 'application' in obj:
                name = obj['application']['name']
        return name

    def get_routes(self, data):
        """
        :param data: An array with data of application
        :return: An array with route objects.
        """
        routes = []
        for obj in data:
            if 'route' in obj:
                routes.append(obj)
        return routes

    def get_routes_name(self, data):
        """
        :param data: An array with route objects
        :return: An name of route
        """
        for obj in data:
            return obj['route']['name']
