"""
Defines a filter_even_numbers function
"""
import re


def filter_even_numbers(input_string):
    """Takes in a space-delimited string and returns the even numbers contained
    in the string

    Args:
        input_string (str): space-delimited string

    Returns:
        (dict):
            {
                "even_numbers": [list of the even numbers from input_string],
                "removed_values": [list of all other values from input_string],
            }

    """
    result = {
        "even_numbers": [],
        "removed_values": [],
    }
    for char in re.split(r" +", input_string.strip(" ")):
        try:
            if float(char) % 2 == 0:
                result["even_numbers"].append(str(char))
            else:
                result["removed_values"].append(str(char))
        except ValueError:
            result["removed_values"].append(str(char))

    return result


def main():
    user_input = input("Enter a list of numbers, separated by spaces: ")
    result = filter_even_numbers(user_input)

    if result["even_numbers"]:
        print(f"The even numbers are {', '.join(result['even_numbers'])}. ")
    if result["removed_values"]:
        print(f"The removed values are {', '.join(result['removed_values'])}.")

if __name__ == "__main__":
    main()
