import io
import os
import sys
import unittest
import unittest.mock

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bac_calc import bac_calc
from bac_calc.bac_calc import get_string_in_list, get_positive_number

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class PositiveNumberTests(unittest.TestCase):
    """Tests the function that prompts user for a positive number"""

    @unittest.mock.patch("builtins.input")
    def test_text_input(self, mock_inputs):
        mock_inputs.side_effect = ["Foo", "Bar", 10]
        named_args = {
            "prompt": "How many drinks have you had?",
            "err_msg": "Please enter a numeric value."
        }
        with captured_output() as (outputs, errors):
            test_val = get_positive_number(**named_args)

        self.assertEqual(10, test_val)

    @unittest.mock.patch("builtins.input")
    def test_negative_value(self, mock_inputs):
        mock_inputs.side_effect = [-999, -100, 10]
        named_args = {
            "prompt": "How many drinks have you had?",
            "err_msg": "Please enter a numeric value."
        }
        with captured_output() as (outputs, errors):
            test_val = get_positive_number(**named_args)

        self.assertEqual(10, test_val)

class ValidSelectionTests(unittest.TestCase):
    """Tests the function that prompts the user for a text response"""

    @unittest.mock.patch("builtins.input")
    def test_case_senstive(self, mock_inputs):
        mock_inputs.side_effect = ["Foo", "Bar", "Baz"]
        named_args = {
            "prompt": "Select a value from the list.",
            "err_msg": "Please enter a valid value.",
            "allowed_vals": ["foo", "Bar", "baz"],
            "case_sensitive": True,
        }
        with captured_output() as (outputs, errors):
            test_val = get_string_in_list(**named_args)

        self.assertEqual("Bar", test_val)

    @unittest.mock.patch("builtins.input")
    def test_case_insenstive(self, mock_inputs):
        mock_inputs.side_effect = ["foo", "bar", "baz"]
        named_args = {
            "prompt": "Select a value from the list.",
            "err_msg": "Please enter a valid value.",
            "allowed_vals": ["FOO", "BAR", "BAZ"],
            "case_sensitive": False,
        }
        with captured_output() as (outputs, errors):
            test_val = get_string_in_list(**named_args)

        self.assertEqual("foo", test_val)

class BACCalculatorTests(unittest.TestCase):
    """Tests the methods of the BACCalculator Class"""

    def setUp(self):
        self.calc = bac_calc.BACCalculator()
        self.calc.gender = "M"
        self.calc.weight = 180
        self.calc.drinks = 5
        self.calc.type = "wine"
        self.calc.hrs_since_last_drink = 0
        self.legal = False

    def test_legality_bac_003(self):
        self.calc.set_legality(0.03)
        self.assertEqual(True, self.calc.legal)

    def test_legality_bac_010(self):
        self.calc.set_legality(0.10)
        self.assertEqual(False, self.calc.legal)

    def test_legality_bac_008(self):
        self.calc.set_legality(0.08)
        self.assertEqual(False, self.calc.legal)

    def test_bac_calc_is_006(self):
        self.assertEqual(0.06, round(self.calc.test_bac(), 2))


if __name__ == "__main__":
    unittest.main()
