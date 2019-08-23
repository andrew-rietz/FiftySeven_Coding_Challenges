import io
import os
import sys
import unittest
import unittest.mock

from contextlib import redirect_stdout

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from numbers_to_names import numbers_to_names

class NumberToNameTests(unittest.TestCase):
    """Tests the the month_number_to_name function"""

    def test_3_is_March(self):
        month = numbers_to_names.month_number_to_name(3)
        self.assertEqual("March", month)

if __name__ == "__main__":
    unittest.main()
