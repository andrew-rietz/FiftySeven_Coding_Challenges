import unittest
import unittest.mock

from tests.context import tax_calculator

class TaxCalculatorWITests(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def setUp(self, mock_inputs):
        mock_inputs.side_effect = ["10", "WI"]
        self.tax = tax_calculator.Taxes()
        self.order = self.tax.checkout()

    def test_WI_tax_amount_is_055(self):
        self.assertEqual(0.55, self.order['tax'])

    def test_WI_total_amount_is_1055(self):
        self.assertEqual(10.55, self.order['total'])

class TaxCalculatorMNTests(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def setUp(self, mock_inputs):
        mock_inputs.side_effect = ["10", "MN"]
        self.tax = tax_calculator.Taxes()
        self.order = self.tax.checkout()

    def test_MN_tax_amount_is_0(self):
        self.assertEqual(0, self.order['tax'])

    def test_MN_total_amount_is_10(self):
        self.assertEqual(10, self.order['total'])

if __name__ == "__main__":
    unittest.main()
