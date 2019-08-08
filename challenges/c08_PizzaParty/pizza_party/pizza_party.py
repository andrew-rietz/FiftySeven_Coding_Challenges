"""
Defines and implements a class that helps share pizza equally
"""
class PizzaCalc():
    """
    Representation of a calculator that determines how many pieces of pizza each person
    in a group can have based on the number of people, pizzas, and slices per pizza.

    Attributes:
        people: An integer count of the number of people
        pizzas: An integer count of the number of pizzas
        slices_per_pizza: An integer count of the number of slices per pizza
    """

    def __init__(self):
        self.people = int(input("How many people? "))
        self.pizzas = int(input("How many pizzas do you have? "))
        self.slices_per_pizza = int(input("How many slices per pizza? "))

    def divide_equally(self):
        pieces = {
            "per_person": (self.pizzas * self.slices_per_pizza) // self.people,
            "leftover": (self.pizzas * self.slices_per_pizza) % self.people,
        }
        return pieces

def main():
    calc = PizzaCalc()
    pieces = calc.divide_equally()
    print(
        f"{calc.people} people with {calc.pizzas} pizzas.\n" +
        f"Each person gets {pieces['per_person']} pieces of pizza.\n" +
        f"There are {pieces['leftover']} pieces leftover."
    )

if __name__ == "__main__":
    main()
