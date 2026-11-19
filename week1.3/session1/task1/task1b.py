# Week 1.3, Session 1: Task 1b

fruit = ['apple','pear','banana','orange']

# loop through the list
while fruit:
	print(fruit.pop())


# Why does this work?

# What features of Python does it rely on?


# fruit.pop, when given no arguments, will simply remove the last item
# this happens repeatedly as it is being looped
# when the last item is popped, the condition (fruit) will no longer be considered 'True' as it's empty
# so, the while loop stops