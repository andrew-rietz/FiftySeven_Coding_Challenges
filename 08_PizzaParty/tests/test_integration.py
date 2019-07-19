import unittest
import unittest.mock
import io
from contextlib import redirect_stdout

from pizza_party import pizza_party

class PizzaPartyIntegrationTest(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def test_output(self, mock_inputs):
        mock_inputs.side_effect = ["3", "2", "6"]

        expected_result = (
            f"3 people with 2 pizzas.\n" +
            f"Each person gets 4 pieces of pizza.\n" +
            f"There are 0 pieces leftover."
        )
        print_output = io.StringIO()
        with redirect_stdout(print_output):
            pizza_party.main()
            test_val = print_output.getvalue().strip()

        self.assertEqual(expected_result, test_val)

if __name__ == "__main__":
    unittest.main()
