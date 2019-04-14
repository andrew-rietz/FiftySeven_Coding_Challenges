'''

An 'expert system' is a type of artificial
intelligence program that uses a knowledge base
and a set of rules to perform a task that a human
expert might do. Many website are available that
will help you self-diagnose a medical issue by
answering a series of questions. And many hardware
and software companies offer online troubleshooting
tools to help people sole simple technical issues
before calling a human.

Create a program that walks the user through
troubleshooting issue with a car. Use the following
decision tree to build the system:

___________________
Example Output
___________________
Is the car silent when you turn the key? y
Are the battery terminals corroded? n
The battery cables may be damaged.
Replace cables and try again.

___________________
Constraints
___________________
Ask only questions that are relevant to the
situation and to the previous answers. Don't ask for
all inputs at once.

'''

tree_loc = ''
tree_val = 'Is the car silent when you turn the key?'
tree = {
    '0':'Does the car mark a clicking noise?',
    '00':'Does the car crank up but fail to start?',
    '000':'Does the engine start and then die?',
    '0001':'Does your car have fuel injection?',
    '00010':'Check to ensure the choke is opening and closing.',
    '00011':'Get it in for service.',
    '01':'Replace the battery.',
    '001':'Check spark plug connections.',
    '1':'Are the battery terminal corroded?',
    '10':'Replace cables and try again.',
    '11':'Clean terminals and try starting again.'
}

print('You will be asked a series of questions. Please respond with either a "Y" or "N".')
while tree_val[len(tree_val)-1]=='?':
    resp = input(tree_val + ' ')
    if resp.upper() == 'Y':
        tree_loc += '1'
        tree_val = tree[tree_loc]
    elif resp.upper() == 'N':
        tree_loc += '0'
        tree_val = tree[tree_loc]
    else:
        print('Invalid input, try again. Please enter either "Y" or "N".')

print(tree_val)
