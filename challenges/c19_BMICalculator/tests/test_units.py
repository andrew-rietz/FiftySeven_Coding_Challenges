import sys
import unittest
import unittest.mock
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bmi_calc import bmi_calc

from bmi_calc.bmi_calc import BMICalculator


class BMICalcTests(unittest.TestCase):
    """Tests the methods of the BACCalculator Class"""

    def setUp(self):
        self.calc = bmi_calc.BMICalculator()

    def test_72inches_180lbs_is_24_4(self):
        self.calc.height = 72
        self.calc.weight = 180
        self.assertEqual(24.4, round(self.calc.get_bmi(),1))

    def test_24_4_is_healthy(self):
        self.calc.bmi = 24.4
        expected_output = "You are within the ideal weight range."
        self.assertEqual(expected_output, self.calc.healthy_range())

    def test_18_4_is_unhealthy(self):
        self.calc.bmi = 18.4
        expected_output = (
            "You are underweight. You should see your doctor."
        )
        self.assertEqual(expected_output, self.calc.healthy_range())

    def test_18_4_is_unhealthy(self):
        self.calc.bmi = 25.1
        expected_output = (
            "You are overweight. You should see your doctor."
        )
        self.assertEqual(expected_output, self.calc.healthy_range())


if __name__ == "__main__":
    unittest.main()
