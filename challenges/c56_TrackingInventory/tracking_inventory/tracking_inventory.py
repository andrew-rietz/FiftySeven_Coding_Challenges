"""
Creates and initiates a PersonalInventory class
"""
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from app_functions import startup, prompt, perform_action
from personal_inventory_class import PersonalInventory


def main():
    inv = startup()
    inv.print_to_terminal(index=False)
    while True:
        action = prompt()
        result = perform_action(inv, action)
        if result == "EXIT":
            break


if __name__ == "__main__":
    main()
