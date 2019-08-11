import unittest
import unittest.mock
import io
import sys
import os

from contextlib import redirect_stdout

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tracking_inventory import tracking_inventory


class TrackingInventoryTests(unittest.TestCase):
    """Tests that the 'main' function works as expected"""


if __name__ == "__main__":
    unittest.main()
