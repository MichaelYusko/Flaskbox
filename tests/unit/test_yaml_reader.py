from flaskbox.reader import YAMLBaseReader

# Instance of YAMLBaseReader class
reader = YAMLBaseReader()


def test_reader_get_name(base_app):
    """Test if name of application is correct
    """
    assert reader.get_name(base_app) == 'Flaskbox API'


def test_reader_get_routes(base_app):
    """Test if a routes returned correct
    """
    routes = reader.get_routes(base_app)
    assert (isinstance(routes, list), len(routes)) == (True, 1)


def test_reader_port(base_app):
    """Test if a route returned correct
    """
    port = reader.get_port(base_app)
    assert port == 5000


def test_reader_fields(base_app):
    routes = reader.get_routes(base_app)
    fields = None
    for route in routes:
        fields = reader.get_fields(route)
    assert (isinstance(fields, list), len(fields)) == (True, 5)
