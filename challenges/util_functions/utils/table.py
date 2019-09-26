"""
Defines re-usable table functions
"""
def ascii_table(data, user_alignment="center"):
    """Creates an ascii table based on the input table_data variable

    Args:
        data (list): A list of lists. Each list corresponds to one row
            in the table and it's assumed that the first contains the column headers. i.e.:
            [['Header 1', 'Header 2'], ['Foo', 'Bar'], [1, 2]]

    Returns:
        table (str): String representation of the table
    """

    table_columns = len(data[0])
    stringified_table_data = [[str(cell) for cell in row] for row in data]
    max_length_by_column = [0] * len(stringified_table_data[0])
    for row in stringified_table_data:
        for cell in range(len(row)):
            cell_characters = len(row[cell])
            if cell_characters > max_length_by_column[cell]:
                max_length_by_column[cell] = cell_characters

    horizontal_breaks = ["-" * (max_length_by_column[i] + 1) for i in range(table_columns)]

    alignment_options = {
        "left": "ljust",
        "right": "rjust",
        "center": "center",
    }
    align = getattr(str, alignment_options[user_alignment])

    table_body = [
        [align(row[i], (max_length_by_column[i] + 1)) for i in range(table_columns)]
        for row in stringified_table_data
    ]
    table = " | ".join(table_body[0]) + "\n" + "-|-".join(horizontal_breaks)
    for row in table_body[1:]:
        table += "\n" + " | ".join(row)

    return table
