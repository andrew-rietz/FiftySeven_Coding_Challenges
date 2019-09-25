import io
import os
import sys
import unittest
import unittest.mock

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from filtering_values.filtering_values import filter_even_numbers

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class FilterEvenNumbersTests(unittest.TestCase):
    """Tests the filter_even_numbers function"""

    def test__even_numbers_match(self):
        input_string = "  1 2 3  4 5   6 7 8   "
        result = filter_even_numbers(input_string)
        expected_result = ["2", "4", "6", "8"]
        self.assertEqual(expected_result, result["even_numbers"])

    def test__removed_values_match(self):
        input_string = "1 2 3 4 5 6 7 8"
        result = filter_even_numbers(input_string)
        expected_result = ["1", "3", "5", "7"]
        self.assertEqual(expected_result, result["removed_values"])


if __name__ == "__main__":
    unittest.main(verbosity=3)
