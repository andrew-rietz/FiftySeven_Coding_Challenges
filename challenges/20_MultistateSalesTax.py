"""

More complex programs may have decisions nested in
other decisions, so that when one decision is made,
additional decisions must be made.

Create a tax calculator that handles multiple states
and multiple counties within each state. The program
prompts the user for the order amount and the state
where the order will be shipped.

For WI residents, prompt for the county of residence
 - For Eau Claire county, add an additional 0.005 tax
 - for Dunn county, add an additional 0.004 tax

 Illinois residents must be charged 8% sales tax with
 no additional county-level charge. All other states
 are not charged tax. The program then displays the
 tax and the total for Wisconsin and Illinois
 residents by just the total for everyone else.

 ___________________
 Example Output
 ___________________
 What is the order amount? 10
 What state do you live in? Wisconsin
 The tax is $0.50
 The total is $10.50

 ___________________
 Constraints
 ___________________
 Ensure that all money is rounded to the nearest
 cent
 Use a single output statement at the end of the
 program to display the program results

 """

tax_rate = 0
out = ""

# Create dictionaries to hold the tax rate for each state / county
county_tax = {"WI": {"Eau Claire": 0.005, "Dunn": 0.004}}
state_tax = {"IL": 0.08, "WI": 0.05}

while True:
    try:
        subtotal = float(input("What is the order amount? "))
        break
    except ValueError:
        print("Please enter a numeric value.")

state = input("What state do you live in? ")

if state in state_tax:
    if state in county_tax:
        county = input("What county do you live in? ")
        if county in county_tax[state]:
            tax_rate = state_tax[state] + county_tax[state][county]
        else:
            tax_rate = state_tax[state]
    tax = tax_rate * subtotal
    out += f"""The tax is ${'{:,.2f}'.format(tax)}.\n"""

total = subtotal * (1 + tax_rate)
out += f"""The total is ${'{:,.2f}'.format(total)}."""
print(out)
