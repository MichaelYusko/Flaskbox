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
        with open(self.app_yml, 'r') as config:
            yml = yaml.load(config)
        return yml

    @property
    def name(self):
        """Get name of application name
        :return: An name of application
        """
        return self._read()['application']['name']
