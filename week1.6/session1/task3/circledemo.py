# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)

import shapes
a = shapes.Point(1, 1)
c = shapes.Circle(10, a, "red")
print(c.area())
print(c.perimeter())
print(c)
d = shapes.Circle(-1, a, "blue")