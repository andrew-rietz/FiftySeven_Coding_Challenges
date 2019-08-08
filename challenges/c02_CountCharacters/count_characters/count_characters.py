"""
Defines and implements a StringParser class that parses the number of characters in a string
"""
class StringParser():
    """
    A representation of a text parser

    Attributes:
        text: A string to be parsed
    """

    def __init__(self):
        self.text = input("What is the input string? ")

    def __str__(self):
        return self.text

    def n_characters(self):
        return len(self.text)


def main():
    parser = StringParser()
    print(f"{parser} has {parser.n_characters()} characters")

if __name__ == "__main__":
    main()
