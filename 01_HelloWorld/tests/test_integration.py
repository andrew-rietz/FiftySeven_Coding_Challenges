from contextlib import redirect_stdout

import unittest
import unittest.mock
import io

from tests.context import hello_world

class IntegrationTests(unittest.TestCase):

    @unittest.mock.patch("builtins.input", lambda *args: "andrew")
    def test_main_valid(self):
        expected_result = "Hello, Andrew, nice to meet you!"
        print_output = io.StringIO()
        with redirect_stdout(print_output):
            hello_world.main()
            test_val = print_output.getvalue().strip()

        self.assertEqual(test_val, expected_result)

if __name__ == "__main__":
    unittest.main()
