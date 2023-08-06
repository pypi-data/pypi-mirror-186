import unittest, sys, os

sys.path.insert(0, os.path.abspath('.'))

import csv_map_converter
from csv_map_converter.models.fields import *

class Product(object):

    enabled = BooleanField()
    name    = StringField()
    price   = IntField()
    labels  = ListField(StringField())
    label  = ListField(StringField(), name = 'labels')
    location = StringField(default = "taipei")


class TestConverterModel(unittest.TestCase):


    def setUp(self):
        self.csv_lines = [
            ['enabled', 'name', 'price', 'labels', '', '', '', 'location'],
            ['1', 'office', '4000', '2017', 'mircrosoft', '', '', 'kaohsiung'],
            ['0', 'dreamweaver', '8000', '2008', 'adobe', 'web', 'browser', ''],
        ]
        self.expected_rows = [
            dict(enabled = True, name = 'office', price = 4000, labels = ['2017', 'mircrosoft'], location = 'kaohsiung'),
            dict(enabled = False, name = 'dreamweaver', price = 8000, labels = ['2008', 'adobe', 'web', 'browser'], location = 'taipei'),
        ]

    def test_convert_model(self):
        convert_result = csv_map_converter.convert(self.csv_lines, Product)
        titles = convert_result.map_result.get_titles()

        for index, model in enumerate(convert_result.models):
            expected_row = self.expected_rows[index]
            for title in titles:
                field_value = getattr(model, title)
                expected = expected_row.get(title)
                self.assertEqual(field_value, expected)
                if isinstance(expected, list):
                    self.assertEqual(field_value, expected)

    def test_convert_model_by_name_attr(self):
        csv_lines = list(self.csv_lines)
        #csv_lines[0][3] = 'label'
        convert_result = csv_map_converter.convert(csv_lines, Product)

        for index, model in enumerate(convert_result.models):
            expected_row = self.expected_rows[index]
            expected = expected_row.get('labels')
            self.assertEqual(model.label, expected)

if __name__ == '__main__':
    unittest.main()
