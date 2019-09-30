import io
import os
import sys
import unittest
import unittest.mock

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from filtering_records.filtering_records import EmployeeDatabase

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class EmployeeDatabaseSetup(unittest.TestCase):
    """Initiates a class instance for use in child tests"""

    def setUp(self):
        super(EmployeeDatabaseSetup, self).__init__()
        self.db = EmployeeDatabase()

class LoadDataTests(EmployeeDatabaseSetup):
    """Tests the load_data method"""

    def test__returns_list_of_length_6(self):
        self.assertEqual(6, len(self.db.load_data()))

    def test__returns_list(self):
        self.assertTrue(isinstance(self.db.load_data(), list))

    def test__last_person_named_Sally_Weber(self):
        employees = self.db.load_data()
        self.assertEqual(
            "Sally Weber",
            employees[-1].get("first_name") + " " + employees[-1].get("last_name")
        )

class FilterStringTests(EmployeeDatabaseSetup):
    """Tests the get_filter_string method"""

    @unittest.mock.patch("builtins.input")
    def test__filter_is_ja(self, mock_inputs):
        mock_inputs.side_effect = ["Ja"]
        with captured_output():
            filter_val = self.db.get_filter_string()
        self.assertEqual("ja", filter_val)

class FilterTests(EmployeeDatabaseSetup):
    """Tests the filter method"""

    def test__2_records_in_result(self):
        self.db.load_data()
        with captured_output():
            filtered_data = self.db.filter("ja")
        self.assertEqual(2, len(filtered_data))

    def test__results_are_jake_jacobsen_and_jacquelyn_jackson(self):
        self.db.load_data()
        expected_result = [
            {
                "first_name": "Jake", "last_name": "Jacobsen",
                "position": "Programmer", "sep_date": "",
            },
            {
                "first_name": "Jacquelyn", "last_name": "Jackson",
                "position": "DBA", "sep_date": "",
            },
        ]
        filtered_data = self.db.filter("ja")
        self.assertEqual(expected_result, filtered_data)

class SortTableTests(EmployeeDatabaseSetup):
    """Tests the sort_table function"""

    def test__aligned_left_sorted_by_first_name(self):
        self.db.load_data()
        self.db.filter("ja")
        ascii_table = self.db.tabulate_filtered_data()
        expected_result = (
            "Name               | Position    | Separation Date \n" +
            "-------------------|-------------|-----------------\n" +
            "Jake Jacobsen      | Programmer  |                 \n" +
            "Jacquelyn Jackson  | DBA         |                 "
        )
        self.assertEqual(expected_result, ascii_table)


if __name__ == "__main__":
    unittest.main(verbosity=3)
