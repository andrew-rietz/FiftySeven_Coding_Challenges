import PrintingQuotes
import unittest
import unittest.mock

class PrintingQuotesTest(unittest.TestCase):

    user_inputs = [
        "These aren't the droids you're looking for",
        "Obi-Wan Kenobi"
    ]

    @unittest.mock.patch("builtins.input")
    def test_get_inputs(self, mock_inputs):
        mock_inputs.side_effect = [
            "These aren't the droids you're looking for",
            "Obi-Wan Kenobi"]
        self.assertEqual(
            PrintingQuotes.get_inputs(),
            {
                "quote": "These aren't the droids you're looking for",
                "author": "Obi-Wan Kenobi",
            }
        )

if __name__ == "__main__":
    unittest.main()
