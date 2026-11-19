import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices
count = int(input("Enter number of random names: "))
for i in range(count):
    nameIndex = random.randint(0, len(names))
    print(names[nameIndex])
    names.pop(nameIndex) # Remove name from list to avoid duplicates
# Display the chosen names, one per line
