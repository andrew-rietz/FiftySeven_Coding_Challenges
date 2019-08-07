import unittest
import unittest.mock
import io
from contextlib import redirect_stdout

if __name__ == '__main__':
    if __package__ is None:
        import sys
        import os
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from currency_conversion import currency_conversion
    else:
        from ..currency_conversion import currency_conversion
else:
    from currency_conversion import currency_conversion

class CurrencyConverterIntegrationTest(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def test_output(self, mock_inputs):
        mock_inputs.side_effect = ["81", "137.51"]

        expected_result = (
            f"81.0 euros at an exchange rate of " +
            f"137.51 is 111.38 U.S. dollars."
        )
        print_output = io.StringIO()
        with redirect_stdout(print_output):
            currency_conversion.main()
            test_val = print_output.getvalue().strip()

        self.assertEqual(expected_result, test_val)

if __name__ == "__main__":
    unittest.main()
