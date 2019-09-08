import io
import os
import sys
import unittest
import unittest.mock

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from adding_numbers import adding_numbers

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class SumNumbersTests(unittest.TestCase):
    """Tests the sum_numbers function"""

    def test__sums_to_6(self):
        input_list = [1, 2, 3]
        self.assertEqual(6, adding_numbers.sum_numbers(input_list))

    def test__sums_to_0(self):
        input_list = [1, 2, -3]
        self.assertEqual(0, adding_numbers.sum_numbers(input_list))

class GetNumbersToSumTests(unittest.TestCase):
    """Tests the get_numbers_to_sum function"""

    @unittest.mock.patch("builtins.input")
    def test__gets_3_inputs(self, mock_inputs):
        mock_inputs.side_effect = [1, 2, "foo", 3]

        with captured_output():
            numbers_to_sum = adding_numbers.get_numbers_to_sum(3)

        expected_result = [1, 2, 3]
        self.assertEqual(expected_result, numbers_to_sum)

class HowManyNumbersTest(unittest.TestCase):
    """Tests the how_many_numbers function"""

    @unittest.mock.patch("builtins.input")
    def test__prompt_how_many_numbers(self, mock_inputs):
        mock_inputs.side_effect = ["foo", "bar", 3]

        with captured_output() as (outputs, errors):
            numbers_to_sum = adding_numbers.how_many_numbers()

        self.assertEqual(3, numbers_to_sum)

class PrintResultTest(unittest.TestCase):
    """Tests the print_result function"""

    def test__total_is_1_5(self):
        expected_result = "The total is 1.5."
        result = adding_numbers.print_result(1.54321)
        self.assertEqual(expected_result, result)

if __name__ == "__main__":
    unittest.main()
