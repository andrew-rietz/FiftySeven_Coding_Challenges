"""

You don't always need a complex control structure to
solve simple problems. Sometimes a program requires
an extra step in one case, but in all other cases
there's nothing to do.

Write a simple program to compute the tax on an
order amount. The program should prompt for the
order amount and the state. If the state is 'WI',
then the order must be charged 5.5% tax. The
program should display the subtotal, tax, and
total for Wisconsin residents but display just
the total for non-residents.

___________________
Example Output
___________________
What is the order amount? 10
What is the state? WI
The subtotal is $10.00.
The tax is $0.55.
The total is $10.55.

** or **

What is the order amount? 10
What is the state? MN
The total is $10.00.

___________________
Constraints
___________________
Implement this program using only a simple if
statement (don't use an else clause)
Ensure all the money is rounded to the nearest cent.
Use a single output statement at the end of the
program to display the program results

"""

subtotal = float(input("What is the order amount? "))
state = str(input("What is the state? "))
tax_rate = 0
out = ""

if state.upper() == "WI":
    tax_rate = 0.055
    tax = round(subtotal * tax_rate, 2)

    out += f"""The subtotal is ${'{:,.2f}'.format(subtotal)}.\n"""
    out += f"""The tax is ${'{:,.2f}'.format(tax)}.\n"""

total = "{:,.2f}".format(round(subtotal * (1 + tax_rate), 2))
out += f"The total is ${total}."
print(out)
