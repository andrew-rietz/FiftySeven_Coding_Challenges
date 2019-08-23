import unittest
import unittest.mock
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from temp_convert import temp_convert


class TempConverterTests(unittest.TestCase):
    """Tests the methods of the BACCalculator Class"""

    def setUp(self):
        self.converter = temp_convert.TempConverter()

    def test_32f_to_c(self):
        self.converter.temp_type = "F"
        self.converter.convert_to = "C"
        self.converter.temp = 32
        self.assertEqual(0, self.converter.convert())

    def test_0c_to_f(self):
        self.converter.temp_type = "C"
        self.converter.convert_to = "F"
        self.converter.temp = 0
        self.assertEqual(32, self.converter.convert())


if __name__ == "__main__":
    unittest.main()
