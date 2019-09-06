import os
import sys
import unittest
import unittest.mock

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from validating_inputs import validating_inputs


class NameValidationTests(unittest.TestCase):
    """Tests the _validate_name and get_name functions"""

    def test__a_is_not_a_name(self):
        expected_result = "A is not a valid middle name. It is too short."
        self.assertEqual(expected_result, validating_inputs._validate_name("middle", "A"))

    def test__blank_val_is_not_a_name(self):
        expected_result = "The middle name must be filled in."
        self.assertEqual(expected_result, validating_inputs._validate_name("middle", ""))

    def test__special_chars_is_not_a_name(self):
        expected_result = "N@me is not a valid middle name. Names may only contain letters."
        self.assertEqual(expected_result, validating_inputs._validate_name("middle", "N@me"))


if __name__ == "__main__":
    unittest.main()
