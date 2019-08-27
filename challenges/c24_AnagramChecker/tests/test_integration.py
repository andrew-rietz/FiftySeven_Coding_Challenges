import unittest
import unittest.mock
import io
import sys
import os

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from anagram_checker import anagram_checker

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class CheckAnagramTests(unittest.TestCase):
    """Tests that the 'main' function works as expected"""

    @unittest.mock.patch("builtins.input")
    def test_valid_anagram(self, mock_inputs):
        mock_inputs.side_effect = ["Note", "tone"]
        expected_result = (
            '"Note" and "tone" are anagrams.'
        )

        with captured_output() as (outputs, errors):
            anagram_checker.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)

    @unittest.mock.patch("builtins.input")
    def test_invalid_anagram(self, mock_inputs):
        mock_inputs.side_effect = ["foo", "bar"]
        expected_result = (
            '"foo" and "bar" are not anagrams.'
        )

        with captured_output() as (outputs, errors):
            anagram_checker.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)

if __name__ == "__main__":
    unittest.main()
