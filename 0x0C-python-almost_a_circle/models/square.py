#!/usr/bin/python3
"""
Contains a Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A square class that inherits from a rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Called when a new instance is initialized"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size attribute"""
        self.width = value
        self.height = value

    def __str__(self):
        """Overrides default print"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Updates square instance attributes"""
        if not args and not kwargs:
            raise TypeError("At least one argument is expected")

        if len(args) == 0:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

        elif len(args) == 1:
            self.id = args[0]

        elif len(args) == 2:
            self.id = args[0]
            self.size = args[1]

        elif len(args) == 3:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]

        elif len(args) == 4:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]

        else:
            raise TypeError("Too many arguments")

    def to_dictionary(self):
        """Returns the dictionary representaion of a square instance

        Example:
            >>> sq = Square(5, 0, 0, 1)
            >>> sq2 = Square(1, 0, 0, 2)
            >>> print(sq)
            [Square] (1) 0/0 - 5
            >>> print(sq2)
            [Square] (2) 0/0 - 1
            >>> sq_dict = sq.to_dictionary()
            >>> print(dict(sorted(sq_dict.items())))
            {'id': 1, 'size': 5, 'x': 0, 'y': 0}
            >>> sq2.update(**sq_dict)
            >>> sq2 == sq
            False
        """
        res = {}
        res["id"] = self.id
        res["size"] = self.size
        res['x'] = self.x
        res['y'] = self.y

        return res
