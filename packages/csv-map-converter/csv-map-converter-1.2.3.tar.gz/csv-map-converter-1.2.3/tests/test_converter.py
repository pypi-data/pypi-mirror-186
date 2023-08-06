import unittest, sys, os

sys.path.insert(0, os.path.abspath('.'))

import csv_map_converter


class TestConverter(unittest.TestCase):

    EMAIL = 'email'

    def setUp(self):
        self.csv_lines = [
            ['enabled', 'title', self.EMAIL, '', '', 'label', '', '', ''],
            ['using if value is 1', '', '', '', '', '', '', '', ''],
            ['1', 'task1', 'a123@emailtest.com', 'b123@emailtest.com', 'c123@emailtest.com', '2016','2017', '2018'],
            ['0', 'task2', 'a123@test.com', 'b123@test.com', 'c123@test.com', '2016', '', ''],
            ['1', 'task3', 'a123@test.com', '', '', '', '', '']
        ]

        self.start_data_row = 2
        self.title_row = 0

    def __get_titles(self):
        titles = self.csv_lines[self.title_row]
        return list(filter(lambda title: title, titles))

    def __get_current_row_data(self, index):
        current_index = index + self.start_data_row
        return self.csv_lines[current_index: current_index + 1][0]

    def __get_emails_by_index(self, index, csv_map_result):
        row_data = self.__get_current_row_data(index)
        indexes = csv_map_result.get_indexes_by_title(self.EMAIL)

        return list(filter(lambda val: val, [row_data[index] for index in indexes]))

    def test_convert_list_field(self):
        convert_result = csv_map_converter.convert(self.csv_lines, start_row = self.start_data_row)
        csv_map_result = convert_result.map_result
        data = csv_map_result.get_content()

        for index, row in enumerate(data):
            convert_emails = row.get(self.EMAIL)
            emails = self.__get_emails_by_index(index, csv_map_result)
            for email in emails: self.assertTrue(email in convert_emails)

    def test_parse_content(self):
        start_data_row = self.start_data_row
        convert_result = csv_map_converter.convert(self.csv_lines, start_row = start_data_row)
        csv_map_result = convert_result.map_result
        data = csv_map_result.get_content()
        self.assertEqual(len(self.csv_lines[start_data_row:]), len(data))

    def test_parse_titles(self):
        convert_result = csv_map_converter.convert(self.csv_lines, start_row = self.start_data_row)
        csv_map_result = convert_result.map_result
        self.assertEqual(csv_map_result.get_titles(), self.__get_titles())

if __name__ == '__main__':
    unittest.main()

