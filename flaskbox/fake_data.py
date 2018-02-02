import random

from faker import Faker


class FakeDate:
    """Class for generating an fake data"""
    def __init__(self):
        self.faker = Faker()

    # default data type values
    _default_types = (
        'string', 'integer', 'boolean',
        'float', 'array_int', 'array_str'
    )

    def _generate_values(self, data, count=8):
        """
        :param data: An data which need to generate
        :param count: An count of list
        :return: An array with objects
        """
        return [data() for _ in range(count)]

    def _set_value(self, field, key):
        """
        :param field: An dict object with field information
        :param key: An key, of object
        :return: An object with a fake data, based on value

            Example:
                input: {'name': 'string'}
                output: {'name': 'Lionel Messi'}
        """
        if field[key] == 'string':
            field[key] = self.faker.name()

        if field[key] == 'integer':
            field[key] = self.faker.random_number()

        if field[key] == 'float':
            field[key] = random.uniform(1, 100)

        if field[key] == 'array_str':
            field[key] = self._generate_values(self.faker.name)

        if field[key] == 'array_int':
            field[key] = self._generate_values(self.faker.random_number)

        if field[key] == 'boolean':
            field[key] = bool(random.getrandbits(1))

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
                    raise TypeError(
                        f"The data type of '{key}' not supported, "
                        f"check your flaskbox.yml file"
                    )
                self._set_value(field, key)
        return fields


# instance of FakeData class
fake_data = FakeDate()
