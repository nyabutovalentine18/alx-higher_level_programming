#!/usr/bin/python3
class Square:
    """ This is the square class. """
    def __init__(self, size=0, position=(0, 0)):
        """ init is called to create an object. self refers to itself
        Args:

            size (int): This is the size of the square.
            position (int, int): These are the coordinates of the square.

        Returns:
            Nothing.

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ This retrieves the size.
        Args:
            None.
        Returns:
            This returns the size.
        """
        return self.__size

    @property
    def position(self):
        """ This will retrieve the position of the square.

        Args:
            None.

        Returns:
            This will return the coordinates.

        """
        return self.__position

    @size.setter
    def size(self, value):
        """ This sets the size of the square.
        Args:
            value (int): This is the value size of the square.
        Return:
            Nothing.
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0 ")

        self.__size = value

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ This will give us the area of a square
        """
        return self.__size ** 2

    def my_print(self):
        """ Prints in stdout
        """

        position, ofthemothafuckingtuple = self.__position
        size = self.__size

        if size == 0:
            print("")
        else:
            for x in range(position):
                print("")
            for y in range(size):
                print(" " * position, end="")
                print("#" * size)
