'''

Arrays don't have to be hard-coded. You can take
user input and store it in an array and then work
with it.

Create a program that picks a winner for a contest or
prize drawing. Prompt for names of contestants until
the user leaves the entry blank. Then randomly
select a winner.

___________________
Example Output
___________________
Enter a name: Homer
Enter a name: Bart
Enter a name: Maggie
Enter a name: Lisa
Enter a name: Moe
Enter a name:
The winner is... Maggie.

___________________
Constraints
___________________
- Use a loop to capture user input into an array
- Use a random number generator to pluck a value
from the array.
- Don't include a blank entry in the array.
- Some languages require that you define the length
of the array ahead of time. You may need to find
another data structure, like an ArrayList

'''

def getInputs():
    contestants = []
    while True:
        newContestant = input('Enter a name: ')
        if newContestant != '':
            contestants.append(newContestant)
        else:
            break
    return contestants

def main():
    from random import choice
    contestants = getInputs()

    winner = (choice(contestants))
    print(f'The winner is... {winner}')

main()
