"""
Creates and initiates a PersonalInventory class
"""
import csv
import json
import pandas as pd
import sys
import os

from collections import OrderedDict

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

        serial = _get_serial()
        if serial is None:
            print("Item not added.")
            return None

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

    def to_csv(self, index=False):
        """
        Writes the table to an CSV document in the ./data folder. May include an index
        column if the user desires.

        Args:
            index: (bool) indicates whether the index should be printed as well
        """
        working_inv = OrderedDict(self.inventory)
        if index:
            working_inv = _add_index(working_inv)

        dimensions = _get_table_dimensions(working_inv)
        table_str = _setup_headers(dimensions, working_inv, style="csv")
        table_str += _setup_body(dimensions, working_inv, style="csv")

        filepath = (
            os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "data", "personal_inventory.csv")
        )
        with open(filepath, "w") as csv_file:
            field_names = list(working_inv.keys())
            writer = csv.DictWriter(csv_file, field_names)

            n_rows = len(list(working_inv.values())[0])
            writer.writeheader()
            for row in range(n_rows):
                single_row_dict = {}
                for col in working_inv.keys():
                    single_row_dict[col] = working_inv[col][row]
                writer.writerow(single_row_dict)

        print("CSV File Created.")
        return "Success"

    def to_html(self, index=False):
        """
        Writes the table to an HTML document in the ./data folder. May include an index
        column if the user desires.

        Args:
            index: (bool) indicates whether the index should be printed as well
        """
        working_inv = OrderedDict(self.inventory)
        if index:
            working_inv = _add_index(working_inv)

        dimensions = _get_table_dimensions(working_inv)
        table_headers = _setup_headers(dimensions, working_inv, style="html")
        table_rows = _setup_body(dimensions, working_inv, style="html")

        filepath = (
            os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "data", "personal_inventory.html")
        )
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
            html_file.write(f"{style}\n<table>")
            html_file.write(table_headers)
            html_file.write(table_rows)
            html_file.write("</table>")

        print("HTML File Created.")
        return "Success"

    def remove_item(self):
        """
        Prompts the user to indicate which item to remove. Then removes the item from inventory
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
            exit="quit()"
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

    def save(self):
        """
        Saves the file to local persistent storage in the ./data folder
        """
        filepath = (
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "local_storage.json")
        )

        with open(filepath, "w", encoding="utf-8") as local_file:
            json.dump(self.inventory, local_file, ensure_ascii=False, indent=4)

        print("Saved to local file.")
        return "Success"

def startup():
    """
    Check for data in local storage. If it exists, load it into a new PersonalInventory
    class instance. Otherwise initiate a new, blank, instance of the same class.

    Returns:
        inv: (obj) A PersonalInventory class object
    """
    filepath = (
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "local_storage.json")
    )

    try:
        with open(filepath, "r") as local_file:
            stored_inventory = json.load(local_file)
        inv = PersonalInventory(stored_inventory)

    except FileNotFoundError:
        inv = PersonalInventory()

    return inv

def prompt():
    """Prompts the user for an action and returns the value of that action"""
    allowed_vals = ["Add", "Remove", "Print", "To CSV", "To HTML", "Save", "Exit"]
    action = user_inputs.get_string_in_list(
        prompt=f"What would you like to do? [{', '.join(allowed_vals)}]:",
        err_msg="Sorry, please enter a valid selection",
        allowed_vals=allowed_vals,
        case_sensitive=False,
        exit="Exit"
    )
    return action.upper()

def perform_action(inventory, action):
    """Takes a PersonalInventory object and an action. Performs the given action on the object"""

    if action == "EXIT":
        inventory.save()
        print("Closing application. Good bye.")
        return "EXIT"

    if action == "ADD":
        inventory.add_item()
    elif action == "REMOVE":
        inventory.remove_item()
    elif action == "PRINT":
        inventory.print_to_terminal()
    elif action == "TO CSV":
        index = user_inputs.get_string_in_list(
            prompt=f"Do you want the index included? [Y/N]:",
            err_msg="Sorry, please enter a valid selection",
            allowed_vals=["Y", "N"],
            case_sensitive=False,
        )
        inventory.to_csv(index=(index.upper() == "Y"))
    elif action == "TO HTML":
        index = user_inputs.get_string_in_list(
            prompt=f"Do you want the index included? [Y/N]:",
            err_msg="Sorry, please enter a valid selection",
            allowed_vals=["Y", "N"],
            case_sensitive=False,
        )
        inventory.to_html(index=(index.upper() == "Y"))
    elif action == "SAVE":
        inventory.save()
    else:
        print("Command not recognized. Try again.")
        return None

    return "Success"

def _get_item_name():
    """Prompts user for the name of an item"""
    while True:
        item_name = input("What is the item's name? (Or type quit() to exit): ")
        if item_name == "quit()":
            return None
        if (item_name is None) or (item_name == ""):
            print("Sorry, that is not a valid name.", end=" ")
            continue

        return item_name

def _get_serial():
    """Prompts user for the serial number of an item"""
    while True:
        serial = input("What is the item's serial number? (Or type quit() to exit): ")
        if serial == "quit()":
            confirm = input(
                "Are you sure you want to quit? The item will be discarded. [Y/N]: "
            )
            if confirm.strip().upper()[0] == "Y":
                return None
            continue
        if (serial is None) or (serial == ""):
            print("Sorry, that is not a valid serial number.", end=" ")
            continue
        return serial

def _get_value():
    """Prompts user for the value of an item. Value must be numeric"""
    while True:
        value = user_inputs.get_any_number(
            prompt="What is the item's value? (Or type quit() to exit)",
            err_msg="Sorry, that is not a valid value.",
            exit="quit()"
        )
        if value is None:
            confirm = input(
                "Are you sure you want to quit? The item will be discarded. [Y/N]: "
            )
            if confirm.strip().upper()[0] == "Y":
                return None
            continue
        return f"${value:,.2f}"

def _add_index(working_inv):
    """
    Adds a numeric index to the dictionary to help end-user when printed to terminal

    Args:
        working_inv: (dict) The dictionary that needs to have an index added

    Returns:
        working_inv: (dict) Dictionary with index column added
    """
    n_rows = len(list(working_inv.values())[0])
    working_inv["index"] = [str(val) for val in range(n_rows)]
    working_inv.move_to_end("index", last=False)

    return working_inv

def _get_table_dimensions(working_inv):
    """Gets the dimensions of an inventory object prior to converting into tabular format

    Args:
        working_inv: (dict) Represents an inventory object

    Returns:
        dimeions: (dict) contains the dimensions of the table:
            n_rows, n_cols, column_widths, and table_width
    """
    dimensions = {
        "column_widths": {},
        "table_width": 0,
        "n_rows": len(list(working_inv.values())[0]),
        "n_cols": len(list(working_inv.keys())),
    }

    if dimensions["n_rows"] == 0:
        print("No items in inventory.")
        return dimensions

    for col in working_inv.keys():
        data_widths = [len(val) for val in working_inv[col]]
        # Add in the column header as well
        data_widths.append(len(str(col)))
        column_width = max(data_widths)
        dimensions["column_widths"][col] = column_width
        dimensions["table_width"] += column_width

    return dimensions

def _setup_headers(dimensions, working_inv, style="terminal"):
    """Prints the table headers to stdout

    Args:
        dimensions: (dict) contains the dimensions of the table:
            n_rows, n_cols, column_widths, and table_width
        working_inv

    Returns:
        header_str: (str) text representation of the row, with the proper delimeters
    """
    prefix = {
        "terminal": "",
        "html": "<th>",
        "csv": "",
    }
    suffix = {
        "terminal": " | ",
        "html": "</th>\n",
        "csv": "",
    }

    header_str = ""

    for col in working_inv.keys():
        header_str += prefix[style]
        if style == "terminal":
            header_str += col.center(dimensions["column_widths"].get(col))
        else:
            header_str += col
        header_str += suffix[style]

    if style == "terminal":
        header_str = "| " + header_str[:-1] + "\n"
    elif style == "html":
        header_str = "<tr>\n" + header_str + "</tr>\n"
    elif style == "csv":
        header_str = header_str + "\n"

    return header_str

def _setup_body(dimensions, working_inv, style="terminal"):
    """Prints the table headers to stdout

    Args:
        dimensions: (dict) contains the dimensions of the table:
            n_rows, n_cols, column_widths, and table_width
        working_inv

    Returns:
        header_str: (str) text representation of the row, with the proper delimeters
    """
    prefix = {
        "terminal": "",
        "html": "    <td>",
        "csv": "",
    }
    suffix = {
        "terminal": " | ",
        "html": "</td>\n",
        "csv": "",
    }
    body_str = ""

    for row in range(dimensions["n_rows"]):
        row_str = ""
        for col in working_inv.keys():
            column_values = working_inv[col]
            row_str += prefix[style]
            if style == "terminal":
                row_str += str(column_values[row]).ljust(dimensions["column_widths"].get(col))
            else:
                row_str += column_values[row]
            row_str += suffix[style]

        if style == "terminal":
            row_str = "| " + row_str[:-1] + "\n"
        elif style == "html":
            row_str = "<tr>\n" + row_str + "</tr>\n"
        elif style == "csv":
            row_str = row_str + "\n"

        body_str += row_str

    return body_str

def main():
    inv = startup()
    inv.print_to_terminal(index=False)
    while True:
        action = prompt()
        result = perform_action(inv, action)
        if result == "EXIT":
            break


if __name__ == "__main__":
    main()
