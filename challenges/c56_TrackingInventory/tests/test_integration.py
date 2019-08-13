import unittest
import unittest.mock
import io
import sys
import os

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tracking_inventory import tracking_inventory

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class TrackingInventoryTests(unittest.TestCase):
    """Tests that the 'main' function works as expected"""

    # with captured_output() as (outputs, errors):
    #     tracking_inventory.main()
    #     test_val = outputs.getvalue().strip()

if __name__ == "__main__":
    unittest.main()
