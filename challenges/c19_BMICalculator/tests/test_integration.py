import unittest
import unittest.mock
import io
import sys
import os

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bmi_calc import bmi_calc

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class BMICalculatorTest(unittest.TestCase):
    """Tests that the 'main' function works as expected"""

    @unittest.mock.patch("builtins.input")
    def test_healthy_bmi(self, mock_inputs):
        mock_inputs.side_effect = ["72", "180"]

        expected_result = (
            "Your BMI is 24.4.\n" +
            "You are within the ideal weight range."
        )

        with captured_output() as (outputs, errors):
            bmi_calc.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)

    @unittest.mock.patch("builtins.input")
    def test_overweight_bmi(self, mock_inputs):
        mock_inputs.side_effect = ["72", "300"]

        expected_result = (
            "Your BMI is 40.7.\n" +
            "You are overweight. You should see your doctor."
        )

        with captured_output() as (outputs, errors):
            bmi_calc.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)

    @unittest.mock.patch("builtins.input")
    def test_underweight_bmi(self, mock_inputs):
        mock_inputs.side_effect = ["72", "100"]

        expected_result = (
            "Your BMI is 13.6.\n" +
            "You are underweight. You should see your doctor."
        )

        with captured_output() as (outputs, errors):
            bmi_calc.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)

if __name__ == "__main__":
    unittest.main()
