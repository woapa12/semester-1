# Week 1.3, Session 2: Write User Information to a File


# Prompt the user for their name, age, and favorite colour.

while True:
    name = input("Name: ")
    age = input("Age: ")
    colour = input("Favourite Colour: ")
    # Open a file called 'user_info.txt' for reading

    if name == "exit":
        break

    with open("user_info.txt", "a") as file:
        file.write(name + "\n")
        file.write(age + "\n")
        file.write(colour + "\n")
        file.write("\n")

# Write each piece of information to the file, each on a new line.

# Hints:
# - Remember to add \n for new lines when writing to files


# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'
