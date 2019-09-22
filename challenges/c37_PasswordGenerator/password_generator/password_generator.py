"""
Defines a PasswordGenerator class and instantiates an instance
"""
import string
import sys
import os
from random import choices, sample

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util_functions.utils import user_inputs


class PasswordGenerator():
    """Represents a password generator object. Generates a password of specified
    length, number of special characters, and number of numeric characters

    Attributes:
        length (int): Required length of the password
        n_special (int): Number of special characters required
        n_numeric (int): Number of numeric values required
    """
    special_chars = r"!#$%&()*+-./:<=>?@[\]^_{|}~"
    numeric_chars = string.digits
    alpha_chars = string.ascii_letters

    def __init__(self):
        self.length = 0
        self.n_special = 0
        self.n_numeric = 0

    def generate(self):
        possible_values = []
        possible_values.extend(choices(self.special_chars, k=self.n_special))
        possible_values.extend(choices(self.numeric_chars, k=self.n_numeric))
        possible_values.extend(choices(self.alpha_chars, k=(self.length - len(possible_values))))
        password = "".join(sample(possible_values, self.length))
        return password


def get_pw_length():
    length = user_inputs.get_positive_number(
        prompt="What's the minimum length?",
        err_msg="Please enter a positive number."
    )
    return length

def get_n_special(max_special):
    n_special = user_inputs.get_string_in_list(
        prompt=f"How many special characters? [0 - {max_special}]:",
        err_msg="Please enter a valid choice.",
        allowed_vals=[str(val) for val in range(max_special + 1)]
    )
    return n_special

def get_n_numeric(max_numeric):
    n_numeric = user_inputs.get_string_in_list(
        prompt=f"How many numbers? [0 - {max_numeric}]:",
        err_msg="Please enter a valid choice.",
        allowed_vals=[str(val) for val in range(max_numeric + 1)]
    )
    return n_numeric

def main():
    pw = PasswordGenerator()
    length = int(get_pw_length())
    n_special = int(get_n_special(length))
    if n_special == length:
        n_numeric = 0
    else:
        n_numeric = int(get_n_numeric(length - n_special))

    pw.length = length
    pw.n_special = n_special
    pw.n_numeric = n_numeric
    password = pw.generate()
    print(f"Your password is:\n{password}")


if __name__ == "__main__":
    main()
