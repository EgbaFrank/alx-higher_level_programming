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
        """Updates the rectangle instance attributes"""
        if not args and not kwargs:
            raise TypeError("at least one argument is expected")

        if len(args) > 5:
            raise TypeError("Too many arguments passed")

        # Handling positional arguments
        if args:
            if args[0] is None:
                raise TypeError("None is not a valid argument")

            attributes = ['id', 'size', 'x', 'y']
            # Iterate over args and attributes simultaneously
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)

        # Handling keyword arguments
        else:
            if not kwargs:
                return

            for key, value in kwargs.items():
                # Check if the key is a valid attribute
                if key in ('id', 'size', 'x', 'y'):
                    setattr(self, key, value)
                else:
                    raise AttributeError(f"Attribute '{key}' is not valid")

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
