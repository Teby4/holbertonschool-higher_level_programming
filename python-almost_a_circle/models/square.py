#!/usr/bin/python3
"""Create Class Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Write the class Square that inherits from Rectangle:
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"


    def update(self, *args, **kwargs):
        """
        Assign arguments to id, width, height, x, and y attributes in order.
        """
        if args is not None:
            if len(args) >= 1:
                self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]

        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
