from flaskbox.helpers import create_init_file


def test_init_file(tmpdir):
    """Check if flaskbox.yml file is created correct
    """
    file = tmpdir.join('flaskbox.yml')
    create_init_file()
    assert file
