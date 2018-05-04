# -*- coding: utf-8 -*-
"""
Created on Tue May 10 08:18:02 2016

@author: WELG
"""


class Coordinate(object):
    i = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #print(object)

    def distance(self, other):
        '''
        Takes a coordinate, return the a distance to that coordinate.
        :param other:
        :return: Distance from current instance to coordinate specified by other
        '''
        '''
        :param other: 
        :return: 
        '''
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"

    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __repr__(self):
        return "Coordinate(" + str(self.x) + ", " + str(self.y) + ")"

    def static_inc():
        i += 1


c = Coordinate(3, 4)
origin = Coordinate(0, 0)

#print(c)

d = Coordinate(5,7)
print(d.x)
print(d.__str__())
print("hello")
print(Coordinate.distance(c,d))
print(c.distance(d))
#c.distance()