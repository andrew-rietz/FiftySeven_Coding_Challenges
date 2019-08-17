"""
Creates and initiates a PersonalInventory class
"""
import csv
import json
import sys
import os

from collections import OrderedDict

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from input_helpers import _get_item_name, _get_serial, _get_value
from output_helpers import _add_index, _get_table_dimensions, _setup_headers, _setup_body

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util_functions.utils import user_inputs


class PersonalInventory():
    """A class for tracking personal inventory

    Attributes:
        inventory: (OrderedDict) dict representing the personal inventory. The dictionary
            has three keys, each corresponding to a list of values

            item_name: (str) Name of the tracked item
            serial: (str) The serial number for the item
            value: (str) The value of the item, in dollars
    """
    def __init__(self, inventory=None):
        self.inventory = inventory
        if self.inventory is None:
            self.inventory = OrderedDict()
            self.inventory = {
                "item_name": [],
                "serial": [],
                "value": [],
            }

    def add_item(self):
        """
        Gathers the name, serial number, and value of a new item. If all three
            are valid, adds the item to the inventory.
        """
        item_name = _get_item_name()
        if item_name is None:
            print("Item not added.")
            return None

        if "," in item_name:
            item_name = item_name.replace(",", "_")
            print("Coerced all instances of commas (',') in item name to underscores ('_').")

        serial = _get_serial()
        if serial is None:
            print("Item not added.")
            return None

        if "," in serial:
            serial = serial.replace(",", "_")
            print("Coerced all instances of commas (',') in serial number to underscores ('_').")

        value = _get_value()
        if value is None:
            print("Item not added.")
            return None

        self.inventory["item_name"].append(item_name)
        self.inventory["serial"].append(serial)
        self.inventory["value"].append(value)
        print("Item added successfully.")
        return "Success"

    def print_to_terminal(self, index=False):
        """
        Writes the table to the terminal in a tabular format. May include an index
        column if the user desires.

        Args:
            index: (bool) indicates whether the index should be printed as well
        """
        working_inv = OrderedDict(self.inventory)
        if index:
            working_inv = _add_index(working_inv)

        dimensions = _get_table_dimensions(working_inv)
        if dimensions["n_rows"] == 0:
            return "Success"

        table_str = ("-" * (dimensions["table_width"] + 3 * dimensions["n_cols"] + 1) + "\n")
        table_str += _setup_headers(dimensions, working_inv, style="terminal")
        table_str += ("-" * (dimensions["table_width"] + 3 * dimensions["n_cols"] + 1) + "\n")
        table_str += _setup_body(dimensions, working_inv, style="terminal")
        table_str += ("-" * (dimensions["table_width"] + 3 * dimensions["n_cols"] + 1) + "\n")

        print(table_str)

        return "Success"

    def to_csv(self, index=False, basedir=None, subdir="data", filename="personal_inventory.csv"):
        """
        Writes the table to an CSV document in the ./data folder. May include an index
        column if the user desires.

        Args:
            index: (bool) indicates whether the index should be printed as well
            basedir: (str) Absolute filepath for the directory the local json file is located within
            subdir: (str) Optional subdirectory that the local json file is located within
            filename: (str) Optional - name of the local json file
        """
        working_inv = OrderedDict(self.inventory)
        if index:
            working_inv = _add_index(working_inv)

        dimensions = _get_table_dimensions(working_inv)

        if basedir is None:
            basedir = os.path.dirname(os.path.abspath(__file__))

        filepath = os.path.join(basedir, subdir, filename)
        with open(filepath, "w") as csv_file:
            field_names = list(working_inv.keys())
            writer = csv.DictWriter(csv_file, field_names)

            writer.writeheader()
            for row in range(dimensions["n_rows"]):
                single_row_dict = {}
                for col in working_inv.keys():
                    single_row_dict[col] = working_inv[col][row]
                writer.writerow(single_row_dict)

        print("CSV File Created.")
        return "Success"

    def to_html(self, index=False, basedir=None, subdir="data", filename="personal_inventory.html"):
        """
        Writes the table to an HTML document in the ./data folder. May include an index
        column if the user desires.

        Args:
            index: (bool) indicates whether the index should be printed as well
            basedir: (str) Absolute filepath for the directory the local json file is located within
            subdir: (str) Optional subdirectory that the local json file is located within
            filename: (str) Optional - name of the local json file
        """
        working_inv = OrderedDict(self.inventory)
        if index:
            working_inv = _add_index(working_inv)

        dimensions = _get_table_dimensions(working_inv)
        table_headers = _setup_headers(dimensions, working_inv, style="html")
        table_rows = _setup_body(dimensions, working_inv, style="html")

        if basedir is None:
            basedir = os.path.dirname(os.path.abspath(__file__))

        filepath = os.path.join(basedir, subdir, filename)
        with open(filepath, "w") as html_file:
            style = (
                "<style>" +
                "    th" +
                "    {border: 1px solid black;" +
                "    border-collapse: collapse;}" +
                "    td" +
                "    {border: 1px solid black;" +
                "    border-collapse: collapse;}" +
                "    table" +
                "    {border: 1px solid black;" +
                "    border-collapse: collapse;}" +
                "</style>"
            )
            html_file.write(f"{style}\n<table cellpadding='4'>")
            html_file.write(table_headers)
            html_file.write(table_rows)
            html_file.write("</table>")

        print("HTML File Created.")
        return "Success"

    def remove_item(self):
        """
        Prints the current inventory and prompts the user to indicate which item
        to remove. Then removes the item from inventory
        """
        n_rows = len(list(self.inventory.values())[0])
        if n_rows == 0:
            print("No items to remove.")
            return "Success"

        print("\nYour current inventory is:")
        self.print_to_terminal(index=True)
        index_to_delete = user_inputs.get_string_in_list(
            prompt="Enter the index of the item to delete. (or enter quit() to cancel):",
            err_msg="Enter a valid index.",
            allowed_vals=[str(index) for index in range(n_rows)],
            exit_val="quit()"
        )
        if index_to_delete is None:
            print("Removal cancelled.")
            return "Success"

        index_to_delete = int(index_to_delete)
        for col in self.inventory.keys():
            column_values = self.inventory[col]
            del column_values[index_to_delete]

        print("Item removed.")
        return "Success"

    def save(self, basedir=None, subdir="data", filename="local_storage.json"):
        """
        Saves the file to local persistent storage in the ./data folder

        Args:
            basedir: (str) Absolute filepath for the directory the local json file is located within
            subdir: (str) Optional subdirectory that the local json file is located within
            filename: (str) Optional - name of the local json file
        """

        if basedir is None:
            basedir = os.path.dirname(os.path.abspath(__file__))

        filepath = (
            os.path.join(basedir, subdir, filename)
        )

        with open(filepath, "w", encoding="utf-8") as local_file:
            json.dump(self.inventory, local_file, ensure_ascii=False, indent=4)

        print("Saved to local file.")
        return "Success"
