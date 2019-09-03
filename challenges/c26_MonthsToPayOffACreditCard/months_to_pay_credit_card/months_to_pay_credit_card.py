"""
Defines and calls a function that compute number of months to pay off a credit card
"""
import os
import sys
from math import log10, ceil

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util_functions.utils import user_inputs

def calculate_months_until_paid_off(balance, apr, payment):
    """Computes the number of months to pay off credit card debt

    Args:
        balance (float): Current balance on the card
        apr (float): Annual percentage rate (interest rate). Must be entered as a percentage.
            For example, 12% would be entered as `12` not `0.12`.
        payment (float): Monthly payment the user can make

    Returns:
        months (int): Number of months until the card is payed off
    """
    daily_interest = apr / 100 / 365
    months = (
        (-1.0 / 30) *
        log10(1 + (balance / payment) * (1 - (1 + daily_interest) ** 30)) /
        log10(1 + daily_interest)
    )
    return ceil(months)


def main():
    balance = user_inputs.get_positive_number(
        prompt="What is your balance?",
        err_msg="Please enter a positive number."
    )
    apr = user_inputs.get_positive_number(
        prompt="What is the APR on the card (as a percent)?",
        err_msg="Please enter a positive percentage (i.e., 12% is entered as 12)."
    )
    payment = user_inputs.get_positive_number(
        prompt="What is the monthly payment you can make?",
        err_msg="Please enter a positive number."
    )

    months = calculate_months_until_paid_off(balance, apr, payment)
    print(f"\nIt will take you {months} months to pay off this card.")


if __name__ == "__main__":
    main()
