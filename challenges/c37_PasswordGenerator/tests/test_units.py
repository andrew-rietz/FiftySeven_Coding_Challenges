import io
import os
import sys
import unittest
import unittest.mock

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from password_generator.password_generator import (
    PasswordGenerator, get_pw_length, get_n_special, get_n_numeric
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

class PasswordGeneratorTests(unittest.TestCase):
    """Tests the PasswordGenerator class"""

    def setUp(self):
        self.pw = PasswordGenerator()
        self.pw.length = 12
        self.pw.n_special = 3
        self.pw.n_numeric = 3

    def test__pw_length_is_12(self):
        with captured_output():
            result = self.pw.generate()
        self.assertEqual(12, len(result))

    def test__n_special_chars_is_3(self):
        possible_values = self.pw.special_chars
        result = self.pw.generate()
        count_special = len([char for char in result if char in possible_values])
        self.assertEqual(3, count_special)

    def test__n_numbers_is_3(self):
        possible_values = self.pw.numeric_chars
        result = self.pw.generate()
        count_numeric = len([char for char in result if char in possible_values])
        self.assertEqual(3, count_numeric)

    def test__n_letters_is_6(self):
        possible_values = self.pw.alpha_chars
        result = self.pw.generate()
        count_letters = len([char for char in result if char in possible_values])
        self.assertEqual(6, count_letters)

class UserInputsTests(unittest.TestCase):
    """Tests the user input functions"""

    @unittest.mock.patch("builtins.input")
    def test__length_is_12(self, mocked_inputs):
        mocked_inputs.side_effect = ["Foo", "-10", "12"]
        with captured_output():
            result = get_pw_length()
        self.assertEqual(12, result)

    @unittest.mock.patch("builtins.input")
    def test__n_special_is_4(self, mocked_inputs):
        mocked_inputs.side_effect = ["Foo", "20", "-3", "4"]
        with captured_output():
            result = int(get_n_special(8))
        self.assertEqual(4, result)

    @unittest.mock.patch("builtins.input")
    def test__n_numeric_is_2(self, mocked_inputs):
        mocked_inputs.side_effect = ["Foo", "16", "-3", "2"]
        with captured_output():
            result = int(get_n_numeric(8))
        self.assertEqual(2, result)


if __name__ == "__main__":
    unittest.main(verbosity=3)
