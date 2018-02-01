from flaskbox.reader import YAMLBaseReader


class Config(YAMLBaseReader):
    """Config class, which providing information from yaml file

        Methods::
            _get_config Read an flaskbox yaml file, and return
                        a dict object with information

        Properties::
            name Return an name of application, based on flaskbox yaml file
            routes Return an array, with routes objects
            value_type Return an array with fields objects, not completed yet
    """

    def _get_config(self):
        """
        :return: Read a flaskbox.yml file
        """
        return super().read()

    @property
    def name(self):
        """
        :return: Return an name of application
        """
        name = self.get_name(self._get_config())
        return name

    @property
    def port(self):
        port = self.get_port(self._get_config())
        return port

    @property
    def routes(self):
        """
        :return: Return an array with route objects
        """
        routes = self.get_routes(self._get_config())
        return routes

    @property
    def value_type(self):
        """
        :return: Return an array with fields objects, not completed yet
        """
        value_type = self.get_fields(self._get_config())
        return value_type


class RouteConfig(Config):
    pass


# Instance of config object
config = Config()
