import io
import os
import sys
import unittest
import unittest.mock

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sorting_records.sorting_records import (
    load_data, get_sort_preference, get_alignment_preference, sort_table
)

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class LoadDataTests(unittest.TestCase):
    """Tests the load_data function"""

    def test__returns_list_of_length_6(self):
        self.assertEqual(6, len(load_data()))

    def test__returns_list(self):
        self.assertTrue(isinstance(load_data(), list))

    def test__last_person_named_Sally_Weber(self):
        employees = load_data()
        self.assertEqual(
            "Sally Weber",
            employees[-1].get("first_name") + " " + employees[-1].get("last_name")
        )

class SortPreferenceTests(unittest.TestCase):
    """Tests the get_sort_preference function"""

    @unittest.mock.patch("builtins.input")
    def test__selection_is_position(self, mock_inputs):
        mock_inputs.side_effect = ["Foo", "bar", "POSITION"]
        with captured_output():
            sort_field = get_sort_preference()
        self.assertEqual("position", sort_field)

class AlignmentPreferenceTests(unittest.TestCase):
    """Tests the get_alignment_preference function"""

    @unittest.mock.patch("builtins.input")
    def test__selection_is_center(self, mock_inputs):
        mock_inputs.side_effect = ["Foo", "bar", "CeNtER"]
        with captured_output():
            alignment = get_alignment_preference()
        self.assertEqual("center", alignment)

class SortTableTests(unittest.TestCase):
    """Tests the sort_table function"""

    def test__aligned_left_sorted_by_first_name(self):
        table = sort_table(load_data(), "first_name", "left")
        expected_result = (
            "Name                 | Position           | Separation Date \n" +
            "---------------------|--------------------|-----------------\n" +
            "Jacquelyn Jackson    | DBA                |                 \n" +
            "Jake Jacobsen        | Programmer         |                 \n" +
            "John Johnson         | Manager            | 2016-12-31      \n" +
            "Michaela Michaelson  | District Manager   | 2015-12-19      \n" +
            "Sally Weber          | Web Developer      | 2015-12-18      \n" +
            "Tuo Xiong            | Software Engineer  | 2016-10-05      "
        )
        self.assertEqual(expected_result, table)


if __name__ == "__main__":
    unittest.main(verbosity=3)
