## 56 Tracking Personal Inventory
Write a program that tracks your personal inventory. The program should
allow you to enter an item, a serial number, and estimated value. The
program should then be able to print out a tabular report in both HTML and
CSV formats that looks like this:

#### Example Output
 Name       | Serial Number | Value  
------------|---------------|--------
 Xbox One   | AXB124AXY     | $399.00
 Samsung TV | S40AZBDE4     | $599.99

***
[Additional constraints and challenges available in the full text.](https://www.amazon.com/Exercises-Programmers-Challenges-Develop-Coding/dp/1680501224)

***
## Design Decisions

1. **Overall Implementation**  
Many of the functions specified in the challenge could be easily accomplished by
importing and making use of the pandas library, which allows easy conversion of a
tabular dataset into csv or html files. There are also methods to easily get a
terminal-style table, such as using a `pandas` dataframe in conjunction with a
package like [terminalTables](https://pypi.org/project/terminaltables/)

  I knowingly opted **not** to make use of these additional libraries and tools for this
implementation, as the purpose was to practice my own coding in Python. In a production
environment it would make sense to take advantage of these other libraries.

2. **OrderedDict**  
I did opt to use an OrderedDict to track inventory. The OrderedDict allows
the benefits of a dictionary, while also allowing me to keep track of the
order in which items are added to the dictionary. This is part of the
`collections` library which is one of the Python distribution core packages.

3.
