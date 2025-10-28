import unittest
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_add(self):
        self.assertEqual(self.calc.add(2, 2), 4)
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 2), 0)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)
    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 2), 1)
    def test_divide_byzero(self):
        self.assertEqual(self.calc.divide(2, 0), None)
if __name__ == "__main__":
    unittest.main()