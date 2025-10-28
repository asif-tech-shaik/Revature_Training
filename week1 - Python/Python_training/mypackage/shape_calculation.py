"""Area, Circumference of SQ, Rectangle, Circle"""

from math import pi

def area_of_square(side):
    """
    Returns the area of a square with side length side.
    :param side: side length of square
    :return: area of square
    """
    return side * side

def area_of_circle(rad):
    """
    Returns the area of a circle with radius rad.
    :param rad: radius of circle
    :return: area of circle
    """
    return pi * rad * rad

def area_of_rectangle(length, breath):
    """
    Returns the area of a rectangle with  length and  breath.
    :param length: length of rectangle
    :param breath: breath of rectangle
    :return: area of rectangle
    """
    return length * breath

def circum_of_circle(radius):
    """
    Returns the circumference of a circle with  radius.
    :param radius: radius of circle
    :return: circumference of circle
    """
    return 2 * pi * radius
