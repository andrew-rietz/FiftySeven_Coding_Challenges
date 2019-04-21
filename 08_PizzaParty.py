"""

Division isn't always exact, and sometimes you'll
write programs that will need to deal with the
leftovers as a whole number instead of a decimal.

Write a program to evenly divide pizzas. Prompt for
the number of people, the number of pizzas, and the
number of slices per pizza. Ensure that the number
of pieces comes out even. Display the number of pieces
each person should get. If there are leftovers,
show the number of leftover pieces.

___________________
Example Output
___________________
How many people? 8
How many pizzas do you have? 2

8 people with 2 pizzas
Each person gets 2 pieces of pizza.
There are 0 leftover pieces.

"""

people = int(input("How many people? "))
pizzas = int(input("How many pizzas do you have? "))
slices = int(input("How many slices per pizza? "))

pieces = (pizzas * slices) // people
leftover = (pizzas * slices) % people

print(
    f"""
{people} people with {pizzas} pizzas.
Each person gets {pieces} pieces of pizza.
There are {leftover} leftover pieces.\
"""
)
