'''

Simple interest is something you use only when
making a quick guess. Most investments use a
compound interest formula, which will be much
more accurate. And this formula requires you to
incorporate exponents into your programs.

Write a program to computer the value of an investment
compounded over time. The program should ask for the
starting amount, the number of years to invest, the
interest rate, and the number of periods per year
to compound.

The formula you'll use for this is:

A = P * (1 + (r/n)) ** (n*t)

Where:
P is the principal amount
r is the annual rate of interest
t is the number of years the amount is invested
n is the number of times the interest is compounded
     per year
A is the amount at the end of the investment

___________________
Example Output
___________________
What is the principal amount? 1500
What is the rate? 4.3
What is the number of years? 6
What is the number of times the interest rate is
compounded per year? 4

$1500 invested at 4.3% for 6 years compounded 4
times per year is $1938.84

___________________
Constraints
___________________
Prompt for the rate as a percentage (life 15, not .15)
Divide the input by 100 in your program
Ensure the fractions of a cent are rounded up to the
next penny.
Ensure the output is formatted as money

'''

import math

'Create a constant to convert %s'
conv_pct = 100

principal = float(input('What is the principal amount? '))
rate = float(input('What is the rate? '))
years = float(input('What is the number of years? '))
n = float(input('What is the number of times the interest is compounded per year? '))

accrued = round(principal * (1+(rate/conv_pct/n)) ** (n * years),2)
accrued = '{:,.2f}'.format(accrued)
principal = '{:,.2f}'.format(principal)

print(f'''
${principal} invested at {rate}% for {years} years
compounded {n} times per year is ${accrued}.
''')
