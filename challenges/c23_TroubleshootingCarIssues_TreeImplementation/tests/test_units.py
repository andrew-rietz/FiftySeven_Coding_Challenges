import os
import sys
import unittest
import unittest.mock

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from compare_numbers import compare_numbers

class MaxInListTests(unittest.TestCase):
    """Tests the max_in_list function"""

    def test_list_of_strings(self):
        input_list = ["asdf", "1", "2", "foo"]
        self.assertEqual("foo", compare_numbers.max_in_list(input_list))

    def test_list_of_numbers(self):
        input_list = [1, -100, 2.5343, 53]
        self.assertEqual(53, compare_numbers.max_in_list(input_list))

    def test_mixed_list(self):
        input_list = [1, -100, 2.5343, 53, "foo"]
        with self.assertRaises(TypeError):
            compare_numbers.max_in_list(input_list)

if __name__ == "__main__":
    unittest.main()
