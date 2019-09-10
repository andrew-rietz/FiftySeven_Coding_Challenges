"""
Defines a function that estimates the number of years to double an investment
"""

def get_positive_nonzero_number(prompt, err_msg):
    """Prompts the user for a positve non-zero number

    Args:
        prompt (str): Prompt for the end user
        err_msg (str): Error message displayed if input is invalid

    Returns:
        number (float): A positive non-zero number
    """
    while True:
        number = input(f"{prompt} ")
        try:
            number = float(number)
            if float(number) <= 0:
                print(err_msg)
            else:
                break
        except ValueError:
            print(err_msg)

    return number


def calc_years_to_double(rate_of_return):
    """Estimates the number of years to double an investment using the rule of 72

    Args:
        rate_of_return (float): Stated rate of return

    Returns:
        (float): Estimated number of years to double investment
    """
    return 72 / rate_of_return

def print_result(years):
    return f"It will take {years} years to double your initial investment."

def main():

    rate_of_return = get_positive_nonzero_number(
        prompt="What is the rate of return?",
        err_msg="Invalid entry. Please enter a number greater than zero."
    )
    years = calc_years_to_double(rate_of_return)
    print(print_result(years))

if __name__ == "__main__":
    main()
