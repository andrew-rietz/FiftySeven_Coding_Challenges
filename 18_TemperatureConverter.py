'''

You'll often need to determine which part of a
program is run based on uesr input or other events.

Create a program that converts temperatures from
Fahrenheit to Celsius or from Celsius to Fahrenheit.
Prompt for the starting temperature. The program
should prompt for the type of conversion and then
perform the conversion.

The formulas are

C = (F - 32) * 5/9
F = (C * 9/5) + 32

___________________
Example Output
___________________
Press C to convert from Fahrenheit to Celsius.
Press F to convert from Celsius to Fahrenheit.
Your choice: C

Please enter the temperature in Fahrenheit: 32
The temperature in Celsius is 0.

___________________
Constraints
___________________
Ensure that you allow upper or lowercase values for
C and F
Use as few output statements as possible and avoid
repeated output strings

'''

type = {'C':'Celsius', 'F':'Fahrenheit'}
opp_type = {'C':'Fahrenheit', 'F':'Celsius'}

while True:
    user_type = input(f'''
Press C to convert from Fahrenheit to Celsius.
Press F to convert from Celsius to Fahrenheit.
Please enter your choice: \
''').upper()
    if user_type == 'C' or user_type == 'F':
        break
    else:
        print('Please enter either C or F.')

while True:
    try:
        temp = float(input(f'Please enter the temperature in {type[user_type]}: '))
        break
    except ValueError:
        print('Please enter a numeric value.')


if user_type == 'C':
    new_temp = (temp * 9/5) + 32
else:
    new_temp = (temp - 32) * 5/9

new_temp = round(new_temp,2)

print(f'The temperature in {opp_type[user_type]} is {new_temp}.\n')
