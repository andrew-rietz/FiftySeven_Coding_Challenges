import os
import sys
import unittest
import unittest.mock

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from paint_calc import paint_calc

class PaintCalcTests(unittest.TestCase):

    @unittest.mock.patch("builtins.input", lambda *args: "600")
    def setUp(self):
        self.paint_calc = paint_calc.PaintCalculator()

    def test_area_is_600(self):
        self.assertEqual(600, self.paint_calc.area)

    def test_conversion_factor_is_350(self):
        self.assertEqual(350, self.paint_calc.GALLON_SF_COVERAGE)

    def test_gallons_is_2(self):
        self.assertEqual(2, self.paint_calc.gallons_needed())

if __name__ == "__main__":
    unittest.main()
