"""

Quotation marks are often used to denote the start
and end of a string. But sometimes we need to print
out the quotation marks themselves by using escape
characters.

Create a program that prompts for a quote and an
author. Display the quotation and author as shown
in the example output.

___________________
Example Output
___________________
What is the quote? These aren't the droids you're
looking for.
Who said it? Obi-Wan Kenobi
Obi-wan Kenobi says, "These aren't the droids
you're looking for."

___________________
Constraints
___________________
Use a single output statement to produce this output,
using appropriate string-escaping techniques for quotes.
If your language supports string interpolation or
string substitution, don't use it for this exercise.
Use string concatenation instead.

"""

quote = input("What is the quote? ")
author = input("Who said it? ")

print(f'{author} says, "{quote}"')
