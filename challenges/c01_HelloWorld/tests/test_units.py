import os
import sys
import unittest
import unittest.mock

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from hello_world import hello_world


class HelloWorldTests(unittest.TestCase):
    @unittest.mock.patch("builtins.input", lambda *args: "andrew")
    def setUp(self):
        self.greet = hello_world.Greeting()

    def test_hello(self):
        self.assertEqual(
            self.greet.hello(),
            "Hello, Andrew, nice to meet you!",
        )

if __name__ == "__main__":
    unittest.main()
