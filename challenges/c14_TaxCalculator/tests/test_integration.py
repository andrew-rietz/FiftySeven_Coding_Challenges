import io
import os
import sys
import unittest
import unittest.mock

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tax_calculator import tax_calculator

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class TaxCalculatorIntegrationTest(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def test_WI_output(self, mock_inputs):
        mock_inputs.side_effect = ["10", "WI"]

        expected_result = (
            f"The subtotal is $10.00.\n" +
            f"The tax is $0.55.\n" +
            f"The total is $10.55."
        )

        with captured_output() as (outputs, errors):
            tax_calculator.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)

    @unittest.mock.patch("builtins.input")
    def test_MN_output(self, mock_inputs):
        mock_inputs.side_effect = ["10", "MN"]

        expected_result = (
            f"The total is $10.00."
        )

        with captured_output() as (outputs, errors):
            tax_calculator.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)

if __name__ == "__main__":
    unittest.main()
