"""

The 'Hello, World' program is the first program
you learn to write in many languages, but it
doesn't involve any input.

So create a program that prompts for your name
and prints a greeting using your name

___________________
Example Output
___________________
What is your name? Brian
Hello, Brian, nice to meet you!

___________________
Constraint
___________________
Keep the input, string concatenation, and
output separate

"""

def is_alpha(name):
    return name.isalpha()

def hello(name):
    greeting = f"Hello, {name.title()}, nice to meet you!"
    return greeting

def main():
    name = input("What is your name? ")
    if is_alpha(name):
        print(hello(name))
    else:
        print("Sorry, please enter a valid name.")

if __name__ == "__main__":
    main()
