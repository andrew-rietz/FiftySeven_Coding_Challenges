"""
Class and methods for temperature conversion
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util_functions.utils import user_inputs


class TempConverter():
    """Represents a temperature conversion calculator

    Attributes:
        TEMP_SCALES: Constant. Defines the temperatures scales usable by the class
        CONVERT_SCALES: Constant. Map of value to convert to

        temp_type: The scale in which the user enters a temperature to convert
        convert_to: The scale the temperature should be converted to
        temp: The user's temperature to be converted
    """

    TEMP_SCALES = {"C": "Celsius", "F": "Fahrenheit"}
    CONVERT_SCALES = {"C": "F", "F": "C"}

    def __init__(self, temp_type=None, convert_to=None, temp=None):
        """Initializes the class"""
        self.temp_type = temp_type
        self.convert_to = convert_to
        self.temp = temp

    def convert(self):
        """Converts from one temperature scale to another

        The formulas to convert from Celsius (C) to Fahrenheit (F) and vice versa
        are shown below:
        C = (F - 32) * 5/9
        F = (C * 9/5) + 32

        Returns:
            new_temp: The converted temperature
        """
        if self.temp_type == "C" and self.convert_to == "F":
            new_temp = (self.temp * 9 / 5) + 32
        elif self.temp_type == "F" and self.convert_to == "C":
            new_temp = (self.temp - 32) * 5 / 9

        return new_temp

def main():
    converter = TempConverter()
    converter.convert_to = user_inputs.get_string_in_list(
        prompt=(
            "Press 'C' to convert from Fahrenheit to Celsius.\n" +
            "Press 'F' to convert from Celsius to Fahrenheit.\n" +
            "Please enter your choice:"
        ),
        err_msg="Enter a valid selection.",
        allowed_vals=list(converter.TEMP_SCALES.keys()),
        case_sensitive=False
    ).upper()
    converter.temp_type = converter.CONVERT_SCALES[converter.convert_to]

    converter.temp = user_inputs.get_any_number(
        prompt=f"Please enter the temperature in {converter.TEMP_SCALES[converter.temp_type]}:",
        err_msg="Please enter a numeric value."
    )

    converted = converter.convert()
    print(f"The temperature in {converter.TEMP_SCALES[converter.convert_to]} is {converted:.1f}.\n")

if __name__ == "__main__":
    main()
