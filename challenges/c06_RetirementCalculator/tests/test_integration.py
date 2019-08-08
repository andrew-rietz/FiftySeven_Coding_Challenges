from datetime import datetime
import io
import os
import sys
import unittest
import unittest.mock

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from retirement_calculator import retirement_calculator

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

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

        with captured_output() as (outputs, errors):
            retirement_calculator.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)

if __name__ == "__main__":
    unittest.main()
