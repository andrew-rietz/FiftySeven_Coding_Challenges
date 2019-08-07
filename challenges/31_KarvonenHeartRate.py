"""

When you loop, you can control how much you increment
the counter; you don't always have to increment by
one.

When getting into a fitness program, you may want to
figure out your target heart rate so you don't
overexert yourself. The Karvonen heart rate formula
is on method you can use to determine your heart rate.
Create a program that prompts for your age and test
your resting heart rate. Use the Karvonen formula to
determine the target heart rate based on a range of
intensities from 55% to 95%. Generate a table with
the results as shown in the example output. The
formula is:

targetHeartRate = (((220 - age) - restingHR) *
    Intensity) + restingHR

___________________
Example Output
___________________
Resting Pulse: 65   Age: 22

Intensity       |  Rate
________________|__________
55%             | 138 bpm
60%             | 145 bpm
65%             | 151 bpm
:               |   :       (extra lines omitted)
85%             | 178 bpm
90%             | 185 bpm
95%             | 191 bpm


___________________
Constraints
___________________
-Don't hard-code the percentages. Use a loop to
increment the percentages from 55 to 95
-Ensure that the heart rate and age are entered as
numbers. Don't allow the user to continue without
entering valid inputs.
-Display the results in a tabular format

"""


def getInputs():
    while True:
        try:
            restingHR = int(input("What is your resting pulse? "))
            break
        except ValueError:
            print("Please enter an integer value.")

    while True:
        try:
            age = int(input("How old are you? "))
            break
        except ValueError:
            print("Please enter an integer value.")

    return (restingHR, age)


def karvonenHR(restingHR, age, intensity):
    targetHeartRate = (((220 - age) - restingHR) * (intensity / 100)) + restingHR
    return str(int(targetHeartRate)) + " bpm"


def prettyTabular(intensity, heartRate):
    # Takes in two values and prints them out in a tabular format
    # If no values passed in, returns a 'line break'
    if intensity == heartRate and intensity == "":
        outString = f"-" * 15 + "|"
        outString += f"-" * 12
    else:
        outString = f"{intensity}".ljust(15) + "|"
        outString += f"  {heartRate}".ljust(10)

    return outString


def main():

    (restingHR, age) = getInputs()

    outString = f"Resting pulse: {restingHR}    Age: {age}"
    outString += "\n" * 2 + prettyTabular("Intensity", "Pulse")
    outString += "\n" + prettyTabular("", "")
    for intensity in range(55, 96, 5):
        outString += "\n" + prettyTabular(
            str(intensity) + "%", karvonenHR(restingHR, age, intensity)
        )

    print(outString)


main()
