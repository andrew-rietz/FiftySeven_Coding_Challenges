"""
A number guessing game
"""
import io
import random
import sys
import os
from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util_functions.utils import user_inputs

def get_string_in_list_track_responses(prompt, err_msg, allowed_vals, case_sensitive=False, exit_val=None):
    """Prompts user for input until they enter an allowed value

    Args:
        prompt: Prompt the user for input
        err_msg: Message to be displayed if user provides bad input
        allowed_vals: List of expected values allowed by the function
        case_sensitive: (Default = True) Tests the values in a case_sensitive manner
        exit: Value which will allow user to exit the loop and cause function to return None

    Returns:
        (dict):
            {
                "user_val": User input from the given list of allowed values,
                "n_responses": Number of responses before a valid value received
            }
    """
    if not case_sensitive:
        allowed_vals = [val.lower() for val in allowed_vals]

    n_responses = 0
    while True:
        user_val = input(f"{prompt.strip()} ").strip()
        if user_val == exit_val:
            return {"user_val": None, "n_responses": n_responses}
        n_responses += 1
        test_val = user_val.lower() if not case_sensitive else user_val
        if test_val not in allowed_vals:
            print(err_msg.strip(), end=" ")
            continue
        return {"user_val": user_val, "n_responses": n_responses}

class GuessingGame():
    """A representation of a number guessing game"""

    def __init__(self, difficulty=1):
        self.difficulty = difficulty
        self.guesses = 0
        self.remaining_numbers = []
        self.number = None
        self.n_guesses = 0

    def set_number(self):
        max_val = 10 ** int(self.difficulty)
        self.remaining_numbers = [str(num) for num in range(1, max_val + 1)]
        self.number = int(random.choice(self.remaining_numbers))

    def check_guess(self, guessed_number):
        self._update_remaining(str(guessed_number))
        if guessed_number == self.number:
            return "Match"
        if guessed_number > self.number:
            return "Too high."
        return "Too low."

    def _update_remaining(self, guessed_number):
        self.remaining_numbers.remove(guessed_number)

    def take_guess(self, prompt, err_msg):
        guessed_number__n_guesses = get_string_in_list_track_responses(
            prompt=prompt,
            err_msg=err_msg,
            allowed_vals=self.remaining_numbers
        )
        guessed_number = guessed_number__n_guesses["user_val"]
        self.n_guesses += guessed_number__n_guesses["n_responses"]
        return int(guessed_number)

def startup():
    difficulty = user_inputs.get_string_in_list(
        prompt=(
            "Let's play Guess the Number.\n" +
            "Pick a difficulty level (1, 2, or 3):"
        ),
        err_msg="Sorry, please choose a valid selection.",
        allowed_vals=["1", "2", "3"],
    )
    return difficulty

def gameover(n_guesses):
    valid_responses = ["Yes", "No"]
    print(f"You got it in {n_guesses} guesses!")
    replay = user_inputs.get_string_in_list(
        prompt=f"Play again? [{'/'.join(valid_responses)}]",
        err_msg=f"Please enter a valid response.",
        allowed_vals=valid_responses,
        case_sensitive=False
    ).strip().title()

    if replay == "Yes":
        return True
    return False


def main():
    while True:
        game = GuessingGame(startup())
        game.set_number()
        guess = game.take_guess(
            prompt="What's your guess?",
            err_msg="Please enter a valid integer (that you haven't already guessed)."
        )
        guess_result = game.check_guess(guess)
        while guess_result != "Match":
            print(guess_result, end=" ")
            guess = game.take_guess(
                prompt="Guess again:",
                err_msg="Please enter a valid integer (that you haven't already guessed).",
            )
            guess_result = game.check_guess(guess)
        replay = gameover(game.n_guesses)
        if not replay:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
