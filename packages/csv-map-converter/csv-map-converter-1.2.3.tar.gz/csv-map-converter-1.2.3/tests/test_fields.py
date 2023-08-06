import unittest, sys, os

sys.path.insert(0, os.path.abspath('.'))

from csv_map_converter.models.fields.base import *

class TestField(unittest.TestCase):

    def __get_long_type(self):
 
        if sys.version_info.major > 2:
            number = int
        else:
            number = long

        return number

    def test_boolean_field(self):
        boolean_field = BooleanField()
        self.assertTrue(boolean_field.to_python('1'))
        self.assertTrue(boolean_field.to_python('True'))
        self.assertTrue(boolean_field.to_python('true'))
        self.assertFalse(boolean_field.to_python('0'))
        self.assertFalse(boolean_field.to_python('False'))
        self.assertFalse(boolean_field.to_python('false'))
        self.assertFalse(boolean_field.to_python(None))

    def test_long_field(self):
        long_field = LongField()
        number = self.__get_long_type()

        self.assertEqual(long_field.to_python('1'), number(1))
        self.assertEqual(long_field.to_python('0'), number(0))
        self.assertEqual(long_field.to_python('-1'), number(-1))

    def test_int_field(self):
        int_field = IntField()
        self.assertEqual(int_field.to_python('1'), int(1))
        self.assertEqual(int_field.to_python('0'), int(0))
        self.assertEqual(int_field.to_python('-1'), int(-1))

    def test_float_field(self):
        float_field = FloatField()
        self.assertEqual(float_field.to_python('1'), float(1))
        self.assertEqual(float_field.to_python('1.1231'), float(1.1231))
        self.assertEqual(float_field.to_python('0'), float(0))
        self.assertEqual(float_field.to_python('-1'), float(-1))
        self.assertEqual(float_field.to_python('-1.1'), float(-1.1))

    def test_string_field(self):
        string_field = StringField()
        texts = ['str1', 'str2', 'str3', '1', '0']
        for text in texts:
            self.assertEqual(string_field.to_python(text), text)

    def test_list_field(self):
        list_field = ListField()
        expected_vals = [1, 2, 3.2, 'test']
        values = list_field.to_python(expected_vals)

        for index, expected_val in enumerate(expected_vals):
            self.assertEqual(values[index], expected_val)

    def test_boolean_list_field(self):
        list_field = ListField(BooleanField())
        input_vals = ['1', '2', '3.2', 'test', '0', 'false']
        expected_vals = [True, True, True, True, False, False]
        values = list_field.to_python(input_vals)

        for index, value in enumerate(values):
            self.assertEqual(value, expected_vals[index])
            self.assertTrue(isinstance(value, bool))

    def test_int_list_field(self):
        list_field = ListField(IntField())
        input_vals = ['1', '2', '3', '0', '-1' , '-32']
        expected_vals = [1, 2, 3, 0, -1, -32]
        values = list_field.to_python(input_vals)
        
        for index, value in enumerate(values):
            self.assertEqual(value, expected_vals[index])
            self.assertTrue(isinstance(value, int))

    def test_long_list_field(self):
        list_field = ListField(LongField())
        number = self.__get_long_type()
        input_vals = ['1', '2', '3', '0', '-1' , '-32']
        expected_vals = [1, 2, 3, 0, -1, -32]
        values = list_field.to_python(input_vals)
        
        for index, value in enumerate(values):
            self.assertEqual(value, expected_vals[index])
            self.assertTrue(isinstance(value, number))
 
    def test_string_list_field(self):
        list_field = ListField(StringField())
        input_vals = ['test1', 'test2', '']
        expected_vals = input_vals
        values = list_field.to_python(input_vals)
        
        for index, value in enumerate(values):
            self.assertEqual(value, expected_vals[index])
            self.assertTrue(isinstance(value, str))
 

if __name__ == '__main__':
    unittest.main()

