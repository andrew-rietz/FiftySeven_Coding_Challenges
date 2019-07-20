import unittest
import unittest.mock
import io
from contextlib import redirect_stdout

from paint_calc import paint_calc

class PaintCalcIntegrationTest(unittest.TestCase):

    @unittest.mock.patch("builtins.input", lambda *args: "600")
    def test_output(self):
        expected_result = (
            "You will need to purchase 2 gallons of paint to cover the 600 square feet.")
        print_output = io.StringIO()
        with redirect_stdout(print_output):
            paint_calc.main()
            test_val = print_output.getvalue().strip()

        self.assertEqual(expected_result, test_val)

if __name__ == "__main__":
    unittest.main()
