"""

Sorting records is helpful, but sometimes you need
to filter down the results to find or display only
what you're looking for.

Given the following data set

First Name          | Last Name           | Position            | Separation Date
--------------------|---------------------|-----------------
John                | Johnson             | Manager             | 2016-12-31
Tuo                 | Xiong               | Software Engineer   | 2016-10-05
Michaela            | Michaelson          | District Manager    | 2015-12-19
Jake                | Jacobsen            | Programmer          |
Jacquelyn           | Jackson             | DBA                 |
Sally               | Weber               | Web Developer       | 2015-12-18

create a program that lets a user locate all records
that match the search string by comparing the search
string to the first or last name field.

___________________
Example Output
___________________
Enter a search string: Jac

Results:
Name                | Position            | Separation Date
--------------------|---------------------|-----------------
Jacquelyn Jackson   | DBA                 |
Jake Jacobsen       | Programmer          |

___________________
Constraints
___________________
- Implement the data using an array of maps or an
associative array.

"""


def setupData():
    employeeInfo = [
        {
            "firstName": "John",
            "lastName": "Johnson",
            "position": "Manager",
            "sepDate": "2016-12-31",
        },
        {
            "firstName": "Tuo",
            "lastName": "Xiong",
            "position": "Software Engineer",
            "sepDate": "2016-10-05",
        },
        {
            "firstName": "Michaela",
            "lastName": "Michaelson",
            "position": "District Manager",
            "sepDate": "2015-12-19",
        },
        {
            "firstName": "Jake",
            "lastName": "Jacobsen",
            "position": "Programmer",
            "sepDate": "",
        },
        {
            "firstName": "Jacquelyn",
            "lastName": "Jackson",
            "position": "DBA",
            "sepDate": "",
        },
        {
            "firstName": "Sally",
            "lastName": "Weber",
            "position": "Web Developer",
            "sepDate": "2015-12-18",
        },
    ]
    return employeeInfo


def main():
    employeeInfo = setupData()

    searchText = input("Enter a search string: ")
    sortedInfo = [
        employee
        for employee in employeeInfo
        if (searchText in employee["firstName"] or searchText in employee["lastName"])
    ]

    outputString = (
        "Name".ljust(20)
        + "|"
        + " Position".ljust(20)
        + "|"
        + " Separation Date".ljust(20)
        + "\n"
    )
    outputString += "-" * 20 + "|" + "-" * 20 + "|" + "-" * 20
    for employee in sortedInfo:
        outputString += "\n"
        outputString += (
            f"""{employee['firstName']} {employee['lastName']}""".ljust(20)
            + "|"
            + f""" {employee['position']}""".ljust(20)
            + "|"
            + f""" {employee['sepDate']}""".ljust(20)
        )

    print(outputString)


main()
