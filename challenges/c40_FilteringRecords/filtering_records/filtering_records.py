import sys
import os
from operator import itemgetter

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util_functions.utils import table, user_inputs

class EmployeeDatabase():
    """Represents a database of employee information (first name, last name,
    position/title, and separation date)

    Attributes:
        employees_data (list): A list of dictionaries. Each dictionary corresponds
            to a single employee and tracks first/last names, title, and
            separation date. Sample dictionary:
            {
                "first_name": "Foo",
                "last_name": "Bar",
                "position": "Programmer",
                :sep_date": "",
            }
        filtered_data (list): A subset of employees_data based on a user search string
    Methods:
        load_data: Loads data into the `employees_data` attribute
        get_filter_string: Prompts the user for a search string
        filter: Filters the `employees_data` attribute to only those records that
            include the user's search string in the employee first or last name
        tabulate_filtered_data: Puts the filtered data into tabular form for printing
    """

    def __init__(self, employees_data=None):
        self.employees_data = employees_data
        self.filtered_data = None

    def load_data(self):
        employee_info = [
            {
                "first_name": "John", "last_name": "Johnson",
                "position": "Manager", "sep_date": "2016-12-31",
            },
            {
                "first_name": "Tuo", "last_name": "Xiong",
                "position": "Software Engineer", "sep_date": "2016-10-05",
            },
            {
                "first_name": "Michaela", "last_name": "Michaelson",
                "position": "District Manager", "sep_date": "2015-12-19",
            },
            {
                "first_name": "Jake", "last_name": "Jacobsen",
                "position": "Programmer", "sep_date": "",
            },
            {
                "first_name": "Jacquelyn", "last_name": "Jackson",
                "position": "DBA", "sep_date": "",
            },
            {
                "first_name": "Sally", "last_name": "Weber",
                "position": "Web Developer", "sep_date": "2015-12-18",
            },
        ]
        self.employees_data = employee_info
        return employee_info

    @staticmethod
    def get_filter_string():
        filter_string = input("Enter a search string: ").strip()
        return filter_string.lower()

    def filter(self, filter_string):
        filtered_data = [
            employee for
            employee in self.employees_data
            if(
                (filter_string in employee["first_name"].lower()) or
                (filter_string in employee["last_name"].lower())
            )
        ]
        self.filtered_data = filtered_data
        return filtered_data

    def tabulate_filtered_data(self):
        table_data = [["Name", "Position", "Separation Date"]]
        for employee in self.filtered_data:
            table_data.append([
                f'{employee["first_name"]} {employee["last_name"]}',
                employee["position"],
                employee["sep_date"],
            ])
        ascii_table = table.ascii_table(data=table_data, user_alignment="left")
        return ascii_table


def main():
    employees = EmployeeDatabase()
    employees.load_data()
    filter_val = employees.get_filter_string()
    employees.filter(filter_val)
    print(employees.tabulate_filtered_data())


if __name__ == "__main__":
    main()
