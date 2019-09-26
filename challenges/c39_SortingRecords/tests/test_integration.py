import unittest
import unittest.mock
import io
import sys
import os

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sorting_records import sorting_records

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class SortingRecordsTests(unittest.TestCase):
    """Tests that the 'main' function works as expected"""

    @unittest.mock.patch("builtins.input")
    def test__main(self, mock_inputs):
        mock_inputs.side_effect = ["position", "center"]
        expected_result = (
            "        Name         |      Position      | Separation Date \n" +
            "---------------------|--------------------|-----------------\n" +
            " Jacquelyn Jackson   |        DBA         |                 \n" +
            "Michaela Michaelson  |  District Manager  |    2015-12-19   \n" +
            "    John Johnson     |      Manager       |    2016-12-31   \n" +
            "   Jake Jacobsen     |     Programmer     |                 \n" +
            "     Tuo Xiong       | Software Engineer  |    2016-10-05   \n" +
            "    Sally Weber      |   Web Developer    |    2015-12-18   "
        )
        with captured_output() as (outputs, _):
            sorting_records.main()
        test_val = outputs.getvalue().split("\n")[-9:-1]
        self.assertEqual(expected_result, "\n".join(test_val))


if __name__ == "__main__":
    unittest.main()
