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



# Finally, add code here to demonstrate use of Point
a = Point(1, 2)
b = Point(3, 4)
print(a.distance())
print(b.distance())
print(a.distance_to(b))
print(b.distance_to(a))