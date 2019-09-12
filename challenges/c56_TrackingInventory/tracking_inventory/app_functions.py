"""
Defines the primary functions used by the application.

Functions:
    startup: Check for data in local storage. If it exists, load it into a new PersonalInventory
        class instance. Otherwise initiate a new, blank, instance of the same class.
    prompt: Prompts the user for an action and returns the selection
    perform_action: Takes a PersonalInventory class object and an action. Performs the given action
        on the object
"""
import json
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tracking_inventory.personal_inventory_class import PersonalInventory

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util_functions.utils import user_inputs


def startup(basedir=None, subdir="data", filename="local_storage.json"):
    """Check for data in local storage. If it exists, load it into a new PersonalInventory
    class instance. Otherwise initiate a new, blank, instance of the same class.

    Args:
        basedir (str): Absolute filepath for the directory the local json file is located within
        subdir (str): Optional subdirectory that the local json file is located within
        filename (str): Optional - name of the local json file

    Returns:
        inv (obj): A PersonalInventory class object
    """
    if basedir is None:
        basedir = os.path.dirname(os.path.abspath(__file__))

    filepath = (
        os.path.join(basedir, subdir, filename)
    )
    try:
        with open(filepath, "r") as local_file:
            stored_inventory = json.load(local_file)
        inv = PersonalInventory(stored_inventory)

    except FileNotFoundError:
        inv = PersonalInventory()

    return inv

def prompt():
    """Prompts the user for an action and returns the selection"""

    allowed_vals = ["Add", "Remove", "Print", "To CSV", "To HTML", "Save", "Exit"]
    action = user_inputs.get_string_in_list(
        prompt=f"What would you like to do? [{', '.join(allowed_vals)}]:",
        err_msg="Sorry, please enter a valid selection",
        allowed_vals=allowed_vals,
        case_sensitive=False,
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
