import unittest
import unittest.mock
import io
import sys
import os

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from troubleshooting_car_issues import troubleshooting_car_issues

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class TroubleShootingCarIssuesTests(unittest.TestCase):
    """Tests that the 'main' function works as expected"""

    def setUp(self):
        self.initial_prompt = "Is the car silent when you turn the key?"
        self.questions = {
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

    @unittest.mock.patch("builtins.input")
    def test_main_function(self, mock_inputs):
        mock_inputs.side_effect = ["NO", "n", "n", "YES", "y"]
        expected_result = (
            'You will be asked a series of questions. Please respond with either a "Y" or "N".\n' +
            "Get it in for service."
        )

        with captured_output() as (outputs, errors):
            troubleshooting_car_issues.main()
            test_val = outputs.getvalue().strip()

        self.assertEqual(expected_result, test_val)


if __name__ == "__main__":
    unittest.main()
