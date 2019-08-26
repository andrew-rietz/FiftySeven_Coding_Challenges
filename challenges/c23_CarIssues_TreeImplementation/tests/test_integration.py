import unittest
import unittest.mock
import io
import sys
import os

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from compare_numbers import compare_numbers

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class CarIssueTests(unittest.TestCase):
    """Tests that the 'main' function works as expected"""

    @unittest.mock.patch("builtins.input")
    def test_8_is_max(self, mock_inputs):
        # Note, need to include the exit case "" in order to exit input loop
        mock_inputs.side_effect = ["3", "-100", "5.432", "8", ""]

        expected_result = (
            "The largest number is 8.0."
        )

        with captured_output() as (outputs, errors):
            compare_numbers.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)

    @unittest.mock.patch("builtins.input")
    def test_exit_case(self, mock_inputs):
        mock_inputs.side_effect = [""]

        expected_result = (
            "Sorry, you must provide at least one number."
        )

        with captured_output() as (outputs, errors):
            compare_numbers.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)

if __name__ == "__main__":
    unittest.main()
