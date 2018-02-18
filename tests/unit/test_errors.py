import pytest

from flaskbox.fake_data import fake_data


def test_generate_value_error():
    with pytest.raises(TypeError):
        fake_data.generate_value([{'key': 'bad type'}])
