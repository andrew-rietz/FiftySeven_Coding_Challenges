'''

Write a program that prompts the user for five
numbers and computes the total of the numbers.

___________________
Example Output
___________________
Enter a number: 1
Enter a number: 2
Enter a number: 3
Enter a number: 4
Enter a number: 5
The total is 15.

___________________
Constraints
___________________
The prompting must use repetition, such as a counted
loop, not three separate prompts.
Create a flow chart before writing the program

'''

def main():
    nums = getInputs(5)
    print(f'The total is {sum(nums)}')

def getInputs(n):
    nums = []
    for num in range(n):
        nums.append(float(input('Enter a number: ')))
    return nums

main()
