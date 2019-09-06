"""
Defines a set of functions that validate user input, then validates some user inputs
"""
import re

def _validate_name(name_type, name):
    """Checks that a provided name is valid

    Names must be at least two characters long and cannot be blank

    Args:
        name_type (str):
        name (str): The name to be validated

    Returns:
        (str): Returns an error message is there is an issue with the name,
            otherwise returns an empty string
    """
    name_type = name_type + " " if name_type else name_type
    if not name:
        return f"The {name_type}name must be filled in."

    if not re.fullmatch("[a-zA-Z]{1,}", name):
        return f"{name} is not a valid {name_type}name. Names may only contain letters."

    if not re.match("[A-Za-z]{2,}", name):
        return f"{name} is not a valid {name_type}name. It is too short."

    return ""

def get_name(name_type, prompt):
    """Prompts the user for a name and checks that input is valid

    If the input is invalid, provides an error message describing the issue

    Args:
        name_type (str): Indicates whether to prompt for a first, middle, or last name
        prompt (str): Prompt the user sees

    Returns:
        result (dict): Dictionary with two keys, `error` and `user_value`
    """
    user_val = input(f"{prompt.strip()} ").strip()
    result = {"error": "", "user_val": None}

    error = _validate_name(name_type, user_val)
    if error:
        result["error"] = error
        return result

    result["user_value"] = user_val
    return result

def _validate_zip_code(zip_code):
    """Checks that a zip code is valid

    Zip codes must be either 5-digit number, a 9-digit number, or a five-digit number
    followed by a hyphen (-) and then a 4-digit number

    Args:
        zip_code (str): Zip code to be validated

    (str): Returns an error message is there is an issue with the zip code,
        otherwise returns an empty string
    """

    five_digit_zip = "[0-9]{5}"
    nine_digit_zip = "[0-9]{5}\-{0,}[0-9]{4}"
    if not (re.fullmatch(five_digit_zip, zip_code) or re.fullmatch(nine_digit_zip, zip_code)):
        return "The ZIP code must be either a five- or nine-digit number."

    return ""

def get_zip_code(prompt):
    """Prompts the user for a zip code and checks that input is valid

    If the input is invalid, provides an error message describing the issue

    Args:
        prompt (str): Prompt the user sees

    Returns:
        result (dict): Dictionary with two keys, `error` and `user_value`
    """
    user_val = input(f"{prompt.strip()} ").strip()
    result = {"error": "", "user_val": None}

    error = _validate_zip_code(user_val)
    if error:
        result["error"] = error
        return result

    result["user_value"] = user_val
    return result

def _validate_employee_id(employee_id):
    """Checks that an employee ID is of the format 'AA-0000' (i.e., two upper case letters,
    followed by a hyphen, followed by four numbers)

    Args:
        employee_id (str): Employee ID to be validated

    (str): Returns an error message is there is an issue with the employee id,
        otherwise returns an empty string
    """
    if not re.fullmatch("[A-Z]{2}\-[0-9]{4}", employee_id):
        return f"{employee_id} is not a valid ID."

    return ""

def get_employee_id(prompt):
    """Prompts the user for an employee ID and checks that input is valid

    If the input is invalid, provides an error message describing the issue

    Args:
        prompt (str): Prompt the user sees

    Returns:
        result (dict): Dictionary with two keys, `error` and `user_value`
    """
    user_val = input(f"{prompt.strip()} ").strip()
    result = {"error": "", "user_val": None}

    error = _validate_employee_id(user_val)
    if error:
        result["error"] = error
        return result

    result["user_value"] = user_val
    return result

def validate_input():
    """
    Gathers and validates user input. Then returns a list of errors or reports
    that no errors were found.
    """
    first_name = get_name("first", "Enter the first name:")
    last_name = get_name("last", "Enter the last name:")
    zip_code = get_zip_code("Enter the ZIP code:")
    employee_id = get_employee_id("Enter an employee ID:")

    errors = []
    if first_name["error"]:
        errors.append(first_name["error"])
    if last_name["error"]:
        errors.append(last_name["error"])
    if zip_code["error"]:
        errors.append(zip_code["error"])
    if employee_id["error"]:
        errors.append(employee_id["error"])

    return errors if errors else ["There were no errors found."]


def main():
    input_validation = validate_input()
    print("\n".join(input_validation))


if __name__ == "__main__":
    main()
