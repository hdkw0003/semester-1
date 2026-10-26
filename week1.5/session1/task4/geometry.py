# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here

# Week 1.5, Session 1: Task 3

class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
   
    def __init__(self, x_coordinate, y_coordinate)
    self.x = x_coordinate
    self.y = y_coordinate

    # Creates a point given X and Y coordinates.

    # Add distance() method here
    self.distance() = math.hypot(x_coordinate, y_coordinate)
    # Uses Pythagoras's Theorem to 

    # Add distance_to() method here
    # (This will need a parameter representing another point)
    self.distance_to() = ((self.distance()) 

# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle
class Circle
  '''
  A Circle in 2D space.
  '''
  def __init__ (self, centre, radius)
  self.centre = (Point.x), (Point.y)
  self.radius = radius
  self.area() = (radius * radius * 3.14159)
  self.perimeter() = (radius * 2 * 3.14150)
    
                          
# Don't add any testing code to this file!
