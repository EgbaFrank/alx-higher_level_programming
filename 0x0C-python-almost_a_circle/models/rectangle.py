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
        if width < 0:
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
        if height < 0:
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

            >>> rect.width = 0
            >>> rect.height = 0
            >>> rect.display()
            <BLANKLINE>

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

        if self.__width != 0 or self.__height != 0:
           for i in range(self.__height):
               res.append(' '*self.__x + '#'*self.__width)
        print('\n'.join(res))

    def __str__(self):
        """Overrides default print"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Updates the rectangle instance attributes"""
        if len(args) == 0 and len(kwargs) == 0:
            raise TypeError("At least one argument is expected")

        if len(args) == 0:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

        elif len(args) == 1:
            self.id = args[0]

        elif len(args) == 2:
            self.id = args[0]
            self.width = args[1]

        elif len(args) == 3:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]

        elif len(args) == 4:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]

        elif len(args) == 5:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]

        else:
            raise TypeError("Too many arguments passed")

    def to_dictionary(self):
        """Returns the dictionary representation

        Example:
            >>> rect = Rectangle(5, 3, 0, 0, 1)
            >>> rect2 = Rectangle(1, 1, 0, 0, 2)
            >>> print(rect)
            [Rectangle] (1) 0/0 - 5/3
            >>> print(rect2)
            [Rectangle] (2) 0/0 - 1/1
            >>> rect_dict = rect.to_dictionary()
            >>> print(dict(sorted(rect_dict.items())))
            {'height': 3, 'id': 1, 'width': 5, 'x': 0, 'y': 0}
            >>> rect2.update(**rect_dict)
            >>> rect2 == rect
            False
        """
        res = {}
        res["id"] = self.id
        res["width"] = self.width
        res["height"] = self.height
        res['x'] = self.x
        res['y'] = self.y

        return res
