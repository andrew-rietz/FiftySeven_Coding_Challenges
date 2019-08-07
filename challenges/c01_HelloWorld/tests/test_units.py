import unittest
import unittest.mock

if __name__ == '__main__':
    if __package__ is None:
        import sys
        import os
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from helloworld import hello_world
    else:
        from ..helloworld import hello_world
else:
    from helloworld import hello_world


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
