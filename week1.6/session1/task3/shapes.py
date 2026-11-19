# Week 1.6, Session 1: Task 3

import math
from point import Point

VALID_COLOURS = {"red", "orange", "yellow", "green", "blue", "purple"}


class Shape:
    """
    Superclass for different types of shape.
    """

    def __init__(self, position, colour):
        """
        Creates a shape with the specified position & colour.
        """
        self.set_position(position)
        self.set_colour(colour)

    def set_position(self, position):
        """
        Moves this shape to the given position.
        """
        if not isinstance(position, Point):
            raise TypeError("position must be a Point")

        self.position = position

    def set_colour(self, colour):
        """
        Sets this shape's colour to the given colour.
        """
        if colour not in VALID_COLOURS:
            raise ValueError(f"invalid color: must be one of {VALID_COLOURS}")

        self.colour = colour


# Implement your Circle class here
# Make sure that it inherits properly from Shape!
class Circle(Shape):
    def set_radius(self, r):
        if isinstance(r, int) or isinstance(r, float):
            if r>0:
                return r
            else:
                raise ValueError
        else:
            raise TypeError
        
    
    def __init__(self, radius, position, colour):
        super().__init__(position, colour)
        self.radius = self.set_radius(radius)

    def __str__(self):
        # red circle, radius 2.5, at (0.0, 0.0)
        return f"{self.colour} circle, radius {self.radius}, at {self.position}"

    def area(self):
        return self.radius**2 * math.pi / 2

    def perimeter(self):
        return self.radius * 2 * math.pi

