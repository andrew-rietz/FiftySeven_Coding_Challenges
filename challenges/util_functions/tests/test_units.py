"""
Unit tests for the utility functions
"""

import io
import os
import sys
import unittest
import unittest.mock

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.user_inputs import get_string_in_list, get_positive_number, get_any_number

class GetStringInListTests(unittest.TestCase):
    """Tests the function that prompts the user for a text response"""

    def setUp(self):
        stdout_trap = io.StringIO()
        sys.stdout = stdout_trap

    @unittest.mock.patch("builtins.input")
    def test_case_senstive(self, mock_inputs):
        mock_inputs.side_effect = ["Foo", "Bar", "Baz"]
        named_args = {
            "prompt": "Select a value from the list.",
            "err_msg": "Please enter a valid value.",
            "allowed_vals": ["foo", "Bar", "baz"],
            "case_sensitive": True,
        }
        self.assertEqual("Bar", get_string_in_list(**named_args))

    @unittest.mock.patch("builtins.input")
    def test_case_insenstive(self, mock_inputs):
        mock_inputs.side_effect = ["foo", "bar", "baz"]
        named_args = {
            "prompt": "Select a value from the list.",
            "err_msg": "Please enter a valid value.",
            "allowed_vals": ["FOO", "BAR", "BAZ"],
            "case_sensitive": False,
        }
        self.assertEqual("foo", get_string_in_list(**named_args))

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
        self.assertEqual(None, get_string_in_list(**named_args))


    def tearDown(self):
        sys.stdout = sys.__stdout__

class GetPositiveNumberTests(unittest.TestCase):
    """Tests the function that prompts user for a positive number"""

    def setUp(self):
        stdout_trap = io.StringIO()
        sys.stdout = stdout_trap

    @unittest.mock.patch("builtins.input")
    def test_text_input(self, mock_inputs):
        mock_inputs.side_effect = ["Foo", "Bar", 10]
        named_args = {
            "prompt": "How many drinks have you had?",
            "err_msg": "Please enter a numeric value."
        }
        self.assertEqual(10, get_positive_number(**named_args))

    @unittest.mock.patch("builtins.input")
    def test_negative_value(self, mock_inputs):
        mock_inputs.side_effect = [-999, -100, 10]
        named_args = {
            "prompt": "How many drinks have you had?",
            "err_msg": "Please enter a numeric value."
        }
        self.assertEqual(10, get_positive_number(**named_args))

    @unittest.mock.patch("builtins.input")
    def test_exit(self, mock_inputs):
        mock_inputs.side_effect = ["fo", "ba", "quit()", "1"]
        named_args = {
            "prompt": "How many drinks have you had?",
            "err_msg": "Please enter a numeric value.",
            "exit_val": "quit()"
        }
        self.assertEqual(None, get_positive_number(**named_args))

    def tearDown(self):
        sys.stdout = sys.__stdout__

class GetAnyNumberTests(unittest.TestCase):
    """Tests the function that prompts user for any number"""

    def setUp(self):
        stdout_trap = io.StringIO()
        sys.stdout = stdout_trap

    @unittest.mock.patch("builtins.input")
    def test_text_input(self, mock_inputs):
        mock_inputs.side_effect = ["Foo", "Bar", 10]
        named_args = {
            "prompt": "How many drinks have you had?",
            "err_msg": "Please enter a numeric value."
        }
        self.assertEqual(10, get_any_number(**named_args))

    @unittest.mock.patch("builtins.input")
    def test_negative_value(self, mock_inputs):
        mock_inputs.side_effect = ["Foo", -100]
        named_args = {
            "prompt": "How many drinks have you had?",
            "err_msg": "Please enter a numeric value."
        }
        self.assertEqual(-100, get_any_number(**named_args))

    @unittest.mock.patch("builtins.input")
    def test_zero_value(self, mock_inputs):
        mock_inputs.side_effect = ["Foo", 0]
        named_args = {
            "prompt": "How many drinks have you had?",
            "err_msg": "Please enter a numeric value."
        }
        self.assertEqual(0, get_any_number(**named_args))

    @unittest.mock.patch("builtins.input")
    def test_exit_is_null_string(self, mock_inputs):
        mock_inputs.side_effect = ["", 100, "asdf"]
        named_args = {
            "prompt": "How many drinks have you had?",
            "err_msg": "Please enter a numeric value.",
            "exit_val": "",
        }
        self.assertEqual(None, get_any_number(**named_args))

    @unittest.mock.patch("builtins.input")
    def test_exit_is_None(self, mock_inputs):
        mock_inputs.side_effect = [None, 100, "asdf"]
        named_args = {
            "prompt": "How many drinks have you had?",
            "err_msg": "Please enter a numeric value.",
            "exit_val": None,
        }
        self.assertEqual(None, get_any_number(**named_args))

    @unittest.mock.patch("builtins.input")
    def test_numeric_exit(self, mock_inputs):
        mock_inputs.side_effect = ["-999", 100, "asdf"]
        named_args = {
            "prompt": "How many drinks have you had?",
            "err_msg": "Please enter a numeric value.",
            "exit_val": "-999"
        }
        self.assertEqual(None, get_any_number(**named_args))

    def tearDown(self):
        sys.stdout = sys.__stdout__
