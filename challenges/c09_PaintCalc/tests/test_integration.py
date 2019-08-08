import io
import os
import sys
import unittest
import unittest.mock

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from paint_calc import paint_calc

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class PaintCalcIntegrationTest(unittest.TestCase):

    @unittest.mock.patch("builtins.input", lambda *args: "600")
    def test_output(self):
        expected_result = (
            "You will need to purchase 2 gallons of paint to cover the 600 square feet.")

        with captured_output() as (outputs, errors):
            paint_calc.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)

if __name__ == "__main__":
    unittest.main()
