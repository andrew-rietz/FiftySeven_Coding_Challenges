import io
import os
import sys
import unittest
import unittest.mock

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from handling_bad_input import handling_bad_input

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class GetPositiveNonzeroNumberTests(unittest.TestCase):
    """Tests the get_positive_nonzero_number function"""

    @unittest.mock.patch("builtins.input")
    def test__rate_is_6(self, mock_inputs):
        mock_inputs.side_effect = ["0", "Foo", "6"]
        with captured_output():
            rate = handling_bad_input.get_positive_nonzero_number(
                prompt="What is the rate of return?",
                err_msg="Invalid input."
            )
        self.assertEqual(6, rate)

class CalcYearsToDoubleTests(unittest.TestCase):
    """Tests the get_numbers_to_sum function"""

    def test__rate_of_4__18_years_to_double(self):
        years = handling_bad_input.calc_years_to_double(4)
        self.assertEqual(18, years)

class PrintResultTest(unittest.TestCase):
    """Tests the print_result function"""

    def test__years_is_18(self):
        expected_result = "It will take 18 years to double your initial investment."
        result = handling_bad_input.print_result(18)
        self.assertEqual(expected_result, result)

if __name__ == "__main__":
    unittest.main()
