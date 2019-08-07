import unittest
import unittest.mock
import io
from contextlib import redirect_stdout

if __name__ == '__main__':
    if __package__ is None:
        import sys
        import os
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from simple_interest import simple_interest
    else:
        from ..simple_interest import simple_interest
else:
    from simple_interest import simple_interest

class SimpleInterestIntegrationTest(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def test_output(self, mock_inputs):
        mock_inputs.side_effect = ["1500", "4.3", "4"]

        expected_result = (
            "After 4 years at 4.30%, the initial investment of $1,500.00 "+
            "will be worth $1,758.00."
        )
        print_output = io.StringIO()
        with redirect_stdout(print_output):
            simple_interest.main()
            test_val = print_output.getvalue().strip()

        self.assertEqual(expected_result, test_val)

if __name__ == "__main__":
    unittest.main()
