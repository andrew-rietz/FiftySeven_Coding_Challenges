"""
Defines a function to check for anagrams
"""

def is_anagram(first_string, second_string):
    """Compares two strings to determine whether they are anagrams

    Args:
        str1 (str): A string to be compared
        str2 (str): A second string

    Returns:
        (bool): True/False indication of whether the two strings are anagrams
    """
    first_string = first_string.lower()
    second_string = second_string.lower()

    if len(first_string) != len(second_string):
        return False

    first_str_letters = [letter for letter in first_string]
    second_str_letters = [letter for letter in second_string]
    while len(first_str_letters) == len(second_str_letters) and len(first_str_letters) > 0:
        try:
            next_letter = first_str_letters.pop(0)
            second_str_letters.pop(second_str_letters.index(next_letter))
        except ValueError:
            return False

    return True


def main():
    first_string = input(
        "Enter two strings and I'll tell you if they're anagrams.\n" +
        "Enter the first string: "
    ).strip()
    second_string = input("Enter the second string: ").strip()

    are_arenot = "are" if is_anagram(first_string, second_string) else "are not"
    print(f'"{first_string}" and "{second_string}" {are_arenot} anagrams.')

if __name__ == "__main__":
    main()
