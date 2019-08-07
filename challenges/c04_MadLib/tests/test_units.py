import unittest
import unittest.mock

if __name__ == '__main__':
    if __package__ is None:
        import sys
        import os
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from madlib import madlib
    else:
        from ..madlib import madlib
else:
    from madlib import madlib

class MadlibUnitTests(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def setUp(self, mock_inputs):
        mock_inputs.side_effect = ["dog", "walk", "blue", "quickly"]
        self.ml = madlib.Madlib()

    def test_noun(self):
        self.assertEqual("dog", self.ml.noun)

    def test_verb(self):
        self.assertEqual("walk", self.ml.verb)

    def test_adjective(self):
        self.assertEqual("blue", self.ml.adjective)

    def test_adverb(self):
        self.assertEqual("quickly", self.ml.adverb)

if __name__ == "__main__":
    unittest.main()
