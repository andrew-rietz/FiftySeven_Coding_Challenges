import unittest
import unittest.mock
import io
import sys
import os

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from magic_8_ball import magic_8_ball

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class MagicEightBallTests(unittest.TestCase):
    """Tests that the 'main' function works as expected"""

    @unittest.mock.patch("builtins.input")
    def test__main(self, mock_inputs):
        possible_values = ["Yes", "No", "Maybe", "Ask again later"]
        mock_inputs.side_effect = ["Did it work?"]
        with captured_output() as (outputs, _):
            magic_8_ball.main()
            test_val = outputs.getvalue().strip()
        self.assertTrue(test_val in possible_values)


if __name__ == "__main__":
    unittest.main()
