"""Helpers method for ApplicationReaer"""

import yaml


def read_file():
    """Read the yaml file"""
    with open('flaskbox.yml', 'r') as file:
        file = yaml.load(file)
    return file


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


def get_routes_name(data):
    """
    :param data: An array with route objects
    :return: An name of route
    """
    for obj in data:
        return obj['route']['name']
