import unittest
import unittest.mock
import io
from contextlib import redirect_stdout

from tax_calculator import tax_calculator

class TaxCalculatorIntegrationTest(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def test_WI_output(self, mock_inputs):
        mock_inputs.side_effect = ["10", "WI"]

        expected_result = (
            f"The subtotal is $10.00.\n" +
            f"The tax is $0.55.\n" +
            f"The total is $10.55."
        )
        print_output = io.StringIO()
        with redirect_stdout(print_output):
            tax_calculator.main()
            test_val = print_output.getvalue().strip()

        self.assertEqual(expected_result, test_val)

    @unittest.mock.patch("builtins.input")
    def test_MN_output(self, mock_inputs):
        mock_inputs.side_effect = ["10", "MN"]

        expected_result = (
            f"The total is $10.00."
        )
        print_output = io.StringIO()
        with redirect_stdout(print_output):
            tax_calculator.main()
            test_val = print_output.getvalue().strip()

        self.assertEqual(expected_result, test_val)

if __name__ == "__main__":
    unittest.main()
