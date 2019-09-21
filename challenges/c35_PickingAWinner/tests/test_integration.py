import unittest
import unittest.mock
import io
import sys
import os

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from picking_a_winner import picking_a_winner

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class PickingAWinnerTests(unittest.TestCase):
    """Tests that the 'main' function works as expected"""

    @unittest.mock.patch("builtins.input")
    def test__main(self, mock_inputs):
        entries = ["Homer", "Bart", "Maggie", "Lisa", "Moe", ""]
        mock_inputs.side_effect = entries
        with captured_output() as (outputs, _):
            picking_a_winner.main()
            winner_name = outputs.getvalue().strip().split()[-1]
        self.assertTrue(winner_name in entries)


if __name__ == "__main__":
    unittest.main()
