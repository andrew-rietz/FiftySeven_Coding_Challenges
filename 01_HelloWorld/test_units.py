import unittest
import HelloWorld

class HelloWorldTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(
            HelloWorld.hello("andrew"),
            "Hello, Andrew, nice to meet you!",
        )

    def test_is_alpha_true(self):
        self.assertEqual(
            HelloWorld.is_alpha("andrew"),
            True,
        )

    def test_is_alpha_false(self):
        self.assertEqual(
            HelloWorld.is_alpha("3van"),
            False,
        )

if __name__ == "__main__":
    unittest.main()
