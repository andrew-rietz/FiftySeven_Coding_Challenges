import unittest
import unittest.mock
import io
from contextlib import redirect_stdout

from compound_interest import compound_interest

class CompoundInterestIntegrationTest(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def test_output(self, mock_inputs):
        mock_inputs.side_effect = ["1500", "4.3", "6", "4"]

        expected_result = (
            f"$1,500.00 invested at 4.30% for " +
            f"6 years compounded 4 times per year is $1,938.84."
        )
        print_output = io.StringIO()
        with redirect_stdout(print_output):
            compound_interest.main()
            test_val = print_output.getvalue().strip()

        self.assertEqual(expected_result, test_val)

if __name__ == "__main__":
    unittest.main()
