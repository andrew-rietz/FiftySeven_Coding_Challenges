import unittest
import unittest.mock
import io
from contextlib import redirect_stdout

if __name__ == '__main__':
    if __package__ is None:
        import sys
        import os
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from madlib import madlib
    else:
        from ..madlib import madlib
else:
    from madlib import madlib

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
