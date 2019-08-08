import io
import os
import sys
import unittest
import unittest.mock

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from count_characters import count_characters

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class IntegrationTests(unittest.TestCase):

    @unittest.mock.patch("builtins.input", lambda *args: "hello")
    def test_main_valid(self):
        expected_result = "hello has 5 characters"

        with captured_output() as (outputs, errors):
            count_characters.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(test_val, expected_result)

    @unittest.mock.patch("builtins.input", lambda *args: "abc 123")
    def test_main_invalid(self):
        expected_result = "abc 123 has 7 characters"

        with captured_output() as (outputs, errors):
            count_characters.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(test_val, expected_result)

if __name__ == "__main__":
    unittest.main()
