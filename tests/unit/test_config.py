from flaskbox.config import config


def test_config_get_name(base_app):
    """Get an application name"""
    name = config.get_name(base_app)
    assert name == base_app[0]['application']['name']


def test_config_get_routes(base_app):
    """Test if an array with routes exists
    """
    routes = config.get_routes(base_app)
    assert (isinstance(routes, list), len(routes)) == (True, 1)


def test_config_get_fields(base_app):
    """If fields exists, return an array with field objects
    """
    fields = None
    routes = config.get_routes(base_app)
    for route in routes:
        fields = config.get_fields(route)
    assert (isinstance(fields, list), len(fields)) == (True, 4)


def test_config_port_not_exists(base_app):
    """If port not exists, return default 5000 port
    """
    port = config.get_port(base_app)
    assert 5000 == port
