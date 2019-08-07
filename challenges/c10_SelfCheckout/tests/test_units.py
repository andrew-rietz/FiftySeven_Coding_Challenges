import unittest
import unittest.mock

if __name__ == '__main__':
    if __package__ is None:
        import sys
        import os
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from self_checkout import self_checkout
    else:
        from ..self_checkout import self_checkout
else:
    from self_checkout import self_checkout

class SelfCheckoutTests(unittest.TestCase):

    #@unittest.mock.patch("builtins.input")
    def setUp(self):
        self.a_shopper = self_checkout.Shopper()
        self.cart_item_1 = self.a_shopper.add_item(25, 2)
        self.cart_item_2 = self.a_shopper.add_item(10, 1)

    def test_cart_has_2_items(self):
        self.assertEqual(2, len(self.a_shopper.cart))

    def test_cart_item_1_has_price_25(self):
        self.assertEqual(25, self.cart_item_1["price"])

    def test_cart_item_1_has_qty_2(self):
        self.assertEqual(2, self.cart_item_1["quantity"])

    def test_cart_item_2_has_price_10(self):
        self.assertEqual(10, self.cart_item_2["price"])

    def test_cart_item_2_has_qty_1(self):
        self.assertEqual(1, self.cart_item_2["quantity"])

    def test_subtotal_is_60_dollars(self):
        self.assertEqual(60, self.a_shopper.checkout()["subtotal"])

    def test_tax_is_3_dollars_30_cents(self):
        self.assertEqual(3.3, self.a_shopper.checkout()["tax"])

    def test_total_is_63_dollars_30_cents(self):
        self.assertEqual(63.3, self.a_shopper.checkout()["total"])

if __name__ == "__main__":
    unittest.main()
