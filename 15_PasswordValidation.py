'''

Passwords are validated by comparing a user-provided
value with a known value that's stored. Either it's
correct or it's not.

Create a simple program that validates user login
credentials. The program must prompt the user for a
username and password. The program should compare
the password given by the user to a known password.
If the password matches, the program should display
"Welcome!" If it didn't matc, the program should
display "I don't know you."

___________________
Example Output
___________________
What is the password? 12345
I don't know you.

** or **

What is the password? abc$123
Welcome!

___________________
Constraints
___________________
Use an if/else statement for this problem
Make sure the program is case sensitive

'''

#Create the password
pw = 'abc$123'

login = str(input('What is the password? '))

if login == pw:
    print('Welcome!')
else:
    print("I don't know you.")
