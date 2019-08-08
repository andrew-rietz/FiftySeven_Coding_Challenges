"""
Defines and implements a compound interest calculator class
Extends the `InterestCalculator` class defined in c11
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

class CompoundInterestCalculator():
    """Represents a compound interest calculator

    Calculates the compound interest earned on an investment over a given period
    of time, and returns the total value of the investment at the end of the
    period.

    Attributes:
        CONV_PCT: An integer constant to convert `interest rates` from numeric to decimal
        principal: A float representing the initial investment
        rate: A float representing the annual interest rate as a percentage
            (i.e., 15% should be entered as 15 not 0.15)
        years: An integer representing the number of years the principal is
            invested
        n: Integer representing the number of times the interest rate is
            compounded per year
    """

    def __init__(self):
        """Initialize the class -- takes user input on creation"""
        self.conv_pct = 100
        self.principal = float(input("Enter the principal amount: "))
        self.rate = float(input("Enter the rate of interest: "))
        self.years = int(input("Enter the number of years (whole numbers only): "))
        self.n = int(input(
            "What is the number of times the interest rate is compounded per " +
            "year? (whole numbers only): "
        ))

    def calc(self):
        """Calculates the value of the investment after a number of years

        Args:
            n/a -- all arguments set during class instantiation

        Returns:
            investment: Total value of the investment based on the specified
                principal, interest rate, and number of years
        """
        investment = round(
            self.principal * (1 + ((self.rate / self.conv_pct) / self.n)) **
            (self.n * self.years),
            2
        )
        return investment

def main():
    compound_interest = CompoundInterestCalculator()
    investment = compound_interest.calc()
    print(
        f"${compound_interest.principal:,.2f} invested at {compound_interest.rate:,.2f}% for " +
        f"{compound_interest.years} years compounded {compound_interest.n} times per year is " +
        f"${investment:,.2f}."
    )

if __name__ == "__main__":
    main()
