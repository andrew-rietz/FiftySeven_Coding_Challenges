import io
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


class PersonalInventoryClassTests(unittest.TestCase):
    """Tests the methods of the PersonalInventory Class"""


class AppFunctionsTests(unittest.TestCase):
    """Tests the applcation functions defined in the app_functions"""

    def setUp(self):
        basedir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(basedir, "mock_data", "test_local_storage.json")
        self.inv_class = personal_inventory_class.PersonalInventory(filepath)

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
        inventory = {
            "item_name": ["Xbox One", "Samsung TV"],
            "serial": ["AXB124AXY", "S40AZBDE4"],
            "value": ["$399.00", "$599.99"]
        }
        self.assertEqual(inventory, startup.inventory)

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


class InputHelpersTests(unittest.TestCase):
    """Tests the applcation functions defined in the app_functions"""

class OutputHelpersTests(unittest.TestCase):
    """Tests the applcation functions defined in the app_functions"""

if __name__ == "__main__":
    unittest.main()
