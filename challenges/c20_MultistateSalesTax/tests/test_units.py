import io
import os
import sys
import unittest
import unittest.mock

from contextlib import redirect_stdout

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from multistate_tax import multistate_tax

class MulistateTaxesClassTests(unittest.TestCase):
    """Tests the methods of the MultistateTaxes Class"""

    def setUp(self):
        self.taxes = multistate_tax.MultistateTaxes()

    def test_100_valid_state_valid_county(self):
        self.taxes.subtotal = 100
        self.taxes.state = "WI"
        self.taxes.county = "DUNN"
        order = self.taxes.checkout()
        self.assertEqual(5.40, round(order["tax"], 2))
        self.assertEqual(105.40, round(order["total"], 2))

    def test_100_valid_state_only(self):
        self.taxes.subtotal = 100
        self.taxes.state = "WI"
        self.taxes.county = "some-fake-county"
        order = self.taxes.checkout()
        self.assertEqual(5.00, round(order["tax"], 2))
        self.assertEqual(105.00, round(order["total"], 2))

    def test_100_invalid_state_and_county(self):
        self.taxes.subtotal = 100
        self.taxes.state = "CA"
        self.taxes.county = "some-fake-county"
        order = self.taxes.checkout()
        self.assertEqual(0.00, round(order["tax"], 2))
        self.assertEqual(100.00, round(order["total"], 2))

if __name__ == "__main__":
    unittest.main()
