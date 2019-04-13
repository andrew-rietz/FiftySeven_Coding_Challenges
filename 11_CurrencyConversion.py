'''

At some point, you might have to deal with
currency exchange rates, and you'll need to ensure
your calculations are as precise as possible.

Write a program that converts currency. Specfically,
convert euros to US dollars. Prompt for the amount
of money in euros you have, and prompt for the
current exchange rate of the euro. Print out the
new amount in US dollars. The formula for currency
conversion is:

(amount_to) = ((amount_from) * (rate_from / rate_to))

where:
- amount_to is the amount in US dollars
- amount_from is the amount in euros
- rate_from is the current exchange rate in euros
- rate_to is the current exchange rate of the dollar

___________________
Example Output
___________________
How many euros are you exchanging? 81
What is the exchange rate? 137.51
81 euros at an exchange rate of 137.51 is
111.38 dollars

___________________
Constraints
___________________
Ensure that fractions of a cent are rounded up
to the next penny
Use a single output statement

'''

import math

amount_from = float(input('How many euros are you exchanging? '))
rate_from = float(input('What is the exchange rate? '))
rate_to = 100

amount_to = round(amount_from * rate_from / rate_to,2)

print(f'''\
{amount_from} euros at an exchange rate of {rate_from} is
{amount_to} U.S. dollars.\
''')
