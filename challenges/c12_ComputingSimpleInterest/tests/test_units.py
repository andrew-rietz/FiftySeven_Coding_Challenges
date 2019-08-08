import os
import sys
import unittest
import unittest.mock

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from simple_interest import simple_interest

class SimpleInterestTests(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def setUp(self, mock_inputs):
        mock_inputs.side_effect = ["1500", "4.3", "4"]
        self.interest = simple_interest.InterestCalculator()

    def test_investment_is_1758(self):
        self.assertEqual(1758, self.interest.calc())

if __name__ == "__main__":
    unittest.main()
