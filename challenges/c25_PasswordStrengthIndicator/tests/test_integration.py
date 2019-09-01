import unittest
import unittest.mock
import io
import sys
import os

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from password_strength_indicator import password_strength_indicator

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class CheckPasswordStrength(unittest.TestCase):
    """Tests that the 'main' function works as expected"""

    def test_passwords(self):
        expected_result = (
            "The password 's p a c e s' is an invalid password (includes spaces).\n" +
            "The password '12345' is a very weak password.\n" +
            "The password 'abcdef' is a weak password.\n" +
            "The password 'abc123xyz' is a strong password.\n" +
            "The password '1337h@xor!' is a very strong password."
        )

        with captured_output() as (outputs, errors):
            password_strength_indicator.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)


if __name__ == "__main__":
    unittest.main()
