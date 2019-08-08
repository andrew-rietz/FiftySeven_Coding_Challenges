"""
Defines and implements a class that performs simple arithmetic
"""
class Calculator():
    """
    Representation of a calculator that takes two numeric inputs and returns
    the result of common arithmetic operations

    Attributes:
        first_num: The first number for the calculation
        second_num: The second number for the calculation
    """

    def __init__(self):
        self.first_num = float(input("What is the first number? "))
        self.second_num = float(input("What is the second number? "))

    def sum(self):
        return self.first_num + self.second_num

    def difference(self):
        return self.first_num - self.second_num

    def product(self):
        return self.first_num * self.second_num

    def quotient(self):
        return self.first_num / self.second_num

def main():
    calc = Calculator()
    print(
        f"{calc.first_num} + {calc.second_num} = {calc.sum():,.1f}\n" +
        f"{calc.first_num} - {calc.second_num} = {calc.difference():,.1f}\n" +
        f"{calc.first_num} * {calc.second_num} = {calc.product():,.1f}\n" +
        f"{calc.first_num} / {calc.second_num} = {calc.quotient():,.1f}"
    )

if __name__ == "__main__":
    main()
