from flaskbox.reader import YAMLBaseReader
from flaskbox.reader_helper import get_name, get_routes


class Config(YAMLBaseReader):
    """Config class which will collect an mock data"""
    def __init__(self):
        self.conf = self.read()

    @property
    def name(self):
        name = get_name(self.conf)
        return name

    @property
    def routes(self):
        routes = get_routes(self.conf)
        return routes


# Instance of config object
config = Config()
