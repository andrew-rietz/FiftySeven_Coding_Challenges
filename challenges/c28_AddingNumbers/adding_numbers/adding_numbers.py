"""
Defines a function that determines the maximum value in a list
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util_functions.utils import user_inputs


def get_numbers_to_sum(n_inputs):
    """Prompts the user to enter the numbers to sum

    Args:
        n_inputs (int): Defines how many numbers to prompt the user for

    Returns:
        numbers_to_sum (obj): A list of numbers
    """
    numbers_to_sum = []
    for _ in range(n_inputs):
        numbers_to_sum.append(float(
            user_inputs.get_any_number(
                prompt="Enter a number:",
                err_msg="Please enter a valid number."
            )
        ))
    return numbers_to_sum

def sum_numbers(numbers_to_sum):
    return sum(numbers_to_sum)

def print_result(total):
    return f"The total is {total:,.1f}."

def how_many_numbers():
    """Prompts the user to define how many numbers should be prompted for and summed

    Returns:
        (int): Number of inputs that should be prompted for in a subsequent step
    """
    n_inputs = user_inputs.get_positive_number(
        prompt="How many numbers do you want to add?",
        err_msg="Please enter a valid number."
    )
    return int(n_inputs)

def main():
    n_inputs = how_many_numbers()
    numbers_to_sum = get_numbers_to_sum(n_inputs)
    total = sum_numbers(numbers_to_sum)
    print(print_result(total))


if __name__ == "__main__":
    main()
