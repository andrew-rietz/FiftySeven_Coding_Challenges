import os
import sys
import unittest
import unittest.mock

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from troubleshooting_car_issues import troubleshooting_car_issues

class TroubleShootingCarIssuesTests(unittest.TestCase):
    """Tests the ExpertSystem class and methods"""
    def setUp(self):
        self.exp_sys = troubleshooting_car_issues.ExpertSystem()
        self.exp_sys.initial_prompt = "Is the car silent when you turn the key?"
        self.exp_sys.questions = {
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

    def test__ExpertSystem__query_is_valid(self):
        prompt = "Does your car have fuel injection?"
        true_false = True
        response = self.exp_sys.query(prompt, true_false)
        self.assertEqual("Get it in for service.", response)

    def test__ExpertSystem__query_is_invalid(self):
        prompt = "Does your car have fuel injection?"
        true_false = "bogus_key"
        response = self.exp_sys.query(prompt, true_false)
        self.assertEqual("Sorry, response not programmed.", response)

    def test__ExpertSystem__is_diagnosis__false(self):
        response = "Does your car have fuel injection?"
        is_diagnosis = self.exp_sys.is_diagnosis(response)
        self.assertEqual(False, is_diagnosis)

    def test__ExpertSystem__is_diagnosis__true(self):
        response = "This is a diagnosis."
        is_diagnosis = self.exp_sys.is_diagnosis(response)
        self.assertEqual(True, is_diagnosis)


if __name__ == "__main__":
    unittest.main()
