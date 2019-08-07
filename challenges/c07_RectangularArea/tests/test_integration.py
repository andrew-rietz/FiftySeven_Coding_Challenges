import unittest
import unittest.mock
import io
from contextlib import redirect_stdout

if __name__ == '__main__':
    if __package__ is None:
        import sys
        import os
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from rectangular_area import rectangular_area
    else:
        from ..rectangular_area import rectangular_area
else:
    from rectangular_area import rectangular_area

class RectangularAreaIntegrationTest(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def test_output(self, mock_inputs):
        mock_inputs.side_effect = ["10", "20"]

        expected_result = (
            f"The area is:\n" +
            f"200.0 square feet\n" +
            f"18.58 square meters"
        )
        print_output = io.StringIO()
        with redirect_stdout(print_output):
            rectangular_area.main()
            test_val = print_output.getvalue().strip()

        self.assertEqual(expected_result, test_val)

if __name__ == "__main__":
    unittest.main()
