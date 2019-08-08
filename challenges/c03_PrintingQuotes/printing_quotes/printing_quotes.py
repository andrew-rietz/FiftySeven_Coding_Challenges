"""
Defines and implements a class that stores a quote and the author it's attributed to
"""
class Citation():
    """
    A representation of a bibliographic citation

    Attributes:
        quote: A string indicating what the quote is
        author: A string indicating who the author is
    """
    def __init__(self):
        self.quote = input("What is the quote? ")
        self.author = input("Who said it? ")

    def __str__(self):
        return f"{self.author} says, \"{self.quote}\""


def main():
    cite = Citation()
    print(cite)

if __name__ == "__main__":
    main()
