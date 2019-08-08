import io
import os
import sys
import unittest
import unittest.mock

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from self_checkout import self_checkout

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class SelfCheckoutIntegrationTest(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def test_output(self, mock_inputs):
        mock_inputs.side_effect = ["25", "2", "10", "1", False]

        expected_result = (
            "Subtotal: $60.00\n" +
            "Tax: $3.30\n" +
            "Total: $63.30"
        )

        with captured_output() as (outputs, errors):
            self_checkout.main()
            test_val = outputs.getvalue().strip()
            test_val = "Subtotal" + test_val.split("Subtotal",1)[1]

        self.assertEqual(expected_result, test_val)

if __name__ == "__main__":
    unittest.main()
