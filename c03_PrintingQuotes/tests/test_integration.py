import unittest
import unittest.mock
import io
from contextlib import redirect_stdout

if __name__ == '__main__':
    if __package__ is None:
        import sys
        import os
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from printing_quotes import printing_quotes
    else:
        from ..printing_quotes import printing_quotes
else:
    from printing_quotes import printing_quotes

class IntegrationTests(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def test_main_valid(self, mock_inputs):
        mock_inputs.side_effect = [
            "These aren't the droids you're looking for",
            "Obi-Wan Kenobi"]
        expected_result = "Obi-Wan Kenobi says, \"These aren't the droids you're looking for\""
        print_output = io.StringIO()
        with redirect_stdout(print_output):
            printing_quotes.main()
            test_val = print_output.getvalue().strip()

        self.assertEqual(test_val, expected_result)

if __name__ == "__main__":
    unittest.main()
