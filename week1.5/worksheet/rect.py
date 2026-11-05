# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        if not (width.is_integer() and height.is_integer()):
            raise TypeError("Width and height must be integers.")

        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        
            
        # raising appropriate exceptions if necessary (see README.md)
        self.width = width
        self.height = height


    def is_square(self):
        """Returns True if it is a square, else False"""
        return self.width == self.height

    def area(self):
        """Calculates the area by multiplying width by height"""
        return self.width * self.height

    def perimeter(self):
        """Calculates perimeter by adding 2 widths and 2 heights"""
        return 2*(self.width + self.height)
    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
