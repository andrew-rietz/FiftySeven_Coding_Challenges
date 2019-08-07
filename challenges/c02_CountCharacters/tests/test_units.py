import unittest
import unittest.mock

if __name__ == '__main__':
    if __package__ is None:
        import sys
        import os
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from count_characters import count_characters
    else:
        from ..count_characters import count_characters
else:
    from count_characters import count_characters

class CountCharactersTest(unittest.TestCase):

    @unittest.mock.patch("builtins.input", lambda *args: "hello")
    def setUp(self):
        self.parse = count_characters.StringParser()

    def test_count_valid(self):
        self.assertEqual(
            self.parse.n_characters(),
            5,
        )

    def test_str_repr(self):
        self.assertEqual(
            str(self.parse),
            "hello",
        )

if __name__ == "__main__":
    unittest.main()
