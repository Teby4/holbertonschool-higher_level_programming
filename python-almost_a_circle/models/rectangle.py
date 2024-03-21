#!/usr/bin/python3
"""Create Class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init of the Rectangle class.
        """
        super().__init__(id)
        self._width = width
        self._height = height
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self._y = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """return Rectangle Area"""
        return self._width * self._height

    def display(self):
        """Print the Rectangle instance with #"""
        for _ in range(self._y):
            print()

        for _ in range(self._height):
            print(" " * self._x + "#" * self._width)

    def __str__(self):
        """str"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self._x, self._y, self._width, self._height))

    def update(self, *args):
        """
        Assign arguments to id, width, height, x, and y attributes in order.
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self._width = args[1]
        if len(args) >= 3:
            self._height = args[2]
        if len(args) >= 4:
            self._x = args[3]
        if len(args) >= 5:
            self._y = args[4]