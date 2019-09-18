import io
import os
import sys
import unittest
import unittest.mock

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from guess_the_number.guess_the_number import (
    GuessingGame, get_string_in_list_track_responses, startup, gameover
)

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class StartUpTest(unittest.TestCase):
    """Tests the startup function"""

    @unittest.mock.patch("builtins.input")
    def test__difficulty_is_2(self, mock_inputs):
        mock_inputs.side_effect = ["Foo", "Bar", "2"]
        with captured_output():
            difficulty = startup()
        self.assertEqual('2', difficulty)

    @unittest.mock.patch("builtins.input")
    def test__gameover_yes_is_true(self, mock_inputs):
        mock_inputs.side_effect = ["Foo", "Bar", "yes"]
        with captured_output() as (outputs, _):
            replay = gameover(4)
        msg = outputs.getvalue().strip().split("\n")[0]
        self.assertTrue((replay == True) and (msg == "You got it in 4 guesses!"))

    @unittest.mock.patch("builtins.input")
    def test__gameover_no_is_false(self, mock_inputs):
        mock_inputs.side_effect = ["Foo", "Bar", "no"]
        with captured_output() as (outputs, _):
            replay = gameover(4)
        msg = outputs.getvalue().strip().split("\n")[0]
        self.assertTrue((replay == False) and (msg == "You got it in 4 guesses!"))

class GetStringInListTrackResponsesTests(unittest.TestCase):
    """Tests the function that prompts the user for a response from a list of values"""

    def setUp(self):
        stdout_trap = io.StringIO()
        sys.stdout = stdout_trap

    @unittest.mock.patch("builtins.input")
    def test_case_senstive(self, mock_inputs):
        mock_inputs.side_effect = ["Foo", "Bar  ", "Baz"]
        named_args = {
            "prompt": "Select a value from the list.",
            "err_msg": "Please enter a valid value.",
            "allowed_vals": ["foo", "Bar", "baz"],
            "case_sensitive": True,
        }
        with captured_output():
            val_n = get_string_in_list_track_responses(**named_args)
            val = val_n["user_val"]
            n = val_n["n_responses"]
        self.assertTrue((val == "Bar") and (n == 2))

    @unittest.mock.patch("builtins.input")
    def test_case_insenstive(self, mock_inputs):
        mock_inputs.side_effect = ["foo", "bar", "baz"]
        named_args = {
            "prompt": "Select a value from the list.",
            "err_msg": "Please enter a valid value.",
            "allowed_vals": ["FOO", "BAR", "BAZ"],
            "case_sensitive": False,
        }
        with captured_output():
            val_n = get_string_in_list_track_responses(**named_args)
            val = val_n["user_val"]
            n = val_n["n_responses"]
        self.assertTrue((val == "foo") and (n == 1))

    @unittest.mock.patch("builtins.input")
    def test_exit(self, mock_inputs):
        mock_inputs.side_effect = ["fo", "ba", "quit()", "baz"]
        named_args = {
            "prompt": "Select a value from the list.",
            "err_msg": "Please enter a valid value.",
            "allowed_vals": ["FOO", "BAR", "BAZ"],
            "case_sensitive": False,
            "exit_val": "quit()"
        }
        with captured_output():
            val_n = get_string_in_list_track_responses(**named_args)
            val = val_n["user_val"]
            n = val_n["n_responses"]
        self.assertTrue((val is None) and (n == 2))

    def tearDown(self):
        sys.stdout = sys.__stdout__

class GuessingGameTests(unittest.TestCase):
    """Tests the GuessingGame class"""

    def setUp(self):
        self.game = GuessingGame()

    def test__set_number_possible_values_1_10(self):
        self.game.difficulty = 1
        self.game.set_number()
        possible_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.assertEqual(self.game.remaining_numbers, possible_numbers)

    def test__set_number_between_1_10(self):
        self.game.difficulty = 1
        self.game.set_number()
        self.assertTrue((self.game.number < 11) and (self.game.number > 0))

    def test__check_guess_is_8(self):
        self.game.set_number()
        self.game.number = 8
        result = self.game.check_guess(8)
        self.assertEqual(result, "Match")

    def test__check_guess_8_not_in_remaining_values(self):
        self.game.set_number()
        self.game.number = 8
        result = self.game.check_guess(8)
        possible_numbers = ["1", "2", "3", "4", "5", "6", "7", "9", "10"]
        self.assertEqual(self.game.remaining_numbers, possible_numbers)

    def test__check_guess_9_is_too_high(self):
        self.game.set_number()
        self.game.number = 8
        result = self.game.check_guess(9)
        self.assertEqual(result, "Too high.")

    def test__check_guess_7_is_too_low(self):
        self.game.set_number()
        self.game.number = 8
        result = self.game.check_guess(7)
        self.assertEqual(result, "Too low.")

    @unittest.mock.patch("builtins.input")
    def test__take_guess_2_is_value(self, mock_inputs):
        self.game.set_number()
        mock_inputs.side_effect = ["foo", "bar", "2"]
        with captured_output():
            result = self.game.take_guess(
                prompt="Enter a number",
                err_msg="Invalid.",
            )
        self.assertEqual(2, result)

    @unittest.mock.patch("builtins.input")
    def test__take_guess_3_is_n_guesses(self, mock_inputs):
        self.game.set_number()
        mock_inputs.side_effect = ["foo", "bar", "2"]
        with captured_output():
            self.game.take_guess(
                prompt="Enter a number",
                err_msg="Invalid.",
            )
        self.assertEqual(3, self.game.n_guesses)


if __name__ == "__main__":
    unittest.main(verbosity=3)
