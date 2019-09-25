import unittest
import unittest.mock
import io
import sys
import os

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from filtering_values import filtering_values

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class FilteringValuesTests(unittest.TestCase):
    """Tests that the 'main' function works as expected"""

    @unittest.mock.patch("builtins.input")
    def test__main(self, mock_inputs):
        mock_inputs.side_effect = ["1 2 3 4 5 6 7 8"]
        with captured_output() as (outputs, _):
            filtering_values.main()
        test_val = outputs.getvalue().strip()
        expected_result = "The even numbers are 2, 4, 6, 8."
        self.assertTrue(expected_result in test_val)


if __name__ == "__main__":
    unittest.main()
