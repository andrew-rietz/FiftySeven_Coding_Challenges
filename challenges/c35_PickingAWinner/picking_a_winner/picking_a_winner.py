"""
Defines a PrizeDrawing class and performs a drawing
"""
from random import choice

class PrizeDrawing():
    """Represents a prize drawing

    Attributes:
        entries (list): A list of the entered participants

    Methods:
        add: Add a participant to the drawing
        pick_winner: Randomly selects a winner from the entries
    """

    def __init__(self):
        self.entries = []

    def add(self, entry):
        if entry:
            self.entries.append(entry)
            return "Success"
        return "Unable to add"

    def pick_winner(self):
        return choice(self.entries)

def get_entry():
    entry = input("Enter a name: ").strip()
    return entry

def main():
    drawing = PrizeDrawing()
    while True:
        entry = get_entry()
        if not entry:
            break
        drawing.add(entry)
    print(f"The winner is... {drawing.pick_winner()}")


if __name__ == "__main__":
    main()
