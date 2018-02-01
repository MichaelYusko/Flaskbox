"""Reader stuff"""

from flaskbox.decorators import file_not_exists
from flaskbox.reader_helper import read_file


class YAMLBaseReader:
    """Base reader class, which working with the flaskbox yaml file

        Methods::
            read Read and return an dict object with information
                 based on flaskbox yaml file
            get_name An name of application
            get_routes Return an array with dict objects
            get_route_name Return a name of route
            get_type return data type of route, not completed yet.
    """

    @file_not_exists
    def read(self):
        """Read the flaskbox.yml file"""
        return read_file()

    @staticmethod
    def get_name(data):
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

    @staticmethod
    def get_fields(data):
        """
        :param data: An route object
        :return: An name of route
        """
        return data['route']['fields']
