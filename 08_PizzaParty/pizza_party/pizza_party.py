class PizzaCalc():
    """
    Representation of a calculator
    Attributes:
        people              (int)
        pizzas              (int)
        slices_per_pizza    (int)
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
