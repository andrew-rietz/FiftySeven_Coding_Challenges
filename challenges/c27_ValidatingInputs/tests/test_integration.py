import unittest
import unittest.mock
import io
import sys
import os

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from validating_inputs import validating_inputs


@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class InputValidationTests(unittest.TestCase):
    """Tests that the 'main' function works as expected"""

    @unittest.mock.patch("builtins.input")
    def test__valid_inputs(self, mock_inputs):
        mock_inputs.side_effect = ["Jimmy", "James", "55555", "TK-4210"]
        expected_result = (
            "There were no errors found."
        )

        with captured_output() as (outputs, errors):
            validating_inputs.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)

    @unittest.mock.patch("builtins.input")
    def test__valid_inputs(self, mock_inputs):
        mock_inputs.side_effect = ["J", "", "ABCDE", "A12-1234"]
        expected_result = (
            'J is not a valid first name. It is too short.\n' +
            'The last name must be filled in.\n' +
            'The ZIP code must be either a five- or nine-digit number.\n' +
            'A12-1234 is not a valid ID.'
        )

        with captured_output() as (outputs, errors):
            validating_inputs.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)

if __name__ == "__main__":
    unittest.main()
