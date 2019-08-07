"""
Defines a set of reusable functions that help process and validate user inputs
"""

def get_positive_number(prompt, err_msg):
    """Prompts user for input until they enter a positive number

    Args:
        prompt: Prompt the user for input
        err_msg: Message to be displayed if user provides bad input

    Returns:
        positive_val: Positive numeric value from user
    """
    while True:
        try:
            positive_val = float(input(f"{prompt.strip()} "))
            if positive_val < 0:
                raise ValueError
            break
        except (ValueError, TypeError):
            print(f"{err_msg.strip()} ", end="")

    return positive_val

def get_any_number(prompt, err_msg):
    """Prompts user for input until they enter a positive number

    Args:
        prompt: Prompt the user for input
        err_msg: Message to be displayed if user provides bad input

    Returns:
        positive_val: Positive numeric value from user
    """
    while True:
        try:
            numeric_val = float(input(f"{prompt.strip()} "))
            break
        except (ValueError, TypeError):
            print(f"{err_msg.strip()} ", end="")

    return numeric_val

def get_string_in_list(prompt, err_msg, allowed_vals, case_sensitive=False):
    """Prompts user for input until they enter an allowed value

    Args:
        prompt: Prompt the user for input
        err_msg: Message to be displayed if user provides bad input
        allowed_vals: List of expected values allowed by the function
        case_sensitive: (Default = True) Tests the values in a case_sensitive manner

    Returns:
        accepted_val: User input from the given list of allowed values
    """
    if not case_sensitive:
        allowed_vals = [val.lower() for val in allowed_vals]

    while True:
        user_val = input(f"{prompt.strip()} ")
        test_val = user_val.lower() if not case_sensitive else user_val
        if test_val not in allowed_vals:
            print(err_msg.strip(), end=" ")
            continue
        return user_val
