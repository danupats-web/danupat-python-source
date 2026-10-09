"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""

class Rectangle:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def getArea(self):
        return f"Area of {self.__width} width and {self.__length} length = {self.__width * self.__length}"

    def getPerimeter(self):
        return f"Perimeter of {self.__width} width and {self.__length} length = {2 * (self.__width + self.__length)}"

    def isSquare(self):
        return self.__width == self.__length

myRectangle = Rectangle(5,10)
print(myRectangle.getArea())

myRectangle2 = Rectangle(10,10)
print(myRectangle2.isSquare())