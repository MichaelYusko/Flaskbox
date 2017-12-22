"""Reader stuff"""
import yaml


class ApplicationReader:
    """
    Helper class for yml read/write actions.
    """
    def __init__(self):
        self.app_yml = 'flaskbox.yml'
        self.blueprints = []

    def _read(self):
        """Read the yml file
        :return: The yml file in dictionary representation
        """
        try:
            with open(self.app_yml, 'r') as config:
                yml = yaml.load(config)
            return yml
        except FileNotFoundError:
            return None

    @property
    def name(self):
        """Get name of application name
        :return: An name of application
        """
        name = 'Flaskbox API'
        if self._read() is None:
            return name
        else:
            return self._read()
