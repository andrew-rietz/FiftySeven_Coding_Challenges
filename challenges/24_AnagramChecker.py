"""

Using functions to abstract the logic away from the
rest of your code makes it easier to read and easier
to maintain.

Create a program that compares two strings and
determines if the two strings are anagrams. The
program should prompt for both input strings and
display the output as shown in the example that
follows.

___________________
Example Output
___________________
Enter two strings and I'll tell you if they're
anagrams:
Enter the first string: note
Enter the second string: tone
"note" and "tone" are anagrams.

___________________
Constraints
___________________
Implement the program using a function called
isAnagram, which takes in two words as its arguments
and retursn True or False. Invoke this function from
your main program.
Check that both words are the same length

"""


def isAnagram(str1, str2):
    l1 = [c for c in str1]
    l2 = [c for c in str2]
    while len(l1) == len(l2) and len(l1) > 0:
        try:
            l2.pop(l2.index(l1[0]))
            l1.pop(0)
        except ValueError:
            l1.pop()
            break

    return len(l1) == len(l2)


def main():
    print("Enter two strings and I'll tell you if they're anagrams.\n")
    str1 = str(input("Enter the first string: "))
    str2 = str(input("Enter the second string: "))

    out = "are" if isAnagram(str1, str2) else "are not"
    print(f'"{str1}" and "{str2}" {out} anagrams.')


main()
