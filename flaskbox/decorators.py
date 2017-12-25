"""Decorators stuff"""
import os
import sys

from flaskbox.colors import ccolors

file_exists_message = ccolors.OK_GREEN.value + 'flaskbox.yml' \
                      + ccolors.ENDC.value + ' already exists'


def if_file_exists(func):
    """Check if file exists"""
    def file_exists(*args, **kwargs):
        """
        If flaskbox.yml file exists
        Print message and exit from the program.
        """
        if os.path.isfile('flaskbox.yml'):
            print(file_exists_message)
            sys.exit(1)
        return func(*args, **kwargs)
    return file_exists
