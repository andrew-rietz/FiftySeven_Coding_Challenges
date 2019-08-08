"""
Defines and implements a class to help with area coverage calculations
"""
import math

class PaintCalculator():
    """
    Representation of a paint coverage calculator

    Attributes:
        GALLON_SF_COVERAGE: An integer constant that describes the area (sq ft) a single can of
            of paint can cover
        area: An integer representing the area (sq ft) to be painted
    """
    # Conversion factor: one gallon == 350 sq ft
    GALLON_SF_COVERAGE = 350

    def __init__(self):
        self.area = int(input("What is the size of the ceiling in square feet? "))

    def gallons_needed(self):
        return math.ceil(self.area / self.GALLON_SF_COVERAGE)

def main():
    calc = PaintCalculator()
    gallons = calc.gallons_needed()
    print(
        f"You will need to purchase {gallons} gallons of paint to cover the " +
        f"{calc.area} square feet."
    )

if __name__ == "__main__":
    main()
