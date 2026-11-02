# Week 1.5, Session 1: Task 3

import math

class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
   
    def __init__(self, x_coordinate, y_coordinate):
      self.x = x_coordinate
      self.y = y_coordinate

    # Creates a point given X and Y coordinates.

    # Add distance() method here
      def distance(self):
         math.hypot(x_coordinate, y_coordinate)
    # Uses Pythagoras's Theorem to 

    # Add distance_to() method here
    # (This will need a parameter representing another point)
      def distance_to(other, self):
        (other.distance() - self.distance())



# Finally, add code here to demonstrate use of Point

p = Point(2.4, 3.6)
print (Point.x)
print (Point.y)
print (Point.distance())
print (Point.distance_to())
