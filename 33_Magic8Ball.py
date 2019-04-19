'''

Arrays are great for storing possible responses from
a program. If you combine that with a random number
generator, you can pick a random entry from this list,
which works great for games.

Create a Magic 8 Ball game that prompts for a
question and then displays either 'Yes', 'No',
'Maybe', or 'Ask again later.'

___________________
Example Output
___________________
What's your question? Will I be rich and famous?
Ask again later.

___________________
Constraint
___________________
The value should be chosen randomly using a pseudo
random number generator. Store the possible choices in
a list and select one at random

'''
def main():
    from random import randrange

    responses = [
                'Yes', 'No', 'Maybe',
                'Ask again later'
                ]

    userQuestion = input("What's your question? ")
    print(responses[randrange(len(responses))])

main()
