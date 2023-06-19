#!/usr/bin/python3
"""
defined base class module
"""


from models.base import Base


class Base:
    """
    class base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor
        Args:
            id = None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


"""
defined class Rectangle that inherits from base
"""


class Rectangle(Base):
    """
    Class Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """ height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """ x setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """y setter """
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area function"""
        return (self.width * self.height)

    def display(self):
        """prints stdout the Reactangle instance with #"""
        print('\n' * self.__y, end="")
        for j in range(self.__height):
            print(' ' * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """returns Rectangle"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)

    def update(self, *args, **kwargs):
        """assigns argument to each attribute"""
        m = len(args)
        if m > 0:
            if 0 < m:
                self.id = args[0]
            if 1 < m:
                self.__width = args[1]
            if 2 < m:
                self.__height = args[2]
            if 3 < m:
                self.__x = args[3]
            if 4 < m:
                self.__y = args[4]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        dict = {'id': self.id, 'width': self.width,
                               'height': self.height,
                               'x': self.x, 'y': self.y}
        return (dict)
