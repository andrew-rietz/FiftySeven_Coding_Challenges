"""
Defines and implements a simple interest calculator class
"""
class InterestCalculator():
    """Represents a simple interest calculator

    Calculates the simple interest earned on an investment over a given period
    of time, and returns the total value of the investment at the end of the
    period.

    Attributes:
        CONV_PCT: A constant to convert `rate` from numeric to decimal
        principal: A float representing the initial investment
        rate: A float representing the annual interest rate as a percentage
            (i.e., 15% should be entered as 15 not 0.15)
        years: An integer representing the number of years the principal is
            invested
    """

    def __init__(self):
        """Initialize the class -- takes user input on creation"""
        self.conv_pct = 100
        self.principal = float(input("Enter the principal amount: "))
        self.rate = float(input("Enter the rate of interest: "))
        self.years = int(input("Enter the number of years (whole numbers only): "))

    def calc(self):
        """Calculates the value of the investment after a number of years

        Args:
            n/a -- all arguments set during class instantiation

        Returns:
            investment: Total value of the investment based on the specified
                principal, interest rate, and number of years
        """
        investment = round(
            self.principal * (1 + (self.rate / self.conv_pct) * self. years),
            2
        )
        return investment

def main():
    simple_int = InterestCalculator()
    investment = simple_int.calc()
    print(
        f"After {simple_int.years} years at {simple_int.rate:,.2f}%, the " +
        f"initial investment of ${simple_int.principal:,.2f} will be worth " +
        f"${investment:,.2f}."
    )

if __name__ == "__main__":
    main()
