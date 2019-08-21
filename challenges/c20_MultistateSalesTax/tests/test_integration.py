import unittest
import unittest.mock
import io
import sys
import os

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from multistate_tax import multistate_tax

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class MultiStateSalesTax(unittest.TestCase):
    """Tests that the 'main' function works as expected"""

    @unittest.mock.patch("builtins.input")
    def test_state_and_county_with_taxes(self, mock_inputs):
        mock_inputs.side_effect = ["100", "WI", "Dunn"]

        expected_result = (
            "The tax is $5.40.\n" +
            "The total is $105.40."
        )

        with captured_output() as (outputs, errors):
            multistate_tax.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)

    @unittest.mock.patch("builtins.input")
    def test_state_with_taxes(self, mock_inputs):
        mock_inputs.side_effect = ["100", "IL", "some_fake_county"]

        expected_result = (
            "The tax is $8.00.\n" +
            "The total is $108.00."
        )

        with captured_output() as (outputs, errors):
            multistate_tax.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)

    @unittest.mock.patch("builtins.input")
    def test_no_taxes(self, mock_inputs):
        mock_inputs.side_effect = ["100", "CA", "some_fake_county"]

        expected_result = (
            "The total is $100.00."
        )

        with captured_output() as (outputs, errors):
            multistate_tax.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)

if __name__ == "__main__":
    unittest.main()
