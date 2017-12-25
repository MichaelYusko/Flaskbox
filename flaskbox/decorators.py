"""Decorators stuff"""
import os
import sys

from flaskbox.messages import file_exists_message, not_exists_message


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


def file_not_exists(func):
    """File not exists"""
    def not_exists(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except FileNotFoundError:
            print(not_exists_message)
            sys.exit(1)
    return not_exists
