import io
import json
import os
import sys
import unittest
import unittest.mock

from contextlib import contextmanager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tracking_inventory import (
    app_functions, input_helpers, output_helpers, personal_inventory_class
)

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class SetUpData(unittest.TestCase):
    """Initializes and cleans up some datasets to be worked with"""

    def setUp(self):
        basedir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(basedir, "mock_data", "test_local_storage.json")
        with open(filepath, "r") as json_file:
            self.test_inventory = json.load(json_file)
        self.inv_class = personal_inventory_class.PersonalInventory(self.test_inventory)
        # The test file looks like:
        # self.test_inventory = {
        #     "item_name": ["Xbox One", "Samsung TV"],
        #     "serial": ["AXB124AXY", "S40AZBDE4"],
        #     "value": ["$399.00", "$599.99"]
        # }

class PersonalInventoryClassTests(SetUpData):
    """Tests the methods of the PersonalInventory Class"""

    @unittest.mock.patch("builtins.input")
    def class_method_test(self, func):
        mock_inputs.side_effect = ["Foo", "Bar", "0.0"]
        with captured_output() as (outputs, errors):
            test_val = self.inv_class.func()
        return test_val

    def test_PersonalInventoryClass__add_item2(self):
        test_val = self.class_method_test(self.inv_class.add_item())
        self.assertEqual("Success", test_val)

    @unittest.mock.patch("builtins.input")
    def test_PersonalInventoryClass__add_item(self, mock_inputs):
        mock_inputs.side_effect = ["Foo", "Bar", "0.0"]
        with captured_output() as (outputs, errors):
            test_val = self.inv_class.add_item()
        self.assertEqual("Success", test_val)

    @unittest.mock.patch("builtins.input")
    def test_PersonalInventoryClass__latest_item_is_item(self, mock_inputs):
        mock_inputs.side_effect = ["Foo", "Bar", "0.0"]
        with captured_output() as (outputs, errors):
            test_val = self.inv_class.add_item()
        self.assertEqual("Success", test_val)

class AppFunctionsTests(SetUpData):
    """Tests the applcation functions defined in the app_functions"""

    def test_startup__no_local_file(self):
        startup = app_functions.startup(subdir="data", filename="this_file_doesnt_exist.json")
        self.assertTrue(isinstance(startup, type(self.inv_class)))

    def test_startup__no_local_file__inventory_is_empty(self):
        startup = app_functions.startup(subdir="data", filename="this_file_doesnt_exist.json")
        inventory = {"item_name": [], "serial": [], "value": []}
        self.assertEqual(inventory, startup.inventory)

    def test_startup__real_local_file(self):
        startup = app_functions.startup(subdir="data", filename="local_storage.json")
        self.assertTrue(isinstance(startup, type(self.inv_class)))

    def test_startup__real_local_file__inventory_not_empty(self):
        basedir = os.path.dirname(os.path.abspath(__file__))
        startup = app_functions.startup(
            basedir=basedir,
            subdir="mock_data", filename="test_local_storage.json"
        )
        self.assertEqual(self.test_inventory, startup.inventory)

    @unittest.mock.patch("builtins.input")
    def test_prompt__valid_input(self, mock_inputs):
        mock_inputs.side_effect = ["Foo", "Bar", "Add"]
        with captured_output() as (outputs, errors):
            test_val = app_functions.prompt()
        self.assertEqual("ADD", test_val)

    @unittest.mock.patch("app_functions.PersonalInventory.add_item")
    def test_perform_action__ADD(self, mocked_func):
        app_functions.perform_action(self.inv_class, "ADD")
        self.assertTrue(mocked_func.called)

    @unittest.mock.patch("app_functions.PersonalInventory.remove_item")
    def test_perform_action__REMOVE(self, mocked_func):
        app_functions.perform_action(self.inv_class, "REMOVE")
        self.assertTrue(mocked_func.called)

    @unittest.mock.patch("app_functions.PersonalInventory.print_to_terminal")
    def test_perform_action__PRINT(self, mocked_func):
        app_functions.perform_action(self.inv_class, "PRINT")
        self.assertTrue(mocked_func.called)

    @unittest.mock.patch("builtins.input")
    @unittest.mock.patch("app_functions.PersonalInventory.to_csv")
    def test_perform_action__TO_CSV(self, mocked_func, mock_inputs):
        mock_inputs.side_effect = ["Y"]
        with captured_output() as (outputs, errors):
            app_functions.perform_action(self.inv_class, "TO CSV")
        self.assertTrue(mocked_func.called)

    @unittest.mock.patch("builtins.input")
    @unittest.mock.patch("app_functions.PersonalInventory.to_html")
    def test_perform_action__TO_HTML(self, mocked_func, mock_inputs):
        mock_inputs.side_effect = ["Y"]
        with captured_output() as (outputs, errors):
            app_functions.perform_action(self.inv_class, "TO HTML")
        self.assertTrue(mocked_func.called)

    @unittest.mock.patch("app_functions.PersonalInventory.save")
    def test_perform_action__SAVE(self, mocked_func):
        app_functions.perform_action(self.inv_class, "SAVE")
        self.assertTrue(mocked_func.called)

    @unittest.mock.patch("app_functions.PersonalInventory.save")
    def test_perform_action__EXIT(self, mocked_func):
        with captured_output() as (outputs, errors):
            app_functions.perform_action(self.inv_class, "EXIT")
        self.assertTrue(mocked_func.called)


class InputHelpersTests(SetUpData):
    """Tests the applcation functions defined in the app_functions"""

    @unittest.mock.patch("builtins.input")
    def test_get_item_name(self, mock_inputs):
        mock_inputs.side_effect = ["", None, "Foo"]
        with captured_output() as (outputs, errors):
            test_val = input_helpers._get_item_name()
        self.assertEqual("Foo", test_val)

    @unittest.mock.patch("builtins.input")
    def test_get_serial(self, mock_inputs):
        mock_inputs.side_effect = ["", None, "Bar"]
        with captured_output() as (outputs, errors):
            test_val = input_helpers._get_serial()
        self.assertEqual("Bar", test_val)

    @unittest.mock.patch("builtins.input")
    def test_get_value(self, mock_inputs):
        mock_inputs.side_effect = ["", None, "Bar", "24.24.24", "10.999"]
        with captured_output() as (outputs, errors):
            test_val = input_helpers._get_value()
        self.assertEqual("$11.00", test_val)


class OutputHelpersTests(SetUpData):
    """Tests the applcation functions defined in the app_functions"""
    def setUp(self):
        super(OutputHelpersTests, self).setUp()
        self.dimensions = output_helpers._get_table_dimensions(self.inv_class.inventory)

    def test_add_index(self):
        test_inv = self.test_inventory
        test_inv["index"] = ["0", "1"]
        test_val = output_helpers._add_index(self.inv_class.inventory)
        self.assertEqual(test_inv, test_val)

    def test_dimensions__nrows_is_2(self):
        self.assertEqual(2, self.dimensions["n_rows"])

    def test_dimensions__ncols_is_3(self):
        self.assertEqual(3, self.dimensions["n_cols"])

    def test_dimensions__table_width_is_26(self):
        self.assertEqual(26, self.dimensions["table_width"])

    def test_dimensions__column_widths_is_3(self):
        column_widths = {'item_name': 10, 'serial': 9, 'value': 7}
        self.assertEqual(column_widths, self.dimensions["column_widths"])


if __name__ == "__main__":
    unittest.main()
