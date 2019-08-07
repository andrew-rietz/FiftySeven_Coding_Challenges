"""

You'll often need to see if one value is within a
certain range and alter the flow of a program as a
result.

Create a program to calculate the body mass index
(BMI) for a person using the person's height in
inches and weight in pounds. The program should
prompt the user for weight and height.

Calculate the BMI by using the following formula:
    bmi = (weight / (height * height)) * 703

If the BMI is between 18.5 and 25, display that the
person is at a normal weight. If they are out of that
range, tell them if they are underweight or overweight
and tell them to consult their doctor.

___________________
Example Output
___________________
Your BMI is 19.5
You are within the ideal weight range.

** or **

Your BMI is 32.5.
You are overweight. You should see your doctor.

___________________
Constraints
___________________
Ensure your program takes only numeric data. Don't
let the user continue unless the data is valid.

"""

while True:
    try:
        height = float(input("Please enter your height in inches: "))
        break
    except ValueError:
        print("Please enter a numeric value.")

while True:
    try:
        weight = float(input("Please enter your weight in pounds: "))
        break
    except ValueError:
        print("Please enter a numeric value.")

bmi = (weight / height ** 2) * 703

if bmi >= 18.5 and bmi <= 25:
    out = "You are within the ideal weight range."
else:
    over_under = "over" if bmi > 25 else "under"
    out = f"You are {over_under} weight. You should see your doctor."

print(f"Your BMI is {'{:.1f}'.format(bmi)}. " + out)
