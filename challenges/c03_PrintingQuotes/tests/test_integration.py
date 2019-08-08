import io
import os
import sys
import unittest
import unittest.mock

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from printing_quotes import printing_quotes

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class IntegrationTests(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def test_main_valid(self, mock_inputs):
        mock_inputs.side_effect = [
            "These aren't the droids you're looking for",
            "Obi-Wan Kenobi"]
        expected_result = "Obi-Wan Kenobi says, \"These aren't the droids you're looking for\""

        with captured_output() as (outputs, errors):
            printing_quotes.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(test_val, expected_result)

if __name__ == "__main__":
    unittest.main()
