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
    def size(self) -> int:
        return (self.width)

    @size.setter
    def size(self, value) -> None:
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"