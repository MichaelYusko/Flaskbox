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

    @staticmethod
    def get_routes(data):
        """
        :param data: An array with data of application
        :return: An array with route objects.
        """
        routes = []
        for obj in data:
            if 'route' in obj:
                routes.append(obj)
        return routes

    @staticmethod
    def get_route_name(data):
        """
        :param data: An route object
        :return: An name of route
        """
        return '/' + data['route']['name'] if data['route']['name'] else None
