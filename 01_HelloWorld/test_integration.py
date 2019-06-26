import unittest
import io
from contextlib import redirect_stdout
import HelloWorld

# @patch("builtins.input", lambda *args: "andrew")
# def test_main_valid(self):
#     evaluated = str(HelloWorld.main())
#     self.assertEqual(evaluated, "Hello, Andrew, nice to meet you!")
#
# if __name__ == "__main__":
#     unittest.main()


def test_main_valid():
    print_output = io.StringIO()
    with redirect_stdout(print_output):
        main_output = HelloWorld.main()
        print(f"main output: {main_output}")
        # with unittest.mock.patch("builtins.input", lambda *args: "andrew"):
        #     assert input() == "andrew"
        #     print("Passed")



test_main_valid()
