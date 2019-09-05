import unittest
import unittest.mock
import io
import sys
import os

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from karvonen_heart_rate import karvonen_heart_rate

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class KarvonenCalculatorTests(unittest.TestCase):
    """Tests that the 'main' function works as expected"""

    @unittest.mock.patch("builtins.input")
    def test_sum_is_(self, mock_inputs):
        mock_inputs.side_effect = ["65", "22"]

        expected_result = (
            "Intensity | Target Heart Rate \n" +
            "----------|------------------ \n" +
            "   55%    |     138.2 bpm     \n" +
            "   60%    |     144.8 bpm     \n" +
            "   65%    |     151.4 bpm     \n" +
            "   70%    |     158.1 bpm     \n" +
            "   75%    |     164.8 bpm     \n" +
            "   80%    |     171.4 bpm     \n" +
            "   85%    |     178.1 bpm     \n" +
            "   90%    |     184.7 bpm     \n" +
            "   95%    |     191.3 bpm     \n"
        )

        with captured_output() as (outputs, errors):
            karvonen_heart_rate.main()
            test_val = outputs.getvalue()

        self.assertEqual(expected_result, test_val)


if __name__ == "__main__":
    unittest.main()
