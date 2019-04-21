"""

Sometimes you have to round up to the next number
rather than follow standard rounding rules.

Calculate gallons of paint needed to paint the ceiling
of a room. Prompt for the length and width, and
assume oen gallon covers 350 square feet. Display the
number of gallons needed to paint the ceiling as a
whole number.

___________________
Example Output
___________________
You will need to purchase 2 gallons of paint
to cover 360 square feet.

___________________
Constraints
___________________
Use a constant to hold the conversion rate
Ensure that you round UP to the next whole number

"""
import math

"Conversion factor: one gallon == 350 sq ft"
conv = 350

area = int(input("What is the size of the " + "ceiling in square feet? "))

gallons = math.ceil(area / conv)

print(
    f"""\
You will need to purchase {gallons} gallons of \
paint to cover {area} square feet.\
"""
)
