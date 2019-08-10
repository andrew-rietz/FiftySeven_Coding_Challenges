import io
import os
import sys
import unittest
import unittest.mock

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from legal_driving_age import legal_driving_age

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class LegalDriveIntegrationTest(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def test_valid_driver(self, mock_inputs):
        mock_inputs.side_effect = ["-9999", "Foo", "18", "MEX"]

        expected_result = (
            "Please enter a numeric value greater than or equal to zero. " * 2 +
            "You are old enough to legally drive in MEX."
        )

        with captured_output() as (outputs, errors):
            legal_driving_age.main()
        test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)

    @unittest.mock.patch("builtins.input")
    def test_invalid_young_driver(self, mock_inputs):
        mock_inputs.side_effect = ["-9999", "Foo", "12", "MEX"]

        expected_result = (
            "Please enter a numeric value greater than or equal to zero. " * 2 +
            "You aren't old enough to legally drive in MEX."
        )

        with captured_output() as (outputs, errors):
            legal_driving_age.main()
        test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)

if __name__ == "__main__":
    unittest.main()
