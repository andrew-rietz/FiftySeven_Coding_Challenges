"""
Defines a function that determines the maximum value in a list
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util_functions.utils import user_inputs

def max_in_list(list_of_vals):
    """Takes a list and returns the maximum. If the provided list is empty
    returns None

    Args:
        list_of_vals: (list) A list of values to compare

    Returns:
        max_val: The maximum value (or 'None' if all values are the same)
    """
    if len(set(list_of_vals)) < 1:
        return None

    max_val = list_of_vals[0]
    for val in list_of_vals:
        if val > max_val:
            max_val = val
    return max_val

def prompt():
    """Prompt user for the desired input"""

    user_in = user_inputs.get_any_number(
        prompt="Enter a number (or enter a blank value to exit):",
        err_msg="Please enter a valid number.",
        exit_val=""
    )
    return user_in

def output(max_val):
    """Return a string to be printed to stdout"""

    if max_val is None:
        return "Sorry, you must provide at least one number."

    return f"The largest number is {max_val}."

def main():
    numbers = []
    while True:
        num = prompt()
        if num is None:
            break
        numbers.append(num)

    max_val = max_in_list(numbers)
    print(output(max_val))
