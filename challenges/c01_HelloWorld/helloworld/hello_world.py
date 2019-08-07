class Greeting():
    """
    A representation of a greeting
    Attributes:
        name    (string)
    """
    def __init__(self):
        self.name = input("What is your name? ")

    def hello(self):
        greeting = f"Hello, {self.name.title()}, nice to meet you!"
        return greeting

def main():
    greet = Greeting()
    print(greet.hello())

if __name__ == "__main__":
    main()
