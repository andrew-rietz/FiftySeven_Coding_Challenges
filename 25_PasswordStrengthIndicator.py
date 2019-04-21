"""

Functions help you abstract away complex operations,
but they also help you build reusable components.

Create a program that determines the complexity of a
given password based on these rules:

- A very weak password contains only numbers and is
fewer than eight characters
- A weak password contains only letters and is fewer
than eight characters.
- A strong password contains letters and at least one
number and is at least eight characters.
- A very strong password contains letters, numbers,
and special characters and is at least eight
characters.

___________________
Example Output
___________________
The password '123456' is a very weak password.
The password 'abcdef' is a weak password.
The password 'abc123xyz' is a strong password.
The password '1337h@xor!' is a very strong password.

___________________
Constraints
___________________
Create a passwordValidator function that takes in the
password as its argument and returns a value you can
evaluate to determine the password length. Do not have
the function return a string - you may need to
support multiple languages in the future.
Use a single output staement.

"""


def passwordValidator(pw):
    letters = [c for c in pw if c.isalpha()]
    digits = [c for c in pw if c.isdigit()]
    special = [c for c in pw if c in "!@#$%^&*()_-+=?<>"]

    strength = 0
    if len(letters) > 0:
        strength += 1
    if len(digits) > 0:
        strength += 1
    if len(special) > 0:
        strength += 1
    if len(pw) >= 8:
        strength += 1
    if len(pw) == len(letters):
        strength = 2
    if len(pw) < 8:
        strength = min(strength, 2)

    if " " in pw:
        print("Passwords cannot include spaces.")
        strength = -1

    return strength


def main():

    pws = ["s p a c e s", "12345", "abcdef", "abc123xyz", "1337h@xor!"]
    strength = {
        1: "a very weak password",
        2: "a weak password",
        3: "a strong password",
        4: "a very strong password",
        -1: "an invalid password (includes spaces)",
    }

    for pw in pws:
        val = passwordValidator(pw)
        print(f"The password '{pw}' is {strength[val]}.")


main()
