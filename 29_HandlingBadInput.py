"""

The rule of 72 is a quick method for estimating how
long it will take to double your investment, by
taking the number 72 and dividing it by the expected
rate of return. It's a good tool that helps you
figure out if the stock, bond, or savings account is
right for you. It's also a good program to write to
test for and prevent bad input because computers can't
divide by zero. And instead of exiting the program
when the user enters invalid input, you can just
keep prompting for inputs until you get one that's
valid.

Write a quick calculator that prompts for the rate of
return on an investment and calculates how many years
it will take to double your investment.

The formula is

years = 72/r

where r is the stated rate of return

___________________
Example Output
___________________
What is the rate of return? 0
Sorry. That's not a valid input.
What is the rate of return? ABC
Sorry. That's not a valid input.
What is the rate of return? 4
It will take 18 years to double your initial investment

___________________
Constraints
___________________
Don't allow the user to enter 0
Don't allow non-numeric values
Use a loop to trap bad input, so you can ensure
that the user enters valid values

"""


def main():

    rate = validateInput("What is the rate of return? ")
    years = calcYears(rate)

    print(f"It will take {years} years to double your initial investment.")


def validateInput(prompt):
    while True:
        inpt = input(f"{prompt}")
        try:
            inpt = float(inpt)
            if float(inpt) < 0:
                print("Sorry - input invalid. Please enter a positive number.")
            elif float(inpt) == 0:
                print(
                    "Sorry - input invalid. Please enter a positive (non-zero) number."
                )
            else:
                break
        except ValueError:
            print("Sorry - input invalid. Please enter a positive number.")
    return float(inpt)


def calcYears(r):
    return round(72 / r, 2)


main()
