import io
import os
import sys
import unittest
import unittest.mock

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bac_calc import bac_calc

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class BACCalculatorIntegrationTest(unittest.TestCase):
    """Tests that the 'main' function works as expected"""

    @unittest.mock.patch("builtins.input")
    def test_over_the_limit(self, mock_inputs):
        mock_inputs.side_effect = ["M", "180", "10", "wine", "0"]

        expected_result = (
            "Your BAC is 0.13.\n" +
            "It is illegal for you to drive."
        )

        with captured_output() as (outputs, errors):
            bac_calc.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)

    @unittest.mock.patch("builtins.input")
    def test_under_the_limit(self, mock_inputs):
        mock_inputs.side_effect = ["M", "180", "5", "wine", "0"]

        expected_result = (
            "Your BAC is 0.06.\n" +
            "It is legal for you to drive."
        )

        with captured_output() as (outputs, errors):
            bac_calc.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)
