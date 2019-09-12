"""
Defines a set of reusable functions that help process and validate user inputs
"""

def get_positive_number(prompt, err_msg, exit_val=None):
    """Prompts user for input until they enter a positive number

    Args:
        prompt: Prompt the user for input
        err_msg: Message to be displayed if user provides bad input
        exit: Value which will allow user to exit the loop and cause function to return None

    Returns:
        positive_val: Positive numeric value from user
    """
    while True:
        user_val = input(f"{prompt.strip()} ")
        if user_val == exit_val:
            return None
        if user_val is None:
            continue
        try:
            positive_val = float(user_val.replace(",", ""))
            if positive_val < 0:
                raise ValueError("Enter value must be greater than zero.")
            break
        except (ValueError, TypeError):
            print(f"{err_msg.strip()} ", end="")

    return positive_val

def get_any_number(prompt, err_msg, exit_val=None):
    """Prompts user for input until they enter any number. Will exit
    and return 'None' if the user enters the exit phrase

    Args:
        prompt: Prompt the user for input
        err_msg: Message to be displayed if user provides bad input
        exit: Value which will allow user to exit the loop and cause function to return None

    Returns:
        positive_val: Numeric value from user, or None if exit phrase is entered
    """
    while True:
        user_val = input(f"{prompt.strip()} ")
        if user_val == exit_val:
            return None
        if user_val is None:
            continue
        try:
            numeric_val = float(user_val.replace(",", ""))
            break
        except (ValueError, TypeError):
            print(f"{err_msg.strip()} ", end="")

    return numeric_val

def get_string_in_list(prompt, err_msg, allowed_vals, case_sensitive=False, exit_val=None):
    """Prompts user for input until they enter an allowed value

    Args:
        prompt: Prompt the user for input
        err_msg: Message to be displayed if user provides bad input
        allowed_vals: List of expected values allowed by the function
        case_sensitive: (Default = True) Tests the values in a case_sensitive manner
        exit: Value which will allow user to exit the loop and cause function to return None

    Returns:
        accepted_val: User input from the given list of allowed values
    """
    if not case_sensitive:
        allowed_vals = [val.lower() for val in allowed_vals]

    while True:
        user_val = input(f"{prompt.strip()} ").strip()
        if user_val == exit_val:
            return None
        test_val = user_val.lower() if not case_sensitive else user_val
        if test_val not in allowed_vals:
            print(err_msg.strip(), end=" ")
            continue
        return user_val
