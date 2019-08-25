"""
Defines an 'ExpertSystem' decision tree class
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util_functions.utils import user_inputs


class ExpertSystem():
    """Represents an 'expert system' that acts as a decision tree

    Attributes:
        initial_prompt (str): First question to kick-off the 'expert system' prompt engine
        responses (obj, dict): A dictionary of prompts for the end-user. Keys are defined
            using a True/False convention where True corresponds to 1 and False corresponds to 0
    """

    def __init__(self, initial_prompt=None, questions=None):
        """Initializes the trouble-shooting object"""
        self.initial_prompt = None if initial_prompt is None else initial_prompt
        self.questions = {} if questions is None else questions

    def query(self, prompt, true_false):
        return self.questions.get(prompt, {}).get(true_false, "Sorry, response not programmed.")

    def is_diagnosis(self, response):
        return response[-1] != "?"

def get_input(prompt):
    return user_inputs.get_string_in_list(
        prompt=f"{prompt} [Y/N]:",
        err_msg="Sorry, please enter a valid [Y/N] value.",
        allowed_vals=["y", "n", "yes", "no"],
        case_sensitive=False
    ).lower()

def main():
    exp_sys = ExpertSystem()
    exp_sys.initial_prompt = "Is the car silent when you turn the key?"
    exp_sys.questions = {
        "Is the car silent when you turn the key?": {
            True: "Are the battery terminal corroded?",
            False: "Does the car mark a clicking noise?",
        },
        "Does the car mark a clicking noise?": {
            True: "Replace the battery.",
            False: "Does the car crank up but fail to start?",
        },
        "Does the car crank up but fail to start?": {
            True: "Check spark plug connections.",
            False: "Does the engine start and then die?",
        },
        "Does the engine start and then die?": {
            True: "Does your car have fuel injection?",
        },
        "Does your car have fuel injection?": {
            True: "Get it in for service.",
            False: "Check to ensure the choke is opening and closing.",
        },
        "Are the battery terminal corroded?":{
            True: "Clean terminals and try starting again.",
            False: "Replace cables and try again.",
        }
    }

    print('You will be asked a series of questions. Please respond with either a "Y" or "N".')
    prompt = exp_sys.initial_prompt
    while True:
        response = get_input(prompt)[0] == "y"
        result = exp_sys.query(prompt, response)
        if exp_sys.is_diagnosis(result):
            print(result)
            break

        prompt = result

if __name__ == "__main__":
    main()
