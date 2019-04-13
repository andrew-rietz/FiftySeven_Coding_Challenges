'''

Working with multiple inputs and currency can
introduce some tricky precision issues.

Create a simple self-checkout system. Prompt for the
prices and quantities of three items. Calculate the
subtotal of the items. Then calculate the tax using a
tax rate of 5.5%. Print out the line items with the
quantity and total, and then print out the subtotal,
tax amount, and total.

___________________
Example Output
___________________
Enter the price of item 1: 25
Enter the quantity of item 1: 2
Enter the price of item 2: 10
Enter the quantity of item 2: 2
Enter the price of item 3: 4
Enter the quantity of item 3: 1
Subtotal: $64.00
Tax: $3.52
Total: $67.52

___________________
Constraints
___________________
Keep the input, processing, and output parts of
your program separate. Collect the input, then do the
math operations and string building, and then print
out the output
Be sure you explicitly convert input to numerical data
before doing any calcluations.

'''

price = {}
qty = {}
subtotal = 0

'Tax rate is set as a constant 5.5%'
tax_rate = 0.055

for item in range(1,4):
    p = input(f'Enter the price of item {item}: ')
    price[item] = round(float(p),2)

    q = input(f'Enter the quantity of item {item}: ')
    qty[item] = round(float(q),2)

    subtotal += price[item] * qty[item]

subtotal = round(subtotal,2)
tax = round(subtotal * tax_rate,2)
total = round(subtotal + tax,2)

subtotal = '{:.2f}'.format(subtotal)
tax = '{:.2f}'.format(tax)
total = '{:.2f}'.format(total)


print(f'''\
Subtotal: ${subtotal}
Tax: ${tax}
Total: ${total}\
''')
