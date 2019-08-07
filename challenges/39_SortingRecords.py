"""

When you're looking at results, you'll want to be
able to sort them so you can find what you're
looking for quickly or do some quick visual
comparisons.

Given the following data set:

First Name          | Last Name           | Position            | Separation Date
--------------------|---------------------|-----------------
John                | Johnson             | Manager             | 2016-12-31
Tuo                 | Xiong               | Software Engineer   | 2016-10-05
Michaela            | Michaelson          | District Manager    | 2015-12-19
Jake                | Jacobsen            | Programmer          |
Jacquelyn           | Jackson             | DBA                 |
Sally               | Weber               | Web Developer       | 2015-12-18

create a program that sorts all employees by last
name and prints them to the screen in a tabular
format.

___________________
Eample Output
___________________

Name                | Position            | Separation Date
--------------------|---------------------|-----------------
Jacquelyn Jackson   | DBA                 |
Jake Jacobsen       | Programmer          |
John Johnson        | Manager             | 2016-12-31
Michaela Michaelson | District Manager    | 2015-12-19
Sally Weber         | Web Developer       | 2015-12-18
Tuo Xiong           | Software Engineer   | 2016-10-05

___________________
Constraints
___________________
Implement the data using a list of maps

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
    from operator import itemgetter

    employeeInfo = setupData()
    employeeInfo = sorted(employeeInfo, key=itemgetter("lastName"))

    outputString = (
        "Name".ljust(20)
        + "|"
        + " Position".ljust(20)
        + "|"
        + " Separation Date".ljust(20)
        + "\n"
    )
    outputString += "-" * 20 + "|" + "-" * 20 + "|" + "-" * 20
    for employee in employeeInfo:
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
