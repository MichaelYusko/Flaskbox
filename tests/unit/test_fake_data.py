import datetime

from flaskbox.fake_data import fake_data


def test_fake_data(base_fields):
    """Test if an array with fake data is return correct
    """
    data = fake_data.generate_value(base_fields)
    assert len(data) == 5


def test_if_correct_values(base_fields):
    """Test if each key has a correct value
    """
    data = fake_data.generate_value(base_fields)
    name = data[0]['name']
    last_name = data[1]['last_name']
    users = data[2]['users']
    ids = data[3]['ids']
    created_at = data[4]['created_at']
    collect_data = (
        isinstance(name, str), isinstance(last_name, str),
        len(users), len(ids),
        isinstance(created_at, datetime.datetime)
    )
    assert collect_data == (True, True, 8, 8, True)
