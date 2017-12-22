from flaskbox.helpers import create_init_file


def test_init_file(tmpdir):
    """Test init file"""
    file = tmpdir.join('flaskbox.yml')
    create_init_file()
    assert file
