"""
Defines and implements a madlib class
"""
class Madlib():
    """
    A representation of a madlib generator

    Attributes:
        noun: A string describing some sort of noun
        verb: A string defining some sort of verb
        adjective: A string defining some sort of adjective
        adverb: A string defining some sort of adverb
    """

    def __init__(self):
        self.noun = input("Enter a noun: ")
        self.verb = input("Enter a verb: ")
        self.adjective = input("Enter an adjective: ")
        self.adverb = input("Enter an adverb: ")

    def __str__(self):
        return f"Do you {self.verb} your {self.adjective} {self.noun} {self.adverb}? That's hilarious!"

def main():
    ml = Madlib()
    print(ml)

if __name__ == "__main__":
    main()
