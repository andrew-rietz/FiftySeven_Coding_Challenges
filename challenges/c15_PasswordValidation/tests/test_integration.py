import unittest
import unittest.mock
import io
from contextlib import redirect_stdout

if __name__ == '__main__':
    if __package__ is None:
        import sys
        import os
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from password_validation import password_validation
    else:
        from ..password_validation import password_validation
else:
    from password_validation import password_validation

class PasswordValidatorIntegrationTest(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def test_good_pw(self, mock_inputs):
        mock_inputs.side_effect = ["abc$123"]

        expected_result = (
            f"Welcome!"
        )
        print_output = io.StringIO()
        with redirect_stdout(print_output):
            password_validation.main()
            test_val = print_output.getvalue().strip()

        self.assertEqual(expected_result, test_val)

    @unittest.mock.patch("builtins.input")
    def test_bad_pw(self, mock_inputs):
        mock_inputs.side_effect = ["wrong_pw"]

        expected_result = (
            f"I don't know you."
        )
        print_output = io.StringIO()
        with redirect_stdout(print_output):
            password_validation.main()
            test_val = print_output.getvalue().strip()

        self.assertEqual(expected_result, test_val)

if __name__ == "__main__":
    unittest.main()
