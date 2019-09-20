import io
import os
import sys
import unittest
import unittest.mock

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from employee_list_removal.employee_list_removal import EmployeeList

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
    """Tests the EmployeeList class and methods"""

    def setUp(self):
        self.list = EmployeeList()
        self.list.employees = {
            "john smith": "John Smith",
            "jackson jackson": "Jackson Jackson",
            "chris jones": "Chris Jones",
            "amanda cullen": "Amanda Cullen",
            "jeremy goodwin": "Jeremy Goodwin",
        }

    def test__new_from_list(self):
        self.list.employees = None
        self.list.import_list(["Foo Bar", "Biz Baz"])
        expected_output = {
            "foo bar": "Foo Bar",
            "biz baz": "Biz Baz",
        }
        self.assertEqual(expected_output, self.list.employees)

    def test__add_from_list(self):
        self.list.import_list(["Foo Bar", "Biz Baz"])
        expected_output = {
            "john smith": "John Smith",
            "jackson jackson": "Jackson Jackson",
            "chris jones": "Chris Jones",
            "amanda cullen": "Amanda Cullen",
            "jeremy goodwin": "Jeremy Goodwin",
            "foo bar": "Foo Bar",
            "biz baz": "Biz Baz",
        }
        self.assertEqual(expected_output, self.list.employees)

    def test__remove_employee__success(self):
        to_remove = "Chris Jones"
        expected_output = {
            "john smith": "John Smith",
            "jackson jackson": "Jackson Jackson",
            "amanda cullen": "Amanda Cullen",
            "jeremy goodwin": "Jeremy Goodwin",
        }
        with captured_output():
            self.list.remove(to_remove)
        self.assertEqual(self.list.employees, expected_output)

    def test__remove_employee__fail(self):
        to_remove = "Foo Bar"
        expected_output = {
            "john smith": "John Smith",
            "jackson jackson": "Jackson Jackson",
            "chris jones": "Chris Jones",
            "amanda cullen": "Amanda Cullen",
            "jeremy goodwin": "Jeremy Goodwin",
        }
        with captured_output():
            self.list.remove(to_remove)
        self.assertEqual(self.list.employees, expected_output)

    def test__print_list(self):
        self.list.employees = {
            "john smith": "John Smith",
            "jackson jackson": "Jackson Jackson",
            "amanda cullen": "Amanda Cullen",
            "jeremy goodwin": "Jeremy Goodwin",
        }
        expected_output = (
            "There are 4 employees:\n" +
            "John Smith\n" +
            "Jackson Jackson\n" +
            "Amanda Cullen\n" +
            "Jeremy Goodwin"
        )
        with captured_output() as (outputs, _):
            self.list.print_to_term()
        result = outputs.getvalue().strip()
        self.assertEqual(expected_output, result)

if __name__ == "__main__":
    unittest.main(verbosity=3)
