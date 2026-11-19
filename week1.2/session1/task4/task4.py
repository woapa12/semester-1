# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?

both = fruit.intersection(vegetables)
print(both)

# Why does the following code diplay five items?

# Doesn't repeat the same elements (tomato)

food = fruit.union(vegetables)
print(food)

# Add an item to fruit
fruit.add("mango")
# Remove an item from vegetables
vegetables.remove("leek")
# Find and display symmetric difference of the two sets
mix = fruit.symmetric_difference(vegetables)
print(mix)