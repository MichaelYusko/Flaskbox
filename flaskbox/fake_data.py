from faker import Faker


class FakeDate:
    """Class for generating an fake data
    """
    def __init__(self):
        self.fake_data = Faker()

    _default_types = ('string', 'array', 'integer', 'array')

    def generate_value(self, type_value: str):
        """
        :param type_value: An available type, see _default_types tuple
        :return: An data, based on type
        """
        # TODO add support for array/integer types.
        data = None
        if type_value not in self._default_types:
            raise ValueError('The {} type not supported'.format(type))
        if type_value == 'string':
            data = self.fake_data.name()
        return data


# instance of FakeData class
fake_data = FakeDate()
