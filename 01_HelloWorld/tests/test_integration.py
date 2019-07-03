from contextlib import redirect_stdout

import unittest
import unittest.mock
import io

from context import HelloWorld

class IntegrationTests(unittest.TestCase):

    @unittest.mock.patch("builtins.input", lambda *args: "andrew")
    def test_main_valid(self):
        expected_result = "Hello, Andrew, nice to meet you!"
        print_output = io.StringIO()
        with redirect_stdout(print_output):
            HelloWorld.main()
            test_val = print_output.getvalue().strip()

        self.assertEqual(test_val, expected_result)
        # assert test_val.strip() == expected_result
        # print(f"Passed. '{input()}' >>> '{expected_result}'")

    @unittest.mock.patch("builtins.input", lambda *args: "3van")
    def test_main_invalid(self):
        expected_result = "Sorry, please enter a valid name."
        print_output = io.StringIO()
        with redirect_stdout(print_output):
            HelloWorld.main()
            test_val = print_output.getvalue().strip()

        self.assertEqual(test_val, expected_result)
        # assert test_val.strip() == expected_result
        # print(f"Passed. '{input()}' >>> '{expected_result}'")

# def main():
#     test_main_valid()
#     test_main_invalid()

if __name__ == "__main__":
    unittest.main()
