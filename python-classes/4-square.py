#!/usr/bin/python3
"""gsegsfdgbdf"""


class Square:
    """etgbdtbdrtbf"""
    def __init__(self, size=0):
        """hntfhbnhgn btf"""
        self.size = size

    @property
    def size(self):
        """thgfbgbnfg"""
        return self.__size

    @size.setter
    def size(self, value):
        """unhbgvfdcsx"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """kjuyrtgfcd"""
        return self.__size ** 2

    def my_print(self):
        """gadfgvaefdgad"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size ** 2):
                print("#" * self.size)
