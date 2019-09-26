import sys
import os
from operator import itemgetter

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util_functions.utils import table, user_inputs


def load_data():
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
    return employee_info

def get_sort_preference():
    fields = ["first_name", "last_name", "position", "sep_date"]
    sort_field = user_inputs.get_string_in_list(
        prompt=f"What field would you like to sort by? [{', '.join(fields)}]",
        err_msg="Please select a valid option.",
        allowed_vals=fields,
    ).lower()
    return sort_field

def get_alignment_preference():
    options = ["left", "right", "center"]
    alignment = user_inputs.get_string_in_list(
        prompt=f"How do you want the final table aligned? [{', '.join(options)}]",
        err_msg="Please select a valid option.",
        allowed_vals=options,
    ).lower()
    return alignment

def sort_table(data, sort_field, alignment):
    sorted_data = sorted(data, key=itemgetter(sort_field))

    table_data = [["Name", "Position", "Separation Date"]]
    for record in sorted_data:
        table_data.append([
            f'{record["first_name"]} {record["last_name"]}',
            record["position"],
            record["sep_date"],
        ])

    output_string = table.ascii_table(data=table_data, user_alignment=alignment)
    return output_string

def main():
    sort_field = get_sort_preference()
    alignment = get_alignment_preference()

    employee_info = load_data()
    ascii_table = sort_table(employee_info, sort_field, alignment)
    print(ascii_table)


if __name__ == "__main__":
    main()
