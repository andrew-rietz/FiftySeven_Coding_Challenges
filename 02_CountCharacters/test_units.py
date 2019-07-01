import unittest
import CountCharacters

class CountCharactersTest(unittest.TestCase):

    def test_count_valid(self):
        self.assertEqual(
            CountCharacters.n_characters("hello"),
            5,
        )

    def test_count_nonsense(self):
        self.assertEqual(
            CountCharacters.n_characters("abc 123"),
            7,
        )

if __name__ == "__main__":
    unittest.main()
