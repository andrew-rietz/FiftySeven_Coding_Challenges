import csv
import io
import json
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

    def setUp(self):
        basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        local_json_filepath = os.path.join(
            basedir, "tracking_inventory", "data", "local_storage.json"
        )
        with open(local_json_filepath, "r") as json_file:
            self.original_json = json.load(json_file)

        local_csv_filepath = os.path.join(
            basedir, "tracking_inventory", "data", "personal_inventory.csv"
        )
        with open(local_csv_filepath, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            self.original_csv = [row for row in reader]

        local_html_filepath = os.path.join(
            basedir, "tracking_inventory", "data", "personal_inventory.html"
        )
        with open(local_html_filepath, "r") as html_file:
            self.original_html = html_file.read()

    @unittest.mock.patch("builtins.input")
    @unittest.mock.patch("tracking_inventory.tracking_inventory.startup")
    def test_tracking_inventory(self, mock_startup, mock_inputs):
        basedir = os.path.dirname(os.path.abspath(__file__))
        json_test_filepath = os.path.join(basedir, "mock_data", "test_local_storage.json")
        with open(json_test_filepath, "r") as json_test_file:
            test_inventory = json.load(json_test_file)
        mock_startup.return_value = (
            tracking_inventory.PersonalInventory(test_inventory)
        )
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
            "------------------------------------\n" +
            "| item_name  |   serial  |  value  |\n" +
            "------------------------------------\n" +
            "| Xbox One   | AXB124AXY | $399.00 |\n" +
            "| Samsung TV | S40AZBDE4 | $599.99 |\n" +
            "------------------------------------\n\n" +
            "Item added successfully.\n" +
            "Item not added.\n\n" +
            "Your current inventory is:\n" +
            "-----------------------------------------------\n" +
            "| index |  item_name   |   serial   |  value  |\n" +
            "-----------------------------------------------\n" +
            "| 0     | Xbox One     | AXB124AXY  | $399.00 |\n" +
            "| 1     | Samsung TV   | S40AZBDE4  | $599.99 |\n" +
            "| 2     | Test Item #1 | TestItem#1 | $100.00 |\n" +
            "-----------------------------------------------\n\n" +
            "Item removed.\n" +
            "------------------------------------\n" +
            "| item_name  |   serial  |  value  |\n" +
            "------------------------------------\n" +
            "| Xbox One   | AXB124AXY | $399.00 |\n" +
            "| Samsung TV | S40AZBDE4 | $599.99 |\n" +
            "------------------------------------\n\n" +
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

    def tearDown(self):
        basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        local_json_filepath = os.path.join(
            basedir, "tracking_inventory", "data", "local_storage.json"
        )
        with open(local_json_filepath, "w") as json_file:
            json.dump(self.original_json, json_file, ensure_ascii=False, indent=4)

        local_csv_filepath = os.path.join(
            basedir, "tracking_inventory", "data", "personal_inventory.csv"
        )
        with open(local_csv_filepath, "w") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerows(self.original_csv)

        local_html_filepath = os.path.join(
            basedir, "tracking_inventory", "data", "personal_inventory.html"
        )
        with open(local_html_filepath, "w") as html_file:
            html_file.write(self.original_html)
