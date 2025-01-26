import math


class Shape:

    def  area(self):
        raise NotImplementedError("The method area() must be overridden by derived classes.")



class Rectangle(Shape):

    def __init__(self, length, width):
        

        self.length = length
        self.width = width

    def area(self):
            return self.length * self.width

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):

        return math.pi * (self.radius ** 2)

    def display_area(shape):
           print(f"The area of the {shape.__class__.__name__.lower()} is: {shape.area():.2f}")


    
        