import unittest
import math

def get_sqrt(n):
  return math.sqrt(n)

def divide(a, b):
  return a / b

class TestUnexpected(unittest.TestCase):
  def test_get_sqrt(self):
    self.assertEqual(get_sqrt(144),12)
    with self.assertRaises(ValueError):
      self.assertEqual(get_sqrt(-144),12)
  def test_divide(self):
    self.assertEqual(divide(144,12),12)
    with self.assertRaises(ZeroDivisionError):
      self.assertEqual(divide(144, 0), 999)
if __name__=='__main__':
    unittest.main()