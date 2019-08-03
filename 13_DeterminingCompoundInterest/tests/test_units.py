import unittest
import unittest.mock

from tests.context import compound_interest

class SimpleInterestTests(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def setUp(self, mock_inputs):
        mock_inputs.side_effect = ["1500", "4.3", "6", "4"]
        self.interest = compound_interest.CompoundInterestCalculator()

    def test_investment_is_1938_and_84(self):
        self.assertEqual(1938.84, self.interest.calc())

if __name__ == "__main__":
    unittest.main()
