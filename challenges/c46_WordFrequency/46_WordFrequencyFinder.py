"""

Knowing how often a word appears in a sentence or
block of text is helpful for creating word clouds
and other types of word analysis. And it's more
useful when running it against lots of text.

Create a program that reads in a file and counts
the frequency of words in the file. Then construct
a historgram displaying the words and the frequency,
and display the histogram to the screen.

___________________
Example Output
___________________
Given the text file words.txt with this content:

badger badger badger badger mushroom mushroom
snake badger badger badger

the program would produce the following output:

badger:   *******
mushroom: **
snake:    *

___________________
Constraints
___________________
- Ensure that the most used word is at the top of
the report and the least used words are at
the bottom

"""


def createDummyInput():
    text = """
    badger badger badger badger mushroom mushroom
    snake badger badger badger
    """
    with open("./46_WordFrequency/words.txt", "w") as writer:
        writer.write(text)

    return "Dummy .txt file created"


def main():

    createDummyInput()
    documentText = []
    with open("./46_WordFrequency/words.txt", "r") as reader:
        documentText = [line.rstrip() + " " for line in reader]

    fullText = "".join(documentText)
    uniqueWords = set(fullText.split())
    wordCount = {}
    for word in uniqueWords:
        wordCount[word] = fullText.upper().count(word.upper())

    longestKey = max([len(k) for k in wordCount.keys()])
    sortedWordCount = sorted(wordCount.items(), key=lambda kv: kv[1], reverse=True)
    for kv in sortedWordCount:
        print(f"{kv[0]}:".ljust(longestKey + 4) + "*" * kv[1])


main()
