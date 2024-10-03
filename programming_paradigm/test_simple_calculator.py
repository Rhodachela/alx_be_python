import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(3, 79), 82)
        self.assertEqual(self.calc.add(797, 41), 838)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(51, 9), 42)
        self.assertEqual(self.calc.subtract(24, 7), 17)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(50, 5), 250)
        self.assertEqual(self.calc.multiply(75, 4), 300)
    def test_divide_valid(self):
        self.assertEqual(self.calc.divide(50, 2), 25)
        self.assertEqual(self.calc.divide(90, 5), 18)
    def test_divide_by_zero(self):
        self.assertEqual(self.calc.divide(28, 0), "Invalid")

if __name__ == "__main__":
    unittest.main()



