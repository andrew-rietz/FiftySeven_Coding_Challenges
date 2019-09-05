import io
import os
import sys
import unittest
import unittest.mock

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from karvonen_heart_rate.karvonen_heart_rate import get_inputs, KarvonenCalculator

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class GetInputsTest(unittest.TestCase):
    """Tests the get_inputs function"""

    @unittest.mock.patch("builtins.input")
    def test__rate_is_6(self, mock_inputs):
        mock_inputs.side_effect = ["Foo", "Bar", "65", "Foo", "Bar", "22"]
        with captured_output():
            inputs_returns = get_inputs()

        expected_result = {
            "resting_heart_rate": 65,
            "age": 22
        }
        self.assertEqual(expected_result, inputs_returns)

class KarvonenCalculatorTests(unittest.TestCase):
    """Tests the KarvonenCalculator class"""
    def setUp(self):
        self.calc = KarvonenCalculator(resting_heart_rate=65, age=22)

    def test__calc_target_heart_rate(self):
        self.assertEqual(151.45, self.calc.calc_target_heart_rate(65))

    def test__generate_heart_rate_data(self):
        expected_result = [
            ["Intensity", "Target Heart Rate"],
            ["65%", "151.4 bpm"],
            ["70%", "158.1 bpm"]
        ]

        with captured_output():
            self.calc.generate_heart_rate_data(65, 70, 5)
        self.assertEqual(expected_result, self.calc.intensity_data)

    def test__print_ascii_table(self):
        with captured_output():
            self.calc.generate_heart_rate_data(65, 70, 5)
            self.calc.print_ascii_table()

        expected_result = (
            "Intensity | Target Heart Rate \n" +
            "----------|------------------ \n" +
            "   65%    |     151.4 bpm     \n" +
            "   70%    |     158.1 bpm     "
        )
        self.assertEqual(expected_result, self.calc.table)


if __name__ == "__main__":
    unittest.main()
