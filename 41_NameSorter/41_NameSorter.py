"""

Alphabetizing the contents of a file, or sorting
its contents, is a great way to get comfortable
manipulating a file in your program.

Create a program that reads in the following list
of names:

Ling, Mai
Johnson, Jim
Zarnecki, Sabrina
Jones, Chris
Jones, Aaron
Swift, Geoffrey
Xiong, Fong

Read this program and sort the list alphabetically.
Then print the sorted list to a file that looks like
the following example output.

___________________
Example Output
___________________
Total of 7 names
-----------------
Ling, Mai
Johnson, Jim
Jones, Aaron
Jones, Chris
Swift, Geoffrey
Xiong, Fong
Zarnecki, Sabrina

___________________
Constraints
___________________
- Don't hard-code the number of names

"""


def writeDummyFile():
    names = [
        "Ling, Mai",
        "Johnson, Jim",
        "Zarnecki, Sabrina",
        "Jones, Aaron",
        "Jones, Chris",
        "Swift, Geoffrey",
        "Xiong, Fong",
    ]
    with open("41_NameSorter/41_InputFile.txt", "w") as writer:
        for name in names:
            writer.write(name + "\n")
        writer.close()


def readDummyFile(fName):
    with open(fName, "r") as reader:
        names = [line.rstrip() for line in reader]
        reader.close()

    return names


def main():
    writeDummyFile()
    names = sorted(readDummyFile("41_NameSorter/41_InputFile.txt"))
    charsInLongestName = max([len(name) for name in names])

    print(names)
    print(f"Total of {len(names)} names")
    print("-" * charsInLongestName)
    print("\n".join(names))


main()
