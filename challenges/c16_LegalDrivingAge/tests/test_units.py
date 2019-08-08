import io
import os
import sys
import unittest
import unittest.mock

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from legal_driving_age import legal_driving_age

from legal_driving_age.legal_driving_age import get_positive_number, check_legal_driver

class GetPositiveNumberTests(unittest.TestCase):

    def setUp(self):
        stdout_trap = io.StringIO()
        sys.stdout = stdout_trap

    @unittest.mock.patch("builtins.input")
    def test_text_input(self, mock_inputs):
        mock_inputs.side_effect = ["Foo", "Bar", 10]
        named_args = {
            "prompt": "What is your age?",
            "err_msg": "Please enter a numeric value greater than or equal to zero."
        }
        self.assertEqual(10, get_positive_number(**named_args))

    @unittest.mock.patch("builtins.input")
    def test_negative_value(self, mock_inputs):
        mock_inputs.side_effect = [-999, -2, 10]
        named_args = {
            "prompt": "What is your age?",
            "err_msg": "Please enter a numeric value greater than or equal to zero."
        }
        self.assertEqual(10, get_positive_number(**named_args))

    def tearDown(self):
        sys.stdout = sys.__stdout__

class CheckLegalDriverTests(unittest.TestCase):

    def test_too_young(self):
        expected_result = "You aren't old enough to legally drive in CDN."
        self.assertEqual(check_legal_driver(2, "CDN"), expected_result)


if __name__ == "__main__":
    unittest.main(buffer=True)
    sys.stdout.flush()
