"""

Sometimes you have to locate and remove an entry
from a list based on some criteria. You may have a
deck of cards and need to discard one so it's no
longer in play, or you may need to remove values
from a list of valid inputs once they've been used.
Storing the values in an array makes this process
easier. Depending on your lanugage you may find it
safer and more efficient to create a new array
instread of modifying the existing one.

Create a small program that contains a list of
employee names. Print out the list of names when the
program runs the first time. Prompt for an employee
name and remove that specific name from the list of
names. Display the remaining employees, each on
its own line.

___________________
Example Output
___________________
There are 5 employees:
John Smith
Jackson Jackson
Chris Jones
Amanda Cullen
Jeremy Goodwin

Enter an employee name to remove: Chris Jones

There are 4 employees:
John Smith
Jackie Jackson
Amanda Cullen
Jeremy Goodwin

___________________
Constraint
___________________
Use an array or list to store the names

"""


def readNames():
    allNames = [
        "John Smith",
        "Jackie Johnson",
        "Chris Jones",
        "Amanda Cullen",
        "Jeremy Goodwin",
    ]
    return allNames


def printNames(allNames):
    for name in allNames:
        print(name)


def removeName(allNames, userEntry):
    nameFound = False
    for name in allNames:
        if userEntry.upper() == name.upper():
            allNames.remove(name)
            nameFound = True
    if not nameFound:
        print("Sorry, that employee is not in the list.")

    return allNames


def main():
    allNames = readNames()
    moreToRemove = ""
    while True:
        print(f"There are {len(allNames)} employees:")
        printNames(allNames)

        if moreToRemove.upper() == "N":
            break

        userEntry = input("Enter an employee name to remove: ").strip()
        allNames = removeName(allNames, userEntry)
        moreToRemove = input("Remove more names? [Y/N] ").strip()

        print("\n" * 100)


main()
