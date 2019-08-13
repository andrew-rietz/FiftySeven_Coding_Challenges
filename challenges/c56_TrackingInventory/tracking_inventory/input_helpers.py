"""
Helper functions used during the application.

Functions:
    _get_item_name: Prompts user for the name of an item
    _get_serial: Prompts user for the serial number of an item
    _get_value: Prompts user for the value of an item. User input must be numeric
"""
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util_functions.utils import user_inputs


def _get_item_name():
    """
    Prompts user for the item_name of an item and returns a cleaned version. Because
    this is intended to be compatible with CSV exports, coerce all commas to underscores.

    Args: n/a

    Returns:
        item_name: (str) Serial number input by the user
    """
    while True:
        item_name = input("What is the item's name? (Or type quit() to exit): ")
        if item_name == "quit()":
            return None
        if (item_name is None) or (item_name.strip() == ""):
            print("Sorry, that is not a valid name.", end=" ")
            continue

        return item_name.strip()

def _get_serial():
    """
    Prompts user for the serial number of an item and returns a cleaned version. Because
    this is intended to be compatible with CSV exports, coerce all commas to underscores.

    Args: n/a

    Returns:
        serial: (str) Serial number input by the user
    """
    while True:
        serial = input("What is the item's serial number? (Or type quit() to exit): ")
        if (serial is None) or (serial.strip() == ""):
            print("Sorry, that is not a valid serial number.", end=" ")
            continue
        if serial == "quit()":
            confirm = input(
                "Are you sure you want to quit? The item will be discarded. [Y/N]: "
            )
            if confirm.strip().upper()[0] == "Y":
                return None
            continue
        return serial.strip()

def _get_value():
    """Prompts user for the value of an item. Value must be numeric

    Args: n/a

    Returns:
        (str) numeric value formatted as float with two decimals
    """
    while True:
        value = user_inputs.get_any_number(
            prompt="What is the item's value? (Or type quit() to exit)",
            err_msg="Sorry, that is not a valid value.",
            exit_val="quit()"
        )
        if value is None:
            confirm = input(
                "Are you sure you want to quit? The item will be discarded. [Y/N]: "
            )
            if confirm.strip().upper()[0] == "Y":
                return None
            continue
        return f"${value:,.2f}"
