"""

Create a program that generates multiplcation tables
for the numbers 0 through 12.

___________________
Example Output
___________________
0 x 0 = 0
0 x 1 = 0
....
12 x 11 = 132
12 x 12 = 144

___________________
Constraint
___________________
Use a nested loop to complete this program

"""


def main():

    for num1 in range(0, 13):
        for num2 in range(0, 13):
            print(f"{num1} x {num2} = {num1 * num2}")


main()
