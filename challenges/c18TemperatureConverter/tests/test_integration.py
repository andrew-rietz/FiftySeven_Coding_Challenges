import unittest
import unittest.mock
import io
import sys
import os

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from temp_convert import temp_convert

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class TempConverterIntegrationTests(unittest.TestCase):
    """Tests that the 'main' function works as expected"""

    @unittest.mock.patch("builtins.input")
    def test_over_the_limit(self, mock_inputs):
        mock_inputs.side_effect = ["C", "32"]

        expected_result = (
            "The temperature in Celsius is 0.0."
        )

        with captured_output() as (outputs, errors):
            temp_convert.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)


if __name__ == "__main__":
    unittest.main()
