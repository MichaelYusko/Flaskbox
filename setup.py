import flaskbox
from setuptools import setup

VERSION = flaskbox.__version__
AUTHOR = flaskbox.__author__


setup_information = {
    'name': 'flaskbox',
    'author': AUTHOR,
    'version': VERSION,
    'url': 'https://github.com/MichaelYusko/Flaskbox',
    'author_email': 'freshjelly12@yahoo.com',
    'description': 'Easy and fast tool for mock an API, with a fake data',
    'packages': ['flaskbox'],
    'classifiers': [
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License'
    ]
}

requirements = [
    'flask==0.12.2',
    'click==6.7',
    'Faker==0.8.8',
    'pyaml==17.10.0'
]

setup_information['install_requires'] = requirements
setup(**setup_information)
