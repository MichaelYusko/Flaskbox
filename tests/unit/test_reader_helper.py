from flaskbox.reader_helper import get_name, get_routes

data = [
    {'application': {'name': 'Flaskbox API'}},
    {'route': 'users'},
    {'route': 'companies'},
    {'route': 'books'}
]


def test_get_name_helper():
    """Test get_name function"""
    name = get_name(data)
    assert name == data[0]['application']['name']


def test_get_routes():
    """Test get_routes function"""
    routes = get_routes(data)
    assert (isinstance(routes, list), len(routes)) == (True, 3)
