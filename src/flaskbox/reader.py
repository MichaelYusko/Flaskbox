"""Reader stuff"""
import yaml


class ApplicationReader:
    def __init__(self):
        self.app_yml = 'flaskbox.yml'
        self.blueprints = []

    def _read(self):
        with open(self.app_yml, 'r') as config:
            yml = yaml.load(config)
            name = yml['application']['name']
        return name
