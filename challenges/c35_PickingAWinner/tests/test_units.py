import io
import os
import sys
import unittest
import unittest.mock

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from picking_a_winner.picking_a_winner import PrizeDrawing, get_entry

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class PrizeDrawingTests(unittest.TestCase):
    """Tests the PrizeDrawing class"""

    def setUp(self):
        self.drawing = PrizeDrawing()

    def test__add_name__valid_input(self):
        self.drawing.add("Foo")
        self.assertTrue("Foo" in self.drawing.entries)

    def test__add_name__invalid_input(self):
        self.drawing.add("")
        self.assertTrue("" not in self.drawing.entries)

    def test__pick_winner(self):
        self.drawing.entries = ["Foo", "Bar", "Baz"]
        winner = self.drawing.pick_winner()
        self.assertTrue(winner in self.drawing.entries)

class GetEntryTests(unittest.TestCase):
    """Tests the get_entry function"""

    @unittest.mock.patch("builtins.input")
    def test__entry_is_foo(self, mock_inputs):
        mock_inputs.side_effect = ["  foo  "]
        self.assertEqual("foo", get_entry())


if __name__ == "__main__":
    unittest.main(verbosity=3)
