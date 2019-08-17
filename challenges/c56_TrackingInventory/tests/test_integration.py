import io
import os
import sys
import unittest
import unittest.mock

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tracking_inventory import tracking_inventory

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class TrackingInventoryIntegrationTest(unittest.TestCase):
    """Tests that the 'main' function works as expected"""

    @unittest.mock.patch("builtins.input")
    def test_tracking_inventory(self, mock_inputs):
        mock_inputs.side_effect = [
            "Add", "Test Item #1", "TestItem#1", "100",
            "Add", "Test Item #2", "quit()", "y",
            "Remove", "2",
            "print",
            "save",
            "to html", "y",
            "to csv", "y",
            "exit"
        ]

        expected_result = (
            "---------------------------------------\n" +
            "|  item_name   |   serial   |  value  |\n" +
            "---------------------------------------\n" +
            "| Item Numba 1 | 1111111111 | $100.00 |\n" +
            "| #2           | ABC123     | $45.43  |\n" +
            "---------------------------------------\n\n" +
            "Item added successfully.\n" +
            "Item not added.\n\n" +
            "Your current inventory is:\n" +
            "-----------------------------------------------\n" +
            "| index |  item_name   |   serial   |  value  |\n" +
            "-----------------------------------------------\n" +
            "| 0     | Item Numba 1 | 1111111111 | $100.00 |\n" +
            "| 1     | #2           | ABC123     | $45.43  |\n" +
            "| 2     | Test Item #1 | TestItem#1 | $100.00 |\n" +
            "-----------------------------------------------\n\n" +
            "Item removed.\n" +
            "---------------------------------------\n" +
            "|  item_name   |   serial   |  value  |\n" +
            "---------------------------------------\n" +
            "| Item Numba 1 | 1111111111 | $100.00 |\n" +
            "| #2           | ABC123     | $45.43  |\n" +
            "---------------------------------------\n\n" +
            "Saved to local file.\n" +
            "HTML File Created.\n" +
            "CSV File Created.\n" +
            "Saved to local file.\n" +
            "Closing application. Good bye."
        )

        with captured_output() as (outputs, errors):
            tracking_inventory.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)
