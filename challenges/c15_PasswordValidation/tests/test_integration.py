import io
import os
import sys
import unittest
import unittest.mock

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from password_validation import password_validation

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class PasswordValidatorIntegrationTest(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def test_good_pw(self, mock_inputs):
        mock_inputs.side_effect = ["abc$123"]

        expected_result = (
            f"Welcome!"
        )

        with captured_output() as (outputs, errors):
            password_validation.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)

    @unittest.mock.patch("builtins.input")
    def test_bad_pw(self, mock_inputs):
        mock_inputs.side_effect = ["wrong_pw"]

        expected_result = (
            f"I don't know you."
        )

        with captured_output() as (outputs, errors):
            password_validation.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)

if __name__ == "__main__":
    unittest.main()
