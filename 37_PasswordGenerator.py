'''

Coming up with a password that meets specific
requirements is something your computer can do. And it
will givev you practice using random number generators
in conjunction with a list of known values.

Create a program that generates a secure password.
Prompt the user for the minimum length, the number of
special characters, and the number of numbers. Then
generate a password for the user using those inputs.

___________________
Example Output
___________________
What's the minimum length? 8
How many special characters? 2
How many numbers? 2
Your password is:
aurn2$1s#

___________________
Constraints
___________________
Use lists to store the characters you'll use to
generate the passwords.
Add some randomness to the password generation

'''

def checkInputIsNumber(inputValue):
    while True:
        try:
            inputValue = int(inputValue)
            break
        except ValueError:
            inputValue = input('Please enter a number.\n')

    return inputValue

def pickValueByCategory(valueCategory):
    from random import choice
    numbers = [str(number) for number in range(0, 10)]
    letters = list('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz')
    specialChars = list('!@#$%^&*()_-<>?')
    categories = {'number':numbers, 'letter':letters, 'special character':specialChars}

    nextCharacter = choice(categories[valueCategory])
    return nextCharacter

def main():
    from random import choice
    minLength = checkInputIsNumber(input("What's the minimum length? "))
    numSpecialChars = checkInputIsNumber(input("How many special characters? "))
    numNumbers = checkInputIsNumber(input("How many numbers? "))
    characterType = ['number', 'letter', 'special character']

    countSpecialChars = 0
    countNums = 0
    countLetters = 0
    password = ''
    for characterNumber in range(0,minLength):

        if countNums == numNumbers and 'number' in characterType:
            characterType.pop(characterType.index('number'))
        elif countSpecialChars == numSpecialChars and 'special character' in characterType:
            characterType.pop(characterType.index('special character'))
        elif countLetters == (minLength - numNumbers - numSpecialChars) and 'letter' in characterType:
            characterType.pop(characterType.index('letter'))

        nextCharacterType = choice(characterType)
        password += pickValueByCategory(nextCharacterType)

        if nextCharacterType == 'number':
            countNums += 1
        elif nextCharacterType == 'special character':
            countSpecialChars += 1
        elif nextCharacterType == 'letter':
            countLetters += 1

    print(password)

main()
