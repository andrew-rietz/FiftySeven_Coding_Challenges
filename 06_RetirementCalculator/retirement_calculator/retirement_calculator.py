from datetime import datetime

class Calculator():
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
