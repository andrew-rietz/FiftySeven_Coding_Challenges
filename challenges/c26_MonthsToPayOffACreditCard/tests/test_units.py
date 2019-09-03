import os
import sys
import unittest
import unittest.mock

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from months_to_pay_credit_card import months_to_pay_credit_card


class IsAnagramTests(unittest.TestCase):
    """Tests the is_anagram function"""

    def test__5000_12apr_100monthly__is_70_months(self):
        months = months_to_pay_credit_card.calculate_months_until_paid_off(5000, 12, 100)
        self.assertEqual(70, months)


if __name__ == "__main__":
    unittest.main()
