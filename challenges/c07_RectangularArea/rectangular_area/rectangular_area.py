"""
Defines and implements a square footage calculator class
"""
class Calculator():
    """
    Representation of an area calculator that takes two numbers and multiplies them together

    Attributes:
        len: A float indicating the length of a surface
        width: A float indicating the width of a surface
    """
    # Conversion factor for ft2 to m2
    IMPERIAL_TO_METRIC = 0.09290304

    def __init__(self):
        self.len = float(input("What is the length of the room in feet? "))
        self.width = float(input("What is the width of the room in feet? "))

    def area_imperial(self):
        return self.len * self.width

    def area_metric(self):
        return (self.len * self.width) * self.IMPERIAL_TO_METRIC

def main():
    calc = Calculator()
    ft2 = calc.area_imperial()
    m2 = calc.area_metric()

    print(
        f"The area is:\n" +
        f"{ft2:,.1f} square feet\n" +
        f"{m2:,.2f} square meters"
    )

if __name__ == "__main__":
    main()
