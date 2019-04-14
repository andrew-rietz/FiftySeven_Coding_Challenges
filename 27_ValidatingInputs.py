'''

Large functions aren't very usable or maintainable. It
makes a lot of sense to break down the logic of a
program into smaller functions that do one thing each.
The program can then call these function in sequence
to perform the work.

Write a program that prompts for a first name, last
name, employee ID, and zip code. Ensure that the
input is valid according to these rules:

-The first and last name must be filled in
-The first and last names must be at least two
characters long
-An employee ID is in the format AA-1234. So, two
letters, a hyphen and four numbers.
-The ZIP code must be a number.

Display appropriate error message on incorrect data

___________________
Example Output
___________________
Enter the first name: J
Enter the last name:
Enter the ZIP code: ABCDE
Enter an employee ID: A12-1234
'J' is not a valid first name. It is too short.
The last name must be filled in.
The ZIP code must be numeric.
A12-1234 is not a valid ID.

** or **

Enter the first name: Jimmy
Enter the last name: James
Enter the ZIP code: 55555
Enter an employee ID: TK-421
There were no errors found.

___________________
Constraints
___________________
Create a function for each type of validation you
need to write. Then create a validate input function
that takes in all of the input data and invokes the
specific vlaidation functions.
Use a single output statement to display the outputs.

'''

def main():
    errs = ''

    fname = input('Enter the first name: ')
    lname = input('Enter the last name: ')
    zip = input('Enter the ZIP code: ')
    id = input('Enter an employee ID: ')

    errs += firstNameFilled(fname)
    errs += lastNameFilled(lname)
    errs += nameLengths(fname, lname)
    errs += zipIsNumber(zip)
    errs += employeeIDFormat(id)

    print(errs)

def firstNameFilled(fname):
    out = ''
    if (len(fname)==0 or fname.isspace()):
        out = 'The first name must be filled in.\n'
    return out

def lastNameFilled(lname):
    out = ''
    if (len(lname)==0 or lname.isspace()):
        out = 'The first name must be filled in.\n'
    return out

def nameLengths(fname, lname):
    out = ''
    if len(fname.strip()) < 2:
        out += f'"{fname.strip()}" is not a valid first name. It is too short.\n'
    if len(lname.strip()) < 2:
        out += f'"{lname.strip()}" is not a valid last name. It is too short.\n'
    return out

def zipIsNumber(zip):
    out = ''
    if len(zip.strip()) == 0:
        out += 'ZIP must be filled in.\n'
    if not zip.isdigit() and not zip.isspace():
        out += 'The ZIP code must be numeric.\n'
    return out

def employeeIDFormat(id):
    import re
    out = ''
    if len(id) != 7:
        out += f'"{id}" is not a valid ID. Length is incorrect.\n'
    if re.match('([a-zA-Z]{2}-[0-9]{4})', id) == None:
        out += f'"{id}" does not match expected format. ID format is [Letter][Letter]-[Num][Num][Num][Num].\n'
    return out

main()
