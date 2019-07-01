import unittest
import unittest.mock
import io
from contextlib import redirect_stdout
import CountCharacters

class IntegrationTests(unittest.TestCase):

    @unittest.mock.patch("builtins.input", lambda *args: "hello")
    def test_main_valid(self):
        expected_result = "hello has 5 characters."
        print_output = io.StringIO()
        with redirect_stdout(print_output):
            CountCharacters.main()
            test_val = print_output.getvalue().strip()

        self.assertEqual(test_val, expected_result)

    @unittest.mock.patch("builtins.input", lambda *args: "abc 123")
    def test_main_invalid(self):
        expected_result = "abc 123 has 7 characters."
        print_output = io.StringIO()
        with redirect_stdout(print_output):
            CountCharacters.main()
            test_val = print_output.getvalue().strip()

        self.assertEqual(test_val, expected_result)

if __name__ == "__main__":
    unittest.main()
