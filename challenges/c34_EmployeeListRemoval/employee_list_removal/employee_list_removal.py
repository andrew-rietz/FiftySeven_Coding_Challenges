"""
Defines an EmployeeList class, instantiates the class, and does some manipulation
"""

class EmployeeList():
    """A representation of an employee list

    Attributes:
        employees (dict): A dict of all current employees, with lowercase name used as key
        {
            "foo bar": "Foo Bar",
            "biz baz": "Biz Baz",
            etc.
        }

    Methods:
        remove: Remove an employee from the list
        print: Print the list to the terminal
    """

    def __init__(self):
        self.employees = None

    def import_list(self, employee_list):
        new_employees = {
            employee.lower(): employee for employee in employee_list
        }
        if self.employees:
            # combine two dicts into a single dict
            self.employees = {**self.employees, **new_employees}
        else:
            self.employees = new_employees


    def remove(self, employee):
        self.employees.pop(employee.lower(), None)

    def print_to_term(self):
        if not self.employees:
            out_string = "There are 0 employees."
        else:
            n = len(self.employees)
            out_string = (
                f"There are {n} employees:\n" +
                "\n".join(list(self.employees.values()))
            )
        print(out_string)

def main():
    e_list = EmployeeList()
    e_list.import_list([
        "John Smith",
        "Jackson Jackson",
        "Chris Jones",
        "Amanda Cullen",
        "Jeremy Goodwin"
    ])
    name_to_remove = input("Enter an employee name to remove: ").strip()
    e_list.remove(name_to_remove)
    e_list.print_to_term()


if __name__ == "__main__":
    main()
