import unittest
import unittest.mock
import io
from contextlib import redirect_stdout

if __name__ == '__main__':
    if __package__ is None:
        import sys
        import os
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from simple_math import simple_math
    else:
        from ..simple_math import simple_math
else:
    from simple_math import simple_math

class SimpleMathIntegrationTest(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def test_output(self, mock_inputs):
        mock_inputs.side_effect = ["10", "5"]
        expected_result = (
            f"10.0 + 5.0 = 15.0\n" +
            f"10.0 - 5.0 = 5.0\n" +
            f"10.0 * 5.0 = 50.0\n" +
            f"10.0 / 5.0 = 2.0"
        )
        print_output = io.StringIO()
        with redirect_stdout(print_output):
            simple_math.main()
            test_val = print_output.getvalue().strip()

        self.assertEqual(expected_result, test_val)

if __name__ == "__main__":
    unittest.main()
