"""

THere will be times when you'll need to read in one
file, modify it, and then write a modified version
of that file to a new file.

Given an input file, read the file and look for all
occurrences of the word utilize. Replace each
occurrence with use. Write the modified file to a
new file.

___________________
Example Output
___________________
Give then input file of:

One should never utilize the word "utilize" in
writing. Use "use" instead.

The program should generate:

One should never use the word "use" in writing.
Use "use" instead.

___________________
Constraints
___________________
- Prompt for the name of the output file
- Write the output to a new file

"""


def createDummyFile():
    fileText = (
        """One should never utilize the word "utilize" in writing. Use "use" instead."""
    )
    with open("./45_WordFinder/dummy.txt", "w") as writer:
        writer.write(fileText)
    return "Dummy text file created"


def main():
    import re

    pattern = re.compile("utilize", re.IGNORECASE)

    createDummyFile()
    fileName = input("What is the name of the file? ")

    with open(fileName, "r") as reader:
        fileWords = [line.split() for line in reader]
    modWords = [[pattern.sub("use", word) for word in line] for line in fileWords]

    print("\n".join([" ".join(line) for line in modWords]))


main()
