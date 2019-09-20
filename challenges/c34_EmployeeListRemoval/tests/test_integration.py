import unittest
import unittest.mock
import io
import sys
import os

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from employee_list_removal import employee_list_removal

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class EmployeeListTests(unittest.TestCase):
    """Tests that the 'main' function works as expected"""

    @unittest.mock.patch("builtins.input")
    def test__main(self, mock_inputs):
        mock_inputs.side_effect = ["Chris Jones"]
        expected_output = (
            "There are 4 employees:\n" +
            "John Smith\n" +
            "Jackson Jackson\n" +
            "Amanda Cullen\n" +
            "Jeremy Goodwin"
        )
        with captured_output() as (outputs, _):
            employee_list_removal.main()
            result = outputs.getvalue().strip()

        self.assertTrue(expected_output in result)


if __name__ == "__main__":
    unittest.main()
