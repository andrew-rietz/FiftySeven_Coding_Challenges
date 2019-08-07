import unittest
import unittest.mock
from datetime import datetime

if __name__ == '__main__':
    if __package__ is None:
        import sys
        import os
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from retirement_calculator import retirement_calculator
    else:
        from ..retirement_calculator import retirement_calculator
else:
    from retirement_calculator import retirement_calculator

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
