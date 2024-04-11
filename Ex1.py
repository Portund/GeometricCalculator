import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def is_right_angled(self):
        sides = sorted([self.a, self.b, self.c])
        return sides[-1] ** 2 == sides[-2] ** 2 + sides[0] ** 2

def calculate_area(shape):
    return shape.area()

def is_right_angled_triangle(triangle):
    return triangle.is_right_angled()