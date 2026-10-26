# Week 1.5, Session 1: Task 4

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle

import geometry

Point.x = int(input("Please input an X coordinate."))
Point.y = int(input("Please input a Y coordinate."))
Circle.centre = ((Point.x), (Point.y))
Circle.radius = 2.5
print round((Circle.area()), 4)
print round((Circle.perimeter()), 4)
