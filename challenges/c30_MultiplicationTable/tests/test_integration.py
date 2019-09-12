import unittest
import unittest.mock
import io
import sys
import os

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from multiplication_table import multiplication_table

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class MultiplicationTableTests(unittest.TestCase):
    """Tests that the 'main' function works as expected"""

    def test_sum_is_(self):
        expected_result = [
            "12 x 9 = 108",
            "12 x 10 = 120",
            "12 x 11 = 132",
            "12 x 12 = 144"
        ]
        with captured_output() as (outputs, errors):
            multiplication_table.main()
            intermediate = outputs.getvalue().strip()
            split = intermediate.split("\n")
            test_val = split[-4:]

        self.assertEqual(expected_result, test_val)


if __name__ == "__main__":
    unittest.main()
