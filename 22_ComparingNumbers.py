"""

Comparing one input to a known value is common enough,
but you'll often need to process a collection of
inputs.

Write a program that asks for three numbers. Check
first to see that all numbers are different. If
they're not different, then exit the program.
Otherwise, display the largest number of the three.

___________________
Example Output
___________________
Enter the first number: 1
Enter the second number: 51
Enter the third number: 2
The largest number is 51.

___________________
Constraints
___________________
Write the function manually. Don't use a built-in
function for finding the largest number in a list.

"""

nums = []

n_vals = int(input("How many numbers to compare? "))
for n in range(1, n_vals + 1):
    nums.append(float(input(f"Enter number {n}: ")))

# remove any duplicates
nums = list(set(nums))
largest = 0

for num in nums:
    if num > largest:
        largest = num

print(f"The largest number is {largest}.")
