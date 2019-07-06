import unittest
import unittest.mock

from tests.context import printing_quotes

class PrintingQuotesTest(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def setUp(self, mock_inputs):
        mock_inputs.side_effect = [
            "These aren't the droids you're looking for",
            "Obi-Wan Kenobi"
        ]
        self.cite = printing_quotes.Citation()


    def test_quote_input(self):
        self.assertEqual(
            self.cite.quote,
            "These aren't the droids you're looking for")

    def test_author_input(self):
        self.assertEqual(
            self.cite.author,
            "Obi-Wan Kenobi")

if __name__ == "__main__":
    unittest.main()
