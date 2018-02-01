from faker import Faker


class FakeDate:
    """Class for generating an fake data"""
    def __init__(self):
        self.faker = Faker()

    # default data type values
    _default_types = (
        'string', 'array', 'integer', 'boolean',
        'float'
    )

    def _set_value(self, field, key):
        """
        :param field: An dict object with field information
        :param key: An key, of object
        :return: An object with a fake data, based on value

            Example:
                input: {'name': 'string'}
                output: {'name': 'Lionel Messi'}
        """
        # TODO add array/boolean/float data types.
        if field[key] == 'string':
            field[key] = self.faker.name()
        if field[key] == 'integer':
            field[key] = self.faker.random_number()
        return field

    def generate_value(self, fields):
        """
        :param fields: An array with fields objects
        :return An array with dict objects

            Example:
                input: [{'string': name}, {'last_name': string}]
                output: [{'name': 'Freddie Mercury'}, {'last_name': '30 Seconds To Mars'}]
        """
        for field in fields:
            for key in list(field.keys()):
                if field[key] not in self._default_types:
                    raise ValueError(
                        f'The {key} data type not supported, '
                        f'check your flaskbox.yml file'
                    )
                self._set_value(field, key)
        return fields


# instance of FakeData class
fake_data = FakeDate()
