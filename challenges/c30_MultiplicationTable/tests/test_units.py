import io
import os
import sys
import unittest
import unittest.mock

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
    """Tests the multiplication_table function"""

    def test__multiplication_table(self):
        with captured_output() as (outputs, errors):
            multiplication_table.multiplication_table(2)

        expected_output = [
            "0 x 0 = 0",
            "0 x 1 = 0",
            "0 x 2 = 0",
            "1 x 0 = 0",
            "1 x 1 = 1",
            "1 x 2 = 2",
            "2 x 0 = 0",
            "2 x 1 = 2",
            "2 x 2 = 4"
        ]
        self.assertEqual("\n".join(expected_output), outputs.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
