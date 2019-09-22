import unittest
import unittest.mock
import io
import sys
import os

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from computing_statistics import computing_statistics

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class ComputingStatisticsTests(unittest.TestCase):
    """Tests that the 'main' function works as expected"""

    @unittest.mock.patch("builtins.input")
    def test__main(self, mock_inputs):
        expected_output = (
            f"Numbers: 100.00, 200.00, 1,000.00, 300.00\n" +
            f"The average is 400.00.\n" +
            f"The minimum is 100.00.\n" +
            f"The maximum is 1,000.00.\n" +
            f"The standard deviation is 353.55."
        )
        mock_inputs.side_effect = ["100", "200", "1000", "300", "done"]
        with captured_output() as (outputs, _):
            computing_statistics.main()
        summary = outputs.getvalue().strip().split("\n")[-5:]
        self.assertEqual("\n".join(summary), expected_output)


if __name__ == "__main__":
    unittest.main()
