import unittest
import unittest.mock
import io
import sys
import os

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from guess_the_number import guess_the_number

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class GuessTheNumberTests(unittest.TestCase):
    """Tests that the 'main' function works as expected"""

    @unittest.mock.patch("builtins.input")
    def test__main(self, mock_inputs):
        mock_inputs.side_effect = [
            "1", # difficulty
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", # guesses
            "No", # don't play again
        ]
        expected_result = "You got it"
        with captured_output() as (outputs, _):
            guess_the_number.main()
            test_val = outputs.getvalue().strip()

        self.assertTrue(expected_result in test_val)

    @unittest.mock.patch("builtins.input")
    def test__goodbye_is_last(self, mock_inputs):
        mock_inputs.side_effect = [
            "1", # difficulty
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", # guesses
            "No", # don't play again
        ]
        expected_result = "Goodbye!"
        with captured_output() as (outputs, _):
            guess_the_number.main()
        test_val = outputs.getvalue().strip().split(" ")[-1]
        self.assertEqual(expected_result, test_val)

if __name__ == "__main__":
    unittest.main()
