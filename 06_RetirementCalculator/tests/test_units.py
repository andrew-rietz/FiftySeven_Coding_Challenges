import unittest
import unittest.mock
from datetime import datetime

from tests.context import retirement_calculator

class RetirementCalcUnitTests(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def setUp(self, mock_inputs):
        mock_inputs.side_effect = ["30", "65"]
        self.retire_calc = retirement_calculator.Calculator()

    def test_age(self):
        self.assertEqual(30, self.retire_calc.age)

    def test_year(self):
        self.assertEqual(datetime.date(datetime.today()).year, self.retire_calc.year)


if __name__ == "__main__":
    unittest.main()
