"""

Write a guess the number game that has three levels
of difficulty. The first level of difficult would
be a number between 1 and 10. The second difficulty
set would be between 1 and 100. The third difficulty
set would be between 1 and 1000.

Prompt for the difficult level, and then start the
game. The computer picks a random number in that
range and prompts the player to guess that number.
Each time the player guesses, the computer should
give the player a hint as to whether the number of
guesses. Once the player guesses the correct number,
the computer should present the number of guesses
and ask if the player would like to play again.

___________________
Example Output
___________________

Let's play Guess the Number.
Pick a difficulty level (1, 2, or 3): 1
I have my number. What's your guess? 1
Too low. Guess again: 5
Too high. Guess again: 2
You got it in 3 guesses!
Play again? n
Goodbye!

___________________
Constraints
___________________
Don't allow any non-numeric data entry.
During the game, count non-numeric entries as
wrong guesses

"""


def createNumbers(difficulty):
    import random

    numbers = {}
    topEnd = "1" + "0" * difficulty
    topEnd = int(topEnd)
    for n in range(1, topEnd + 1):
        numbers[n] = ""

    number = random.randrange(1, topEnd + 1)
    return (numbers, number)


def getInput():
    validInput = False
    difficulty = input(
        """\
Let's play Guess the Number.
Pick a difficulty level (1, 2, or 3): """
    )
    while not (validInput):
        while True:
            try:
                difficulty = int(difficulty)
                break
            except ValueError:
                difficulty = input("Please enter a number between 1 and 3.\n")

        validInput = difficulty >= 1 and difficulty <= 3
        if not (validInput):
            difficulty = input("Please enter a number between 1 and 3.\n")

    return difficulty


def checkGuessIsNumber(guess, number, nGuesses):
    while True:
        try:
            guess = int(guess)
            nGuesses += 1
        except ValueError:
            nGuesses += 1
            guess = input("Please enter a number.\n")

    return (guess, number, nGuesses)


def playGame():
    difficulty = getInput()
    (numbers, number) = createNumbers(difficulty)
    number = int(number)

    nGuesses = 0

    guess = input("""I have my number. What's your guess? """)

    while guess != number:
        (guess, number, nGuesses) = checkGuessIsNumber(guess, number, nGuesses)

        if guess > number:
            guess = input("""Too high. What's your guess? """)
        elif guess < number:
            guess = input("""Too low. What's your guess? """)

    print(f"""You got it in {nGuesses} guesses!""")


def main():
    play = True

    while play:
        print("\n" * 100)
        playGame()
        playAgain = input("Play again? [Y/N]  ")
        if playAgain.upper() == "N":
            play = False

    print("Goodbye!")


main()
