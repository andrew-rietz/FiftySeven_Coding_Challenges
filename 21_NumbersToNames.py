"""

Many programs display information to the end user in
one form but use a different form inside the program.
For example, you may show the word 'Blue' on the
screen, but behind the scenes you'll have a numerical
value for that color or an internal value because you
may need to represent the textual description in
another languagae for Spanish-speaking visitors.

Write a program that converts a number from 1 to 12 to
the corresponding month. Prompt for a number and
display the corresponding calendar month, with 1 being
January and 12 being December. For any value outside
that range, display an appropriate error message.

___________________
Example Output
___________________
Please enter the number of the month:
The name of the month is March.

___________________
Constraints
___________________
Use a switch or case statement for this program.
Use a single output statement for this program.

"""
# NOTE: Python does not support switch / case statments.
# Will implement using a dictionary instead.

months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

num_val = int(input("Please enter the number of the month: "))
print(f"The name of the month is {months[num_val]}.")
