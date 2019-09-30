import unittest
import unittest.mock
import io
import sys
import os

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from filtering_records import filtering_records

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class FilterRecordsTest(unittest.TestCase):
    """Tests that the 'main' function works as expected"""

    @unittest.mock.patch("builtins.input")
    def test__main(self, mock_inputs):
        mock_inputs.side_effect = ["ja"]
        expected_result = (
            "Name               | Position    | Separation Date \n" +
            "-------------------|-------------|-----------------\n" +
            "Jake Jacobsen      | Programmer  |                 \n" +
            "Jacquelyn Jackson  | DBA         |                 "

        )
        with captured_output() as (outputs, _):
            filtering_records.main()
        test_val = outputs.getvalue().split("\n")[-5:-1]
        self.assertEqual("\n".join(test_val), expected_result)


if __name__ == "__main__":
    unittest.main()
