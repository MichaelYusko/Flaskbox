"""Helpers method for ApplicationReaer"""

import yaml


def read_file():
    """Read the yaml file"""
    with open('flaskbox.yml', 'r') as file:
        file = yaml.load(file)
    return file
