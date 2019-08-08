"""
Defines and implements a retirement calculator class
"""
from datetime import datetime

class Calculator():
    """
    Representation of a retirement calculator that determines when an end user can retire 

    Attributes:
        year: A datetime object representing the current year
        age: An integer representing the end-user's current age
        retirement_age: An integer representing the age at which end user wants to retire
        years_to_retire: An integer representing the number of years until end user can retire
        retirement_year: A datetime object representing the year in which end user can retire
    """
    def __init__(self):
        self.year = datetime.date(datetime.today()).year
        self.age = int(input("What is your current age? "))
        self.retirement_age = int(input("At what age would you like to retire? "))
        self.years_to_retire = self.retirement_age - self.age
        self.retirement_year = self.year + self.years_to_retire

    def print_result(self):
        return(
            f"You have {self.years_to_retire} years left until you can retire.\n" +
            f"It's {self.year}, so you can retire in {self.retirement_year}."
        )

def main():
    retirement_calc = Calculator()
    print(retirement_calc.print_result())

if __name__ == "__main__":
    main()
