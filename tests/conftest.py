import yaml


def create_init_file():
    """Create Init file"""
    base_app = {'application': 'My restful API'}
    with open('flaskbox.yml', 'w') as file:
        yaml.dump(base_app, file, default_flow_style=False)
