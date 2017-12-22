"""Helpers method for ApplicationReaer"""


def get_name(data):
    """
    :param data: An array with data of application
    :return: An application name
    """
    name = None
    for obj in data:
        if 'application' in obj:
            return obj['application']['name']
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
