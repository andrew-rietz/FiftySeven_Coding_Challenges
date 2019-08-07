"""

Statistics is important in our field. When measuring
response times or rending times it's helpful to
collect data so you can easily spot abnormalities.
For example, the standard deviation helps you
determine which values are outliers and which values
are within  normal ranges.

Write a program that prompts for response times from
a website in milliseconds. It should keep asking
for values until the user enters 'done.'

The program should print the average time (meanVal), the
minimum time, the maximum time, and the standard
deviation.

To compute the average (meanVal):
1. Compute the sum of all values
2. Divide the sum by the number of values

To compute the standard deviation:
1. Calculate the difference from the meanVal for each
number and square it.
2. Compute the meanVal of the squared values.
3. Take the square root of the meanVal.

___________________
Example Output
___________________
Enter a number: 100
Enter a number: 200
Enter a number: 1000
Enter a number: 300
Enter a number: done
Numbers: 100, 200, 1000, 300
The average is 400.
The minmum is 100.
The maximum is 1000.
The standard deviation is 353.55

--> Note: std dev calculated above seems incorrect
___________________
Constraints
___________________
- Use loops and arrays to perform the input and
mathematical operations.
- Be sure the exclude the 'done' entry from the array
of inputs.
- Be sure to properly convert numeric values
to strings.
- Keep the input separate from the processing
and output.

"""


def getInputs():
    numbers = []
    while True:
        lastNumber = input("Enter a number: ")
        if lastNumber.upper() == "DONE":
            break
        numbers.append(float(lastNumber))
    return numbers


def calcMean(numbers):
    return sum(numbers) / len(numbers)


def calcStandardDeviation(numbers):
    smallestNumber = min(numbers)
    largestNumber = max(numbers)
    meanVal = calcMean(numbers)
    differenceFromMeanSquared = []
    for number in numbers:
        differenceFromMeanSquared.append((number - meanVal) ** 2)

    meanValOfDifferenceSquared = calcMean(differenceFromMeanSquared)
    standardDeviation = (meanValOfDifferenceSquared) ** (0.5)

    return [meanVal, smallestNumber, largestNumber, standardDeviation]


def main():
    numbers = getInputs()
    calculatedValues = calcStandardDeviation(numbers)
    meanVal = round(calculatedValues[0], 2)
    smallestNumber = calculatedValues[1]
    largestNumber = calculatedValues[2]
    standardDeviation = round(calculatedValues[3], 2)
    printNumbers = [str(number) for number in numbers]

    print(
        f"Numbers: {', '. join(printNumbers)}\n"
        f"The average is {meanVal}.\n"
        f"The minimum is {smallestNumber}.\n"
        f"The maximum is {largestNumber}.\n"
        f"The standard deviation is {standardDeviation}"
    )


main()
