import os
import sys
import unittest
import unittest.mock

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from currency_conversion import currency_conversion

class CurrencyConverterTests(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def setUp(self, mock_inputs):
        mock_inputs.side_effect = ["81", "137.51"]
        self.exchange = currency_conversion.CurrencyConverter()

    def test_euros_is_81(self):
        self.assertEqual(81, self.exchange.amount_from)

    def test_exchange_rate_is_137_51(self):
        self.assertEqual(137.51, self.exchange.rate_from)

    def test_convert_is_111_38(self):
        self.assertEqual(111.38, round(self.exchange.convert(), 2))

if __name__ == "__main__":
    unittest.main()
