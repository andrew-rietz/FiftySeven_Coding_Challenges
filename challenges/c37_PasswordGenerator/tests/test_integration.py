import unittest
import unittest.mock
import io
import sys
import os
import random

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from password_generator import password_generator

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class PasswordGeneratorTests(unittest.TestCase):
    """Tests that the 'main' function works as expected"""

    @unittest.mock.patch("builtins.input")
    def test__main(self, mock_inputs):
        random.seed(0)
        mock_inputs.side_effect = ["12", "3", "3"]
        with captured_output() as (outputs, _):
            password_generator.main()
            password = outputs.getvalue().strip().split("\n")[-1]
        self.assertEqual("5/]AVp_4OEy2", password)


if __name__ == "__main__":
    unittest.main()
