"""
Defines and instantiates a Magic 8 Ball class
"""
from random import randrange

class MagicEightBall():
    """Represents a magic eight ball"""

    def __init__(self):
        self.responses = ["Yes", "No", "Maybe", "Ask again later"]

    def answer(self):
        index = randrange(len(self.responses))
        return self.responses[index]


def main():
    eight_ball = MagicEightBall()

    userQuestion = input("What's your question? ")
    print(eight_ball.answer())


if __name__ == "__main__":
    main()
