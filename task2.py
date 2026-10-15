# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

numbers = read_numbers()
if not numbers:
    sys.exit("Error: no numbers provided")
# Get median
numbers.sort()
l = len(numbers)
if l%2 == 0:
    median = (numbers[l//2] + numbers[(l//2)+ 1]) / 2
else:
    median = numbers[l//2]

print("Minimum =",min(numbers))
print("Maximum =",max(numbers))
print("Mean =",sum(numbers)/len(numbers))
print("Median =",median)