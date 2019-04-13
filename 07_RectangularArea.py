'''

When working in a global environment, you'll have to
present information in both metric and Imperial units.
And you'll need to know when to do the conversion to
ensure the most accurate results.

Create a program that calculates the area of a room.
Prompt the user for the length and width of the room
in feet. Then display the area in both square feet
and square meters.

The formula for this conversion is:

m**2 = f**2 * 0.09290304

___________________
Example Output
___________________
What is the length of the room in feet? 15
What is the width of the room in feet? 20
You entered dimensions of 15 feet by 20 feet.
The area is:
300 square feet
27.781 square meters

___________________
Constraints
___________________
Keep the calculations separate from the output
Use a constant to hold the conversion factor

'''

'Conversion factor for ft2 to m2'
conv = 0.09290304

'Rest of the code'
len = float(input('What is the length of the room' +
                  'in feet? '))
width = float(input('What is the width of the ' +
                    'room in feet? '))

ft2 = round(len * width,0)
m2 = round(ft2 * conv,3)

print(f'''\
The area is:
{ft2} square feet
{m2} square meters\
''')
