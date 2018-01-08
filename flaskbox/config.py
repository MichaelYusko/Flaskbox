from flaskbox.reader import YAMLBaseReader


class Config(YAMLBaseReader):
    """Config class which will collect an mock data"""

    def _get_config(self):
        return super().read()

    @property
    def name(self):
        name = self.get_name(self._get_config())
        return name

    @property
    def routes(self):
        routes = self.get_routes(self._get_config())
        return routes


# Instance of config object
config = Config()
