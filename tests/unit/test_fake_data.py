from flaskbox.fake_data import fake_data


def test_fake_data(base_fields):
    data = fake_data.generate_value(base_fields)
    assert len(data) == 4


def test_if_correct_values(base_fields):
    data = fake_data.generate_value(base_fields)
    name = data[0]['name']
    last_name = data[1]['last_name']
    users = data[2]['users']
    ids = data[3]['ids']
    collect_data = (isinstance(name, str), isinstance(last_name, str), len(users), len(ids))
    assert collect_data == (True, True, 8, 8)
