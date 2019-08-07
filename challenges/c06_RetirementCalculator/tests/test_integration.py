import unittest
import unittest.mock
import io
from datetime import datetime
from contextlib import redirect_stdout

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

class RetirementCalcIntegrationTest(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def test_output(self, mock_inputs):
        mock_inputs.side_effect = ["30", "65"]
        current_year = datetime.date(datetime.today()).year
        years_left = 65-30

        expected_result = (
            f"You have {years_left} years left until you can retire.\n" +
            f"It's {current_year}, so you can retire in {current_year + years_left}."
        )
        print_output = io.StringIO()
        with redirect_stdout(print_output):
            retirement_calculator.main()
            test_val = print_output.getvalue().strip()

        self.assertEqual(expected_result, test_val)

if __name__ == "__main__":
    unittest.main()
