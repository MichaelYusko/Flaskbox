from flaskbox.fake_data import fake_data


def test_fake_data(base_fields):
    data = fake_data.generate_value(base_fields)
    assert len(data) == 4
