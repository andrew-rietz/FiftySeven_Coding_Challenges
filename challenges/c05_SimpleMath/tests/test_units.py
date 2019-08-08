import os
import sys
import unittest
import unittest.mock

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from simple_math import simple_math

class MathTests(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def setUp(self, mock_inputs):
        mock_inputs.side_effect = ["10", "5"]
        self.calc = simple_math.Calculator()

    def test_first_num(self):
        self.assertEqual(self.calc.first_num, 10.0)

    def test_second_num(self):
        self.assertEqual(self.calc.second_num, 5.0)

    def test_sum(self):
        self.assertEqual(self.calc.sum(), 15.0)

    def test_difference(self):
        self.assertEqual(self.calc.difference(), 5.0)

    def test_product(self):
        self.assertEqual(self.calc.product(), 50.0)

    def test_quotient(self):
        self.assertEqual(self.calc.quotient(), 2.0)

if __name__ == "__main__":
    unittest.main()
