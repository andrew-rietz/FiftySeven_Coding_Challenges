"""
Defines a StatsCalculator class and instantiates it
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util_functions.utils import user_inputs

class StatsCalculator():
    """Represents a statistical summary calculator

    Attributes:
        population (list): The sample data points. Must be numeric

    Methods:
        min: Returns min value in population
        max: Returns max value in population
        mean: Returns the mean of the population
        stddev: Returns the standard deviation of the population
        summary: Retuns all of the above
    """

    def __init__(self):
        self.population = []

    def add_to_pop(self, population):
        """Attempts to add values to the population. Argument must be either
        a float, int, or list.

        Args:
            population (list, int, float): Value(s) to add to the population
        """
        if isinstance(population, (int, float)):
            self.population.append(float(population))
            return "Success"
        if isinstance(population, list):
            for val in population:
                try:
                    self.population.append(float(val))
                except ValueError:
                    pass
            return "Success"
        return "'sample' must be a list, integer, or float"

    def _mean(self):
        if not self.population:
            return None
        return sum(self.population) / len(self.population)

    def mean(self):
        return self._mean()

    def _min(self):
        if not self.population:
            return None
        return min(self.population)

    def min(self):
        return self._min()

    def _max(self):
        if not self.population:
            return None
        return max(self.population)

    def max(self):
        return self._max()

    def _stddev(self):
        if not self.population:
            return None
        mean = self._mean()
        diff_from_mean_squared = [
            ((val - mean) ** 2) for val in self.population
        ]
        stddev = (sum(diff_from_mean_squared) / len(diff_from_mean_squared)) ** 0.5
        return stddev

    def stddev(self):
        return self._stddev()

    def summary(self):
        if not self.population:
            return None
        return (
            f"The average is {self._mean():,.2f}.\n" +
            f"The minimum is {self._min():,.2f}.\n" +
            f"The maximum is {self._max():,.2f}.\n" +
            f"The standard deviation is {self._stddev():,.2f}."
        )

def get_number():
    number = user_inputs.get_any_number(
        prompt="Enter a number:",
        err_msg="You must enter a number (or 'done' to exit).",
        exit_val="done"
    )
    return number

def main():
    calc = StatsCalculator()
    while True:
        number = get_number()
        if number is None:
            break
        calc.add_to_pop(number)
    if calc.population:
        print(
            f"Numbers: {', '.join(f'{val:,.2f}' for val in calc.population)}\n" +
            f"{calc.summary()}"
        )


if __name__ == "__main__":
    main()
