import os
import sys
import unittest
import unittest.mock

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from anagram_checker import anagram_checker

class IsAnagramTests(unittest.TestCase):
    """Tests the is_anagram function"""

    def test_valid_anagram(self):
        self.assertEqual(True, anagram_checker.is_anagram("Note", "tone"))

    def test_invalid_anagram(self):
        self.assertEqual(False, anagram_checker.is_anagram("foo", "bar"))


if __name__ == "__main__":
    unittest.main()
