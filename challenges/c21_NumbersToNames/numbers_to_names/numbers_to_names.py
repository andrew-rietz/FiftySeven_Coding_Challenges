"""
Defines a function that converts a numeric value to the name of a month
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util_functions.utils import user_inputs

def month_number_to_name(number):
    """Converts a numeric value to the name of a month

    Args:
        number: (int) The number of a month (i.e., in the range 1-12)

    Returns:
        name: (str) The name of the month
    """
    numbers_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    return numbers_names[number]

def main():
    num = int(user_inputs.get_string_in_list(
        prompt="Please enter the number of the month (i.e., 1-12):",
        err_msg="Please enter a value between 1 and 12.",
        allowed_vals=[str(n) for n in range(1, 13)]
    ))
    name = month_number_to_name(num)
    print(f"The name of the month is {name}.")
