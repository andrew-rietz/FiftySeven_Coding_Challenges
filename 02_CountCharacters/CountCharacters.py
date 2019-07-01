"""

Create a program that prompts for an input string
and displays output that shows the input string
and the number of characters the string contains.

___________________
Example output
___________________
What is the input string? Homer
Homer has 5 characters.

___________________
Constraints
___________________
Be sure the output contains the original string
Use a single output statement to construct the output
Use a built-in function to determine the length of
the string

"""

def n_characters(word):
    return len(word)

def main():
    word = input("What is the input string? ")
    print(f"{word} has {n_characters(word)} characters.")

if __name__ == "__main__":
    main()
