from string_utils import *
import unittest

class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string('mochi'), 'ihcom')
    def test_capitalize_string(self):
        self.assertEqual(capitalize_string('somesh'), 'Somesh')
    def test_is_capitalized(self):
        self.assertTrue(is_capitalized('Somesh'))

if __name__ == '__main__':
    unittest.main()

