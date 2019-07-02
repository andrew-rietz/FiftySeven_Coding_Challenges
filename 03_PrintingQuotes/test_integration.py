import unittest
import unittest.mock
import io
from contextlib import redirect_stdout
import PrintingQuotes

class IntegrationTests(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def test_main_valid(self, mock_inputs):
        mock_inputs.side_effect = [
            "These aren't the droids you're looking for",
            "Obi-Wan Kenobi"]
        expected_result = "Obi-Wan Kenobi says, \"These aren't the droids you're looking for\""
        print_output = io.StringIO()
        with redirect_stdout(print_output):
            PrintingQuotes.main()
            test_val = print_output.getvalue().strip()

        self.assertEqual(test_val, expected_result)

if __name__ == "__main__":
    unittest.main()
