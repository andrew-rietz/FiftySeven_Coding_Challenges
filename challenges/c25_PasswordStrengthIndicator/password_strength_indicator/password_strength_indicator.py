"""
Defines and calls a function that validates a password
"""

def password_validator(password):
    """Function that checks password strength based on a set of rules

    Args:
        password (str): The password to be validated (non-hashed)

    Returns:
        strength (int): Numeric rating of the passwords strength. Higher number indicates a
            more secure password. Invalid passwords receive a `None` value.
    """
    letters = [char for char in password if char.isalpha()]
    digits = [char for char in password if char.isdigit()]
    special = [char for char in password if char in "!@#$%^&*()_-+=?<>"]

    if " " in password:
        return None

    strength = 0
    strength += len(letters) > 0
    strength += len(digits) > 0
    strength += len(special) > 0
    strength += len(password) >= 8

    if len(password) < 8:
        if len(password) == len(letters):
            return 2
        return min(strength, 2)

    return strength


def main():

    passwords = ["s p a c e s", "12345", "abcdef", "abc123xyz", "1337h@xor!"]
    strength = {
        1: "a very weak password",
        2: "a weak password",
        3: "a strong password",
        4: "a very strong password",
        None: "an invalid password (includes spaces)",
    }

    for password in passwords:
        val = password_validator(password)
        print(f"The password '{password}' is {strength[val]}.")


if __name__ == "__main__":
    main()
