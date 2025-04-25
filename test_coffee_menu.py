import unittest
from coffee_menu import *

class TestCoffeeMenu(unittest.TestCase):
    def setUp(self):
        self.menu = CoffeeMenu()
    def tearDown(self):
        self.menu = None
    def test_get_price_existing_item(self):
        self.assertEqual(self.menu.get_price('latte'),2.75)
    def test_get_price_non_existing_item(self):
        self.assertIsNone(self.menu.get_price('none'))
    def test_add_item(self):
        self.menu.add_item('coffee',2.00)
        self.assertEqual(self.menu.get_price('coffee'),2.00)
if __name__ == '__main__':
    unittest.main()
