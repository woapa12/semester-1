import random

# Get user to input how many random numbers they want
count = int(input("Number of random numbers: "))
# Generate this many random numbers
numbers = [random.random() for i in range(count)]
# Write the random numbers to a file named random.txt, one number per line
numberString = ""
for i in numbers:
    numberString += str(i) + "\n"
with open("random.txt","w") as f:
    
    print(numberString)
    f.write(numberString)