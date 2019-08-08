import io
import os
import sys
import unittest
import unittest.mock

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from hello_world import hello_world

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

    @unittest.mock.patch("builtins.input", lambda *args: "andrew")
    def test_main_valid(self):
        expected_result = "Hello, Andrew, nice to meet you!"
        print_output = io.StringIO()

        with captured_output() as (outputs, errors):
            hello_world.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(test_val, expected_result)

if __name__ == "__main__":
    unittest.main()
