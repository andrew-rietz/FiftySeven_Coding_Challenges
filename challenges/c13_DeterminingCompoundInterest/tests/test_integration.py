import io
import os
import sys
import unittest
import unittest.mock

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from compound_interest import compound_interest

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class CompoundInterestIntegrationTest(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def test_output(self, mock_inputs):
        mock_inputs.side_effect = ["1500", "4.3", "6", "4"]

        expected_result = (
            f"$1,500.00 invested at 4.30% for " +
            f"6 years compounded 4 times per year is $1,938.84."
        )

        with captured_output() as (outputs, errors):
            compound_interest.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)

if __name__ == "__main__":
    unittest.main()
