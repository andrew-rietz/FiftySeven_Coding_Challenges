import unittest
import unittest.mock
import io
import sys
import os

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from adding_numbers import adding_numbers

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class AddingNumbersTests(unittest.TestCase):
    """Tests that the 'main' function works as expected"""

    @unittest.mock.patch("builtins.input")
    def test_sum_is_86_6(self, mock_inputs):
        mock_inputs.side_effect = ["3", "-100", "5.432", "8"]

        expected_result = (
            "The total is -86.6."
        )

        with captured_output() as (outputs, errors):
            adding_numbers.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)


if __name__ == "__main__":
    unittest.main()
