import unittest
import unittest.mock
import io
from contextlib import redirect_stdout

from tests.context import madlib

class MadlibIntegrationTest(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def test_output(self, mock_inputs):
        mock_inputs.side_effect = ["dog", "walk", "blue", "quickly"]
        expected_result = "Do you walk your blue dog quickly? That's hilarious!"
        print_output = io.StringIO()
        with redirect_stdout(print_output):
            madlib.main()
            test_val = print_output.getvalue().strip()

        self.assertEqual(test_val, expected_result)

if __name__ == "__main__":
    unittest.main()
