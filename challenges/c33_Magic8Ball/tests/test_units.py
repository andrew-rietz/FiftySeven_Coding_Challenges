import io
import os
import sys
import unittest
import unittest.mock

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from magic_8_ball.magic_8_ball import MagicEightBall

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
    """Tests the magic_eight_ball class"""

    def setUp(self):
        self.ball = MagicEightBall()

    @unittest.mock.patch("builtins.input")
    def test__response_in_list(self, mocked_inputs):
        mocked_inputs.side_effect = ["Does it work?"]
        possible_values = ["Yes", "No", "Maybe", "Ask again later"]
        with captured_output():
            result = self.ball.answer()

        self.assertTrue(result in possible_values)


if __name__ == "__main__":
    unittest.main(verbosity=3)
