import io
import os
import sys
import unittest
import unittest.mock

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from simple_math import simple_math

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class SimpleMathIntegrationTest(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def test_output(self, mock_inputs):
        mock_inputs.side_effect = ["10", "5"]
        expected_result = (
            f"10.0 + 5.0 = 15.0\n" +
            f"10.0 - 5.0 = 5.0\n" +
            f"10.0 * 5.0 = 50.0\n" +
            f"10.0 / 5.0 = 2.0"
        )

        with captured_output() as (outputs, errors):
            simple_math.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)

if __name__ == "__main__":
    unittest.main()
