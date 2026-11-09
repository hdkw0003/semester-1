# Week 1.7, Session 1: Task 2 - unit tests for the methods in Point and Circle
import math
from geometry import Point, Circle

def test_point_constructor():
    p = Point(5, -2)
    assert p.x == 5
    assert p.y == -2

def test_point_distance():
    assert Point(0, 0).distance() == 0.0
    assert Point(6, 8).distance() == 10.0
    
def test_point_distance_to():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    assert p1.distance_to(p2) == 5.0
    
    # complete the implementation for
    # testing distance_to()

# Write test functions to test the __init__(), 
# area() and perimeter() methods in Circle class
# you can use the default value for centre coordinates

def test_init_circle():
    '''Intended for testing the constructor of a circle.
    '''
    p = Point(1.0, 1.0)
    c = Circle(5, p)
    
    assert c.radius == 5
    assert c.centre == Point(1.0, 1.0)

def test_area_circle():
    '''Intended to test the area function of the Circle class.'''
    p = Point(1.0, 1.0)
    c = Circle(5, p)
    assert c.area == math.pi * 6 * 6

def test_perimeter_circle():
    '''Intended to test the perimeter function of the Circle class.'''
    p = Point(1.0, 1.0)
    c = Circle(5, p)
    assert c.perimeter == math.pi * 6 * 2

