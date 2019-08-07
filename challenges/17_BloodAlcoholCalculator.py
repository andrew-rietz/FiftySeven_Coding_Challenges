"""

Sometimes you have to perform a more complex
calculation based on some provided inputs and then use
that result to make a determination.

Create a program that prompts for your weight, gender,
number of drinks, the amount of alcohol by volume of
the drinks consumed, and the amount of time since your
last drink. Calculate your blood alcohol content (BAC)
using this formula.

    BAC = (A * 5.14 / W * r) - 0.015 * H

Where
A = total alcohol consumed in ounces
W = body weight in pounds
r = alcohol distribution ratio
    = 0.73 for men
    = 0.66 for women
H = number of hours since the last drink

Display whether or not it's legal to drive by
comparing the BAC to 0.08

___________________
Example Output
___________________
Your BAC is 0.08
It is not legal for you to drive.

___________________
Constraint
___________________
Prevent the user from entering non-numeric values.

"""

# Create a dictionary to hold common assumptions
# for alcohol content of beverages

alc = {"beer": 5, "wine": 12, "liquor": 40}
oz = {"beer": 12, "wine": 5, "liquor": 1.5}
gender = input("What is your gender (M/F)? ")
while True:
    try:
        weight = float(input("How much do you weigh (in pounds)? "))
        break
    except ValueError:
        print("Please enter a numeric value.")
while True:
    try:
        drinks = float(input("How many drinks have you had? "))
        break
    except ValueError:
        print("Please enter a numeric value.")
type = input("Are you drinking beer, wine, or liquor? ")
while True:
    try:
        last_drink = float(input("How long ago was your last drink (in hours)? "))
        break
    except ValueError:
        print("Please enter a numeric value.")

r = 0.73 if gender.upper() == "M" else 0.66

alcohol = drinks * oz[type] * alc[type] / 100
bac = round((alcohol * 5.14 / weight * r) - 0.015 * last_drink, 2)

legal = "not legal" if bac >= 0.08 else "legal"

print(
    f"""
Your BAC is {'{:.2f}'.format(bac)}.
It is {legal} for you to drive.
"""
)
