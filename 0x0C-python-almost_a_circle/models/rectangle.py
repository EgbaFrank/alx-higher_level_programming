#!/usr/bin/python3
"""
Contains a rectngle model class
"""
from models.base import Base


class Rectangle(Base):
    """A rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Called at new instance initialization"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the width of the rectangle instance"""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width of the rectangle instance"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Gets the height of the rectangle instance"""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height of the rectangle instance"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Gets x of the rectangle instance"""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets x of the rectangle instance"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Gets y of the rectangle instance"""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets y of the rectangle instance"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Computes the area of the rectangle instance

        Returns:
            int: area of the rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """Prints a rectangle to stdout

        Example:
            >>> rect = Rectangle(3, 4)
            >>> rect.display()
            ###
            ###
            ###
            ###

            >>> rect.width = 1
            >>> rect.height = 1
            >>> rect.display()
            #

            >>> rect1 = Rectangle(3, 4, 3, 2)
            >>> rect1.display()
            <BLANKLINE>
            <BLANKLINE>
               ###
               ###
               ###
               ###
        """
        res = []
        for _ in range(self.__y):
            print()

        for i in range(self.__height):
            res.append(' '*self.__x + '#'*self.__width)
        print('\n'.join(res))

    def __str__(self):
        """Overrides default print"""
        return (f"[Rectangle] ({self.id}) {self.x}/"
                f"{self.y} - {self.width}/{self.height}")

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

            attributes = ['id', 'width', 'height', 'x', 'y']
            # Iterate over args and attributes simultaneously
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)

        # Handling keyword arguments
        else:
            if not kwargs:
                return

            for key, value in kwargs.items():
                # Check if the key is a valid attribute
                if key in ('id', 'width', 'height', 'x', 'y'):
                    setattr(self, key, value)
                else:
                    raise AttributeError(f"Attribute '{key}' is not valid")

    def to_dictionary(self):
        """Returns the dictionary representation"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
