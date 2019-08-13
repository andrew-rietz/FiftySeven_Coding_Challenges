"""
Helper functions used during the application.

Functions:
    _add_index: Adds a numeric index to the dictionary to help end-user when printed to terminal,
        or output as csv / html
    _get_table_dimensions: Gets the dimensions of an inventory object prior to converting into
        tabular format
    _setup_headers: Sets up the table headers in preparation for printing to either the
        terminal or html file
    _setup_body: Sets up the table body in preparation for printing to either the terminal or
        html file
"""
from collections import OrderedDict


def _add_index(working_inv):
    """
    Adds a numeric index to the dictionary to help end-user when printed to terminal,
    or output as csv / html.

    Args:
        working_inv: (OrderedDict) Represents a PersonalInventory class

    Returns:
        working_inv: (OrderedDict) Dictionary with index added as the first key. The associated
            value is a list of integers from 0 to the maximum length of the ararys associated
            with the other keys in the OrderedDict.
    """
    working_inv = OrderedDict(working_inv)
    n_rows = len(list(working_inv.values())[0])
    working_inv["index"] = [str(val) for val in range(n_rows)]
    working_inv.move_to_end("index", last=False)

    return working_inv

def _get_table_dimensions(working_inv):
    """Gets the dimensions of an inventory object prior to converting into tabular format

    Args:
        working_inv: (OrderedDict) Represents a PersonalInventory class

    Returns:
        dimeions: (dict) contains the dimensions of the table:
            n_rows, n_cols, column_widths, and table_width
    """
    dimensions = {
        "column_widths": {},
        "table_width": 0,
        "n_rows": len(list(working_inv.values())[0]),
        "n_cols": len(list(working_inv.keys())),
    }

    if dimensions["n_rows"] == 0:
        print("No items in inventory.")
        return dimensions

    for col in working_inv.keys():
        data_widths = [len(val) for val in working_inv[col]]
        # Add in the column header as well
        data_widths.append(len(str(col)))
        column_width = max(data_widths)
        dimensions["column_widths"][col] = column_width
        dimensions["table_width"] += column_width

    return dimensions

def _setup_headers(dimensions, working_inv, style="terminal"):
    """
    Sets up the table headers in preparation for printing to either the terminal or html file

    Args:
        dimensions: (dict) contains the dimensions of the table:
            n_rows, n_cols, column_widths, and table_width
        working_inv: (OrderedDict) Represents a PersonalInventory class
        style: (str) Defines the style of the resultant table. Allowed values are
            'terminal' or 'html'.

    Returns:
        header_str: (str) text representation of the row, with the proper delimeters for
            the given style
    """
    prefix = {
        "terminal": "",
        "html": "<th>",
    }
    suffix = {
        "terminal": " | ",
        "html": "</th>\n",
    }
    if style not in list(prefix.keys()):
        print("Sorry, style not recognized. Aborting.")
        return "Failed"

    header_str = ""

    for col in working_inv.keys():
        header_str += prefix[style]
        if style == "terminal":
            header_str += col.center(dimensions["column_widths"].get(col))
        else:
            header_str += col
        header_str += suffix[style]

    if style == "terminal":
        header_str = "| " + header_str[:-1] + "\n"
    elif style == "html":
        header_str = "<tr>\n" + header_str + "</tr>\n"

    return header_str

def _setup_body(dimensions, working_inv, style="terminal"):
    """
    Sets up the table body in preparation for printing to either the terminal or html file

    Args:
        dimensions: (dict) contains the dimensions of the table:
            n_rows, n_cols, column_widths, and table_width
        working_inv: (OrderedDict) Represents a PersonalInventory class
        style: (str) Defines the style of the resultant table. Allowed values are
            'terminal' or 'html'.

    Returns:
        header_str: (str) text representation of the row, with the proper delimeters for
            the given style
    """
    prefix = {
        "terminal": "",
        "html": "    <td>",
    }
    suffix = {
        "terminal": " | ",
        "html": "</td>\n",
    }
    if style not in list(prefix.keys()):
        print("Sorry, style not recognized. Aborting.")
        return "Failed"

    body_str = ""

    for row in range(dimensions["n_rows"]):
        row_str = ""
        for col in working_inv.keys():
            column_values = working_inv[col]
            row_str += prefix[style]
            if style == "terminal":
                row_str += str(column_values[row]).ljust(dimensions["column_widths"].get(col))
            else:
                row_str += column_values[row]
            row_str += suffix[style]

        if style == "terminal":
            row_str = "| " + row_str[:-1] + "\n"
        elif style == "html":
            row_str = "<tr>\n" + row_str + "</tr>\n"

        body_str += row_str

    return body_str
