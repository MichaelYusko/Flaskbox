from faker import Faker


class FakeDate:
    """Class for generating an fake data
    """
    def __init__(self):
        self.fake_data = Faker()
