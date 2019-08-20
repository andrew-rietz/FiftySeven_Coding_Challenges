"""
Class and functions for calculating BMI Calcs
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util_functions.utils import user_inputs

class BMICalculator():
    """A representation of a BMI calculator

    Attributes:
        HEALTHY_BMI: A tuple defining the low end and high end of the healthy
            BMI range

        height: individual's height, in inches
        weight: individual's weight, in pounds
        bmi: Calculated. individual's bmi
    """
    HEALTHY_BMI = (18.5, 25)

    def __init__(self, height=None, weight=None):
        """Inits BMICalculator with 'None' as defaults"""
        self.height = height
        self.weight = weight
        self.bmi = None

    def get_bmi(self):
        """Calculates the Body Mass Index (BMI) of the individual

        BMI is calculated using the formula below:
        bmi = (weight / (height * height)) * 703

        Returns:
            bmi: the individual's BMI
        """
        self.bmi = (self.weight / (self.height ** 2)) * 703
        return self.bmi

    def healthy_range(self):
        """Determines whether the individual is within their ideal weight range

        Returns:
            diagnosis: Tells the individual whether they are within the healthy
                BMI range or if they should see a doctor.
        """
        if self.bmi is None:
            self.get_bmi()

        healthy_low, healthy_high = self.HEALTHY_BMI
        if self.bmi >= healthy_low and self.bmi <= healthy_high:
            diagnosis = "You are within the ideal weight range."
        else:
            over_under = "over" if self.bmi > healthy_high else "under"
            diagnosis = f"You are {over_under}weight. You should see your doctor."

        return diagnosis


def main():
    height = user_inputs.get_positive_number(
        prompt="Please enter your height in inches:",
        err_msg="Please enter a numeric value."
    )
    weight = user_inputs.get_positive_number(
        prompt="Please enter your weight in pounds:",
        err_msg="Please enter a numeric value."
    )

    calc = BMICalculator(height, weight)
    diagnosis = calc.healthy_range()
    print(f"Your BMI is {calc.bmi:.1f}.\n{diagnosis}")

if __name__ == "__main__":
    main()
