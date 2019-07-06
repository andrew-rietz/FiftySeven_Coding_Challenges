class Citation():
    """
    A representation of a citation
    Attributes:
        quote   (string)
        author  (string)
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
