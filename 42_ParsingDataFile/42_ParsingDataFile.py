"""

Sometimes data comes in as a structured format that
you have to break down and turn into records so you
can process them. CSV, or comma-separated values, is
a common standard for doing this.

Construct a program that reads in the following
data file:

Ling,Mai,55900
Johnson,Jim,56500
Jones,Aaron,46000
Jones,Chris,34500
Swift,Geoffrey,14200
Xiong,Fong,65000
Zarnecki,Sabrina,51500

Process the records and display the results
formatted as a table, evenly spaced, as shown in
the example output.

___________________
Example Output
___________________

Last        First       Salary
-------------------------------
Ling        Mai         55900
Johnson     Jim         56500
Jones       Aaron       46000
Jones       Chris       34500
Swift       Geoffrey    14200
Xiong       Fong        65000
Zarnecki    Sabrina     51500

___________________
Constraints
___________________
- Write your own code to parse the data. Don't use
a CSV parser.
- Use spaces to align the columns
- Make each column one space longer than the longest
value in the coluumn

"""


def writeDummyFile():
    inputData = [
        "Ling,Mai,55900",
        "Johnson,Jim,56500",
        "Jones,Aaron,46000",
        "Jones,Chris,34500",
        "Swift,Geoffrey,14200",
        "Xiong,Fong,65000",
        "Zarnecki,Sabrina,51500",
    ]

    with open("42_ParsingDataFile/42_InputFile.csv", "w") as writer:
        writer.write("\n".join(inputData))


def readDummyFile(fName):
    with open("42_ParsingDataFile/42_InputFile.csv", "r") as reader:
        employeeRecords = [line.rstrip() for line in reader]

    splitData = [[val for val in line.split(",")] for line in employeeRecords]
    return splitData


def main():
    writeDummyFile()
    employeeRecords = readDummyFile("42_ParsingDataFile/42_InputFile.csv")
    # employeeRecords = sorted(employeeRecords, key=lambda employeeRecords: employeeRecords[0])

    lastNameColumnWidth = max([len(lastName[0]) for lastName in employeeRecords]) + 1
    firstNameColumnWidth = max([len(firstName[0]) for firstName in employeeRecords]) + 1
    salaryColumnWidth = max([len(salary[0]) for salary in employeeRecords]) + 1

    outString = (
        "Last".ljust(lastNameColumnWidth)
        + "First".ljust(firstNameColumnWidth)
        + "Salary".ljust(salaryColumnWidth)
        + "\n"
        + "-" * sum([lastNameColumnWidth, firstNameColumnWidth, salaryColumnWidth])
    )
    for employee in employeeRecords:
        outString += (
            "\n"
            + employee[0].ljust(firstNameColumnWidth)
            + employee[1].ljust(salaryColumnWidth)
            + employee[2].ljust(lastNameColumnWidth)
        )

    print(outString)


main()
