#!/usr/bin/python3
"""nnnfof"""


class Square:
    """erngiueguf"""
    def __init__(self, size=0):
        """ofevioef"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """egefgfgs"""
        return self.__size ** 2
