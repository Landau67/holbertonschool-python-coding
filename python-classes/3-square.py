#!/usr/bin/python3
"""eefvuyfvf"""


class Square:
    """egefgesrgser"""

    def __init__(self, size=0):
        """vsfgsfgsf"""
        self.__size = size

    @property
    def size(self):
        """sdcfgvbhnjk"""
        return self.__size

    @size.setter
    def size(self, value):
        """afdfsdf"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """egefgfgs"""
        return self.__size ** 2
