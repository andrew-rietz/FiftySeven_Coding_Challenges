'''

Computing simple interest is a great way to quickly
figure out whether an investment has value. It's
also a good way to get comfortable with explicitly
coding the order of operations in your programs.

Create a program that computes simple interest.
Prompt for the principal amount, the rate as a
percentage, and the time, and display the
amount accrued (principal + interest).

The formula for simple interest is A = P * (1 + r *t),
where P is the principal amount, r is the annual rate
of interest, t is the number of years the amount is
invested, and A is the amount at the end of the
investment.

___________________
Example Output
___________________
Enter the principal: 1500
Enter the rate of interest: 4.3
Enter the number of years: 4

After 4 years at 4.3%, the investment will
be worth $1758.

___________________
Constraints
___________________
Prompt for the rate as a percentage (like 15, not
0.15). Divide the input by 100 in your program.
Ensure the fractions of a cent are rounded up to the
next penny.
Ensure that the output is formatted as money.

'''
import math

'Create a constant to convert %s'
conv_pct = 100

principal = float(input('Enter the principal: '))
rate = float(input('Enter the rate of interest: '))
years = float(input('Enter the number of years: '))

accrued = round(principal * (1+(rate/conv_pct)*years),2)
accrued = '{:,.2f}'.format(accrued)
principal = '{:,.2f}'.format(principal)

print(f'''
After {years} years at {rate}%, the initial \
investment of ${principal} will
be worth ${accrued}\
''')
