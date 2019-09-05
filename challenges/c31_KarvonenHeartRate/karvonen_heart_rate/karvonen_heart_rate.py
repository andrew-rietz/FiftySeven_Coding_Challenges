"""
Defines a set of functions and a class that generates a Karvonen Heart Rate table based on user input
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util_functions.utils import user_inputs

def get_inputs():
    """Prompts the user to enter their age and resting heart rate

    Args:
        n/a

    Returns:
        (dict): {"resting_heart_rate": resting_heart_rate, "age": age}
    """
    resting_heart_rate = user_inputs.get_positive_number(
        prompt="What is your resting pulse?",
        err_msg="Please enter a positive number."
    )
    age = user_inputs.get_positive_number(
        prompt="How old are you?",
        err_msg="Please enter a positive number."
    )
    return {"resting_heart_rate": resting_heart_rate, "age": age}

class KarvonenCalculator():
    """Represents an individualized Karvonen Heart Rate calculator

    Attributes:
        resting_heart_rate (float): individual's resting heart rate
        age (float): individual's age
    """
    def __init__(self, resting_heart_rate=None, age=None):
        self.resting_heart_rate = resting_heart_rate
        self.age = age
        self.intensity_data = None
        self.table = None

    def calc_target_heart_rate(self, intensity):
        """Calculates the target heart rate base on resting heart rate, age, and intensity

        Args:
            resting_heart_rate (float): individual's resting heart rate
            age (float): individual's age
            intensity (float): desired intensity level

        Returns:
            target_heart_rate (float): Target heart rate to achieve desired intensity
        """
        target_heart_rate = (
            (((220 - self.age) - self.resting_heart_rate) * (intensity / 100)) +
            self.resting_heart_rate
        )
        return target_heart_rate

    def generate_heart_rate_data(self, low_bound=0, high_bound=100, step_size=1):
        """Generates a list of 2-element lists. The first element in each list is the intensity,
        and the second element is the target heart rate

        Args:
            low_bound (float): low bound for the intensities
            high_bound (float): high bound for the intensities
            step_size (float): increments in which to step from low_bound to high_bound

        Returns:
            heart_rate_intensities (list): A list of 2-element lists. The first element in
                each list is the intensity, and the second element is the target heart rate.
        """
        heart_rate_intensities = [["Intensity", "Target Heart Rate"]]
        for intensity in range(low_bound, high_bound + step_size, step_size):
            heart_rate_intensities.append(
                [f"{intensity}%", f"{self.calc_target_heart_rate(intensity):,.1f} bpm"]
            )

        self.intensity_data = heart_rate_intensities
        return "Success"


    def print_ascii_table(self):
        """Creates an ascii table based on the input table_data variable

        Args:
            self.intensity_data (list): A list of lists. Each list corresponds to one row
                in the table and it's assumed that the first contains the column headers. i.e.:
                [['Header 1', 'Header 2'], ['Foo', 'Bar'], [1, 2]]

        Returns:
            table (str): String representation of the table
        """
        table_columns = len(self.intensity_data[0])
        stringified_table_data = [
            [str(cell) for cell in sub_list]
            for sub_list in self.intensity_data
        ]
        max_length_by_column = [0] * len(stringified_table_data[0])
        for sub_list in stringified_table_data:
            for cell in range(len(sub_list)):
                cell_characters = len(sub_list[cell])
                if cell_characters > max_length_by_column[cell]:
                    max_length_by_column[cell] = cell_characters

        horizontal_breaks = ["-" * (max_length_by_column[i]+1) for i in range(table_columns)]
        table_body = [
            [sub_list[i].center(max_length_by_column[i]+1) for i in range(table_columns)]
            for sub_list in stringified_table_data
        ]
        table = "| ".join(table_body[0]) + "\n" + "|".join(horizontal_breaks) + " "
        for sub_list in table_body[1:]:
            table += "\n" + "| ".join(sub_list)

        self.table = table
        print(self.table)
        return "Success"


def main():
    user_values = get_inputs()

    heart_rate_calculator = KarvonenCalculator()
    heart_rate_calculator.resting_heart_rate = user_values["resting_heart_rate"]
    heart_rate_calculator.age = user_values["age"]
    heart_rate_calculator.generate_heart_rate_data(55, 95, 5)
    heart_rate_calculator.print_ascii_table()


if __name__ == "__main__":
    main()
