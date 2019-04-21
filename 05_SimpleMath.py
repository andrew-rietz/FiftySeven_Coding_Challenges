"""

You'll often write program that deal with numbers. And
depending on the programming language you use, you'll
have to convert the inputs you get to numerical data
types.

Write a program that prompts for two numbers. Print
the sum, difference, product, and quotient of those
numbers as shown in the example output

___________________
Example Output
___________________
What is the first number? 10
What is the second number? 5
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2

___________________
Constraints
___________________
Values coming from the user will be strings. Ensure
that you convert these values to numbers before
doing the match.
Keep inputs and outputs separate from the numerical
conversions and other processing.
Generate a single output statement with line breaks
in the appropriate spots.

"""

firstnum = input("What is the first number? ")
secondnum = input("What is the second number? ")

firstnum = float(firstnum)
secondnum = float(secondnum)

sum = round(firstnum + secondnum, 1)
difference = round(firstnum - secondnum, 1)
product = round(firstnum * secondnum, 1)
quotient = round(firstnum / secondnum, 1)

print(
    f"""
    {firstnum} + {secondnum} = {sum}\n
    {firstnum} - {secondnum} = {difference}\n
    {firstnum} * {secondnum} = {product}\n
    {firstnum} / {secondnum} = {quotient}
"""
)
