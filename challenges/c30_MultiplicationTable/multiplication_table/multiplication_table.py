"""
Defines a function that creates a multiplication table
"""
def multiplication_table(base):
    """Creates a multiplication table for every number from 0 to base"""
    for first_num in range(base+1):
        for second_num in range(base+1):
            print(f"{first_num} x {second_num} = {first_num * second_num}")

def main():
    multiplication_table(12)


if __name__ == "__main__":
    main()
