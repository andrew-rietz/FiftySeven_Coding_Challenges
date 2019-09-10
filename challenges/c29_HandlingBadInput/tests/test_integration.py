import unittest
import unittest.mock
import io
import sys
import os

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from handling_bad_input import handling_bad_input

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class HandlingBadInputTests(unittest.TestCase):
    """Tests that the 'main' function works as expected"""

    @unittest.mock.patch("builtins.input")
    def test_sum_is_(self, mock_inputs):
        mock_inputs.side_effect = ["0", "ABC", "4"]

        expected_result = (
            "It will take 18.0 years to double your initial investment."
        )

        with captured_output() as (outputs, errors):
            handling_bad_input.main()
            test_val = outputs.getvalue().strip().split("\n")[-1]

        self.assertEqual(expected_result, test_val)


if __name__ == "__main__":
    unittest.main()
