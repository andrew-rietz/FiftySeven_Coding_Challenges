'''

You can test for equality, but you may need to
test to see how a number compares to known value and
display a message if the number is too low or too
high.

Write a program that asks the user for their age and
compare it to the legal driving age of sixteen. If the
user is sixteen or older the program should display
"You are old enough to legally drive." If the user is
under sixteen, the program should display "You are
not old enough to legally drive."

___________________
Example Output
___________________
What is your age? 15
You are not old enough to legally drive.

** or **

What is your age? 35
You are old enough to legally drive.

___________________
Constraints
___________________
Use a single output statement
Use a ternary operator to write this program. If your
language doesn't support a ternary operator, use a
regular if/else statement, and still use a single
output statement to display the message.

'''

age = int(input('What is your age? '))
check = "aren't" if age<16 else 'are'
print(f'You {check} old enough to legally drive')
