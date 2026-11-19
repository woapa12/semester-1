# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math


# Week 1.5, Session 1: Task 3

class Point:
    """
    A Point in 2D space.
    """
    # Add constructor here
    def __init__(self, x_coordinate, y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate


    # Add distance() method here
    def distance(self):
        return ((self.x)**2 + (self.y)**2) ** 0.5
    
    # Add distance_to() method here
    # (This will need a parameter representing another point)
    def distance_to(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2) ** 0.5


# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

class Circle:
    """A circle defined by it's centre and radius"""

    def __init__(self, centreIn, radiusIn):
        self.centre = centreIn # Point object
        self.radius = radiusIn # Float

    def area(self):
        return(self.radius**2 * math.pi)

    def perimeter(self):
        return(self.radius*2 * math.pi)

# Don't add any testing code to this file!
