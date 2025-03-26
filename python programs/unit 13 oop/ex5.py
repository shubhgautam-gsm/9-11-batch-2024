from abc import ABC 

class Shape(ABC): #main model class 1

    def area(self):
        pass

class Rectangle(Shape): #sub model class 2
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape): #sub model class 2
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Triangle(Shape): #sub model class 2
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Usage of Abstraction
rectangle = Rectangle(10,20)
# rectangle.mymethod(10,30)
print("Area of Rectangle:", rectangle.area())  # Output: Area of Rectangle: 20

circle = Circle(3)
print("Area of Circle:", circle.area())  # Output: Area of Circle: 28.26

triangle = Triangle(4, 3)
print("Area of Triangle:", triangle.area())  # Output: Area of Triangle: 6.0



